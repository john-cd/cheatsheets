---
title: CloudFormation
category: devops
tags: AWS IAC
---

## CloudFormation Basics

Use YAML instead of JSON for modern templates.

```yaml
AWSTemplateFormatVersion: '2010-09-09'
Description: A simple modern EC2 instance template
Parameters:
  InstanceType:
    Type: String
    Default: t3.micro
    AllowedValues: [t3.micro, t3.small, m5.large]
Resources:
  MyEC2Instance:
    Type: AWS::EC2::Instance
    Properties:
      InstanceType: !Ref InstanceType
      ImageId: ami-0c55b159cbfafe1f0
      Tags:
        - Key: Name
          Value: ModernInstance
Outputs:
  InstanceId:
    Value: !Ref MyEC2Instance
```
