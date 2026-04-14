# Documentation Update Plan

This document tracks the update and improvement of all cheatsheets and markdown files in the repository.

The goal is to ensure all cheatsheets remain technical, very concise, and directed at software engineers.

## Global Tasks
- [ ] **Update documentation structure for easier navigation** (e.g., group related topics, consolidate redundant drafts).
- [ ] **Add more code snippets for Docker and Python** across relevant cheatsheets.
- [ ] **Format, lint, and split large files** to maintain readability and conciseness.

## Files

### docs/Big_Data/Hadoop_Ecosystem.md
- [x] Content refresh: Update to match newest Hadoop ecosystem trends.
- [x] Formatting: Add architecture code examples and diagrams.

### docs/Big_Data/Install_Spark_2.3_Locally.md
- [x] Removal: Spark 2.x, Python 2.x, and Java 8 are obsolete. Remove or replace with a general modern setup guide.

### docs/Big_Data/Spark_APIs.md
- [x] Update to newest version: Upgrade APIs to Spark 3.x/4.x.
- [x] Link additions: Add references to official Spark API docs.

### docs/Big_Data/Spark_Basics.md
- [x] Update to newest version: Refresh contents to modern Spark.
- [x] Content expansion: Add concise code snippets.

### docs/Big_Data/Spark_Development_with_sbt_and_InteliJ.md
- [x] Update to newest version: Refresh IntelliJ and sbt setup steps.

### docs/Big_Data/Spark_on_AWS_EMR.md
- [x] Content refresh: Align with the latest AWS EMR console and configurations.

### docs/Big_Data/Spark_on_EC2.md
- [x] Removal: Assess for removal as EMR and Kubernetes are the preferred deployment targets.

### docs/Big_Data/Spark_on_Kubernetes.md
- [x] Update to newest version: K8s and Spark versions are outdated. Refresh configurations.

### docs/Cloud/AWS.md
- [x] File splitting: The file is too large; separate into Compute, Storage, DBs, etc.
- [x] Update to newest version: Remove outdated Putty/Cygwin steps; favor WSL/Windows Terminal.

### docs/Cloud/AWS_Lambda.md
- [x] Content expansion: Add practical deployment, serverless config, and trigger code snippets.

### docs/Cloud/Serverless.md
- [x] Content refresh: Update to reflect modern serverless architectures.

### docs/Containers/Debug_Kubernetes.md
- [x] Content expansion: Add `kubectl debug` and modern debugging strategies.
- [x] Link additions: Point to official K8s troubleshooting guides.

### docs/Containers/Deploy_to_Kubernetes  (Helm).md
- [x] Update to newest version: Remove Helm 2 / Tiller references; update to Helm 3.

### docs/Containers/Deploy_to_Kubernetes.md
- [x] Content refresh: Merge with Helm documentation or focus purely on native manifests.

### docs/Containers/Docker.md
- [x] **Content expansion: Add more code snippets for Docker** (Dockerfiles, compose, multi-stage builds).

### docs/Containers/Helm_Chart_Creation.md
- [ ] Update to newest version: Align with Helm 3 chart structure.

### docs/Containers/Kubernetes_Cheatsheet.md
- [ ] Content refresh: Update deprecated K8s API versions and outdated commands.

### docs/Containers/Kubernetes_Concepts.md
- [ ] Formatting: Add code examples for key concepts (Deployments, Services, ConfigMaps).

### docs/Containers/Kubernetes_Examples.md
- [ ] Formatting: Add more examples of modern K8s objects (Ingress, CRDs).

### docs/Containers/Minikube_Install_in_Ubuntu_on_Windows.md
- [ ] Update to newest version: Shift focus to WSL2 and K8s 1.30+.

### docs/Containers/Minikube_Install_on_Windows.md
- [ ] Update to newest version: Update K8s version, remove `helm init` instructions.

### docs/Data_Science/Data_Manipulation.md
- [ ] Formatting: Add Python (pandas/NumPy) code examples.

### docs/Data_Science/Data_Visualization.md
- [ ] Update to newest version: Refresh libraries and code examples.

### docs/Data_Science/Deep_Learning.md
- [ ] Update to newest version: Refresh frameworks (TensorFlow 2.x, modern PyTorch).

