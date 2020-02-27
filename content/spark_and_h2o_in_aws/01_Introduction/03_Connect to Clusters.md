# Connect to Clusters

# Connect to H2O cluster

You connect to a cluster through 

1. IP address and port number; 

2. URL where the cluster is running. Assuming an H2O cluster is running at [http://127.0.0.1:54321](http://127.0.0.1:54321/). You can connect to it in two ways:

**Option 1:**

    import h2o
    h2o.connect(ip=127.0.0.1, port=54321,  verbose=True)

**Option 2:**

    import h2o
    h2o.connect(http="http://127.0.0.1:54321", https=True, verbose=True)

You can launch a cluster locally and connect to it.

    import h2o
    h2o.init(ip="localhost", port=54321)

Output:

    Checking whether there is an H2O instance running at http://localhost:54321 ..... not found.
    Attempting to start a local H2O server...
      Java Version: openjdk version "1.8.0_222"; OpenJDK Runtime Environment (AdoptOpenJDK)(build 1.8.0_222-b10); OpenJDK 64-Bit Server VM (AdoptOpenJDK)(build 25.222-b10, mixed mode)
      Starting server from /Users/mingchen/path/to/venv/lib/python3.7/site-packages/h2o/backend/bin/h2o.jar
      Ice root: /var/folders/mv/122vn3nn0kx39q71g1sx5wkh0000gn/T/tmpbip7r_4a
      JVM stdout: /var/folders/mv/122vn3nn0kx39q71g1sx5wkh0000gn/T/tmpbip7r_4a/h2o_mingchen_started_from_python.out
      JVM stderr: /var/folders/mv/122vn3nn0kx39q71g1sx5wkh0000gn/T/tmpbip7r_4a/h2o_mingchen_started_from_python.err
      Server is running at http://127.0.0.1:54321
    Connecting to H2O server at http://127.0.0.1:54321 ... successful.
    --------------------------  ------------------------------------------------------------------
    H2O cluster uptime:         02 secs
    H2O cluster timezone:       America/New_York
    H2O data parsing timezone:  UTC
    H2O cluster version:        3.28.0.1
    H2O cluster version age:    23 days
    H2O cluster name:           H2O_from_python_mingchen_9plyn9
    H2O cluster total nodes:    1
    H2O cluster free memory:    7.111 Gb
    H2O cluster total cores:    16
    H2O cluster allowed cores:  16
    H2O cluster status:         accepting new members, healthy
    H2O connection url:         http://127.0.0.1:54321
    H2O connection proxy:       {'http': None, 'https': None}
    H2O internal security:      False
    H2O API Extensions:         Amazon S3, XGBoost, Algos, AutoML, Core V3, TargetEncoder, Core V4
    Python version:             3.7.3 final
    --------------------------  ------------------------------------------------------------------
    Closing connection _sid_a42f at exit
    H2O session _sid_a42f closed.

# Connect to Spark cluster

Similar to H2O, you connect to a Spark cluster through a master URL, which can be in one of the following formats:

[Untitled](https://www.notion.so/76e4fe40a8514ca0a92d8c2058b8ca9d)

    from pyspark import SparkConf, SparkContext
    sc = SparkContext(master='local[*]')
    spark = SparkSession(sparkContext=sc)

- SparkContext represents the connection to a Spark cluster. It is the main entry point for Spark functionality.
- SparkSession is the entry point to programming Spark with the Dataset and DataFrame API.

***SparkContext*** is like the front door to the Spark cluster house, while ***SparkSession*** is like a door to a room within the Spark cluster house.

By default, Spark Web UI uses port **4040**. You can access it through master url:4040. In local model, it is localhost:4040.

# Connect through PySparkling

***Pysparkling*** enables starting H2O services on Spark. You just need to provide a SparkContext or SparkSession object.

    from pyspark import SparkContext
    from pyspark.sql import SparkSession
    from pysparkling import H2OContext
    import h2o
    
    sc = SparkContext(master='local')
    spark = SparkSession(sc)
    H2OContext.getOrCreate(sc)  # start H2O services
    print(h2o.H2OFrame([[1,2,3], [4, 5, 6]]))   # now you can use h2o APIs