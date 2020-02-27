# Create RDD

# Use SparkContext.parallelize()

parallelize() distribute a local python collection to form an RDD. Common built-in python collections include dist, list, tuple or set.

    from pyspark import SparkContext
    
    sc = SparkContext(master="local[*]")
    rdd = sc.parallelize([1, 2, 3])
    print(rdd.collect())

Output:

    [1, 2, 3]

# Use SparkContext.textFile()

Read a text file from HDFS, a local file system (available on all nodes), or any Hadoop-supported file system URI, and return it as an RDD of Strings. Each line of the text file is an element of the RDD object.

    from pyspark import SparkContext
    from tempfile import gettempdir
    import os
    
    sc = SparkContext(master="local[*]")
    path = os.path.join(gettempdir(), 'test_file.txt')
    print(path)
    with open(path, "w") as f:
        _ = f.write("1st row\n2nd row\n3rd row")
    test_file = sc.textFile(path)
    print(test_file.collect())

Output:

    ['1st row', '2nd row', '3rd row']

# Create RDD from a DataFrame

TODO