### docs/Data_Science/Dimensionality_Reduction.md
- [ ] Content expansion: Provide concise examples of PCA and t-SNE.

### docs/Data_Science/Keras.md
- [ ] Update to newest version: Align with Keras 3.

### docs/Data_Science/Machine_Learning.md
- [ ] Formatting: Add brief, technical code examples.

### docs/Data_Science/Recommenders.md
- [ ] Content expansion: Add technical examples and expand beyond basic theory.

### docs/Data_Science/scikit-learn.md
- [x] Update to newest version: Refresh scikit-learn API changes.

### docs/Databases/Mongodb.md
- [x] Update to newest version: Remove deprecated keywords and update syntax.

### docs/Databases/Redshift.md
- [x] Formatting: Add advanced SQL code examples.

### docs/Databases/SQL.md
- [x] Update to newest version: Update syntax and add references to modern SQL dialects.

### docs/DevOps/CloudFormation.md
- [x] Update to newest version: Refresh templates to modern standards.

### docs/DevOps/Git.md
- [x] Content refresh: Add modern commands like `git switch` and `git restore`.

### docs/DevOps/Orchestrator_Scheduler.md
- [x] Update to newest version: Focus on modern tools (Airflow, Dagster, Prefect).

### docs/Java/Gradle.md
- [x] Update to newest version: Ensure compatibility with modern Gradle DSL and Java versions.

### docs/Java/Java.md
- [x] Update to newest version: Update syntax references to Java 21+.

### docs/Java/Log4j.md
- [x] Update to newest version: Upgrade to Log4j2 and add Log4Shell mitigation context.

### docs/Java/Maven.md
- [x] Update to newest version: Refresh POM structure best practices.

### docs/Java/Spring.md
- [x] Formatting: Add modern Spring Boot 3 code examples.

### docs/Linux/Linux.md
- [x] Update to newest version: Refresh standard CLI tooling and commands.

### docs/Linux/Virtualization.md
- [x] Content expansion: Clarify differences between KVM, Hyper-V, and modern container runtime engines.

### docs/Markup_and_Documentation/Jekyll.md
- [x] Update to newest version: Check compatibility with newer Ruby and GitHub pages updates.

### docs/Markup_and_Documentation/Markdown.md
- [x] Update to newest version: Align with current CommonMark specs.

### docs/Markup_and_Documentation/MkDocs.md
- [x] Update to newest version: Ensure Material for MkDocs best practices are included.

### docs/Markup_and_Documentation/reStructuredText.md
- [x] Update to newest version: Refresh Sphinx configurations.

### docs/Microservices/Microservices.md
- [x] Content expansion: Add concise examples of gRPC, REST, and GraphQL APIs.

### docs/Privacy/Privacy_engineering.md
- [x] Content expansion: Expand on GDPR/CCPA technical implementations.

### docs/Python/Flask.md
- [x] Update to newest version: Ensure compatibility with modern Flask (3.x).

### docs/Python/Jupyter.md
- [x] Update to newest version: Transition notes heavily to JupyterLab.

### docs/Python/Matplotlib.md
- [x] Link additions: Point to current Matplotlib galleries and documentation.

### docs/Python/Python.md
- [x] **Content expansion: Add more code snippets for modern Python features.**

### docs/Python/Python3.md
- [x] File splitting / merge: Consolidate fully with `Python.md`.

### docs/Scala/Akka.md
- [x] Link additions: Update references to current Akka or Pekko forks.

### docs/Scala/Play_Framework.md
- [x] Update to newest version: Check Play 3.x compatibility.

### docs/Scala/Scala_Collections.md
- [x] Link additions: Fix and update missing http/https links.

### docs/Scala/Scala_Database_Access.md
- [x] Content expansion: Add examples (Slick, Doobie, Quill).

### docs/Scala/Scala_Design_Patterns.md
- [x] Update to newest version: Reflect changes in Scala 3 constructs.

### docs/Scala/Scala_Generalities.md
- [x] Update to newest version: Refresh basic syntax for Scala 3.

### docs/Scala/Scala_Language.md
- [x] Update to newest version: Incorporate Scala 3 features (givens, enums).

