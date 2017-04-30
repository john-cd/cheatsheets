# Redshift best practices

- smaller node types load data faster
Best Practices for load
- 1 file in S3 per slice (instances in RedShift)
- compressed using gzip compression
- file size: 1MB to 1GB compressed 

Workflows: move from staging table to production table
make sure to wrap the entire workflow into ONE transactions
COMMITs are very expensive in RedShift
disable statistics on staging tables
make sure that the distribution keys match between staging and prod tables
compress your staging tables


VACUUM / SORTING

Rolling out tiered storage - queryable data that is stored in S3, not RedShift - this year

 WLM - can have multiple queues - assign memory to the queue - in the future will allow assignment of CPU % max. Also more features 

Do ANALYZE after VACUUM

COPY from S3 is the fastest
COPY from EMR HDFS may be faster, but most people don't use HDFS - they store data in S3

First column of SORTKEY should not be compressed

Do not do concurrent COPY

