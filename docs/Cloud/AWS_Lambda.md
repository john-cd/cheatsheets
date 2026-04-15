---
title: AWS Lambda
category: cloud
tags: aws lambda cloud
---

# AWS Lambda

## Useful Links

- [Building a Dynamic DNS for Route 53 using CloudWatch Events and Lambda](https://github.com/awslabs/aws-lambda-ddns-function)
- [Lambkin](https://github.com/jarpy/lambkin) - CLI tool for generating and managing simple functions in AWS Lambda

## Serverless Framework Configuration Example

To deploy a Lambda function via the [Serverless Framework](https://www.serverless.com/), configure a `serverless.yml` file:

```yaml
service: my-python-lambda
frameworkVersion: '3'

provider:
  name: aws
  runtime: python3.10
  region: us-east-1

functions:
  hello:
    handler: handler.hello
    events:
      - httpApi:
          path: /hello
          method: get
```

Deploy with:

```shell
sls deploy
```

## Python Lambda Handler Example

An example API Gateway trigger handler `handler.py`:

```python
import json

def hello(event, context):
    body = {
        "message": "Go Serverless v3.0! Your function executed successfully!",
        "input": event,
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response
```
