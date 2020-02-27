# Aggregation Functions

RDD provides methods that aggregate elements in two ways:

- aggregate elements within partitions first, and then aggregate results from each partition
- aggregate elements within key-based groups first, and then aggregate results from each of those groups.

No matter which way, RDD elements are aggregated in **two steps:** 

- step 1: **within-group elements aggregation,**
- step 2: **between-group aggregation**.

Here a **group** can be a ***partition*** or a ***key***. RDD provides methods that allows us to 

- provide a single aggregation function for both steps; or
- provide separate aggregation functions for each step.

# **How aggregation function works?**

We use an example to explain how aggregation function works. Elements in an RDD can be treated as being grouped either by partition or key (in key-value pair RDD).

## Elements in a 2-partitions RDD

    [[1, 2, 3], [4, 5, 6]]

## Aggregation function

Generally, an aggregation function takes in two elements: 

- 1. a neutral zero value predefined by user;
- 2. an RDD element.

In step 1, RDD element is literally an RDD element. In step 2, RDD element is an aggregated value from a partition or key-based group.

    def agg(zeroValue, rdd_element):
        return zeroValue + rdd_element

Assuming zeroValue=0, the step 1 aggregation is:

    [agg(agg(agg(0, 1), 2), 3), agg(agg(agg(0, 4), 5), 6)] = [6, 15]

After step 1 aggregation, the new RDD has two elements: [6, 15]. In step 2 aggregation:

    agg(agg(0, 6), 15) = 21

# Aggregate by partitions

## Single aggregation function: `fold()`

    from pyspark import SparkContext
    
    sc = SparkContext(master="local[*]")
    rdd = sc.parallelize([1, 2, 3, 4, 5, 6], numSlices=2)   # a 2-partition RDD
    # the aggregation function basically aggregate elements by addition
    def agg(zeroValue, rdd_element):
        return zeroValue + rdd_element
    zeroValue = 0
    print(rdd.fold(zeroValue, agg))

Output:

    21

## Separate aggregation functions: `aggregation()`

This method allows us to define two separate aggregation functions for each of the two steps. In the following example, the first aggregation function adds up the numbers in each partitions; the second aggregation function counts how many partition sums can be evenly divided by 2.

    from pyspark import SparkContext
    
    sc = SparkContext(master="local[*]")
    rdd = sc.parallelize([1, 1, 1, 2, 2, 2, 3, 3, 3], numSlices=3)  # define a 3-partitions RDD
    # first aggregation function to sum up the numbers in each partition
    def agg_step_1(zeroValue, rdd_element):
        return zeroValue + rdd_element
    
    # second aggregation function to count how many partition sums can be evenly divided by 2
    def agg_step_2(zeroValue, rdd_element):
        if rdd_element % 2 == 0:
            return zeroValue + 1
        else:
            return zeroValue
    
    zeroValue = 0
    print(rdd.aggregate(zeroValue, agg_step_1, agg_step_2))

- Partition 1: 1 + 1 + 1 = 3; 3 % 2 = 1
- Partition 2: 2 + 2 + 2 = 6; 6 % 2 = 0
- Partition 3: 3 + 3 + 3 = 9; 9 % 2 = 1

Therefore, only the sum of partition 2 can be evenly divided by 2.

Output:

    1

# **Aggregate by keys**

## S**ingle aggregation function: `foldByKey()`**

    from pyspark import SparkContext
    
    sc = SparkContext(master="local[*]")
    rdd = sc.parallelize([
        ('a', range(1, 11)),
        ('b', range(11, 21)),
        ('c', range(21, 31))
    ]).flatMapValues(lambda x: x)
    print(rdd.foldByKey(0, lambda x, y: x + y).collect())

Output:

    [('b', 155), ('c', 255), ('a', 55)]

## S**eparate aggregation functions: `aggregateByKey()`**

    from pyspark import SparkContext
    
    sc = SparkContext(master="local[*]")
    rdd = sc.parallelize([
        ('a', range(1, 11)),
        ('b', range(11, 21)),
        ('c', range(21, 31))
    ]).flatMapValues(lambda x: x)
    
    
    def agg_1(zeroValue, rdd_element):
        return zeroValue + rdd_element
    
    
    def agg_2(zeroValue, rdd_element):
        return zeroValue + rdd_element
    
    
    zeroValue = 0
    print(rdd.aggregateByKey(zeroValue, agg_1, agg_2).collect())

Output:

    [('b', 155), ('c', 255), ('a', 55)]