# Spark on AWS EMR

## Key Links

[Spark on AWS EMR](http://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-spark.html )

## Create a EMR Cluster with Spark using the AWS Console

The following procedure creates a cluster with Spark installed.

1. Open the Amazon EMR console at [https://console.aws.amazon.com/elasticmapreduce/]( https://console.aws.amazon.com/elasticmapreduce/ ).
1. Choose Create cluster to use Quick Create.
	1. For the Software Configuration field, choose Amazon Release Version emr-5.0.0 or later.
	1. In the Select Applications field, choose either All Applications or Spark.
	1. Select other options as necessary and then choose Create cluster
	

## Create a EMR Cluster with Spark using the AWS CLI

*Simple cluster:*

```bash
aws emr create-cluster --name "Spark cluster" --release-label emr-5.0.0 --applications Name=Spark \ 
--ec2-attributes KeyName=myKey --instance-type m3.xlarge --instance-count 3 --use-default-roles
```

Note: For Windows, replace the above Linux line continuation character (\) with the caret (^).


*When using a config file:*

```bash
aws emr create-cluster --release-label --applications Name=Spark \
--instance-type m3.xlarge --instance-count 3 --configurations https://s3.amazonaws.com/mybucket/myfolder/myConfig.json
```

*Sample myConfig.json:*

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

*Using Spot instances:*

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

## Connect to the Master Node using SSH

To connect to the master node using SSH, you need the public DNS name of the master node and your Amazon EC2 key pair private key. The Amazon EC2 key pair private key is specified when you launch the cluster.

1. To retrieve the cluster identifier / the public DNS name of the master node, type the following command:

```shell
aws emr list-clusters
```

The output lists your clusters including the cluster IDs. Note the cluster ID for the cluster to which you are connecting.

```json
"Status": {     "Timeline": {         "ReadyDateTime": 1408040782.374,         "CreationDateTime": 1408040501.213     },     "State": "WAITING",     "StateChangeReason": {         "Message": "Waiting after step completed"     } }, "NormalizedInstanceHours": 4,"Id": "j-2AL4XXXXXX5T9", "Name": "My cluster"
```

1. To list the cluster instances including the master public DNS name for the cluster, type one of the following commands. Replace j-2AL4XXXXXX5T9 with the cluster ID returned by the previous command.

```shell
aws emr list-instances --cluster-id j-2AL4XXXXXX5T9Or:aws emr describe-clusters --cluster-id j-2AL4XXXXXX5T9
```


## View the Web Interfaces Hosted on Amazon EMR Clusters

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
