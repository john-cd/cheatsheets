# Install Spark Locally

Modern Spark (3.x and 4.x) runs on Java 17+, Python 3.10+ and R 4.x+. For the Scala API, Spark uses Scala 2.12 or 2.13.

## Download Spark

[Download Apache Spark](https://spark.apache.org/downloads.html)

## Prerequisites

### Java

You need to have Java installed on your system PATH, or the `JAVA_HOME` environment variable pointing to a Java installation. Modern Spark versions recommend Java 17.

```shell
java -version
```

### Python

For PySpark, you need a modern Python environment (Python 3.10+).

```shell
python3 --version
```

## Running Spark Locally

Test that Spark is properly installed by running the Scala shell:

```shell
./bin/spark-shell --master local[2]
```

### PySpark

To run Spark interactively in a Python interpreter, use `bin/pyspark`:

```shell
./bin/pyspark --master local[2]
```

Or submit Spark jobs:

```bash
./bin/spark-submit examples/src/main/python/pi.py 10
```

## Running on Windows (WSL is Recommended)

The recommended way to run Spark on Windows is via **Windows Subsystem for Linux (WSL2)**.
Running Spark natively on Windows requires additional setups (like downloading `winutils.exe` and setting `HADOOP_HOME`), which can be problematic. WSL provides a native Linux environment making Spark installation straightforward.

1. Install WSL2 and Ubuntu.
2. Install Java: `sudo apt install openjdk-17-jdk`
3. Download and extract Spark tarball.
4. Run `spark-shell` or `pyspark`.
