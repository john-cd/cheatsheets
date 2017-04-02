# Overview

## Basic services

- Compute: EC2 (auroscaling, load balancing)
- Security: VPC (security groups), IAM (users/groups/application roles)

## Storage

- S3: file-level storage, static web site hosting
- Glacier: long-term storage
- EBS: block-level storage (HDD-like for EC2 instances)
Databases (OLTP):
- RDS: relational databases (MySQL, PostgreSQL, MSSQL...)
- DynanoDB: noSQL database (no schema) using solid-state drives

## Analytics

- Redshift: PostgreSQL-based columnstore OLAP database that uses SQL. MPP architecture.
- EMR: Hadoop clusters (Hive, Pig, HBase) for data transformation
- Data Pipeline: simple graphical ETL between S3, DynamoDB, Redshift

## Application Services

- notifications: SNS (alerts by email, SMS...), SES (bulk email)
- workflows: SQS (async message queues for component decoupling), SWF (task-oriented workflows - complicated, requires programming)
- document search: CloudSearch

## Management

- Cloudwatch (monitor services and instances e.g. CPU utilization, etc...), CloudTrail (monitor API calls)

## Deployment

- three solutions: Elastic beanstalk (simple, mostly web or Linux worker), CloudFormation (JSON templates - more difficult, but many existing templates), OpsWork (higher level than CloudFormation, uses non-native components - Chef-based) see http://aws.amazon.com/opsworks/faqs/

## Desktop in the cloud

Workspaces

Prerequisites

- Install AWS command line interface:
http://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-set-up.html
S3 command line user guide: http://docs.aws.amazon.com/cli/latest/userguide/cli-s3.html

- AWS toolkit for Visual Studio
http://docs.aws.amazon.com/AWSToolkitVS/latest/UserGuide/welcome.html

- AWS tools for PowerShell
https://aws.amazon.com/documentation/powershell/

- Unix tools on Windows: http://www.cygwin.com/
linux command quick reference http://www.washington.edu/computing/unix/unixqr.html


- Putty SSH client for Windows:

1. Download and install PuTTY from http://www.chiark.greenend.org.uk/~sgtatham/putty/. Be sure to install the entire suite.

2. Start PuTTYgen (for example, from the Start menu, click All Programs > PuTTY > PuTTYgen).

3. Under Type of key to generate, select SSH-2 RSA.

4. Load the .pem file (private key) downloaded from the console (in "credentials" folder) 

5. Save private key

See http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/get-set-up-for-amazon-ec2.html

- Local IP address 

current (3/17/14): 76.192.162.16/32
to restrict to the local AT&T subnet: 76.192.160.0/22  

Console

- For IAM users with a password, use
https://alphabravo.signin.aws.amazon.com/console/



## Command Line

http://aws.amazon.com/documentation/cli/

## EC2

- log onto instance with putty SSH 
http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-connect-to-instance-linux.html#using-putty
login as: ec2-user (Amazon Linux) or: ubuntu


- Use a shell script to configure the instance:
http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/user-data.html

	* User data: You can specify user data to configure an instance during launch, or to run a configuration script. To attach a file, select the As file option and browse for the file to attach.



Bash shell documentation:
http://tldp.org/HOWTO/Bash-Prog-Intro-HOWTO.html


## S3

- GUI tools to upload / manage files:
AWS console
CloudBerry

- command line s3 clients:
AWS command line (see above)
S3 command line tools
Shell Script To Transfer Files From Amazon S3 Bucket.
aws command line tools
python script to upload file to s3

## Redshift

1) Use
- large-scale SQL database.
- Querying in Redshift is FAST
- full SQL compared to Hadoop's (somewhat limited) HiveQL (http://hive.apache.org/)
- Redshift isn’t a complete replacement for a Hadoop system (no streaming)

2) Tools
- install SQL tool:
http://docs.aws.amazon.com/redshift/latest/gsg/rs-gsg-prereq.html
- other SQL tools:
http://www.aginity.com/workbench/redshift/
- with Microsoft SSDT:
http://stackoverflow.com/questions/17323590/redshift-with-ssis-ssdt

3) Notes

http://redshiftuser.wordpress.com/

http://www.full360.com/2013/02/14/amazon-redshift-full360-review-first-impressions.html

http://www.slideshare.net/joeharris76/migration-to-redshift-from-sql-server

- only three ways to get data into Redshift:

* COPY from S3 (delimited text files)
* COPY from DynamoDB (NoSQL datastore)
* JDBC/ODBC transactions (not efficient for bulk loading)

TODO review http://apievangelist.com/2013/02/10/bringing-etl-to-the-masses-with-apis/

- Tables have ‘keys’ that define how the data is split across slices. The recommended practice is to split based upon commonly-joined columns, so that joined data resides on the same slice, thus avoiding the need to move data between systems.

4) Examples:
COPY table1 FROM 's3://bucket1/' credentials 'aws_access_key_id=abc;aws_secret_access_key=xyz' delimiter '|' gzip removequotes truncatecolumns maxerror 1000
select distinct(field1) from table1
select count(dinstinct field2) from table1
Data Pipeline
- Setup:  http://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-get-setup.html
In short:
1) Install data pipeline CLI tools
...

## API Gateway

https://medium.com/aws-activate-startup-blog/api-security-for-modern-web-apps-a6a7f226a6d#.7iaoyaueq


## SWF

The Amazon Simple Workflow Service (Amazon SWF) makes it easy to build applications that coordinate work across distributed components. In Amazon SWF, a task represents a logical unit of work that is performed by a component of your application. Coordinating tasks across the application involves managing intertask dependencies, scheduling, and concurrency in accordance with the logical flow of the application. Amazon SWF gives you full control over implementing tasks and coordinating them without worrying about underlying complexities such as tracking their progress and maintaining their state.

When using Amazon SWF, you implement workers to perform tasks. These workers can run either on cloud infrastructure, such as Amazon Elastic Compute Cloud (Amazon EC2), or on your own premises. You can create tasks that are long-running, or that may fail, time out, or require restarts—or that may complete with varying throughput and latency. Amazon SWF stores tasks and assigns them to workers when they are ready, tracks their progress, and maintains their state, including details on their completion. To coordinate tasks, you write a program that gets the latest state of each task from Amazon SWF and uses it to initiate subsequent tasks. Amazon SWF maintains an application's execution state durably so that the application is resilient to failures in individual components. With Amazon SWF, you can implement, deploy, scale, and modify these application components independently.

Amazon SWF offers capabilities to support a variety of application requirements. It is suitable for a range of use cases that require coordination of tasks, including media processing, web application back-ends, business process workflows, and analytics pipelines.



## EMR

http://aws.amazon.com/elasticmapreduce/faqs/


Extract, Transform, and Load (ETL) Data with Amazon EMR
http://docs.aws.amazon.com/ElasticMapReduce/latest/DeveloperGuide/emr-etl.html


http://aws.amazon.com/articles/Elastic-MapReduce

Apache LogAnalysis using Pig
http://aws.amazon.com/articles/Elastic-MapReduce/2728

Run Spark and Shark on Amazon Elastic MapReduce
http://aws.amazon.com/articles/Elastic-MapReduce/4926593393724923

Apache Accumulo and Amazon Elastic MapReduce
http://aws.amazon.com/articles/Elastic-MapReduce/2065170233315712


## RedShift

Managing Clusters in Virtual Private Cloud (VPC)
http://docs.aws.amazon.com/redshift/latest/mgmt/managing-clusters-vpc.html


