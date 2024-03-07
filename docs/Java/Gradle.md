---
title: Gradle Basics
category: java
tags: tools 
comments: true
---
# Gradle

## Install

In Windows 10 WSL, install `sdkman`

```bash
sudo apt install zip
curl -s "https://get.sdkman.io" | bash
source "$HOME/.sdkman/bin/sdkman-init.sh"
sdk version
```

Install gradle

```bash
sdk install gradle
gradle -v
```

Create a gradle project (for Java)

```bash
cd /mnt/d/code/gradle
gradle init --type java-application  
```

You can now use `./gradlew` or `gradlew.bat` in the project folder

## Usage with Java

[Example for the JVM](
https://hackersandslackers.com/building-java-projects-with-gradle/
)

## Common commands

* `./gradlew tasks` in your project directory lists which tasks you can run in your project, such as building or running your code.
* `./gradlew projects`
* `./gradlew properties`

Most commonly used Java tasks:

* `./gradlew build` will compile your project's code into a /build folder.
* `./gradlew run` will run the compiled code in your build folder.
* `./gradlew clean` will purge that build folder.
* `./gradlew test` will execute unit tests without building or running your code again.

## Build process

* Gradle launches as a new JVM process
* It parses the `gradle.properties` file and configures Gradle accordingly
* Next, it creates a Settings instance for the build
* Then, it evaluates the `settings.gradle` file against the Settings object
* It creates a hierarchy of Projects, based on the configured Settings object
* Finally, it executes each `build.gradle` file against its project

In case of a multi-project build, we'd probably have multiple different `build.gradle` files, one for each project.
The `build.gradle` file is executed against a Project instance, with one Project instance created per subproject.

## Groovy DSL

Every Gradle build is made up of one or more projects. What a project represents depends on what it is that you are doing with Gradle. For example, a project might represent a library JAR or a web application.

Each project is made up of one or more tasks. A task represents some atomic piece of work which a build performs. This might be compiling some classes, creating a JAR, generating Javadoc, or publishing some archives to a repository.

### Tasks

Tasks are snippets that we can run directly from the command line in our project directory via `./gradlew [TASK_NAME]`

```bash
./gradlew copy
```

```groovy
task copy(type: Copy, group: "Custom", description: "Copies sources to the dest directory") {
    from "src"
    into "dest"
}

// accessing task properties
println copy.destinationDir
println project.copy.destinationDir
```

```groovy
task('copy2', type: Copy) {
    description 'Copies the resource directory to the target directory.'
    from(file('src'))
    into(buildDir)
    include('**/*.txt', '**/*.xml', '**/*.properties')
    timeout = Duration.ofMillis(50000)
}
```

```groovy
task hello {
    group = 'Worthless tasks'
    description = 'An utterly useless task'
    // extra (custom) properties
    ext.myProperty = "myValue"
    doLast {
        println 'Hello world!'
    }
}

// API call
hello.doLast {
    println "Greetings from the $hello.name task."  // accessing task property in interpolated string
}

hello.configure {
    doLast {
        println 'Hello again'
    }
}

task next {
    dependsOn hello   // or 'hello' if lazy initialized - task dependency 
    doLast {
       println hello.myProperty
    }
}
```

```bash
./gradlew -q hello
./gradlew -q next
```

```groovy
// dynamic tasks
4.times { counter ->
    task "task$counter" {
        doLast {
            println "I'm task number $counter"
        }
    }
}

// default tasks
defaultTasks 'task0', 'task1'
```

```groovy
import org.apache.commons.codec.binary.Base64

// dependencies for the build script
buildscript {
    repositories {
        mavenCentral()
    }
    dependencies {
        classpath group: 'commons-codec', name: 'commons-codec', version: '1.2'
    }
}

task encode {
    doLast {
        // using the build script dependencies
        def byte[] encodedString = new Base64().encode('hello world\n'.getBytes())
        println new String(encodedString)
    }
}

// you can also declare methods
File[] fileList(String dir) {
    file(dir).listFiles({file -> file.isFile() } as FileFilter).sort()
}
```

### Plugins

[https://plugins.gradle.org/](https://plugins.gradle.org/)

```groovy
plugins {
    id "base"
}
```

Essential plugins for Java:

```groovy
plugins {
    id 'java'
    id 'application'
}

apply plugin:'application'
```

### Dependencies and repositories

```groovy
repositories {
    jcenter()  // or mavenCentral()
}

dependencies {
    implementation 'com.google.guava:guava:26.0-jre'  // implementation is a configuration defined by the java plugin
    compile group: 'mysql', name: 'mysql-connector-java', version: '5.1.13'

    testImplementation 'junit:junit:4.12'
}

// pointer to the Java entrypoint
mainClassName="com.someorg.someprj.App"
```
