---
title: Gradle Basics
category: java
tags: tools 
comments: true
---
# Gradle

## Install

Use `sdkman` for easy installation:

```shell
curl -s "https://get.sdkman.io"
source "$HOME/.sdkman/bin/sdkman-init.sh"
sdk install gradle
```

## Modern `build.gradle.kts` (Kotlin DSL)

```kotlin
plugins {
    id("java")
    id("application")
}

repositories {
    mavenCentral()
}

dependencies {
    testImplementation("org.junit.jupiter:junit-jupiter:5.9.2")
    testRuntimeOnly("org.junit.platform:junit-platform-launcher")
}

application {
    mainClass.set("com.example.Main")
}

tasks.named<Test>("test") {
    useJUnitPlatform()
}
```
