---
title: Linux Cheatsheet
category: Linux
tags:
---

## Vim

[Vim Commands Cheat Sheet]( https://www.fprintf.net/vimCheatSheet.html )

```
:q
:q!
:wq
:wq {file}

:e[dit] {file}

i  insert
dd  delete [count] lines
```

## Bash

- [BASH Programming - Introduction]( http://tldp.org/HOWTO/Bash-Prog-Intro-HOWTO.html )
- [Bash CheatSheet for UNIX Systems]( https://gist.github.com/LeCoupa/122b12050f5fb267e75f )
- [Bash Cheat Sheet]( ftp://ftp.psu.ac.th/pub/bash-howto/reference_bash-cheat.pdf )

```bash
#!/bin/bash

varname=value
echo $varname
```

Don't forget chmod +x filename


## Amazon Linux

[Amazon Linux Basics]( http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AmazonLinuxAMIBasics.html )

### Adding Packages

```bash
sudo yum update -y                  # all packages
sudo yum install -y package_name
sudo yum install -y httpd24 php56 mysql55-server php56-mysqlnd
```

### Start a Service

```bash
sudo service docker start
sudo service jenkins start
sudo service nginx start
```

### Autostarting a service on Amazon Linux

- [Tutorial on "Chkconfig" Command in Linux with Examples]( http://www.yourownlinux.com/2015/01/tutorial-on-chkconfig-command-in-linux-with-examples.html )
- [man page]( http://linux.die.net/man/8/chkconfig )

```bash
# check a service is configured for startup
sudo chkconfig sshd
echo $?  # 0 = configured for startup
# or
sudo chkconfig --list mysqld
sudo chkconfig --list         # all services

# add a service
sudo chkconfig --add vsftpd
sudo chkconfig mysqld on
sudo chkconfig --level 3 httpd on  # specific runlevel
```

## Linux Boot Process

- [ Linux Boot Process]( http://www.thegeekstuff.com/2011/02/linux-boot-process/ )
- [ Scripts in /etc/init.d ]( http://www.novell.com/documentation/suse91/suselinux-adminguide/html/ch13s04.html )

You can also use a ``/etc/rc.d/rc.local`` script.


### Running Commands on your Linux Instance at Launch

- Paste a user data script into the ``User data`` field

```bash
#!/bin/bash
yum update -y
yum install -y httpd24 php56 mysql55-server php56-mysqlnd
service httpd start
chkconfig httpd on
groupadd www
usermod -a -G www ec2-user
chown -R root:www /var/www
chmod 2775 /var/www
find /var/www -type d -exec chmod 2775 {} +
find /var/www -type f -exec chmod 0664 {} +
echo "<?php phpinfo(); ?>" > /var/www/html/phpinfo.php
```

- Or use ``cloud-init``
    - [cloud-init for AWS EC2]( http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AmazonLinuxAMIBasics.html#CloudInit )
    - [cloud-init docs]( http://cloudinit.readthedocs.io/en/latest/ )

File location: ``/etc/sysconfig/cloudinit``

Cloud-init output log file: ``/var/log/cloud-init-output.log``

### Install the SSM Agent on EC2 Instances at Start-Up

```bash
#!/bin/bash
cd /tmp
curl https://amazon-ssm-region.s3.amazonaws.com/latest/linux_amd64/amazon-ssm-agent.rpm -o amazon-ssm-agent.rpm
yum install -y amazon-ssm-agent.rpm
```

## Linux desktop

[How can I connect to an Amazon EC2 Linux instance with desktop functionality from Windows?]( https://aws.amazon.com/premiumsupport/knowledge-center/connect-to-linux-desktop-from-windows/ )

