# Spark Basics

- [Main Web Site](https://spark.apache.org/)
- [Apache Spark on Wikipedia](https://en.wikipedia.org/wiki/Apache_Spark)

## Creating a SparkSession

Since Spark 2.x, `SparkSession` is the entry point for reading data and executing SQL queries over data.

**Scala:**

```scala
import org.apache.spark.sql.SparkSession

val spark = SparkSession.builder()
  .appName("SparkBasics")
  .master("local[*]")
  .config("spark.some.config.option", "some-value")
  .getOrCreate()
```

**Python (PySpark):**

```python
from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("SparkBasics") \
    .master("local[*]") \
    .getOrCreate()
```

## Useful Links

- [Official Quick Start](https://spark.apache.org/docs/latest/quick-start.html)
- [RDD Programming Guide](https://spark.apache.org/docs/latest/rdd-programming-guide.html)
- [Spark SQL, DataFrames and Datasets Guide](https://spark.apache.org/docs/latest/sql-programming-guide.html)
- [Spark on AWS EMR](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-spark.html)
- [Databricks Reference Apps](https://www.gitbook.com/book/databricks/databricks-spark-reference-applications/details)

## Spark Connectors

- [MongoDB Spark connector](https://www.mongodb.com/products/spark-connector)
- [Elasticsearch Hadoop (for Spark)](https://www.elastic.co/guide/en/elasticsearch/hadoop/current/spark.html)

## Ecosystem Integrations

- **Graph Processing:** [Graphx programming guide](https://spark.apache.org/docs/latest/graphx-programming-guide.html)
- **Notebooks:** Apache Zeppelin and JupyterLab are commonly used interactive environments for Spark. Zeppelin server is usually found at port 8890.
  - [Zeppelin](https://zeppelin.apache.org/)
