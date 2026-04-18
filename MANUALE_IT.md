# GeneForge AI Labs — Manuale Motore Interno

## 🏆 Regole d'oro

> Segui sempre queste regole. Violare anche una sola può compromettere la qualità del clone o causare il freeze del sistema.

1. **🔥 Thermal First** — Se la GPU supera i 78 °C, rallenta o ferma l'esecuzione. Il throttling è reale.
2. **🧠 Nessun CEO Meta senza Council** — Il CEO Meta non decide mai da solo. Deve sempre attivare il Council of Agents.
3. **📄 Documenta prima di clonare** — Il clone personalizzato non parte senza documentazione approvata e QA sign-off.
4. **🔴 Red Team è obbligatorio** — Ogni deliverable deve passare lo stress-test del Red Team (Compliance + QA GATE).
5. **🤖 Non inventare ruoli** — Gli agenti non devono mai simulare o inventare ruoli falsi. Rispondi solo con il ruolo assegnato.
6. **💾 Corporate Memory è sacra** — Ogni decisione, documento e checkpoint viene salvato. Non bypassare la memoria.
7. **🌡️ 45 °C è il tuo amico** — Se il Council gira a ~41–45 °C, stai nel range ottimale. Se sale oltre 50 °C, intervenire.
8. **📦 .geneclone è portabile** — Non legare mai il pacchetto a un hardware specifico. Deve girare su qualsiasi Linux.

---

## 1. Cos'è il motore interno

Il **GeneForge Internal Personalization Engine** è il sistema che trasforma un template pubblico (`Templates/`) in un clone AI personalizzato per un cliente specifico. È completamente isolato sotto la cartella `internal/` e non tocca il codice del demo pubblico.

Componenti principali:
- **CLI interna** (`internal/cli.py`) — punto di ingresso per tutte le operazioni
- **Council of Agents** (`internal/engine/council_orchestrator.py`) — decision-making multi-agente con Red Team
- **Corporate Memory** (`internal/memory/client_memory.py`) — persistenza JSON/YAML dei documenti e delle decisioni
- **Personalization Pipeline** (`internal/engine/personalization_pipeline.py`) — flusso end-to-end automatizzato
- **System Monitor** (`internal/engine/system_monitor.py`) — guardie termiche per DGX Spark

---

## 2. Requisiti

- **Hardware**: NVIDIA DGX Spark (Grace Blackwell, aarch64)
- **OS**: DGX OS 7.x / Ubuntu 24.04
- **Python**: 3.12
- **Virtual env**: `~/quigley_training/venv` (già configurato nel sistema)
- **LLM backend**: Ollama locale su `http://localhost:11434`
- **Modello consigliato**: `nemotron-30b:latest`

Attiva l'ambiente prima di usare la CLI:
```bash
source ~/quigley_training/venv/bin/activate
```

---

## 3. Comandi disponibili

Tutti i comandi partono da `python3 -m internal.cli`.

### `init-client`
Inizializza un nuovo cliente nel motore interno.
```bash
python3 -m internal.cli init-client \
  --id <CLIENT_ID> \
  --template <TEMPLATE_ID>
```
**Esempio:**
```bash
python3 -m internal.cli init-client \
  --id acme-corp \
  --template AI_ML_PLATFORM
```

### `add-doc`
Carica un documento nella Corporate Memory del cliente.
```bash
python3 -m internal.cli add-doc \
  --client <CLIENT_ID> \
  --filename <NOME_FILE> \
  --summary "<DESCRIZIONE_BREVE>"
```
**Esempio:**
```bash
python3 -m internal.cli add-doc \
  --client acme-corp \
  --filename company_overview.md \
  --summary "Mission, visione, valori e obiettivi strategici 2026."
```

> **Nota**: il file deve trovarsi fisicamente in `internal/clients/<CLIENT_ID>/docs/`. Il comando registra il nome e il summary in memoria.

### `run-council`
Attiva manualmente il Council of Agents per un topic specifico.
```bash
python3 -m internal.cli run-council \
  --client <CLIENT_ID> \
  --template <TEMPLATE_ID> \
  --topic "<TOPIC>" \
  [--model nemotron-30b:latest]
```
**Esempi:**
```bash
# Architecture Decision
python3 -m internal.cli run-council \
  --client acme-corp \
  --template AI_ML_PLATFORM \
  --topic "Architecture Decision: How should we personalize this template for the client?"

# Pre-Delivery Review
python3 -m internal.cli run-council \
  --client acme-corp \
  --template AI_ML_PLATFORM \
  --topic "Pre-Delivery Review: Is the personalized package ready for delivery?"
```

### `build`
Esegue solo la fase di packaging (richiede che il blueprint personalizzato esista già).
```bash
python3 -m internal.cli build \
  --client <CLIENT_ID> \
  --template <TEMPLATE_ID>
```

### `test-run`
**Comando consigliato per i test.** Esegue l'intera pipeline end-to-end in un colpo solo:
1. Inizializza il client (se manca il dossier)
2. Architecture Council
3. Blueprint Personalization
4. Pre-Delivery Council
5. Packaging
6. Generazione Final Report

```bash
python3 -m internal.cli test-run \
  --client <CLIENT_ID> \
  --template <TEMPLATE_ID>
```

---

## 4. Flusso passo-passo (modo manuale)

### Step 1: Crea il cliente
```bash
python3 -m internal.cli init-client --id acme-corp --template AI_ML_PLATFORM
```

