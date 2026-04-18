# GeneForge Internal Engine — Quick Start

> **Get a test clone running in 5 minutes.**  
> For the full manual, see [MANUALE.md](MANUALE.md).

---

## ⚡ Requirements
- Active DGX Spark, Ollama running `nematron-30b:latest`
- Virtual environment activated: `source ~/quigley_training/venv/bin/activate`

---

## One-liner (test/demo)

```bash
cd /home/aintel/GeneForge-Mother-Clone-v1.0
python3 -m internal.cli test-run --client <CLIENT_NAME> --template <TEMPLATE>
```

**Example:**
```bash
python3 -m internal.cli test-run --client acme-corp --template AI_ML_PLATFORM
```

Runs everything: Intake → Architecture Council → Personalization → Pre-Delivery Council → Packaging → Report.

---

## Manual flow (full control)

### 1. Initialize client
```bash
python3 -m internal.cli init-client --id acme-corp --template AI_ML_PLATFORM
```

### 2. Drop documents into the docs folder
```bash
mkdir -p internal/clients/acme-corp/docs
# copy your .md / .pdf / .yaml files here
```

### 3. Load documents into memory
```bash
python3 -m internal.cli add-doc \
  --client acme-corp \
  --filename company_overview.md \
  --summary "Company mission and values"
```

### 4. Run full pipeline
```bash
python3 -m internal.cli test-run --client acme-corp --template AI_ML_PLATFORM
```

---

## Output

After execution, check:
```
internal/clients/acme-corp/output/
├── GeneForge-Custom-AcmeCorp-v1.0.geneclone   # Final package
└── FINAL_REPORT.md                              # Summary report
```

---

## Quick config

Edit `internal/config/internal_config.yaml` to tune:
- `temperature` / `ceo_temperature` — quality vs creativity
- `timeout_per_agent` — if Nemotron is slow
- `cooldown_seconds` — pause between agents
- `batch_size` — agents run in parallel

---

## Troubleshooting

| Issue | Fix |
|-------|-----|
| `CEO Meta format drift detected` | Normal — enforcer auto-corrects |
| Timeout | Increase `timeout_per_agent` in the YAML config |
| Temp > 80°C | Engine auto-pauses |
| `ImportError` | `source ~/quigley_training/venv/bin/activate` |
| File upload fails on Firefox | Firefox Snap blocks filesystem access → use Chrome or see [firefox-snap-upload-fix](https://github.com/geneforge-ai/firefox-snap-upload-fix) |

---

For the full manual see `internal/MANUALE.md`.
