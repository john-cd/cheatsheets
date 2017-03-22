---
title: Serverless Cheatsheet
category: cloud
tags: python dotNET
---

# Serverless Cheatsheet

[Serverless home page](https://serverless.com/)

## Install

```bash
npm install -g serverless
```

## Examples

[Serverless Examples](https://github.com/serverless/examples)

[Serverless Starter](https://github.com/serverless/serverless-starter)

[Python example](https://serverlesscode.com/post/python-on-serverless-intro/)

[C# example](https://serverless.com/blog/serverless-v1.4.0/)


## Cheatsheet

* Create a Service:

```bash
# NodeJS
serverless create -p [SERVICE NAME] -t aws-nodejs

# C#
serverless create --path serverlessCSharp --template aws-csharp
```

* Install a Service

This is a convenience method to install a pre-made Serverless Service locally by downloading the Github repo and unzipping it.

```bash
serverless install -u [GITHUB URL OF SERVICE]
```

* Deploy All

Use this when you have made changes to your Functions, Events or Resources in ``serverless.yml`` or you simply want to deploy all changes within your Service at the same time.

```bash
serverless deploy -s [STAGE NAME] -r [REGION NAME] -v
```

* Deploy Function

Use this to quickly overwrite your AWS Lambda code on AWS, allowing you to develop faster.

```bash
serverless deploy function -f [FUNCTION NAME] -s [STAGE NAME] -r [REGION NAME]
```

* Invoke Function

Invokes an AWS Lambda Function on AWS and returns logs.

```bash
serverless invoke -f [FUNCTION NAME] -s [STAGE NAME] -r [REGION NAME] -l
```

* Streaming Logs

Open up a separate tab in your console and stream all logs for a specific Function using this command.

```bash
serverless logs -f [FUNCTION NAME] -s [STAGE NAME] -r [REGION NAME]
```
