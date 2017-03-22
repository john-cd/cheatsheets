---
title:  CloudFormation Basics
category: devops
tags: AWS
---

## DevOps Philosophy

[Why we use Terraform and not Chef, Puppet, Ansible, SaltStack, or CloudFormation](https://blog.gruntwork.io/why-we-use-terraform-and-not-chef-puppet-ansible-saltstack-or-cloudformation-7989dad2865c#.sp4ce0kog)


## Tools

- [AWS CLI cloudformation](http://docs.aws.amazon.com/cli/latest/reference/cloudformation/index.html#cli-aws-cloudformation)
   - [aws cloudformation validate-template](http://docs.aws.amazon.com/cli/latest/reference/cloudformation/validate-template.html)
- [boto3 cloudformation](http://boto3.readthedocs.io/en/latest/reference/services/cloudformation.html)


## [YAML](https://en.wikipedia.org/wiki/YAML)

- [YAML Cheatsheet](http://lzone.de/cheat-sheet/YAML)
- [YAML Cheatsheet 2](https://gist.github.com/anonymous/1486924)

YAML notation for folded text: `>`

```yaml
data: >
   Wrapped text
   will be folded
   into a single
   paragraph

   Blank lines denote
   paragraph breaks
```

## Sample Templates

[Templates for the US East (Northern Virginia) Region](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-sample-templates-us-east-1.html)

[AWSlabs on GitHub](https://github.com/awslabs)
- [Startup kit templates](https://github.com/awslabs/startup-kit-templates)
- [AWS CloudFormation Sample Templates](https://github.com/awslabs/aws-cloudformation-templates)

[Cloudonaut Templates](https://cloudonaut.io/templates-for-aws-cloudformation/)

[Free Templates for AWS CloudFormation (Cloudonaut)](https://github.com/widdix/aws-cf-templates)

[Deploying Microservices with Amazon ECS, AWS CloudFormation, and an Application Load Balancer](https://github.com/awslabs/ecs-refarch-cloudformation)


## Template Basics

[Template Basics](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/gettingstarted.templatebasics.html)

[Template Anatomy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-anatomy.html)

```yaml
---
AWSTemplateFormatVersion: "version date"

Description:
  String

Metadata:
  template metadata

Parameters:
  set of parameters

Mappings:
  set of mappings

Conditions:
  set of conditions

Transform:
  set of transforms

Resources:
  set of resources

Outputs:
  set of outputs
```

With examples:

```yaml
---
AWSTemplateFormatVersion: "2010-09-09"

Description: >
  Here are some
  details about
  the template.

Metadata:
  Instances:
    Description: "Information about the instances"
  Databases: 
    Description: "Information about the databases"

Parameters: 
  InstanceTypeParameter: 
    Type: String            # String, Number, List<Number>, CommaDelimitedList e.g. "test,dev,prod", or an AWS-specific types such as Amazon EC2 key pair names and VPC IDs.
    Default: t2.micro
    AllowedValues: 
      - t2.micro
      - m1.small
    Description: Enter t2.micro or m1.small. Default is t2.micro.
    # AllowedPattern: "[A-Za-z0-9]+" # A regular expression that represents the patterns you want to allow for String types.
    # ConstraintDescription: Malformed input-Parameter MyParameter must match pattern [A-Za-z0-9]+
    # MinLength: 2  # for String
    # MaxLength: 10
    # MinValue: 0   # for Number types.
    # MaxValue: 100 
    # NoEcho: True

Mappings: 
  RegionMap: 
    us-east-1: 
      "32": "ami-6411e20d"
    us-west-1: 
      "32": "ami-c9c7978c"
    eu-west-1: 
      "32": "ami-37c2f643"
    ap-southeast-1: 
      "32": "ami-66f28c34"
    ap-northeast-1: 
      "32": "ami-9c03a89d"

Conditions: 
  CreateProdResources: !Equals [ !Ref EnvType, prod ]

Transform:
  set of transforms

Resources:
  Ec2Instance:
      Type: AWS::EC2::Instance
      Properties:
        InstanceType:
          Ref: InstanceTypeParameter  # reference to parameter above
        ImageId: ami-2f726546

Outputs: 
  VolumeId: 
    Condition: CreateProdResources
    Value: 
      !Ref NewVolume
```

- The Ref function can refer to input parameters that are specified at stack creation time.

## Examples

### S3

```yaml
Resources:
  HelloBucket:
    Type: AWS::S3::Bucket  # AWS::ProductIdentifier::ResourceType
```

### EC2

```yaml
Resources:
  Ec2Instance:
    Type: AWS::EC2::Instance
    Properties:
      SecurityGroups:
      - Ref: InstanceSecurityGroup
      KeyName: mykey
      ImageId: ''
  InstanceSecurityGroup:
    Type: AWS::EC2::SecurityGroup
    Properties:
      GroupDescription: Enable SSH access via port 22
      SecurityGroupIngress:
      - IpProtocol: tcp
        FromPort: '22'
        ToPort: '22'
        CidrIp: 0.0.0.0/0    
```