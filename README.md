# GeneForge AI Labs — Manuals

> **The official documentation hub for GeneForge AI Clones.**  
> Build, personalize, deploy, and run autonomous AI agents tailored to your organization.

---

## 🧬 What is GeneForge?

GeneForge transforms generic AI/ML templates into **fully personalized company clones** running on local hardware (including NVIDIA DGX Spark). The Internal Personalization Engine uses a **Council of Agents** with built-in Red Teaming to ensure every decision is robust, compliant, and tailored to your culture.

This repository contains all user-facing documentation — from 5-minute quickstarts to deep technical references.

---

## 📚 Document Library

| # | Document | For | What it covers | ⏱️ |
|---|----------|-----|----------------|-----|
| 1 | **[QUICKSTART.md](QUICKSTART.md)** | Engineers, demo operators | Get your first clone running in one command | 2 min |
| 2 | **[CUSTOMER_JOURNEY_GUIDE.md](CUSTOMER_JOURNEY_GUIDE.md)** | Clients, Project Managers, CIOs | The 8-step journey from contract to `.geneclone` delivery | 8 min |
| 3 | **[GENEFORGE_DEPLOY_GUIDE.md](GENEFORGE_DEPLOY_GUIDE.md)** | Client IT / DevOps teams | Extract, verify, install, and launch a `.geneclone` package | 6 min |
| 4 | **[MANUALE.md](MANUALE.md)** | GeneForge engineering team | Internal engine: CLI, Council of Agents, Corporate Memory, thermal guardrails | 15 min |
| 5 | **[CUDA_DEVELOPMENT_GUIDE.md](CUDA_DEVELOPMENT_GUIDE.md)** | CUDA/AI developers | DGX Spark optimization, NVCC flags, unified memory, thermal management | 10 min |

---

## 🌍 Translations

Core documents are available in **English**, **Italian (Italiano)**, and **Bulgarian (Български)**.

| Document | 🇬🇧 English | 🇮🇹 Italiano | 🇧🇬 Български |
|----------|-----------|------------|--------------|
| **Quickstart** | [QUICKSTART_EN.md](QUICKSTART_EN.md) | [QUICKSTART_IT.md](QUICKSTART_IT.md) | [QUICKSTART_BG.md](QUICKSTART_BG.md) |
| **Customer Journey** | [CUSTOMER_JOURNEY_GUIDE_EN.md](CUSTOMER_JOURNEY_GUIDE_EN.md) | [CUSTOMER_JOURNEY_GUIDE_IT.md](CUSTOMER_JOURNEY_GUIDE_IT.md) | [CUSTOMER_JOURNEY_GUIDE_BG.md](CUSTOMER_JOURNEY_GUIDE_BG.md) |
| **Deploy Guide** | [GENEFORGE_DEPLOY_GUIDE_EN.md](GENEFORGE_DEPLOY_GUIDE_EN.md) | [GENEFORGE_DEPLOY_GUIDE_IT.md](GENEFORGE_DEPLOY_GUIDE_IT.md) | [GENEFORGE_DEPLOY_GUIDE_BG.md](GENEFORGE_DEPLOY_GUIDE_BG.md) |
| **Manuale / Manual** | [MANUALE_EN.md](MANUALE_EN.md) | [MANUALE_IT.md](MANUALE_IT.md) | [MANUALE_BG.md](MANUALE_BG.md) |

---

## 🎯 "I am a…" — Quick Navigation

### 📝 Client who just signed the contract
→ Start here: **[CUSTOMER_JOURNEY_GUIDE.md](CUSTOMER_JOURNEY_GUIDE.md)**  
Learn what documents to prepare, what happens at each phase, and when you'll receive your clone.

### 🖥️ IT admin receiving a `.geneclone` file
→ Start here: **[GENEFORGE_DEPLOY_GUIDE.md](GENEFORGE_DEPLOY_GUIDE.md)**  
Step-by-step instructions to extract, verify integrity, install dependencies, and launch the onboarding wizard.

