# Spark Basics

- [Main Web Site]( http://spark.apache.org/ )
- [Apache Spark on Wikipedia]( http://en.wikipedia.org/wiki/Apache_Spark )

## Useful Links

- [Ampcamp big data bootcamp](http://ampcamp.berkeley.edu/)
- [RDDs Simplified]( http://datalakes.com/rdds-simplified/ )
- [Elasticsearch and Apache Lucene for Apache Spark and MLlib]( https://spark-summit.org/2016/events/elasticsearch-and-apache-lucene-for-apache-spark-and-mllib/ )
- [Spark on AWS]( https://aws.amazon.com/emr/details/spark/ )
- [Running Apache Spark on AWS]( https://www.getblueshift.com/running-apache-spark-1-0-on-aws/ )
- [Running Apache Spark EMR and EC2 scripts on AWS with read write S3]( https://bigsnarf.wordpress.com/2015/01/21/running-apache-spark-emr-on-aws/ )
- [Spark on EMR - How to Submit a Spark Application with EMR Steps]( https://github.com/awslabs/emr-bootstrap-actions/blob/master/spark/examples/spark-submit-via-step.md )
- [Databricks Reference Apps]( https://www.gitbook.com/book/databricks/databricks-spark-reference-applications/details )
- [Introduction to Apache Spark with Examples and Use Cases]( http://www.hadoop360.com/blog/introduction-to-apache-spark-with-examples-and-use-cases )


## Spark on a local machine

### Install

To run Spark interactively in a Python interpreter, use ``bin/pyspark``:

```sh
./bin/pyspark --master local[2]
```

### Submit jobs

```bash
./bin/spark-submit examples/src/main/python/pi.py 10
```

## Spark and MongoDB

- [Using MongoDB with Apache Spark]( https://databricks.com/blog/2015/03/20/using-mongodb-with-spark.html )
- [MongoDB Spark connector]( https://www.mongodb.com/products/spark-connector )

## Spark and NLP

- [Dictionary Based Annotation at Scale with Spark, SolrTextTagger and OpenNLP]( https://spark-summit.org/eu-2015/events/dictionary-based-annotation-at-scale-with-spark-solrtexttagger-and-opennlp/ )

Here is a complete set of example on how to use DL4J (Deep Learning for Java) that uses UIMA on the SPARK platform

[Deep Learning for Java]( https://github.com/deeplearning4j/dl4j-spark-cdh5-examples )

and in the following project the use of CTAKES UIMA module from within the Spark framework

[Natural Language Processing with Apache Spark]( https://dzone.com/articles/in-progress-natural-language-processing )

## GraphX

- [Graphx programming guide]( https://spark.apache.org/docs/latest/graphx-programming-guide.html )



## Spark on AWS EMR

[Spark on AWS EMR](http://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-spark.html )

### Create a Cluster With Spark

To launch a cluster with Spark installed using the console

The following procedure creates a cluster with Spark installed.

1. Open the Amazon EMR console at [https://console.aws.amazon.com/elasticmapreduce/]( https://console.aws.amazon.com/elasticmapreduce/ ).
1. Choose Create cluster to use Quick Create.
	1. For the Software Configuration field, choose Amazon Release Version emr-5.0.0 or later.
	1. In the Select Applications field, choose either All Applications or Spark.
	1. Select other options as necessary and then choose Create cluster.NoteTo configure Spark when you are creating the cluster, see Configure Spark.

To launch a cluster with Spark installed using the AWS CLI

Create the cluster with the following command:

```bash
aws emr create-cluster --name "Spark cluster" --release-label emr-5.0.0 --applications Name=Spark \ --ec2-attributes KeyName=myKey --instance-type m3.xlarge --instance-count 3 --use-default-roles
```

Note: For Windows, replace the above Linux line continuation character (\) with the caret (^).

### With the AWS CLI

*Simple cluster:*

```bash
aws emr create-cluster --name "Spark cluster" --release-label  --applications Name=Spark \
--ec2-attributes KeyName=myKey --instance-type m3.xlarge --instance-count 3 --use-default-roles
```

*With config file:*

```bash
aws emr create-cluster --release-label --applications Name=Spark \
--instance-type m3.xlarge --instance-count 3 --configurations https://s3.amazonaws.com/mybucket/myfolder/myConfig.json
```

*myConfig.json:*

```json
[
  {
    "Classification": "spark",
    "Properties": {
      "maximizeResourceAllocation": "true"
    }
  }
]
```

*With Spot instances:*

```bash
aws emr create-cluster --name "Spot cluster" --release-label emr-5.0.0 --applications Name=Spark \
--use-default-roles --ec2-attributes KeyName=myKey \
--instance-groups InstanceGroupType=MASTER,InstanceType=m3.xlarge,InstanceCount=1,BidPrice=0.25 \
InstanceGroupType=CORE,BidPrice=0.03,InstanceType=m3.xlarge,InstanceCount=2

# InstanceGroupType=TASK,BidPrice=0.10,InstanceType=m3.xlarge,InstanceCount=3
```

*In Java:*

```java
// start Spark on EMR in java
AmazonElasticMapReduceClient emr = new AmazonElasticMapReduceClient(credentials);
Application sparkApp = new Application() .withName("Spark");
Applications myApps = new Applications();
myApps.add(sparkApp);
RunJobFlowRequest request = new RunJobFlowRequest() .withName("Spark Cluster") .withApplications(myApps) .withReleaseLabel("") .withInstances(new JobFlowInstancesConfig() .withEc2KeyName("myKeyName") .withInstanceCount(1) .withKeepJobFlowAliveWhenNoSteps(true) .withMasterInstanceType("m3.xlarge") .withSlaveInstanceType("m3.xlarge") ); RunJobFlowResult result = emr.runJobFlow(request);
```

*Connect to the Master Node Using SSH*

To connect to the master node using SSH, you need the public DNS name of the master node and your Amazon EC2 key pair private key. The Amazon EC2 key pair private key is specified when you launch the cluster.

To retrieve the public DNS name of the master node using the AWS CLI

1. To retrieve the cluster identifier, type the following command.aws emr list-clustersThe output lists your clusters including the cluster IDs. Note the cluster ID for the cluster to which you are connecting."Status": {     "Timeline": {         "ReadyDateTime": 1408040782.374,         "CreationDateTime": 1408040501.213     },     "State": "WAITING",     "StateChangeReason": {         "Message": "Waiting after step completed"     } }, "NormalizedInstanceHours": 4,"Id": "j-2AL4XXXXXX5T9", "Name": "My cluster"

1. To list the cluster instances including the master public DNS name for the cluster, type one of the following commands. Replace j-2AL4XXXXXX5T9 with the cluster ID returned by the previous command.aws emr list-instances --cluster-id j-2AL4XXXXXX5T9Or:aws emr describe-clusters --cluster-id j-2AL4XXXXXX5T9



### View Web Interfaces Hosted on Amazon EMR Clusters

- [View Web Interfaces Hosted on Amazon EMR Clusters]( http://docs.aws.amazon.com//ElasticMapReduce/latest/ManagementGuide/emr-web-interfaces.html )

- YARN ResourceManager: [http://master-public-dns-name:8088]( http://master-public-dns-name:8088/ )
- YARN NodeManager: [http://slave-public-dns-name:8042]( http://slave-public-dns-name:8042/ )
- Hadoop HDFS NameNode: [http://master-public-dns-name:50070]( http://master-public-dns-name:50070/ )
- Hadoop HDFS DataNode: [http://slave-public-dns-name:50075]( http://slave-public-dns-name:50075/ )
- Spark HistoryServer: [http://master-public-dns-name:18080]( http://master-public-dns-name:18080/ )
- Zeppelin: [http://master-public-dns-name:8890]( http://master-public-dns-name:8890/ )
- Hue: [http://master-public-dns-name:8888]( http://master-public-dns-name:8888/ )
- Ganglia: [http://master-public-dns-name/ganglia]( http://master-public-dns-name/ganglia/ )
- HBase UI: [http://master-public-dns-name:16010]( http://master-public-dns-name:16010/ )


## Launching Applications with spark-submit

[Launching applications with spark submit] ( https://spark.apache.org/docs/latest/submitting-applications.html#launching-applications-with-spark-submit )


### Apache Zeppelin

Connect to Zeppelin using the same SSH tunneling method to connect to other web servers on the master node. Zeppelin server is found at port 8890.

[Zeppelin]( https://zeppelin.incubator.apache.org )


## DataFrames API

DataFrame operations: 
- printSchema()
- select()
- show()
- count()
- groupBy()
- sum()
- limit()
- orderBy()
- filter()
- withColumnRenamed()
- join()
- withColumn()

```scala
// In the Regular Expression below:
// ^  - Matches beginning of line
// .* - Matches any characters, except newline

pagecountsEnWikipediaArticlesOnlyDF
 .filter($"article".rlike("""^Apache_.*"""))
 .orderBy($"requests".desc)
 .show() // By default, show will return 20 rows

// Import the sql functions package, which includes statistical functions like sum, max, min, avg, etc.
import org.apache.spark.sql.functions._

pagecountsEnWikipediaDF.groupBy("project").sum().show()
```

#### Columns

A new column is constructed based on the input columns present in a dataframe:

```scala
df("columnName") // On a specific DataFrame.
col("columnName") // A generic column no yet associated with a DataFrame.
col("columnName.field") // Extracting a struct field
col("`a.column.with.dots`") // Escape `.` in column names.
$"columnName" // Scala short hand for a named column.
expr("a + 1") // A column that is constructed from a parsed SQL Expression.
lit("abc") // A column that produces a literal (constant) value.
```

Column objects can be composed to form complex expressions:

```scala
$"a" + 1
$"a" === $"b"
```

#### File Read

CSV - Create a DataFrame with the anticipated structure

```scala
val clickstreamDF = sqlContext.read.format("com.databricks.spark.csv")
  .option("header", "true")
  .option("delimiter", "\\t")
  .option("mode", "PERMISSIVE")
  .option("inferSchema", "true")
  .load("dbfs:///databricks-datasets/wikipedia-datasets/data-001/clickstream/raw-uncompressed")
```
  
PARQUET - To create Dataset[Row] using SparkSession

```scala
val people = spark.read.parquet("...")
val department = spark.read.parquet("...")

people.filter("age > 30")
  .join(department, people("deptId") === department("id"))
  .groupBy(department("name"), "gender")
  .agg(avg(people("salary")), max(people("age")))
```

#### Repartitioning / Caching

```scala
val clickstreamNoIDs8partDF = clickstreamNoIDsDF.repartition(8)
clickstreamNoIDs8partDF.registerTempTable("Clickstream")
sqlContext.cacheTable("Clickstream")
```

An ideal partition size in Spark is about 50 MB - 200 MB.
The cache gets stored in Project Tungsten binary compressed columnar format.
