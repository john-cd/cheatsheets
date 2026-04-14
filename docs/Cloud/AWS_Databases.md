# AWS Databases and Analytics

## Redshift

1) Use Case

- Large-scale SQL analytical database
- Querying in Redshift is FAST
- Redshift isn’t a complete replacement for a Hadoop system (no streaming, no text processing)

1) Get data into Redshift:

- COPY from S3 (delimited text files)
- COPY from DynamoDB (NoSQL datastore)
- JDBC/ODBC transactions (not efficient for bulk loading)

Tables have ‘keys’ that define how the data is split across slices. The recommended practice is to split based upon commonly-joined columns, so that joined data resides on the same slice, thus avoiding the need to move data between systems.

1) Examples:

```sql
COPY table1 FROM 's3://bucket1/' credentials 'aws_access_key_id=abc;aws_secret_access_key=xyz' delimiter '|' gzip removequotes truncatecolumns maxerror 1000
SELECT DISTINCT field1 FROM table1
SELECT COUNT(DISTINCT field2) FROM table1
```

## EMR

- [EMR FAQs](https://aws.amazon.com/emr/faqs/)
- [Extract, Transform, and Load (ETL) Data with Amazon EMR](https://docs.aws.amazon.com/ElasticMapReduce/latest/DeveloperGuide/emr-etl.html) <!-- TODO: Verify if this specific AWS Developer Guide link is still active. -->
