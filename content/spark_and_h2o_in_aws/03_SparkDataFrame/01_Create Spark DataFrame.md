# Create Spark DataFrame

## Create a SparkSession object

A **DataFrame** is a distributed collection of data grouped into named columns. It is equivalent to a relational table in Spark SQL, and can be created using various functions in **SparkSession**.

To create a DataFrame, we need to create a SparkSession object first:

    from pyspark.sql import SparkSession
    
    spark = SparkSession.builder \
        .master("local") \
        .getOrCreate()
    
    print(type(spark))

Output:

    <class 'pyspark.sql.session.SparkSession'>

## Create a DataFrame

Below are the two main options for creating a DataFrame using the entry point **SparkSession**.

- Use `SparkSession.createDataFrame()`
- Use `[SparkSession.read](http://sparksession.read)`

### Use `SparkSession.createDataFrame()`

We can create a DataFrame from an **RDD**, a **list** or a **pandas.DataFrame**.

- **From an RDD**

    When creating a DataFrame from an RDD, the elements in the RDD have to be a **`pyspark.sql.Row`**.

        from pyspark.sql import SparkSession
        from pyspark import SparkContext
        from pyspark.sql import Row
        
        sc = SparkContext()
        spark = SparkSession.builder \
            .master("local") \
            .getOrCreate()
        
        # create an RDD in which elements are pyspark.sql.Row objects
        rdd = sc.parallelize([
            Row(a=1, b=2),
            Row(a=0, b=3),
            Row(a=4, b=1)
        ])
        df = spark.createDataFrame(rdd)
        print(df.show())

    Output:

        +---+---+
        |  a|  b|
        +---+---+
        |  1|  2|
        |  0|  3|
        |  4|  1|
        +---+---+

- **From a List**

    When creating a DataFrame from a list, the list is a 2-D list. Elements in the 2-D list should have same data type.

    An example of 2-D list with same data type in each column:

        l = [['a', 1, Row(x=1, y=2)],
             ['b', 2, Row(x=3, y=4)],
             ['c', 3, Row(x=5, y=6)]]

    Let's see how we can create a DataFrame from the above list.

        from pyspark.sql import SparkSession
        from pyspark.sql import Row
        
        spark = SparkSession.builder \
            .master("local") \
            .getOrCreate()
        
        
        l = [['a', 1, Row(x=1, y=2)],
             ['b', 2, Row(x=3, y=4)],
             ['c', 3, Row(x=5, y=6)]]
        
        df = spark.createDataFrame(l, schema=['c1', 'c2', 'c3'])
        print(df.show())

    Output:

        +---+---+------+
        | c1| c2|    c3|
        +---+---+------+
        |  a|  1|[1, 2]|
        |  b|  2|[3, 4]|
        |  c|  3|[5, 6]|
        +---+---+------+

- **From a pandas.DataFrame**

    Create a DataFrame from pandas.DataFrame is simple. We just pass a pandas.DataFrame to the `createDataFrame()`.

        from pyspark.sql import SparkSession
        from pyspark.sql import Row
        import pandas as pd
        
        spark = SparkSession.builder \
            .master("local") \
            .getOrCreate()
        
        pandas_df = pd.DataFrame({
            'c1': ['a', 'b', 'c'],
            'c2': [1, 2, 3],
            'c3': [Row(x=1, y=2), Row(x=3, y=4), Row(x=5, y=6)]
        })
        
        df = spark.createDataFrame(pandas_df)
        print(df.show())

    Output:

        +---+---+------+
        | c1| c2|    c3|
        +---+---+------+
        |  a|  1|[1, 2]|
        |  b|  2|[3, 4]|
        |  c|  3|[5, 6]|
        +---+---+------+

### Use `SparkSession.read`

[`SparkSession.read`](http://sparksession.read) returns a `pyspark.sql.DataFrameReader` **class which has a lot of methods for reading data from files and database as a DataFrame**. Below are a list of those methods:

- `csv()`: read from csv files
- `jdbc()`: construct a DataFrame representing the database table named table accessible via JDBC URL url and connection properties
- `json()`: loas json files
- `orc()`: loads ORC files
- `parquet()`: loads Parquet files
- `text()`: load text files and returns a DataFrame

We use `csv()` as an example to show how DataFrame can be created through `pyspark.sql.DataFrameReader`.

    from pyspark.sql import SparkSession
    from pyspark.sql import Row
    import pandas as pd
    from tempfile import mkstemp
    
    spark = SparkSession.builder \
        .master("local") \
        .getOrCreate()
    
    # create a dataset and save it to a csv file
    _, file_path = mkstemp(suffix='.csv')
    pandas_df = pd.DataFrame({
        'c1': ['a', 'b', 'c'],
        'c2': [1, 2, 3],
        'c3': [Row(x=1, y=2), Row(x=3, y=4), Row(x=5, y=6)]
    })
    pandas_df.to_csv(file_path, index=False)
    
    print('Reading data from {}'.format(file_path))
    print('-'*50)
    # use pyspark.DataFrameReader to import data as a DataFrame
    df = spark.read.csv(file_path, sep=',', header=True, inferSchema=True)
    print(df.show())

Output:

    Reading data from /var/folders/mv/122vn3nn0kx39q71g1sx5wkh0000gn/T/tmp6_z5xi3g.csv
    ----------------------------------------------------------------------------------------------------
    +---+---+-------------+
    | c1| c2|           c3|
    +---+---+-------------+
    |  a|  1|Row(x=1, y=2)|
    |  b|  2|Row(x=3, y=4)|
    |  c|  3|Row(x=5, y=6)|
    +---+---+-------------+