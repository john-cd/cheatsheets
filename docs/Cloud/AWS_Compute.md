# AWS Compute

## AWS EC2

- Log onto instance with SSH via WSL / Windows Terminal

```shell
ssh -i /path/to/key.pem ec2-user@ec2-198-51-100-1.compute-1.amazonaws.com
```

login as: `ec2-user` (Amazon Linux) or: `ubuntu` (Ubuntu)

[Bash shell documentation](https://tldp.org/HOWTO/Bash-Prog-Intro-HOWTO.html)

- Use a shell script to configure the instance [link](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/user-data.html)

- User data: You can specify user data to configure an instance during launch, or to run a configuration script.
