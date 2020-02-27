# Create H2OFrame

H2OFrame is similar to pandas’ `DataFrame`, or R’s data.frame. One of the critical distinction is that the data is generally not held in memory, instead it is located on a (possibly remote) H2O cluster, and thus H2OFrame `represents a mere handle to that data`.

# Create H2OFrame From a Python Ojbect

The following types are permissible for *python object.*

- `tuple` ()
- `list` []
- `dict` {}
- `collections.OrderedDict`
- `numpy.ndarray`
- `pandas.DataFrame`

- **From a 1-D list/tuple**

        l = [1, 2, 3]
        H2OFrame(l)

    Output:

        C1
        ----
           1
           2
           3

- **From a dictionary: `{name: list}`**

        d = {
            'a': [1, 2, 3]
        }
        H2OFrame(d)

    Output:

        a
        ---
          1
          2
          3

- **From a 2-D flat list/array**

        l_2d = [['a', 1, 4],
                ['b', 2, 5],
                ['c', 3, 6]]
        H2OFrame(l_2d)

    Output:

        C1      C2    C3
        ----  ----  ----
        a        1     4
        b        2     5
        c        3     6

- **From a pandas DataFrame**

        pdf = pd.DataFrame({
            'a': [1, 2, 3],
            'b': ['x', 'y', 'z']
        })
        H2OFrame(pdf)

    Output:

        a  b
        ---  ---
          1  x
          2  y
          3  z

# Create H2OFrame by importing from a file

Load data using either `[h2o.import_file](http://docs.h2o.ai/h2o/latest-stable/h2o-py/docs/h2o.html#h2o.import_file)` or `[h2o.upload_file](http://docs.h2o.ai/h2o/latest-stable/h2o-py/docs/h2o.html#h2o.upload_file)`.

- `[h2o.import_file](http://docs.h2o.ai/h2o/latest-stable/h2o-py/docs/h2o.html#h2o.import_file)` uses cluster-relative names and ingests data in parallel.
- `[h2o.upload_file](http://docs.h2o.ai/h2o/latest-stable/h2o-py/docs/h2o.html#h2o.upload_file)` uses Python client-relative names and single-threaded file upload from the client.