# Subset RDD

In this section we explore RDD methods that subset an RDD. The new RDD has less elements than the old RDD. However, the methods do not perform any calculation on individual elements.

# **Extract elements by order**

## `first()`

This method returns the first element of an RDD.

    from pyspark import SparkContext
    sc = SparkContext(master="local[*]")
    
    print(sc.parallelize([1, 2, 3, 4]).first())

Output:

    1

## `top()`

This method first sort all the elements in descending order, and then return the top N elements.

    from pyspark import SparkContext
    sc = SparkContext(master="local[*]")
    
    print(sc.parallelize([4, 5, 8, 1, 2, 3]).top(2))

Output:

    [8, 5]

# Extract elements randomly

## `sample()`

Randomly select a fraction of elements from an RDD.

    from pyspark import SparkContext
    sc = SparkContext(master="local[*]")
    
    print(sc.parallelize(range(20)).sample(False, 0.5, seed=123).collect())

Output:

    [5, 6, 7, 8, 9, 12, 14, 15, 17]

## `sampleByKey()`

Randomly select a fraction of each key-group elements from an RDD.

    from pyspark import SparkContext
    sc = SparkContext(master="local[*]")
    
    rdd = sc.parallelize([('a', range(0, 10)), ('b', range(10, 20)), ('c', range(20, 30))]).flatMapValues(lambda x: x)
    fractions = {'a': 0.5, 'b': 0.3, 'c': 0.6}
    print(rdd.sampleByKey(False, fractions, seed=123).collect())

Output:

    [('a', 0), ('a', 3), ('a', 5), ('a', 6), ('a', 8), ('b', 10), ('b', 11), ('b', 15), ('c', 21), ('c', 22), ('c', 23), ('c', 25), ('c', 26), ('c', 27), ('c', 28)]

# Extract elements by function return

## `filter()`

Pass each elements to a function, if the function returns True, that element is selected.

    from pyspark import SparkContext
    sc = SparkContext(master="local[*]")
    
    rdd = sc.parallelize([1, 2, 3, 4, 5])
    print(rdd.filter(lambda x: x % 2 == 0).collect())

Output:

    [2, 4]