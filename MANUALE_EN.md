# GeneForge AI Labs — Internal Engine Manual

## 🏆 Golden Rules

> Always follow these rules. Violating even one can compromise clone quality or cause a system freeze.

1. **🔥 Thermal First** — If the GPU exceeds 78 °C, slow down or stop execution. Throttling is real.
2. **🧠 No CEO Meta without Council** — CEO Meta never decides alone. It must always activate the Council of Agents.
3. **📄 Document before you clone** — The personalized clone does not start without approved documentation and QA sign-off.
4. **🔴 Red Team is mandatory** — Every deliverable must pass the Red Team stress test (Compliance + QA GATE).
5. **🤖 Do not invent roles** — Agents must never simulate or invent fake roles. Respond only with the assigned role.
6. **💾 Corporate Memory is sacred** — Every decision, document, and checkpoint is saved. Do not bypass memory.
7. **🌡️ 45 °C is your friend** — If the Council runs at ~41–45 °C, you are in the optimal range. If it goes above 50 °C, intervene.
8. **📦 .geneclone is portable** — Never tie the package to specific hardware. It must run on any Linux.

---

## 1. What the internal engine is

The **GeneForge Internal Personalization Engine** is the system that transforms a public template (`Templates/`) into a custom AI clone for a specific client. It is completely isolated under the `internal/` folder and does not touch the public demo code.

Main components:
- **Internal CLI** (`internal/cli.py`) — entry point for all operations
- **Council of Agents** (`internal/engine/council_orchestrator.py`) — multi-agent decision-making with Red Team
- **Corporate Memory** (`internal/memory/client_memory.py`) — JSON/YAML persistence of documents and decisions
- **Personalization Pipeline** (`internal/engine/personalization_pipeline.py`) — automated end-to-end flow
- **System Monitor** (`internal/engine/system_monitor.py`) — thermal guards for DGX Spark

---

## 2. Requirements

- **Hardware**: NVIDIA DGX Spark (Grace Blackwell, aarch64)
- **OS**: DGX OS 7.x / Ubuntu 24.04
- **Python**: 3.12
- **Virtual env**: `~/quigley_training/venv` (pre-configured on the system)
- **LLM backend**: Local Ollama at `http://localhost:11434`
- **Recommended model**: `nemotron-30b:latest`
- **Default quantization**: `Q4_K_M` (from May 2026) — ensures maximum stability on DGX Spark. FP4 will be re-enabled after NVIDIA official fix for GB10.

Activate the environment before using the CLI:
```bash
source ~/quigley_training/venv/bin/activate
```

---

## 3. Available commands

All commands run via `python3 -m internal.cli`.

### `init-client`
Initializes a new client in the internal engine.
```bash
python3 -m internal.cli init-client \
  --id <CLIENT_ID> \
  --template <TEMPLATE_ID>
```
**Example:**
```bash
python3 -m internal.cli init-client \
  --id acme-corp \
  --template AI_ML_PLATFORM
```

### `add-doc`
Uploads a document into the client's Corporate Memory.
```bash
python3 -m internal.cli add-doc \
  --client <CLIENT_ID> \
  --filename <FILE_NAME> \
  --summary "<SHORT_DESCRIPTION>"
```
**Example:**
```bash
python3 -m internal.cli add-doc \
  --client acme-corp \
  --filename company_overview.md \
  --summary "Mission, vision, values, and 2026 strategic goals."
```

> **Note**: the file must physically exist in `internal/clients/<CLIENT_ID>/docs/`. The command registers the name and summary in memory.

### `run-council`
Manually activates the Council of Agents for a specific topic.
```bash
python3 -m internal.cli run-council \
  --client <CLIENT_ID> \
  --template <TEMPLATE_ID> \
  --topic "<TOPIC>" \
  [--model nemotron-30b:latest]
```
**Examples:**
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
Runs only the packaging phase (requires the customized blueprint to already exist).
```bash
python3 -m internal.cli build \
  --client <CLIENT_ID> \
  --template <TEMPLATE_ID>
```

### `test-run`
**Recommended command for testing.** Runs the entire end-to-end pipeline in one shot:
1. Initializes the client (if the dossier is missing)
2. Architecture Council
3. Blueprint Personalization
4. Pre-Delivery Council
5. Packaging
6. Final Report generation

```bash
python3 -m internal.cli test-run \
  --client <CLIENT_ID> \
  --template <TEMPLATE_ID>
```

---

## 4. Step-by-step flow (manual mode)

### Step 1: Create the client
```bash
python3 -m internal.cli init-client --id acme-corp --template AI_ML_PLATFORM
```

