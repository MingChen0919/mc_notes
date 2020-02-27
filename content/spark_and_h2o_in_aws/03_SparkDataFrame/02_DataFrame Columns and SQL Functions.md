# DataFrame Columns and SQL Functions

A `pyspark.sql.Column` **represents** a column in a DataFrame. Column instances can be created by:

1. select a column out of a DataFrame
2. create from an **expression**

Many functions from the **pyspark.sql** module and almost all the functions from the **pyspark.sql.functions** module apply to `pyspark.sql.Column` and returns a Column **expression**.

> An **expression** in a programming language is a combination of one or more constants, variables, operators, and functions that the programming language interprets (according to its particular rules of precedence and of association) and computes to produce ("to return", in a stateful environment) another value.

**Column expressions are used by DataFrame APIs to manipulate and transform DataFrames.**

# Create a **`Column`** instance

Let's first create an example DataFrame

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

## 1. Select a `Column` out of a DataFrame

    print('Option 1: {}'.format(type(df.c1)))
    print('Option 2: {}'.format(type(df["c1"])))

Output:

    Option 1: <class 'pyspark.sql.column.Column'>
    Option 2: <class 'pyspark.sql.column.Column'>

## 2. Create from an expression

The `Column` class has implemented many methods that manipulate a Column instance and return a new Column expression. Functions from the `pyspark.sql.functions` module also take a Column expression as input and return a new Column expression.

### Methods from **`Column`** class

Below are just a couple of examples of using methods from `Column` class to create new Column expressions. There are many other methods available from the class.

    print(type(df.c1.like('ora%')))
    print(type(df.c2.desc()))

Output:

    <class 'pyspark.sql.column.Column'>
    <class 'pyspark.sql.column.Column'>

### Functions from `pyspark.sql.functions` module

Most of functions from the `pyspark.sql.functions` module take in a Column expression and return a new Column expression. Let's see a few examples:

    print(type(F.concat_ws('-', df.c1, df.c2)))
    print(type(F.when(df.c2 > 2, 0).otherwise(1)))

Output:

    <class 'pyspark.sql.column.Column'>
    <class 'pyspark.sql.column.Column'>

# Evaluate Column Expressions

**Column expressions** are just expressions. Before they are evaluated, no operations occur to any variables and objects. To use those column expressions to manipulate `DataFrame`s, we need to evaluate them.

We use `pyspark.sql.DataFrame.select()` to project (evaluate) these Column expressions.

In the previous sections, we have created the following Column expressions:

    c1 = df.c1  # select `c1` column out of DataFrame df
    col_exp_like = df.c1.like('ora%')   # filter df rows by using column `c1`
    col_exp_desc = df.c2.desc() # sort df by column `c2`
    col_exp_concat = F.concat_ws('-', df.c1, df.c2) # concatenate column `c1` and `c2` with
    col_exp_when = F.when(df.c2 > 2, 0).otherwise(1) # create a new column expression based on values on column `c2`

All Column expressions above except for the `df.c2.desc()` can be passed to select() for evaluation. `df.c2.desc()` is a sort expression which usually work with `orderBy()`.

    c1 = df.c1  # select `c1` column out of DataFrame df
    col_exp_like = df.c1.like('ora%')   # filter df rows by using column `c1`
    col_exp_desc = df.c2.desc() # sort df by column `c2`
    col_exp_concat = F.concat_ws('-', df.c1, df.c2) # concatenate column `c1` and `c2` with
    col_exp_when = F.when(df.c2 > 2, 0).otherwise(1)
    
    all_cols = [c1, col_exp_like, col_exp_concat, col_exp_when]
    new_df = df.select(all_cols)
    print(new_df.show())

Output:

    +------+------------+--------------------+------------------------------------+
    |    c1|c1 LIKE ora%|concat_ws(-, c1, c2)|CASE WHEN (c2 > 2) THEN 0 ELSE 1 END|
    +------+------------+--------------------+------------------------------------+
    |orange|        true|            orange-1|                                   1|
    | apple|       false|             apple-2|                                   1|
    | grape|       false|             grape-3|                                   0|
    +------+------------+--------------------+------------------------------------+

To evaluate `df.c2.desc()`:

    print(df.orderBy(df.c2.desc()).show())

Output:

    +------+---+------+
    |    c1| c2|    c3|
    +------+---+------+
    | grape|  3|[5, 6]|
    | apple|  2|[3, 4]|
    |orange|  1|[1, 2]|
    +------+---+------+