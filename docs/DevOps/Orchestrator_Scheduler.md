---
title: Orchestrators and Schedulers
category: devops
tags: orchestration scheduling
---

# Orchestrators and Schedulers

## Modern Tools

### [Apache Airflow](https://airflow.apache.org/)
Python-based orchestration framework using DAGs.
```python
from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG('modern_dag', start_date=datetime(2023, 1, 1), schedule_interval='@daily') as dag:
    task1 = BashOperator(task_id='print_date', bash_command='date')
```

### [Dagster](https://dagster.io/)
Data orchestrator for machine learning, analytics, and ETL. Focuses on data assets.

### [Prefect](https://www.prefect.io/)
Modern orchestration tool with native Python semantics and a hybrid execution model.
