# Connect H2O Cluster Through PySparkling

We want to launch an H2O cluster through pysparkling so that we can use Spark APIs to manipulate data and H2O APIs to implement machine learning models.

- Create `SparkContext` and `H2OContext`

    We connect to H2O cluster from Spark cluster, so we need a `SparkContext`.

        from pyspark import SparkContext
        from pysparkling import H2OContext
        
        sc = SparkContext(master='local')
        hc = H2OContext.getOrCreate(sc)

- Test h2o connection

    Now we have a connection to the H2O cluster, we can use the APIs

        import h2o
        
        df = h2o.import_file("http://h2o-public-test-data.s3.amazonaws.com/smalldata/iris/iris_wheader.csv")
        print(df)

    Output:

        sepal_len    sepal_wid    petal_len    petal_wid  class
        -----------  -----------  -----------  -----------  -----------
                5.1          3.5          1.4          0.2  Iris-setosa
                4.9          3            1.4          0.2  Iris-setosa
                4.7          3.2          1.3          0.2  Iris-setosa
                4.6          3.1          1.5          0.2  Iris-setosa
                5            3.6          1.4          0.2  Iris-setosa
                5.4          3.9          1.7          0.4  Iris-setosa
                4.6          3.4          1.4          0.3  Iris-setosa
                5            3.4          1.5          0.2  Iris-setosa
                4.4          2.9          1.4          0.2  Iris-setosa
                4.9          3.1          1.5          0.1  Iris-setosa
        
        [150 rows x 5 columns]