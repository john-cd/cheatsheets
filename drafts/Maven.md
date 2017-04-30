# Maven

[http://maven.apache.org/]( http://maven.apache.org/ )

[Maven Cheatsheet]( https://eckobar.files.wordpress.com/2007/02/maven-cheatsheet.pdf )

[Maven Quick Ref]( https://maven.apache.org/guides/MavenQuickReferenceCard.pdf )

[apache-maven-2]( https://dzone.com/refcardz/apache-maven-2 )

[maven]( http://deeplearning4j.org/maven.html )

[Download / Install]( http://maven.apache.org/download.cgi )

```sh
cd /usr/local
ln -s apache-maven-3.0.5 maven
export PATH=/usr/local/maven/bin:$PATH
mvn -v
```

``~/.m2/settings.xml``

A file containing user-specific configuration for authentication, repositories, and other information to customize the behavior of Maven.

``~/.m2/repository/``

This directory contains your local Maven repository. When you download a dependency from a remote Maven repository, Maven stores a copy of the dependency in your local repository.


## Directory Layout

[Introduction to the standard directory layout](https://maven.apache.org/guides/introduction/introduction-to-the-standard-directory-layout.html )


Without customization, source code is assumed to be in ``${basedir}/src/main/java`` and resources are assumed to be in ``${basedir}/src/main/resources``. Tests are assumed to be in ``${basedir}/src/test``, and a project is assumed to produce a JAR file. Maven assumes that you want the compile bytecode to ``${basedir}/target/classes`` and then create a distributable JAR file in ``${basedir}/target``

WAR files:  https://en.wikipedia.org/wiki/WAR_(file_format)    https://tomcat.apache.org/tomcat-7.0-doc/appdev/deployment.html 
The /WEB-INF directory in the WAR file contains a file named web.xml which defines the structure of the web application.

You can run ``mvn site`` and then find an index.html file in target/site that contains links to JavaDoc and a few reports about your source code.


bring up a menu of choices
```
mvn archetype:generate -DgroupId=com.dw -DartifactId=es-demo -DarchetypeArtifactId=maven-archetype-quickstart -DinteractiveMode=false
```

create java project
```
mvn archetype:create -DgroupId=org.yourcompany.project -DartifactId=application
```

create web project

```
mvn archetype:create -DgroupId=org.yourcompany.project -DartifactId=application -DarchetypeArtifactId=maven-archetype-webapp
```

clean project: will delete target directory

```
mvn clean
```

validate project: validate the project is correct and all necessary information is available

```
mvn validate
```

compile project: compile source code, classes stored in target/classes

```
mvn compile
```

test project: run tests using a suitable unit testing framework

```
mvn test
```

package project: take the compiled code and package it in its distributable format, such as a JAR / WAR

```
mvn package
```

verify project: run any checks to verify the package is valid and meets quality criteria

```
mvn verify
```

install project: install the package into the local repository, for use as a dependency in other projects locally

```
mvn install
mvn clean install -DskipTests -Dmaven.javadoc.skip=true
```

deploy project: done in an integration or release environment, copies the final package to the remote repository for sharing with other developers and projects

```
mvn deploy
```

deploy-file: can be used for deploying a external jar file to repository

```
mvn deploy:deploy-file -Dfile=/path/to/jar/file -DrepositoryId=repos-server -Durl=http ://repos.company.o
```

## POM files

use the search engine at repository.sonatype.org to find dependencies by name and get the xml necessary to paste into your pom.xml

```
<project>
  <modelVersion>4.0.0</modelVersion>
  <groupId>org.sonatype.mavenbook</groupId>
  <artifactId>my-project</artifactId>
  <version>1.0-SNAPSHOT</version>
</project>
```


[Nexus] ( https://www.sonatype.com/nexus-repository-oss )