### docs/Scala/Scala_Testing.md
- [x] Update to newest version: Refresh ScalaTest / MUnit examples.

### docs/Scala/Scala_Types.md
- [x] Update to newest version: Add union and intersection types (Scala 3).

### docs/Scala/Scaladoc.md
- [x] Update to newest version: Update tags to align with Scala 3 / Dotty scaladoc tool.

### docs/Scala/sbt.md
- [x] Update to newest version: Refresh obsolete dates and versions.

### docs/Search/ElasticSearch.md
- [ ] Update to newest version: Refresh to ElasticSearch 8.x.
- [ ] File splitting: Break out plugins, APIs, and architectures. Remove Sense/Kopf and obsolete references.

### docs/Search/Logstash.md
- [ ] Update to newest version: Align with latest ELK stack.

### docs/Software_Development/Development_Tools.md
- [ ] Formatting: Add relevant CLI code examples.

### docs/Software_Development/Eclipse.md
- [ ] Removal: Assess for removal as IntelliJ is the modern standard.

### docs/Software_Development/IntelliJ.md
- [ ] Link additions: Add links to official documentation and keymaps.

### docs/Web/Bootstrap.md
- [ ] Update to newest version: Update to Bootstrap 5, fix links.

### docs/Web/CORS.md
- [ ] Formatting: Add server-side and client-side code examples.

### docs/Web/jQuery.md
- [ ] Removal: Assess for removal, or strictly mark as legacy context documentation.

### docs/Windows/Command_Prompt_Here.md
- [ ] Removal: Assess for removal; replace with Windows Terminal/WSL notes.

### docs/dotNET/ASPdotNET.md
- [ ] Update to newest version: Align with modern ASP.NET Core framework.

### docs/dotNET/AkkadotNET.md
- [ ] Link additions: Add references to official documentation.

### docs/dotNET/C#.md
- [ ] Update to newest version: Include modern C# features and syntax.

### docs/dotNET/Multithreading.md
- [ ] Update to newest version: Emphasize modern Task Parallel Library (TPL).

### docs/dotNET/WPF.md
- [ ] Update to newest version: Refresh UI patterns.

### docs/index.md
- [ ] Update documentation structure: Implement navigation improvements.

### drafts/Analytical_Tools.md
- [ ] Formatting: Add relevant configuration examples.

### drafts/Azure.md
- [ ] Content expansion: Fill in the brief placeholders.

### drafts/Citizen_developer_tools.md
- [ ] Content expansion: Expand on low-code platforms and add links.

### drafts/Cloud_Computing.md
- [ ] Content expansion: Add substance to the brief overview.

### drafts/DataScience.md
- [ ] Formatting: Add code examples and fix outdated references.

### drafts/Data_Visualization.md
- [ ] Content expansion: Distinguish from the similarly named file in docs/.

### drafts/Databases.md
- [ ] Content expansion: Expand out brief sections.

### drafts/ELK.md
- [ ] File splitting / merge: Consolidate with ElasticSearch and Logstash files.

### drafts/ETL.md
- [ ] Content expansion: Expand placeholders.

### drafts/Hive.md
- [ ] Content expansion: Add HiveQL examples.

### drafts/Java.md
- [ ] File splitting / merge: Combine with `docs/Java/Java.md`.

### drafts/Kong.md
- [ ] Content expansion: Add API Gateway configurations.

### drafts/Logging.md
- [ ] Content expansion: Add structured logging examples.

### drafts/Play_Framework2.md
- [ ] File splitting / merge: Combine with `docs/Scala/Play_Framework.md`.

### drafts/Scala2.md
- [ ] File splitting / merge: Integrate relevant parts into main Scala documentation.

### drafts/Scala3.md
- [ ] File splitting / merge: Move contents to `docs/Scala/Scala_Language.md`.

### drafts/Software_Design.md
- [ ] Content expansion: Elaborate on system design principles.

### drafts/Stream_Processing.md
- [ ] Content expansion: Add Kafka/Flink concepts.

### drafts/Terraform2.md
- [ ] Content expansion: Rename and expand with modern Terraform practices.

### drafts/Windows_Tools.md
- [ ] Removal: Assess for removal or update with modern dev tooling (WSL, Windows Terminal).
