# GeneForge AI Labs — Quick Start

> **Get a test clone running in 5 minutes.**  
> For the full manual, see [MANUALE.md](MANUALE.md).

---

## ⚡ Prerequisites
- DGX Spark (or any Linux) with Ollama running `nemotron-30b:latest`
- Virtual environment activated: `source ~/quigley_training/venv/bin/activate`

---

## One-Command Test Run

```bash
cd /home/aintel/GeneForge-Mother-Clone-v1.0
python3 -m internal.cli test-run --client <CLIENT> --template <TEMPLATE>
```

**Example:**
```bash
python3 -m internal.cli test-run --client acme-corp --template AI_ML_PLATFORM
```

This runs the full pipeline: Intake → Architecture Council → Personalization → Pre-Delivery Review → Packaging → Report.

---

## Manual Steps (if you need control)

```bash
# 1. Initialize client
python3 -m internal.cli init-client --id acme-corp --template AI_ML_PLATFORM

# 2. Add documents to internal/clients/acme-corp/docs/
# 3. Register them in memory
python3 -m internal.cli add-doc --client acme-corp \
  --filename company_overview.md --summary "Mission and values"

# 4. Run full pipeline
python3 -m internal.cli test-run --client acme-corp --template AI_ML_PLATFORM
```

---

## Output

```
internal/clients/acme-corp/output/
├── GeneForge-Custom-AcmeCorp-v1.0.geneclone   # Final package
└── FINAL_REPORT.md                              # Audit report
```

---

## Quick Config

Edit `internal/config/internal_config.yaml` to tune:
- `temperature` / `ceo_temperature` — quality vs creativity
- `timeout_per_agent` — if Nemotron is slow
- `cooldown_seconds` — pause between agents
- `batch_size` — parallel agents

---

## Troubleshooting

| Problem | Fix |
|---------|-----|
| `CEO Meta format drift detected` | Normal — enforcer auto-corrects |
| Timeout | Increase `timeout_per_agent` in config |
| Temp > 80°C | Engine auto-pauses; improve ventilation |
| `ImportError` | `source ~/quigley_training/venv/bin/activate` |
| Firefox upload fails | Use Chrome or see [firefox-snap-upload-fix](https://github.com/geneforge-ai/firefox-snap-upload-fix) |

---

For the full manual see [MANUALE.md](MANUALE.md).
