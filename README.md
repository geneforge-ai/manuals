# GeneForge User Manuals

> **Your complete guide to building, deploying, and running GeneForge AI clones.**

---

## 📚 Document Index

| Document | Who is it for? | What you'll learn | Read time |
|----------|----------------|-------------------|-----------|
| **[QUICKSTART.md](QUICKSTART.md)** | New users, demo operators | Get your first clone running in 5 minutes | ⏱️ 2 min |
| **[CUSTOMER_JOURNEY_GUIDE.md](CUSTOMER_JOURNEY_GUIDE.md)** | Clients, Project Managers | The 8-step journey from contract signature to `.geneclone` delivery | ⏱️ 8 min |
| **[GENEFORGE_DEPLOY_GUIDE.md](GENEFORGE_DEPLOY_GUIDE.md)** | Client IT / DevOps teams | How to extract, install, and launch a `.geneclone` package | ⏱️ 6 min |
| **[MANUALE.md](MANUALE.md)** | GeneForge engineering team | Internal engine: CLI, Council of Agents, Corporate Memory, thermal guardrails | ⏱️ 15 min |
| **[CUDA_DEVELOPMENT_GUIDE.md](CUDA_DEVELOPMENT_GUIDE.md)** | CUDA/AI developers | DGX Spark hardware specs, NVCC flags, thermal & power management | ⏱️ 10 min |

---

## 🎯 Quick Navigation

### I'm a client who just signed the contract
→ Start here: **[CUSTOMER_JOURNEY_GUIDE.md](CUSTOMER_JOURNEY_GUIDE.md)**  
Learn what documents to prepare, what happens at each phase, and when you'll receive your clone.

### I'm an IT admin receiving a `.geneclone` file
→ Start here: **[GENEFORGE_DEPLOY_GUIDE.md](GENEFORGE_DEPLOY_GUIDE.md)**  
Step-by-step instructions to extract, install dependencies, and launch the onboarding wizard.

### I'm a developer optimizing for DGX Spark
→ Start here: **[CUDA_DEVELOPMENT_GUIDE.md](CUDA_DEVELOPMENT_GUIDE.md)**  
Compute capability, unified memory, NVCC flags, and thermal guardrails.

### I'm on the GeneForge team running a demo
→ Start here: **[QUICKSTART.md](QUICKSTART.md)**  
The absolute minimum to get a test clone running.

---

## 🧬 What is GeneForge?

GeneForge transforms generic AI/ML templates into **fully personalized company clones** running on NVIDIA DGX Spark. The Internal Personalization Engine uses a **Council of Agents** with built-in Red Teaming to ensure every decision is robust, compliant, and tailored to the client's culture.

---

## 🖥️ System Requirements

| Component | Minimum | Recommended |
|-----------|---------|-------------|
| **Hardware** | Any Linux x86_64 or ARM64 | NVIDIA DGX Spark (Grace Blackwell) |
| **OS** | Ubuntu 22.04+ | DGX OS 7.x |
| **Python** | 3.10+ | 3.12 |
| **GPU** | Not required (CPU mode works) | NVIDIA Blackwell GB10 |
| **Browser** | Any modern browser | Chrome / Chromium |

---

## 🆘 Troubleshooting by Symptom

| Symptom | Likely Document | Section |
|---------|-----------------|---------|
| "How long until I get my clone?" | CUSTOMER_JOURNEY_GUIDE.md | [Timeline](CUSTOMER_JOURNEY_GUIDE.md#summary-timeline) |
| "How do I install the `.geneclone` file?" | GENEFORGE_DEPLOY_GUIDE.md | [Deployment Steps](GENEFORGE_DEPLOY_GUIDE.md#deployment-steps) |
| `sm_121 not compatible` warning | CUDA_DEVELOPMENT_GUIDE.md | [Common Pitfalls](CUDA_DEVELOPMENT_GUIDE.md#6-common-pitfalls) |
| Firefox upload fails silently | — | See [firefox-snap-upload-fix](https://github.com/geneforge-ai/firefox-snap-upload-fix) |
| Need to run a quick test | QUICKSTART.md | [Single Command](QUICKSTART.md#comando-unico-testdemo) |

---

## 📦 Related Repositories

- [GeneForge Core](https://github.com/geneforge-ai) — Organization landing page
- [Firefox Snap Upload Fix](https://github.com/geneforge-ai/firefox-snap-upload-fix) — Browser workaround for DGX Spark users

---

## 📜 License

All documents in this repository are released under the **MIT License** unless otherwise specified.

---

*Last updated: 2026-04-16*  
*Version: 1.1*
