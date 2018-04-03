# Install Spark 2.3 Locally

Spark runs on Java 8+, Python 2.7+/3.4+ and R 3.1+. For the Scala API, Spark 2.3.0 uses Scala 2.11. 

## Download Spark

[ Link ]( https://spark.apache.org/downloads.html )


## Java

All you need is to have java installed on your system PATH, or the JAVA_HOME environment variable pointing to a Java installation.

```shell
java -version 
```

## Scala

Download the Scala binaries for windows -- you will need Scala 11.x (not 10.x or 12.x) for Spark 2.3

- [Latest Scala]( http://www.scala-lang.org/download/ )
- [Scala version 2.11.12]( https://www.scala-lang.org/download/2.11.12.html )

Test correct installation of scala:

```shell
scala -version
```

Set PATH for Scala if needed:

```shell
export PATH = $PATH:/usr/local/scala/bin
```

Test that Spark is properly installed:

```shell
./bin/spark-shell --master local[2]
```

On Windows, use CMD or PowerShell, not git bash


## Error: Failure to locate the winutils binary in the hadoop binary path

- HADOOP_HOME (or the variable hadoop.home.dir property) needs to be set properly.
- Known Hadoop for Windows issue: winutils is not included in the Apache distribution


You can fix this problem in two ways

- Install a full native windows Hadoop version. The ASF does not currently release such a version; releases are available externally.
Or: get the WINUTILS.EXE binary from a Hadoop redistribution. There is a repository of this for some Hadoop versions on github.

Then

- Set the environment variable %HADOOP_HOME% to point to the directory above the BIN dir containing WINUTILS.EXE.
- Or: run the Java process with the system property hadoop.home.dir set to the home directory.


[Explanation on Hadoop Wiki]( https://wiki.apache.org/hadoop/WindowsProblems )

[Stack Overflow]( https://stackoverflow.com/questions/19620642/failed-to-locate-the-winutils-binary-in-the-hadoop-binary-path?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa )

[Windows binaries for some Hadoop versions]( https://github.com/steveloughran/winutils )


## Run Spark on the local machine

To run Spark interactively in a Python interpreter, use ``bin/pyspark``:

```sh
./bin/pyspark --master local[2]
```

Or submit Spark jobs:

```bash
./bin/spark-submit examples/src/main/python/pi.py 10
```


## Additional Links

[Spark Installation Tutorial]( https://www.tutorialspoint.com/apache_spark/apache_spark_installation.htm )

