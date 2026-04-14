---
title: Java Pointers
category: java
tags: libraries tools
comments: true
---

## Install [Java](https://www.java.com/en/)

[JDK download](https://www.oracle.com/technetwork/java/javase/downloads/index-jsp-138363.html)

```bash
java -version
```

## Java Tools

[List 1](https://www.loggly.com/blog/8-tools-for-every-java-developers-toolkit/)

[List 2](https://blog.newrelic.com/2014/05/21/toolsforjavadevelopers/)

- [Eclipse](https://eclipse.org/downloads/) IDE
- [Maven](https://maven.apache.org/download.cgi) or Graddle build tool
- [Nexus](https://www.sonatype.org/nexus/) private repository
- [Maven public repository](https://mvnrepository.com/)
- [Phabrikator](https://www.phacility.com/) code review
  - [Phabrikator blog](https://scn.sap.com/community/abap/blog/2014/11/24/code-review-with-phabricator--an-open-source-software-engineering-platform)
- [Jenkins](https://jenkins.io/) CI / CD automation server
- [JProfiler](https://www.ej-technologies.com/products/jprofiler/overview.html)
- [FindBugs](https://findbugs.sourceforge.net/) static analysis or [Checker Framework](https://types.cs.washington.edu/checker-framework/)
- [Checkstyle](https://checkstyle.sourceforge.net/) coding standard checker
  - [Style guidelines](https://logging.apache.org/log4j/2.x/javastyle.html)

## Java Libraries

[Libraries](https://www.devsaran.com/blog/16-java-development-tools-web-developers)

- [Log4j](https://logging.apache.org/)
- [Spring](https://www.spring.io)
  - [Spring Cloud for Amazon Web Services](https://cloud.spring.io/spring-cloud-aws/)
  - [Spring boot code generator](https://start.spring.io/)
- [Apache Commons](https://commons.apache.org/)
- [Guava](https://github.com/google/guava)
- [Jackson JSON](https://wiki.fasterxml.com/JacksonHome) or [GSON](https://github.com/google/gson/blob/master/UserGuide.md)
- [Hibernate](https://hibernate.org/orm/)
on the JVM.
- [Play framework](https://www.playframework.com/)
- [Spark web microframework](https://sparkjava.com/)
- [Akka](https://akka.io/) - actor model, to build highly concurrent, distributed, and resilient message-driven applications

## Modern Java Features (Java 17 / 21)

### Records
```java
public record User(String name, int age) {}
```

### Pattern Matching for switch (Java 21)
```java
static String formatterPatternSwitch(Object obj) {
    return switch (obj) {
        case Integer i -> String.format("int %d", i);
        case Long l    -> String.format("long %d", l);
        case Double d  -> String.format("double %f", d);
        case String s  -> String.format("String %s", s);
        default        -> obj.toString();
    };
}
```

### Text Blocks
```java
String html = """
              <html>
                  <body>
                      <p>Hello, world</p>
                  </body>
              </html>
              """;
```
