# AWS Services Overview

## Basic Services

- Compute: EC2 (autoscaling, ELB load balancing), Lambda
- Networking / Security: VPC (security groups), IAM (users/groups/application roles)

## Storage

- S3: secure, scalable object-level storage, static web site hosting
- Glacier: long-term storage
- EBS: block-level storage (for EC2 instances)

## Databases

- RDS: relational databases (MySQL, PostgreSQL, MSSQL, MariaDB, Aurora)
- DynamoDB: scalable NoSQL database backed by solid-state drives

## Analytics

- RedShift: PostgreSQL-based columnstore OLAP database that uses SQL. MPP architecture.
- EMR: Hadoop cluster (Hive, Spark, Flink).

## ETL / ELT / Batch Processing

- Glue
- Batch
- Data Pipeline: orchestrate data transfers between S3, DynamoDB, Redshift

## Application Services

- Notifications: SNS (alerts by email, SMS), SES (bulk email)
- Queue: SQS (async message queues for component decoupling)
- Workflows, State Machine as a Service: AWS Step Functions
- Document Search: ElasticSearch, CloudSearch

## Monitoring

- CloudWatch (monitor services and instances e.g. CPU utilization, etc...)
- CloudTrail (monitor API calls)

## Infrastructure Deployment / Automation

- Elastic Beanstalk (simple, mostly web or Linux worker)
- CloudFormation (JSON / YAML templates - more difficult, but many existing templates)
- CDK (Cloud Development Kit) - Infrastructure as code using Python/TypeScript/etc.

## Tools

- Windows Terminal and WSL (Windows Subsystem for Linux) are highly recommended over Putty or Cygwin.

- AWS [command line interface](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-set-up.html)

- [AWS toolkit for Visual Studio](https://docs.aws.amazon.com/AWSToolkitVS/latest/UserGuide/welcome.html)

## Example

```text
Review this cheatsheet and adapt the commands to your environment before execution.
```
