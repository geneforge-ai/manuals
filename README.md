# GeneForge User Manuals

Official user documentation for the **GeneForge Internal Personalization Engine**.

## 📚 Available Manuals

| Document | Purpose | Audience |
|----------|---------|----------|
| [`MANUALE.md`](MANUALE.md) | Complete guide covering installation, CLI commands, pipeline flow, configuration, and troubleshooting | System integrators, DevOps, advanced users |
| [`QUICKSTART.md`](QUICKSTART.md) | One-page cheat sheet with the essential commands to get started in 5 minutes | New users, demo operators, field engineers |

## 🎯 What is GeneForge?

GeneForge transforms generic AI/ML templates into **fully personalized company clones** running on NVIDIA DGX Spark. The Internal Personalization Engine uses a **Council of Agents** with Red Teaming to ensure every decision is robust, compliant, and tailored to the client's culture.

## 🚀 Quick Start (30 seconds)

```bash
source ~/quigley_training/venv/bin/activate
cd /home/aintel/GeneForge-Mother-Clone-v1.0
python3 -m internal.cli test-run --client my-company --template AI_ML_PLATFORM
```

For the full guide, see [`QUICKSTART.md`](QUICKSTART.md).

## 🖥️ Hardware Requirements

- **NVIDIA DGX Spark** (Grace Blackwell, aarch64)
- DGX OS 7.x / Ubuntu 24.04
- Ollama with `nemotron-30b:latest` (or compatible local LLM)

## 📦 Related Repositories

- [GeneForge Core](https://github.com/geneforge-ai) — Main project repository
- [Firefox Snap Upload Fix](https://github.com/geneforge-ai/firefox-snap-upload-fix) — Browser workaround for DGX Spark users

---

*Last updated: Phase 2 completed — CEO Meta strict prompt + parameterized fallback verified.*
