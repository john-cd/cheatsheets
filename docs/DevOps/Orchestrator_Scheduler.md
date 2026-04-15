---
title: Orchestrators / Schedulers
category: devops
tags: Airflow Luigi Pinball Snowplow
---

# Orchestrators / Schedulers

Tools to build complex pipelines of batch jobs. They handle dependency resolution, workflow management, visualization.

## Links

- [Luigi vs Airflow vs Pinball](https://bytepawn.com/luigi-airflow-pinball.html)
- [Airflow Documentation](https://airflow.incubator.apache.org/)
- [Luigi](https://github.com/spotify/luigi)
- [Petabyte-Scale Data Pipelines with Docker, Luigi and Elastic Spot Instances](https://tech.adroll.com/blog/data/2015/09/22/data-pipelines-docker.html)
- [Snowplow](https://snowplowanalytics.com/product/)

## Modern Tools

### Airflow

[Apache Airflow](https://airflow.apache.org/)

Python-based orchestration framework using DAGs.

```python
from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG('modern_dag', start_date=datetime(2023, 1, 1), schedule_interval='@daily') as dag:
    task1 = BashOperator(task_id='print_date', bash_command='date')
```

## Dagster

[Dagster](https://dagster.io/)

Data orchestrator for machine learning, analytics, and ETL. Focuses on data assets.

### Prefect

[Prefect](https://www.prefect.io/)

Modern orchestration tool with native Python semantics and a hybrid execution model.