### ⚡ Developer running a quick test
→ Start here: **[QUICKSTART.md](QUICKSTART.md)**  
The absolute minimum to get a test clone running in 5 minutes.

### 🛠️ GeneForge engineer building a clone
→ Start here: **[MANUALE.md](MANUALE.md)**  
Internal CLI, Council orchestration, Corporate Memory, and thermal guardrails.

### 🎛️ CUDA developer optimizing for DGX Spark
→ Start here: **[CUDA_DEVELOPMENT_GUIDE.md](CUDA_DEVELOPMENT_GUIDE.md)**  
Compute capability, unified memory, NVCC flags, and thermal guardrails.

### 🔬 AI researcher or ML engineer
→ Start here: **[MANUALE.md](MANUALE.md)** + **[CUDA_DEVELOPMENT_GUIDE.md](CUDA_DEVELOPMENT_GUIDE.md)**  
Understand the Council architecture, then dive into hardware-specific optimizations.

---

## 🖥️ System Requirements

| Component | Minimum | Recommended |
|-----------|---------|-------------|
| **Hardware** | Any Linux x86_64 or ARM64 | NVIDIA DGX Spark (Grace Blackwell) |
| **OS** | Ubuntu 22.04+ | DGX OS 7.x |
| **Python** | 3.10+ | 3.12 |
| **GPU** | Not required (CPU mode works) | NVIDIA Blackwell GB10 |
| **Browser** | Any modern browser | Chrome / Chromium |
| **Memory** | 4 GB RAM | 8 GB+ RAM |
| **Storage** | 2 GB free | 5 GB free |

---

## 🆘 Troubleshooting by Symptom

| Symptom | Likely Document | Section |
|---------|-----------------|---------|
| "How long until I get my clone?" | CUSTOMER_JOURNEY_GUIDE.md | [Summary Timeline](CUSTOMER_JOURNEY_GUIDE.md#summary-timeline) |
| "How do I install the `.geneclone` file?" | GENEFORGE_DEPLOY_GUIDE.md | [Deployment Steps](GENEFORGE_DEPLOY_GUIDE.md#deployment-steps) |
| "How do I verify package integrity?" | GENEFORGE_DEPLOY_GUIDE.md | [Verify Package Integrity](GENEFORGE_DEPLOY_GUIDE.md#step-3--verify-package-integrity) |
| `sm_121 not compatible` warning | CUDA_DEVELOPMENT_GUIDE.md | [Common Pitfalls](CUDA_DEVELOPMENT_GUIDE.md#6-common-pitfalls) |
| Firefox upload fails silently | — | See [firefox-snap-upload-fix](https://github.com/geneforge-ai/firefox-snap-upload-fix) |
| Need to run a quick test | QUICKSTART.md | [Single Command](QUICKSTART.md#comando-unico-testdemo) |

---

## 🔑 License Activation

GeneForge packages include a **machine-bound license** (`license.key`) for commercial protection while keeping the `.geneclone` package fully portable.

**Client-side:**
- Run [`scripts/collect-uuid.sh`](scripts/collect-uuid.sh) to get your System UUID
- Email it to `info@geneforge.eu` to receive your `license.key`

**GeneForge-side:**
- Use [`scripts/generate-license.py`](scripts/generate-license.py) to sign and generate `license.key` files

See [GENEFORGE_DEPLOY_GUIDE.md](GENEFORGE_DEPLOY_GUIDE.md) for full activation steps.

---

## 📦 Related Repositories

- [GeneForge Core](https://github.com/geneforge-ai) — Organization landing page
- [Firefox Snap Upload Fix](https://github.com/geneforge-ai/firefox-snap-upload-fix) — Browser workaround for DGX Spark users

---

## 📜 License

All documents in this repository are released under the **MIT License** unless otherwise specified.

---

*Last updated: 2026-04-16*  
*Version: 1.2 — Multilingual documentation suite*
