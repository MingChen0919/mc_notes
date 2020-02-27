# H2O, Spark, and Sparkling Water

This wiki is built in Notion. Here are all the tips you need to contribute.

# What is H2O?

H2O is an in-memory, distributed cluster that provides capability to build machine learning models on big data.

Inside H2O, a **Distributed Key/Value (DKV)** store is used to access and reference data, models, objects, etc., across all nodes/machines. The algorithms are implemented in a map reduce style and utilize the Java Fork/Join framework.

The data is read in parallel and is distributed across the cluster, stored in memory in a columnar format in a compressed way.

H2O’s REST API allows access to all the capabilities of H2O from an external program or script, via JSON over HTTP. The REST API is used by H2O’s web interface and other language bindings (like H2O-Python).

# What is Spark?

Spark is also an in-memory, distributed cluster for providing comprehensive capability of data munging and machine learning implementation. The fast and unified framework to manage data processing, makes Spark a preferred solution for big data analysis.

In general, Spark is better than H2O at data manipulation while H2O is better than Spark at machine learning implementation. So we want to bring together the advantages of both H2o and Spark. Basically, we want to prepare our data in Spark and then build machine learning models on the data with H2O. This can be achieved with the help of **Sparkling Water**.

# What is Sparkling Water?

Sparkling Water is an integration of H2O into the Spark ecosystem. It is designed as a regular Spark application and provides a way to **start H2O services on each node of a Spark cluster and access data stored in data structures of Spark and H2O**.

Sparkling Water creates an *H2OContext* that is used to **start H2O services on the Spark executors**. An *H2OContext* is a connection to H2O cluster and also facilitates communication between H2O and Spark.

Sparkling Water also enables low cost data copying between H2O and Spark.

Next  Previous