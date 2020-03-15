## Useful Links

[http://maven.apache.org/]( http://maven.apache.org/ )

[Maven Cheatsheet]( https://eckobar.files.wordpress.com/2007/02/maven-cheatsheet.pdf )

[Maven Quick Ref]( https://maven.apache.org/guides/MavenQuickReferenceCard.pdf )

[Apache-maven-2]( https://dzone.com/refcardz/apache-maven-2 )

[Maven Basics]( http://deeplearning4j.org/maven.html )

[Maven Download / Install]( http://maven.apache.org/download.cgi )

[Nexus]( https://www.sonatype.com/nexus-repository-oss )

## Basics

- Install:

```shell
cd /usr/local
ln -s apache-maven-3.0.5 maven
export PATH=/usr/local/maven/bin:$PATH
mvn -v
```

- Settings file: 

```shell
~/.m2/settings.xml
```

It contains user-specific configuration for authentication, repositories, and other information to customize the behavior of Maven.

- Maven Repo:

```shell
~/.m2/repository/
```

This directory contains your local Maven repository. When you download a dependency from a remote Maven repository, Maven stores a copy of the dependency in your local repository.


### Directory Layout

[Introduction to the standard directory layout](https://maven.apache.org/guides/introduction/introduction-to-the-standard-directory-layout.html )

Without customization, source code is assumed to be in ``${basedir}/src/main/java`` and resources are assumed to be in ``${basedir}/src/main/resources``. 
Tests are assumed to be in ``${basedir}/src/test``, and a project is assumed to produce a JAR file. 
Maven assumes that you want the compile bytecode to ``${basedir}/target/classes`` and then create a distributable JAR file in ``${basedir}/target``

For [WAR files]( https://en.wikipedia.org/wiki/WAR_(file_format) ), the ``/WEB-INF`` directory  contains a file named ``web.xml`` which defines the structure of the web application.
See  also [Tomcat Deployment guide]( https://tomcat.apache.org/tomcat-7.0-doc/appdev/deployment.html )


## Cheatsheet

- Bring up a menu of choices

```shell
mvn archetype:generate -DgroupId=com.dw -DartifactId=es-demo -DarchetypeArtifactId=maven-archetype-quickstart -DinteractiveMode=false
```

- Create a Java project

```shell
mvn archetype:create -DgroupId=org.yourcompany.project -DartifactId=application
```

- Create a web project

```shell
mvn archetype:create -DgroupId=org.yourcompany.project -DartifactId=application -DarchetypeArtifactId=maven-archetype-webapp
```

- Clean project (will delete target directory)

```shell
mvn clean
```

- Validate project (validate the project is correct and all necessary information is available)

```shell
mvn validate
```

- Compile project (compile source code, classes stored in target/classes)

```shell
mvn compile
```

- Test project (run tests using a suitable unit testing framework)

```shell
mvn test
```

- Package project (take the compiled code and package it in its distributable format, such as a JAR / WAR)

```shell
mvn package
```

- Verify project (run any checks to verify the package is valid and meets quality criteria)

```shell
mvn verify
```

- Install project (install the package into the local repository, for use as a dependency in other projects locally)

```shell
mvn install
mvn clean install -DskipTests -Dmaven.javadoc.skip=true
```

- Deploy project (done in an integration or release environment, copies the final package to the remote repository for sharing with other developers and projects)

```shell
mvn deploy
```

- Deploy-file (can be used for deploying a external jar file to repository)

```shell
mvn deploy:deploy-file -Dfile=/path/to/jar/file -DrepositoryId=repos-server -Durl=http ://repos.company.o
```

You can run ``mvn site`` and then find an ``index.html`` file in ``target/site`` that contains links to JavaDoc and a few reports about your source code.


## POM files

Use the search engine at [repository.sonatype.org]( http://repository.sonatype.org ) to find dependencies by name and get the ``xml`` necessary to paste into your ``pom.xml``

```xml
<project>
  <modelVersion>4.0.0</modelVersion>
  <groupId>org.sonatype.mavenbook</groupId>
  <artifactId>my-project</artifactId>
  <version>1.0-SNAPSHOT</version>
</project>
```