### Step 2: Prepara i documenti
```bash
mkdir -p internal/clients/acme-corp/docs
# copia i tuoi file markdown/pdf/yaml
```

### Step 3: Carica i documenti in Corporate Memory
```bash
python3 -m internal.cli add-doc --client acme-corp \
  --filename company_overview.md \
  --summary "Descrizione azienda, mission e valori"

python3 -m internal.cli add-doc --client acme-corp \
  --filename process_map.md \
  --summary "Mappa dei processi principali"
```

### Step 4: Avvia il primo Council (Architecture Decision)
```bash
python3 -m internal.cli run-council \
  --client acme-corp \
  --template AI_ML_PLATFORM \
  --topic "Architecture Decision: How should we personalize this template for the client?"
```

### Step 5: Controlla il risultato
Consulta i log in:
- `internal/clients/acme-corp/council_logs/`
- `internal/clients/acme-corp/pipeline_checkpoints/`

### Step 6: Avvia la pipeline completa (o usa `test-run`)
Se vuoi procedere manualmente, esegui `build` dopo aver personalizzato il blueprint. In alternativa, usa direttamente `test-run`.

---

## 5. Flusso rapido con `test-run`

Per la maggior parte dei test e delle demo, usa direttamente:

```bash
python3 -m internal.cli test-run --client acme-corp --template AI_ML_PLATFORM
```

Questo comando:
- Auto-inizializza il client se non ha un dossier
- Esegue il Council su Architecture Decision
- Personalizza il blueprint
- Esegue il Council su Pre-Delivery Review
- Genera il pacchetto `.geneclone`
- Scrive il `FINAL_REPORT.md`

---

## 6. Struttura output di un cliente

Dopo una `test-run` riuscita, trovi:

```
internal/clients/<CLIENT_ID>/
├── client_memory.json          # Dossier + documenti + decisioni
├── client_memory.yaml          # Cache leggibile
├── docs/                       # Documenti caricati
├── output/
│   ├── GeneForge-Custom-<Nome>-v1.0.geneclone   # Pacchetto finale
│   └── FINAL_REPORT.md         # Report riassuntivo
├── council_logs/               # Log dettagliati di ogni Council
├── pipeline_checkpoints/       # Checkpoint step-by-step
└── .work/                      # Blueprint personalizzato (temp)
```

---

## 7. Esempio completo end-to-end

```bash
# 1. Attiva ambiente
source ~/quigley_training/venv/bin/activate
cd /home/aintel/GeneForge-Mother-Clone-v1.0

# 2. Inizializza
python3 -m internal.cli init-client \
  --id geneforge-realistic-test \
  --template AI_ML_PLATFORM

# 3. Crea documenti
mkdir -p internal/clients/geneforge-realistic-test/docs
cat > internal/clients/geneforge-realistic-test/docs/company_overview.md << 'EOF'
# GeneForge AI Labs
Mission: democratize safe AI clones...
EOF

# 4. Carica in memoria
python3 -m internal.cli add-doc \
  --client geneforge-realistic-test \
  --filename company_overview.md \
  --summary "Company mission and strategic priorities"

# 5. Esegui pipeline completa
python3 -m internal.cli test-run \
  --client geneforge-realistic-test \
  --template AI_ML_PLATFORM

# 6. Leggi il report
cat internal/clients/geneforge-realistic-test/output/FINAL_REPORT.md
```

---

## 8. Configurazione runtime

Il file `internal/config/internal_config.yaml` contiene i parametri del motore:

```yaml
council:
  default_model: "nemotron-30b:latest"
  temperature: 0.3
  ceo_temperature: 0.25
  max_tokens_per_agent: 500
  ceo_max_tokens: 800
  timeout_per_agent: 60
  red_team_timeout: 90
  cooldown_seconds: 3.0
  batch_size: 2
  warning_temp_c: 72.0
  critical_temp_c: 80.0
```

Modifica questi valori per adattare velocità, qualità e stress termico.

---

## 9. Troubleshooting

| Sintomo | Causa probabile | Soluzione |
|---------|-----------------|-----------|
| `CEO Meta format drift detected` | Nemotron ha simulato il marker dentro `<think>` | **Normale** — il format enforcer interviene automaticamente e corregge |
| Timeout dopo 60s | Nemotron-30B è lento su prompt lunghi | Aumenta `timeout_per_agent` nel config YAML |
| Temp > 80°C | DGX Spark surriscaldato | Il motore si mette in pausa automaticamente; migliora la ventilazione |
| `ImportError` | Virtual environment non attivato | `source ~/quigley_training/venv/bin/activate` |
| `add-doc` chiede `--summary` | Argomento obbligatorio mancante | Aggiungi `--summary "..."` |
| L'upload dei file non funziona su Firefox | Firefox Snap blocca l'accesso al filesystem | Usa Chrome/Chromium o vedi [firefox-snap-upload-fix](https://github.com/geneforge-ai/firefox-snap-upload-fix) |

---

## 10. Note operative

- **Non modificare mai** i file in `wizard/` o `Templates/` durante il lavoro interno: il motore è progettato per lavorare in sola lettura su quei path.
- Ogni Council aggiunge 2 decisioni alla `client_memory.json`. Per client a lungo termine, pianifica una logica di pruning/decadimento.
- Il pacchetto `.geneclone` è un file `.zip` rinominato: portatile, non legato a hardware specifico.

---

*Ultimo aggiornamento: Fase 2 completata — CEO Meta strict prompt + fallback parametrizzato verificati.*
