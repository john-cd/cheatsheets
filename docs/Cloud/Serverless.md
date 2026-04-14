---
title: Serverless Cheatsheet
category: cloud
tags: python dotNET
---

# Serverless Cheatsheet

[Serverless Framework home page](https://www.serverless.com/)

Modern serverless architectures emphasize event-driven design, leveraging managed services (like EventBridge, SQS, and API Gateway) to trigger ephemeral compute (Lambda) with minimal operational overhead.

## Install

```bash
npm install -g serverless
```

## Examples

[Serverless Examples](https://github.com/serverless/examples)

## CLI Cheatsheet

Note: `sls` is an alias for the `serverless` command.

- Create a Service:

```bash
# NodeJS
sls create -p [SERVICE NAME] -t aws-nodejs

# Python
sls create --path myService --template aws-python3
```

- Deploy All

Use this when you have made changes to your Functions, Events or Resources in `serverless.yml` or you simply want to deploy all changes within your Service at the same time.

```bash
sls deploy --stage [STAGE NAME] --region [REGION NAME] --verbose
```

- Deploy Function

Use this to quickly overwrite your AWS Lambda code on AWS, allowing you to develop faster without deploying CloudFormation changes.

```bash
sls deploy function -f [FUNCTION NAME]
```

- Invoke Function

Invokes an AWS Lambda Function on AWS and returns logs.

```bash
sls invoke -f [FUNCTION NAME] -l
```

- Invoke Local

Invokes a function locally for testing.

```bash
sls invoke local -f [FUNCTION NAME] -d '{"data": "value"}'
```

- Streaming Logs

Open up a separate tab in your console and stream all logs for a specific Function.

```bash
sls logs -f [FUNCTION NAME] -t
```

- Remove Service

Deletes all deployed AWS resources associated with the service.

```bash
sls remove --stage [STAGE]
```
