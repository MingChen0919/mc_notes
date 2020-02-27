# Create Virtual Environment and Install Packages

First step is to create an empty folder as your working directory. Within that directory we create a python virtual environment to handle all dependencies.

**Create virtual environment *venv***

    python -m venv venv

**Activate virtual environment**

    . venv/bin/activate

# Install packages

**Install H2O, Spark and AWS interaction packages**

    pip install h2o pyspark
    pip install sagemaker boto3

**Install Pysparkling**

Although there is a pysparkling package in PyPI ([https://pypi.org/project/pysparkling/](https://pypi.org/project/pysparkling/)), it is NOT the python package for Sparkling Water. Below is the code you need to install an H2O Pysparkling version (see [https://s3.amazonaws.com/h2o-release/sparkling-water/spark-2.4/3.28.0.1-1-2.4/index.html](https://s3.amazonaws.com/h2o-release/sparkling-water/spark-2.4/3.28.0.1-1-2.4/index.html)).

    pip install h2o_pysparkling_2.4