# Hadoop Ecosystem

Hadoop is not a single product, but rather a software family. Modern data ecosystems have evolved to prioritize the separation of compute and storage (e.g., cloud-native object storage like S3 replacing HDFS in many cloud deployments).

Its core and common components consist of the following:

- **HDFS**: The distributed file system for Hadoop, now often supplemented or replaced by cloud object stores (e.g., AWS S3, Azure Data Lake).
- **YARN**: The resource management and job scheduling technology.
- **Hive**: Used to facilitate structure for the data, running SQL-like queries.
- **HBase**: A scalable, distributed, NoSQL database built on top of Hadoop.
- **Spark**: A unified analytics engine for large-scale data processing, largely replacing MapReduce.
- **Kafka / Flink**: Often integrated for real-time stream processing.
- Packaging for Hadoop: [BigTop](https://bigtop.apache.org/)

## Modern Big Data Architecture

```text
+-----------------------+       +-------------------------+       +-------------------+
|      Data Sources     |       |    Compute / Processing |       |    Storage        |
| (DBs, Streams, Logs)  +------>+  (Spark, Flink, Hive)   +<----->+ (S3, ADLS, HDFS)  |
+-----------------------+       +-------------------------+       +-------------------+
                                            ^                               |
                                            |                               v
                                +-------------------------+       +-------------------+
                                |    Orchestration        |       |    Serving        |
                                |  (Airflow, Dagster)     |       | (HBase, Trino)    |
                                +-------------------------+       +-------------------+
```

## Hadoop and Mongo

- [Hadoop and MongoDB](https://www.mongodb.com/hadoop-and-mongodb)
- [Hadoop and MongoDB Use Cases](https://docs.mongodb.org/ecosystem/use-cases/hadoop/)

## AWS EMR

[Amazon EMR Best Practices](https://media.amazonwebservices.com/AWS_Amazon_EMR_Best_Practices.pdf)

Amazon EMR is a cloud-native big data platform that simplifies running big data frameworks. Modern EMR includes:

- Hadoop (HDFS, YARN)
- Spark
- Hive
- HBase
- Presto / Trino
- Flink
- Zeppelin
- ZooKeeper
