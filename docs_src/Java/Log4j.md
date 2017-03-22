---
title: Apache Log4j 2
category: java
tags: Java Logs
---

# Apache Log4j 2

http://www.tutorialspoint.com/log4j/log4j_quick_guide.htm
http://www.tutorialspoint.com/log4j/index.htm


## Key Components

* loggers: Responsible for capturing logging information.
* appenders: Responsible for publishing logging information to various preferred destinations.
* layouts: Responsible for formatting logging information in different styles.


There are seven levels of logging defined within the API: OFF, DEBUG, INFO, ERROR, WARN, FATAL, and ALL.


## Install

https://logging.apache.org/log4j/2.x/download.html

```bash
$ gunzip apache-log4j-1.2.15.tar.gz
$ tar -xvf apache-log4j-1.2.15.tar
$ pwd
/usr/local/apache-log4j-1.2.15
$ export CLASSPATH=$CLASSPATH:/usr/local/apache-log4j-1.2.15/log4j-1.2.15.jar
$ export PATH=$PATH:/usr/local/apache-log4j-1.2.15/
```

### Maven Snippet

```Maven
<dependencies>
<dependency>
<groupId>org.apache.logging.log4j</groupId>
<artifactId>log4j-api</artifactId>
<version>2.6.1</version>
</dependency>
<dependency>
<groupId>org.apache.logging.log4j</groupId>
<artifactId>log4j-core</artifactId>
<version>2.6.1</version>
</dependency>
</dependencies>
```

### log4j.properties

All the libraries should be available in CLASSPATH and yourlog4j.properties file should be available in PATH.

```ini
# Define the root logger with appender file
log = /usr/home/log4j
log4j.rootLogger = WARN, FILE

# Define the file appender
log4j.appender.FILE=org.apache.log4j.FileAppender
log4j.appender.FILE.File=${log}/log.out

# Define the layout for file appender
log4j.appender.FILE.layout=org.apache.log4j.PatternLayout
log4j.appender.FILE.layout.conversionPattern=%m%n
```

### Snippets

```java
import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

public class MyTest {

	private static final Logger logger = LogManager.getLogger(); // equiv to  LogManager.getLogger(MyTest.class);
	private static final Logger logger = LogManager.getLogger("HelloWorld");

	public static void main(String[] args) {
	     logger.setLevel(Level.WARN);
	     logger.info("Hello, World!");
	     // string interpolation
	     logger.debug("Logging in user {} with birthday {}", user.getName(), user.getBirthdayCalendar());

	     // pre-Java 8 style optimization: explicitly check the log level
	     // to make sure the expensiveOperation() method is only called if necessary
	     if (logger.isTraceEnabled()) {
		logger.trace("Some long-running operation returned {}", expensiveOperation());
	     }

	     // Java-8 style optimization: no need to explicitly check the log level:
	     // the lambda expression is not evaluated if the TRACE level is not enabledlogger.trace("Some long-running operation returned {}", () -> expensiveOperation());
	     }
}

// FORMATTER LOGGER
public static Logger logger = LogManager.getFormatterLogger("Foo");

logger.debug("Logging in user %s with birthday %s", user.getName(), user.getBirthdayCalendar());
logger.debug("Logging in user %1$s with birthday %2$tm %2$te,%2$tY", user.getName(), user.getBirthdayCalendar());
//
logger.debug("Logging in user {} with birthday {}", user.getName(), user.getBirthdayCalendar());
```
