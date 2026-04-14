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
