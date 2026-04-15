# Documentation Update Plan

This document tracks the update and improvement of all cheatsheets and markdown files in the repository.

The goal is to ensure all cheatsheets remain technical, very concise, and directed at software engineers.

- [x] **Update documentation structure for easier navigation** (e.g., group related topics, consolidate redundant drafts).
- [ ] **Add more code snippets for Docker and Python** across relevant cheatsheets.
- [ ] **Format, lint, and split large files** to maintain readability and conciseness.

- [ ] update all code examples to latest version of the dependencies
- [ ] embed long code examples with --8<--
- [ ] add tests?

- [ ] Fix Markdown formatting, including: single top-level heading, zero or two trailing spaces, headings should be surrounded by a blank line
- [ ] Make sure the Markdown text forms full sentences with proper capitalization
- [ ] Add commentary around code blocks and comments within to explain how they work and what they do.
- [ ] code comments should generally start with a capitalized letter and end with a period.
- [ ] Verify all URLs / links - update what you can; add a note otherwise
- [ ] Add internal links between markdown files
- [ ] update UPDATE.md file with tasks (fixes, improvements, suggestions...) to improve the cheat sheets

- [ ] compare the new cheatsheets vs .orig and validate
- [ ] consolidate all python cheatsheeets in this repo
- [ ] consolidate with my website in one repo??

## Files

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

### Added Tasks

- [ ] `docs/Web/jQuery.md`: Add more modern JavaScript (ES6+) examples
- [ ] `docs/Containers/Kubernetes_Concepts.md`: Expand on Kubernetes custom resources (CRDs)