### Step 2: Prepare documents
```bash
mkdir -p internal/clients/acme-corp/docs
# copy your markdown/pdf/yaml files
```

### Step 3: Load documents into Corporate Memory
```bash
python3 -m internal.cli add-doc --client acme-corp \
  --filename company_overview.md \
  --summary "Company description, mission, and values"

python3 -m internal.cli add-doc --client acme-corp \
  --filename process_map.md \
  --summary "Map of main processes"
```

### Step 4: Launch the first Council (Architecture Decision)
```bash
python3 -m internal.cli run-council \
  --client acme-corp \
  --template AI_ML_PLATFORM \
  --topic "Architecture Decision: How should we personalize this template for the client?"
```

### Step 5: Check the result
Review the logs in:
- `internal/clients/acme-corp/council_logs/`
- `internal/clients/acme-corp/pipeline_checkpoints/`

### Step 6: Run the full pipeline (or use `test-run`)
If you want to proceed manually, run `build` after customizing the blueprint. Alternatively, just use `test-run`.

---

## 5. Fast track with `test-run`

For most tests and demos, run directly:

```bash
python3 -m internal.cli test-run --client acme-corp --template AI_ML_PLATFORM
```

This command:
- Auto-initializes the client if it has no dossier
- Runs the Council on Architecture Decision
- Customizes the blueprint
- Runs the Council on Pre-Delivery Review
- Generates the `.geneclone` package
- Writes the `FINAL_REPORT.md`

---

## 6. Client output structure

After a successful `test-run`, you will find:

```
internal/clients/<CLIENT_ID>/
├── client_memory.json          # Dossier + documents + decisions
├── client_memory.yaml          # Human-readable cache
├── docs/                       # Uploaded documents
├── output/
│   ├── GeneForge-Custom-<Name>-v1.0.geneclone   # Final package
│   └── FINAL_REPORT.md         # Summary report
├── council_logs/               # Detailed logs for each Council
├── pipeline_checkpoints/       # Step-by-step checkpoints
└── .work/                      # Customized blueprint (temp)
```

---

## 7. Complete end-to-end example

```bash
# 1. Activate environment
source ~/quigley_training/venv/bin/activate
cd /home/aintel/GeneForge-Mother-Clone-v1.0

# 2. Initialize
python3 -m internal.cli init-client \
  --id geneforge-realistic-test \
  --template AI_ML_PLATFORM

# 3. Create documents
mkdir -p internal/clients/geneforge-realistic-test/docs
cat > internal/clients/geneforge-realistic-test/docs/company_overview.md << 'EOF'
# GeneForge AI Labs
Mission: democratize safe AI clones...
EOF

# 4. Load into memory
python3 -m internal.cli add-doc \
  --client geneforge-realistic-test \
  --filename company_overview.md \
  --summary "Company mission and strategic priorities"

# 5. Run full pipeline
python3 -m internal.cli test-run \
  --client geneforge-realistic-test \
  --template AI_ML_PLATFORM

# 6. Read the report
cat internal/clients/geneforge-realistic-test/output/FINAL_REPORT.md
```

---

## 8. Runtime configuration

The file `internal/config/internal_config.yaml` holds the engine parameters:

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

Edit these values to tune speed, quality, and thermal stress.

---

## 9. Troubleshooting

| Symptom | Probable cause | Fix |
|---------|----------------|-----|
| `CEO Meta format drift detected` | Nemotron simulated the marker inside `<think>` | **Normal** — the format enforcer intervenes automatically and corrects |
| Timeout after 60s | Nemotron-30B is slow on long prompts | Increase `timeout_per_agent` in the YAML config |
| Temp > 80°C | DGX Spark overheating | The engine auto-pauses; improve ventilation |
| `ImportError` | Virtual environment not activated | `source ~/quigley_training/venv/bin/activate` |
| `add-doc` asks for `--summary` | Missing required argument | Add `--summary "..."` |
| File upload fails on Firefox | Firefox Snap blocks filesystem access | Use Chrome/Chromium or see [firefox-snap-upload-fix](https://github.com/geneforge-ai/firefox-snap-upload-fix) |

---

## 10. Operational notes

- **Never modify** files in `wizard/` or `Templates/` during internal work: the engine is designed to read-only from those paths.
- Every Council adds 2 decisions to `client_memory.json`. For long-term clients, plan a pruning/decay logic.
- The `.geneclone` package is a renamed `.zip` file: portable, not tied to specific hardware.

---

*Last updated: Phase 2 completed — CEO Meta strict prompt + parameterized fallback verified.*
