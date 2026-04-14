---
title: RedShift
category: databases
tags: Redshift DW Warehouse
---

Amazon Redshift is a fully managed, petabyte-scale data warehouse service in the cloud. You can analyze all your data using standard SQL and your existing Business Intelligence (BI) tools.

## Redshift Best Practices

- Smaller node types load data faster
- Best Practices for data load:
  - 1 file in S3 per slice (instances in RedShift)
  - Compressed using gzip compression
  - File size: 1MB to 1GB compressed
  - COPY from S3 is the fastest
  - COPY from EMR HDFS may be faster, but most people don't use HDFS - they store data in S3
  - First column of SORTKEY should not be compressed

- Workflows: move from staging table to production table
- Make sure to wrap the entire workflow into ONE transaction
- COMMITs are very expensive in RedShift
- Disable statistics on staging tables
- Make sure that the distribution keys match between staging and prod tables
- Compress your staging tables

- Do ANALYZE after VACUUM

## Advanced SQL Code Examples

**Window Functions:**
```sql
SELECT event_id, event_time,
       LEAD(event_time) OVER (PARTITION BY user_id ORDER BY event_time) AS next_event_time
FROM events;
```

**Materialized Views:**
```sql
CREATE MATERIALIZED VIEW mv_sales_summary
BACKUP NO
AS
SELECT sellerid, sum(qtysold) as total_qty, sum(pricepaid) as total_price
FROM sales
GROUP BY sellerid;

REFRESH MATERIALIZED VIEW mv_sales_summary;
```
