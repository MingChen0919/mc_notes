# User Defined Functions (UDF)

User Defined Functions are customized `pyspark.sql.functions` that operate on Column expressions and return a new Column expression. If there isn't any built-in `pyspark.sql.functions` available for us to manipulate DataFrame the way we want, we can define a customized sql function to achieve the goal with `udf()`.

**Two steps to use `udf()`:**

1. define a custom function

        def foo(x: int):
        	return x + 3

2. convert custom function to a sql function with `udf()`

        from pyspark.sql.functions import udf
        from pyspark.sql.types import *
        
        foo_udf = udf(foo, returnType=IntegerType())

The most challenging thing for using `udf()` is to correctly identify the **returnType** for the custom function. Next, I will provide examples of UDFs that return different data types.

We create the following DataFrame to play with:

    from pyspark.sql import SparkSession
    from pyspark.sql import Row
    import pandas as pd
    
    
    spark = SparkSession.builder \
        .master("local") \
        .getOrCreate()
    
    pandas_df = pd.DataFrame({
        'c1': ['orange', 'apple', 'grape'],
        'c2': [1, 2, 3],
        'c3': [Row(x=1, y=2), Row(x=3, y=4), Row(x=5, y=6)]
    })
    df = spark.createDataFrame(pandas_df)
    print(df.show())

Output:

    +------+---+------+                                                             
    |    c1| c2|    c3|
    +------+---+------+
    |orange|  1|[1, 2]|
    | apple|  2|[3, 4]|
    | grape|  3|[5, 6]|
    +------+---+------+

# Return an integer: `IntegerType()`

- Define a function to calculate the **length of** **column c1**

        def foo(x):
            return len(x)

- Convert the function `foo` to a `udf` function

        foo_udf = F.udf(foo, returnType=IntegerType())

- Apply the `udf` function

        df.select(foo_udf(df.c1)).show()

    Output:

        +-------+
        |foo(c1)|
        +-------+
        |      6|
        |      5|
        |      5|
        +-------+

# Return a float: `FloatType()`

- Define a function to **multiply column c2 by 0.5**

        def foo(x):
            return x * 0.5

- Convert the function `foo` to a `udf` function

        foo_udf = F.udf(foo, returnType=FloatType())

- Apply the `udf` function

        df.select(foo_udf(df.c2)).show()

    Output:

        +-------+
        |foo(c2)|
        +-------+
        |    0.5|
        |    1.0|
        |    1.5|
        +-------+

# Return a str: `StringType()`

- Define a function to replicate string in column c1 by N times, where N is the value in column c2

        def foo(c1, c2):
            return c1 * c2

- Convert the function `foo` to a `udf` function

        foo_udf = F.udf(foo, returnType=StringType())

- Apply the `udf` function

        df.select(foo_udf(df.c1, df.c2)).show(

    Output:

        +---------------+
        |    foo(c1, c2)|
        +---------------+
        |         orange|
        |     appleapple|
        |grapegrapegrape|
        +---------------+

# Return a list of homogeneous elements: `ArrayType()`

When the User Defined Function return an array-like value in which all elements have the same data type, we use this scheme.

- Define a function to make N copies of the string in column c1 and put them in a list, where N is the number in column c2

        def foo(c1, c2):
            return [c1] * c2

- Convert the function `foo` to a `udf` function

    The function `foo()` returns a list. All elements in the list are `str`. Therefore, the `returnType` should be `ArrayType(StringType())`.

        foo_udf = F.udf(foo, returnType=ArrayType(StringType()))

- Apply the `udf` function

        df.select(foo_udf(df.c1, df.c2)).show(truncate=False)

    Output:

        +---------------------+
        |foo(c1, c2)          |
        +---------------------+
        |[orange]             |
        |[apple, apple]       |
        |[grape, grape, grape]|
        +---------------------+

# Return a list of heterogeneous elements: `StructType()`

If the User Defined Function returns a list of elements which are heterogeneous in type, we use `StructType()`. The example below uses a `udf` function to merge a string column and an integer column. The value in the string column is copied N times and put in a list, the return value is in the format of `[ArrayType(StringType), IntegerType]`.

- Define User Defined Function

        def foo(c1, c2):
            return [[c1] * c2, c2]

- Convert the function `foo` to a `udf` function

    In the return expression of the `foo` function

    - `[c1] * c2` is a list of strings
    - `c2` is an integer

        # Define the return type
        return_type = StructType([
            StructField('f1', ArrayType(StringType())),
            StructField('f2', IntegerType())
        ])
        
        foo_udf = F.udf(foo, returnType=return_type)

- Apply the `udf` function

        df.select(foo_udf(df.c1, df.c2)).show(truncate=False)

    Output:

        +--------------------------+
        |foo(c1, c2)               |
        +--------------------------+
        |[[orange], 1]             |
        |[[apple, apple], 2]       |
        |[[grape, grape, grape], 3]|
        +--------------------------+