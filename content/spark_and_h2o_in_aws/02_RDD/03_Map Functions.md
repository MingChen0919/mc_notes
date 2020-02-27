# Map Functions

This section provides examples of how to apply a map function to elements of an RDD

# Apply a function to each element

This group of methods apply a function to each element of an RDD.

## **`map()`**

Return a new RDD by applying a function to all elements of this RDD.

    from pyspark import SparkContext
    sc = SparkContext(master="local[*]")
    rdd = sc.parallelize([1, 2, 3])
    print(rdd.map(lambda x: x + 1).collect())

Output:

    [2, 3, 4]

If your goal is to apply some operations to each element with side effect instead of transforming the elements, you should use the method foreach(). Below is an example:

Instead of manipulating each element, we just want to use is as a file name to create some files.

    from pyspark import SparkContext
    from tempfile import mkdtemp
    import os
    sc = SparkContext(master="local[*]")
    
    rdd = sc.parallelize(['a.txt', 'b.txt', 'c.txt'])
    dir = mkdtemp()
    def f(x):
        path = os.path.join(dir, x)
        print(path)
    rdd.foreach(f)

Output:

    /var/folders/mv/122vn3nn0kx39q71g1sx5wkh0000gn/T/tmpqe_59ohz/c.txt
    /var/folders/mv/122vn3nn0kx39q71g1sx5wkh0000gn/T/tmpqe_59ohz/b.txt
    /var/folders/mv/122vn3nn0kx39q71g1sx5wkh0000gn/T/tmpqe_59ohz/a.txt

## `flatMap()`

Return a new RDD by first applying a function to all elements of this RDD, and then flattening the results.

    from pyspark import SparkContext
    sc = SparkContext(master="local[*]")
    rdd = sc.parallelize([[1], [1, 2], [1, 2, 3]])
    print(rdd.flatMap(lambda x: [i**2 for i in x]).collect())

Output:

    [1, 1, 4, 1, 4, 9]

# **Apply a function to each value of a key-value pair RDD**

This group of methods require input RDD to be a **key-value pair RDD**. Each value is passed through the map function without changing the keys.

## **`mapValues()`**

    from pyspark import SparkContext
    sc = SparkContext(master="local[*]")
    
    rdd = sc.parallelize([('a', 1), ('b', 2), ('c', 3)])    # create a key-value pair RDD
    print(rdd.mapValues(lambda x: x**2).collect())

Output:

    [('a', 1), ('b', 4), ('c', 9)]

## `flatMapValues()`

    sc = SparkContext(master="local[*]")
    
    rdd = sc.parallelize([('a', [1, 2, 3]), ('b', [4, 5]), ('c', [6])])    # create a key-value pair RDD
    print(rdd.flatMapValues(lambda x: [i**2 for i in x]).collect())

Output:

    [('a', 1), ('a', 4), ('a', 9), ('b', 16), ('b', 25), ('c', 36)]

# **Apply a function to each partition**

For this group of methods, RDD first turn each element into an iterator and then use a generator to yield these iterators (elements) from each partition. Therefore, the map function provided should be able to take in a generator as input. Remember that elements yielded from the generator are iterator object. If you have functions inside the map function that directly operate on the yielded elements, they should be functions that are available to take in iterator as argument.

## **`mapPartitions()`**

    sc = SparkContext(master="local[*]")
    
    rdd = sc.parallelize([1, 2, 3, 4, 5, 6], numSlices=4) # create an RDD with 4 partitions
    # define a map function to get sum of all elements in each partition
    def map_sum(iterator):
        yield sum(iterator)
    
    # define a map function to count the number of elements in each partition
    def map_len(iterator):
        yield len(list(iterator))
    
    print('Sum in each partition: {}'.format(rdd.mapPartitions(map_sum).glom().collect()))
    print('Number of elements in each partition: {}'.format(rdd.mapPartitions(map_len).glom().collect()))

Output:

    Sum in each partition: [[1], [5], [4], [11]]
    Number of elements in each partition: [[1], [2], [1], [2]]

Here we defined two map functions. In each function, we used yield instead of return since the input to the map function is a **generator**. Inside the first map function, we called sum() which operates on iterator object. Inside the second map function, we called len() which does not take iterator as input. We first convert iterator to a list then apply len() to it.

If you just want to apply some operations with side effect, use `foreachPartitions()`