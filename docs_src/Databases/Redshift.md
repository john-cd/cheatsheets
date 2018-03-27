---
title: RedShift
category: databases
tags: Redshift DW Warehouse
---

## Redshift Best Practices

- Smaller node types load data faster
- Best Practices for data load:
+ 1 file in S3 per slice (instances in RedShift)
+ Compressed using gzip compression
+ File size: 1MB to 1GB compressed 
+ COPY from S3 is the fastest
+ COPY from EMR HDFS may be faster, but most people don't use HDFS - they store data in S3
+ First column of SORTKEY should not be compressed

- Workflows: move from staging table to production table
- Make sure to wrap the entire workflow into ONE transaction
- COMMITs are very expensive in RedShift
- Disable statistics on staging tables
- Make sure that the distribution keys match between staging and prod tables
- Compress your staging tables

- Do ANALYZE after VACUUM

