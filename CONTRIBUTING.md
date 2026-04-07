# Contributing to CSI Operations

We welcome contributions that improve clarity, accuracy, safety, and reproducibility.

## How to propose changes

1. Create a new branch:

    git checkout -b feature/update-sop-name

2. Edit the relevant Markdown files.
3. Commit with a descriptive message:

    git commit -m "Update acceptance criteria for sample preparation"

4. Open a Pull Request (PR) and describe:
- What changed
- Why it changed
- Any implications for downstream workflows

## SOP formatting guidelines

Each SOP should include:

- **Title**
- **Version**
- **Author(s)**
- **Last review date**
- **Purpose**
- **Scope**
- **Responsibilities**
- **Materials and equipment**
- **Procedure**
- **Quality control / acceptance criteria**
- **Hazards and safety**
- **References**
- **Attachments**

Use YAML front matter at the top of each SOP:

```yaml
---
title: Sample Preparation
version: 1.3
author: Christophe
review_cycle: 12 months
---

## Optional: Building the documentation website

If using MkDocs:
1. Install dependencies:

    pip install mkdocs-material

2. Build locally:

    mkdocs serve

3. Deploy to GitHub Pages:

    mkdocs gh-deploy


## Code of Conduct

Be constructive, respectful, and transparent.


---

### **sop-index.md**

```markdown
# SOP Index

This index provides an overview of all Standard Operating Procedures in the CSI laboratory.

## Sample Preparation

- [Sample Preparation](sop/sample-preparation/sample-preparation.md)
- [Hazards](sop/sample-preparation/hazards.md)
- [Acceptance Criteria](sop/sample-preparation/acceptance-criteria.md)

## ICP-OES

- [ICP-OES Operation](sop/icp-oes/icp-oes-operation.md)
- [Calibration Procedure](sop/icp-oes/calibration.md)
- [Troubleshooting Guide](sop/icp-oes/troubleshooting.md)

## DNA Extraction

- [DNA Extraction](sop/dna-extraction/dna-extraction.md)

---

If you add a new SOP, please update this index accordingly.
