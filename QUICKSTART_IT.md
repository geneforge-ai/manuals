# GeneForge Internal Engine — Quick Start

> **Avvia un clone di test in 5 minuti.**  
> Per il manuale completo, vedi [MANUALE.md](MANUALE.md).

---

## ⚡ Requisiti
- DGX Spark attivo, Ollama in esecuzione con `nematron-30b:latest`
- Virtual environment attivato: `source ~/quigley_training/venv/bin/activate`

---

## Comando unico (test/demo)

```bash
cd /home/aintel/GeneForge-Mother-Clone-v1.0
python3 -m internal.cli test-run --client <NOME_CLIENTE> --template <TEMPLATE>
```

**Esempio:**
```bash
python3 -m internal.cli test-run --client acme-corp --template AI_ML_PLATFORM
```

Esegue tutto: Intake → Architecture Council → Personalization → Pre-Delivery Council → Packaging → Report.

---

## Flusso manuale (controllo totale)

### 1. Inizializza il cliente
```bash
python3 -m internal.cli init-client --id acme-corp --template AI_ML_PLATFORM
```

### 2. Carica i documenti nella cartella docs
```bash
mkdir -p internal/clients/acme-corp/docs
# copia i tuoi file .md / .pdf / .yaml qui
```

### 3. Carica i documenti in memoria
```bash
python3 -m internal.cli add-doc \
  --client acme-corp \
  --filename company_overview.md \
  --summary "Mission e valori azienda"
```

### 4. Esegui la pipeline completa
```bash
python3 -m internal.cli test-run --client acme-corp --template AI_ML_PLATFORM
```

---

## Output

Dopo l'esecuzione, trovi in:
```
internal/clients/acme-corp/output/
├── GeneForge-Custom-AcmeCorp-v1.0.geneclone   # Pacchetto finale
└── FINAL_REPORT.md                              # Report riassuntivo
```

---

## Configurazione rapida

Modifica `internal/config/internal_config.yaml` per regolare:
- `temperature` / `ceo_temperature` — qualità vs creatività
- `timeout_per_agent` — se Nemotron è lento
- `cooldown_seconds` — pausa tra agenti
- `batch_size` — agenti eseguiti in parallelo

---

## Troubleshooting

| Problema | Soluzione |
|----------|-----------|
| `CEO Meta format drift detected` | Normale — l'enforcer corregge automaticamente |
| Timeout | Aumenta `timeout_per_agent` nel config YAML |
| Temp > 80°C | Il motore si mette in pausa automaticamente |
| `ImportError` | `source ~/quigley_training/venv/bin/activate` |
| L'upload dei file non funziona su Firefox | Firefox Snap blocca l'accesso al filesystem → usa Chrome o vedi [firefox-snap-upload-fix](https://github.com/geneforge-ai/firefox-snap-upload-fix) |

---

Per il manuale completo vedi `internal/MANUALE.md`.
