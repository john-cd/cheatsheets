# AWS Services Overview

## Basic Services

- Compute: EC2 (autoscaling, ELB load balancing)
- Networking / Security: VPC (security groups), IAM (users/groups/application roles)


## Storage

- S3: secure, scalable object-level storage, static web site hosting...
- Glacier: long-term storage
- EBS: block-level storage (for EC2 instances)


## Databases

- RDS: relational databases (MySQL, PostgreSQL, MSSQL, MariaDB, Aurora...)
- DynamoDB: scalable NoSQL database backed by solid-state drives


## Analytics

- RedShift: PostgreSQL-based columnstore OLAP database that uses SQL. MPP architecture.
- EMR: Hadoop cluster (Hive, Pig, HBase, Spark...).


## ETL / ELT / Batch Processing

- Glue
- Batch
- Data Pipeline: orchestrate data transfers between S3, DynamoDB, Redshift


## Application Services

- Notifications: SNS (alerts by email, SMS...), SES (bulk email)
- Queue: SQS (async message queues for component decoupling) 
- Workflows, State Machine as a Service: AWS Step Functions, SWF (task-oriented workflows - complicated)
- Document Search: ElasticSearch, CloudSearch


## Monitoring

- Cloudwatch (monitor services and instances e.g. CPU utilization, etc...)
- CloudTrail (monitor API calls)


## Infrastructure Deployment / Automation

- Elastic Beanstalk (simple, mostly web or Linux worker)
- CloudFormation (JSON / YAML templates - more difficult, but many existing templates)
- OpsWork (higher level than CloudFormation, uses non-native components - Chef-based)


## Desktop in the Cloud

- WorkSpaces


# Details

## Tools

- Unix tools on Windows: [Cygwin]( http://www.cygwin.com/ )

- Putty SSH client for Windows [doc](  http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/get-set-up-for-amazon-ec2.html )

1. Download and install PuTTY [link]( http://www.chiark.greenend.org.uk/~sgtatham/putty/ ). Be sure to install the entire suite.
2. Start PuTTYgen (for example, from the Start menu, click All Programs > PuTTY > PuTTYgen).
3. Under Type of key to generate, select SSH-2 RSA.
4. Load the .pem file (private key) downloaded from the console (in "credentials" folder) 
5. Save private key

- AWS [command line interface]( http://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-set-up.html )

- [AWS toolkit for Visual Studio]( http://docs.aws.amazon.com/AWSToolkitVS/latest/UserGuide/welcome.html )

- [AWS tools for PowerShell]( https://aws.amazon.com/documentation/powershell/ )


## AWS EC2

- Log onto instance with [Putty SSH]( http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-connect-to-instance-linux.html#using-putty)

login as: ec2-user (Amazon Linux) or: ubuntu

[Bash shell documentation]( http://tldp.org/HOWTO/Bash-Prog-Intro-HOWTO.html )


- Use a shell script to configure the instance [link]( http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/user-data.html )

* User data: You can specify user data to configure an instance during launch, or to run a configuration script. To attach a file, select the "As file" option and browse for the file to attach.


## AWS S3

GUI tools to upload / manage files:

- AWS Console
- S3 Browser
- CloudBerry

Command-line s3 clients:

- AWS command line (see above)
- S3 command line tools


## Redshift

1) Use Case

- Large-scale SQL analytical database
- Querying in Redshift is FAST
- Full SQL compared to [HiveQL](http://hive.apache.org/)
- Redshift isn’t a complete replacement for a Hadoop system (no streaming, no text processing)

2) Tools

- install SQL [tool]( http://docs.aws.amazon.com/redshift/latest/gsg/rs-gsg-prereq.html )
- or [Aginity]( http://www.aginity.com/workbench/redshift/ )
- Microsoft [SSDT]( http://stackoverflow.com/questions/17323590/redshift-with-ssis-ssdt )

3) Get data into Redshift:

* COPY from S3 (delimited text files)
* COPY from DynamoDB (NoSQL datastore)
* JDBC/ODBC transactions (not efficient for bulk loading)

Tables have ‘keys’ that define how the data is split across slices. The recommended practice is to split based upon commonly-joined columns, so that joined data resides on the same slice, thus avoiding the need to move data between systems.

4) Examples:

```sql
COPY table1 FROM 's3://bucket1/' credentials 'aws_access_key_id=abc;aws_secret_access_key=xyz' delimiter '|' gzip removequotes truncatecolumns maxerror 1000
SELECT DISTINCT field1 FROM table1
SELECT COUNT(DISTINCT field2) FROM table1
```

## EMR

[EMR FAQs]( http://aws.amazon.com/elasticmapreduce/faqs/ )


[Extract, Transform, and Load (ETL) Data with Amazon EMR] ( http://docs.aws.amazon.com/ElasticMapReduce/latest/DeveloperGuide/emr-etl.html )

[EMR article]( http://aws.amazon.com/articles/Elastic-MapReduce )


## SWF

The Amazon Simple Workflow Service (Amazon SWF) makes it easy to build applications that coordinate work across distributed components. In Amazon SWF, a task represents a logical unit of work that is performed by a component of your application. Coordinating tasks across the application involves managing intertask dependencies, scheduling, and concurrency in accordance with the logical flow of the application. Amazon SWF gives you full control over implementing tasks and coordinating them without worrying about underlying complexities such as tracking their progress and maintaining their state.

When using Amazon SWF, you implement workers to perform tasks. These workers can run either on cloud infrastructure, such as Amazon Elastic Compute Cloud (Amazon EC2), or on your own premises. You can create tasks that are long-running, or that may fail, time out, or require restarts—or that may complete with varying throughput and latency. Amazon SWF stores tasks and assigns them to workers when they are ready, tracks their progress, and maintains their state, including details on their completion. To coordinate tasks, you write a program that gets the latest state of each task from Amazon SWF and uses it to initiate subsequent tasks. Amazon SWF maintains an application's execution state durably so that the application is resilient to failures in individual components. With Amazon SWF, you can implement, deploy, scale, and modify these application components independently.

Amazon SWF offers capabilities to support a variety of application requirements. It is suitable for a range of use cases that require coordination of tasks, including media processing, web application back-ends, business process workflows, and analytics pipelines.

