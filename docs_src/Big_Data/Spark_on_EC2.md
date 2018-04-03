# Install Spark on EC2 with Flintrock

## Key Links

[ Flintrock GitHub Repo]( https://github.com/nchammas/flintrock )

## Configurable CLI Defaults

Flintrock lets you persist your desired configuration to a YAML file so that you don't have to keep typing out the same options over and over at the command line.

To setup and edit the default config file, run this:

```shell
flintrock configure
```

## Sample config.yaml

```yaml
provider: ec2

services:
  spark:
    version: 2.2.0

launch:
  num-slaves: 1

providers:
  ec2:
    key-name: key_name
    identity-file: /path/to/.ssh/key.pem
    instance-type: m3.medium
    region: us-east-1
    ami: ami-97785bed
    user: ec2-user
```

With a config file like that, you can now launch a cluster:

```shell
flintrock launch test-cluster
```