# GeneForge AI Labs — Quick Start

> **Avvia un clone di test in 5 minuti.**  
> Per il manuale completo, vedi [MANUALE_IT.md](MANUALE_IT.md).

---

## ⚡ Prerequisiti
- DGX Spark (o qualsiasi Linux) con Ollama in esecuzione con `nemotron-30b:latest`
- Ambiente virtuale attivato: `source ~/quigley_training/venv/bin/activate`

---

## Comando Unico (test/demo)

```bash
cd /home/aintel/GeneForge-Mother-Clone-v1.0
python3 -m internal.cli test-run --client <CLIENTE> --template <TEMPLATE>
```

**Esempio:**
```bash
python3 -m internal.cli test-run --client acme-corp --template AI_ML_PLATFORM
```

Esegue l'intera pipeline: Intake → Architecture Council → Personalization → Pre-Delivery Council → Packaging → Report.

---

## Passaggi Manuali (se hai bisogno di controllo)

```bash
# 1. Inizializza cliente
python3 -m internal.cli init-client --id acme-corp --template AI_ML_PLATFORM

# 2. Aggiungi documenti in internal/clients/acme-corp/docs/
# 3. Registrali in memoria
python3 -m internal.cli add-doc --client acme-corp \
  --filename company_overview.md --summary "Mission e valori"

# 4. Esegui pipeline completa
python3 -m internal.cli test-run --client acme-corp --template AI_ML_PLATFORM
```

---

## Output

```
internal/clients/acme-corp/output/
├── GeneForge-Custom-AcmeCorp-v1.0.geneclone   # Pacchetto finale
└── FINAL_REPORT.md                              # Report di audit
```

---

## Configurazione Rapida

Modifica `internal/config/internal_config.yaml` per regolare:
- `temperature` / `ceo_temperature` — qualità vs creatività
- `timeout_per_agent` — se Nemotron è lento
- `cooldown_seconds` — pausa tra agenti
- `batch_size` — agenti in parallelo

---

## Troubleshooting

| Problema | Soluzione |
|----------|-----------|
| `CEO Meta format drift detected` | Normale — l'enforcer corregge automaticamente |
| Timeout | Aumenta `timeout_per_agent` nel config |
| Temp > 80°C | Il motore si mette in pausa automaticamente |
| `ImportError` | `source ~/quigley_training/venv/bin/activate` |
| Upload Firefox fallito | Usa Chrome o vedi [firefox-snap-upload-fix](https://github.com/geneforge-ai/firefox-snap-upload-fix) |

---

Per il manuale completo vedi [MANUALE_IT.md](MANUALE_IT.md).
