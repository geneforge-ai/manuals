# Guida al Deploy di GeneForge — Pacchetto `.geneclone`

Questa guida descrive come ricevere, estrarre, distribuire ed eseguire un **GeneForge Custom Clone** confezionato come artefatto `.geneclone`.

---

## 1. Cos'è un pacchetto `.geneclone`?

Un file `.geneclone` è un **archivio ZIP rinominato** che contiene un clone AI completamente personalizzato:

```
GeneForge-Custom-<CompanyName>-v1.0.geneclone
├── agents/                     # Prompt degli agent AI personalizzati
├── config/                     # File di configurazione (YAML, JSON)
├── restore-geneclone.sh        # Script di ripristino automatico
└── wizard/
    ├── app_onboarding.py       # Wizard di onboarding Streamlit
    ├── launch_onboarding.sh    # Helper di avvio
    └── requirements.txt        # Dipendenze Python
```

> **Nota:** Il pacchetto è **indipendente dall'hardware** (hardware-agnostic). Non è vincolato a una macchina specifica. È possibile distribuirlo su qualsiasi sistema Linux che soddisfi i requisiti indicati di seguito.

---

## 2. Requisiti di Sistema

### Requisiti Minimi
| Componente | Requisito |
|-----------|-------------|
| **OS** | Linux (Ubuntu 22.04+ consigliato) |
| **Python** | 3.10 o superiore |
| **Bash** | GNU bash 4.0+ |
| **Memoria** | 4 GB RAM (8 GB consigliati) |
| **Archiviazione** | 2 GB di spazio libero |
| **Rete** | Accesso a Internet per l'installazione iniziale delle dipendenze |

### Consigliati per un'Esperienza Completa
| Componente | Requisito |
|-----------|-------------|
| **GPU** | GPU NVIDIA con CUDA 11.8+ (opzionale — funziona anche in modalità CPU) |
| **OS** | DGX OS 7.x / Ubuntu 24.04 |
| **Browser** | Chrome, Chromium o Firefox (non-Snap) |
| **Ambiente Python** | `venv` o `conda` |

---

## 3. Fasi di Deploy

### Fase 1 — Ricezione del Pacchetto

Il file `.geneclone` viene consegnato dal team GeneForge tramite:
- Trasferimento file sicuro (SFTP, email crittografata)
- Archivio condiviso (S3, Google Drive, NAS interno)
- Supporto fisico (chiavetta USB)

Posizionare il file in una directory di lavoro:
```bash
mkdir -p ~/geneforge-deploy
cp /path/to/GeneForge-Custom-*-v1.0.geneclone ~/geneforge-deploy/
```

### Fase 2 — Estrazione del Pacchetto

Un `.geneclone` è un file ZIP standard. Estrarlo con uno dei seguenti metodi:

> **✅ Consigliato: Opzione B — Script di ripristino** (gestisce automaticamente la struttura delle directory e i permessi).

**Opzione A — Script di ripristino (consigliato ⭐)**
```bash
cd ~/geneforge-deploy
bash restore-geneclone.sh ~/my-clone
```

Lo script di ripristino esegue automaticamente:
- Creazione della struttura delle directory di destinazione
- Copia degli agent, dei file di configurazione e della wizard
- Impostazione dei permessi di esecuzione sui file `.sh`
- Verifica della presenza di un ambiente virtuale Python
- Verifica che i file critici siano presenti

**Opzione B — Unzip (manuale)**
```bash
cd ~/geneforge-deploy
unzip GeneForge-Custom-*-v1.0.geneclone -d my-clone/
```

> ⚠️ Lo unzip manuale salta i controlli sui permessi. Potrebbe essere necessario eseguire `chmod +x` sugli script in seguito.

### Fase 3 — Verifica dell'Integrità del Pacchetto ✅

**Verifica sempre prima di installare.** Questo garantisce che il pacchetto non sia stato danneggiato o manomesso durante il trasferimento.

```bash
cd ~/geneforge-deploy
sha256sum -c checksum.sha256
```

**Output atteso:**
```
GeneForge-Custom-*-v1.0.geneclone: OK
```

**Se vedi `FAILED`:**
```
GeneForge-Custom-*-v1.0.geneclone: FAILED
sha256sum: WARNING: 1 computed checksum did NOT match
```

> 🛑 **Non procedere.** Il pacchetto potrebbe essere danneggiato, incompleto o manomesso. Contatta immediatamente il supporto GeneForge con il tuo client ID e la data di consegna.

**Cosa protegge il checksum:**
- Download parziali o interruzioni di rete
- Corruzione del file durante il trasferimento
- Modifiche non autorizzate
- Degradazione del supporto di archiviazione

### Fase 4 — Installazione delle Dipendenze

```bash
cd ~/my-clone/wizard

# Opzione 1 — Python di sistema
pip install -r requirements.txt

# Opzione 2 — Ambiente virtuale (consigliato)
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Dipendenze tipiche:
- `streamlit`
- `plotly`
- `pandas`
- `numpy`

### Fase 5 — Avvio della Wizard di Onboarding

```bash
cd ~/my-clone/wizard
source venv/bin/activate  # se si utilizza venv

# Avvio
streamlit run app_onboarding.py \
  --server.port 8501 \
  --server.address 0.0.0.0 \
  --server.headless true
```

La wizard sarà disponibile all'indirizzo:
```
http://localhost:8501
```

Se si effettua il deploy su un server remoto, accedervi tramite:
```
http://<server-ip>:8501
```

### Fase 6 — Completamento dell'Onboarding

Aprire la wizard nel browser e seguire i passaggi guidati:
1. **Health Check** — Verificare la compatibilità del sistema
2. **Agent Activation** — Inizializzare gli agent AI personalizzati
3. **Integration Test** — Convalidare le connessioni alle fonti dati
4. **Go Live** — Iniziare a utilizzare il clone

---

## 4. Struttura delle Directory Dopo il Deploy

```
~/my-clone/
├── agents/
│   ├── ceo-meta/
│   │   └── system-prompt.md
│   ├── cloner/
│   ├── compliance-ai-act/
│   └── ... (personalizzati per cliente)
├── config/
│   ├── nim_config.yaml
│   └── ollama_config.yaml
├── wizard/
│   ├── app_onboarding.py
│   ├── launch_onboarding.sh
│   └── requirements.txt
└── logs/                     # Generato in fase di esecuzione
```

---

## 5. Esecuzione del Clone (Headless / Produzione)

Per il deploy in produzione senza la wizard:

```bash
cd ~/my-clone

# Attivazione ambiente
source venv/bin/activate

# Esecuzione applicazione principale (se applicabile)
python3 -m agents.intake_analysis

# Oppure utilizzare il launcher fornito
bash wizard/launch_onboarding.sh --headless
```

---

## 6. Aggiornamento del Clone

Quando si riceve un pacchetto `.geneclone` aggiornato:

```bash
# 1. Backup del deploy corrente
cp -r ~/my-clone ~/my-clone-backup-$(date +%Y%m%d)

# 2. Arresto dei servizi in esecuzione
pkill -f streamlit
pkill -f app_onboarding.py

# 3. Estrazione del nuovo pacchetto
unzip GeneForge-Custom-*-v2.0.geneclone -d my-clone-new/

# 4. Migrazione delle configurazioni personalizzate (se presenti)
cp ~/my-clone/config/custom.yaml ~/my-clone-new/config/

# 5. Sostituzione del vecchio con il nuovo
mv ~/my-clone ~/my-clone-old
mv ~/my-clone-new ~/my-clone

# 6. Riavvio
bash ~/my-clone/wizard/launch_onboarding.sh
```

---

## 7. Rollback

Se la nuova versione causa problemi:

```bash
# Arresto del servizio corrente
pkill -f streamlit

# Ripristino del backup
rm -rf ~/my-clone
mv ~/my-clone-backup-20260416 ~/my-clone

# Riavvio
bash ~/my-clone/wizard/launch_onboarding.sh
```

---

## 8. Troubleshooting

| Problema | Causa | Soluzione |
|---------|-------|----------|
| `unzip: cannot find` | Estensione del file nascosta | Rinominare: `mv file.geneclone file.zip` ed estrarre |
| `ModuleNotFoundError: streamlit` | Dipendenze non installate | Eseguire `pip install -r requirements.txt` |
| `Address already in use` | Porta 8501 occupata | Cambiare porta: `--server.port 8502` |
| La wizard si carica ma mostra errori | Blocco da parte di Firefox Snap | Utilizzare Chrome/Chromium |
| `Permission denied` su `.sh` | Script non eseguibili | `chmod +x restore-geneclone.sh` |
| Prestazioni lente | Nessuna GPU / solo CPU | Comportamento atteso su sistemi senza GPU; ridurre la concorrenza degli agent |
| I prompt degli agent non vengono caricati | Directory `agents/` mancante | Estrarre nuovamente il pacchetto; verificare la struttura delle directory |
| Verifica checksum fallita | Pacchetto corrotto o manomesso | 🛑 Non installare. Contatta immediatamente il supporto GeneForge |
| `restore-geneclone.sh: not found` | Script non estratto | Riestrai con Opzione A (script di ripristino) |
| Wizard pagina bianca dopo login | Cache del browser | Hard-refresh: `Ctrl+Shift+R` o prova modalità incognito |
| Alto uso CPU dopo l'avvio | Troppi agenti attivi | Modifica `config/nim_config.yaml`: imposta `max_concurrent_agents: 2` |

### Troubleshooting Esteso

#### "Lo script di ripristino fallisce con 'directory not found'"
- **Causa:** Si è eseguito `restore-geneclone.sh` dall'interno dello ZIP senza estrarlo prima.
- **Correzione:** Estrarre prima il `.geneclone`, quindi eseguire lo script dalla cartella estratta:
  ```bash
  unzip GeneForge-Custom-*-v1.0.geneclone -d temp/
  bash temp/restore-geneclone.sh ~/my-clone
  ```

#### "Streamlit si avvia ma la pagina è vuota"
- **Causa:** Firewall che blocca la porta 8501, oppure problema di cache del browser.
- **Correzione:**
  ```bash
  # Provare una porta diversa
  streamlit run app_onboarding.py --server.port 8502
  # Oppure accedere tramite IP invece di localhost
  streamlit run app_onboarding.py --server.address $(hostname -I | awk '{print $1}')
  ```

#### "Visualizzo '404: Not Found' per le risorse statiche"
- **Causa:** La cartella `agents/` o `config/` risulta mancante dall'estrazione.
- **Correzione:** Estrarre nuovamente utilizzando lo script di ripristino (Opzione B) invece dello unzip manuale.

#### "Il clone risponde lentamente o va in timeout"
- **Causa:** Esecuzione su macchina solo-CPU con impostazioni predefinite.
- **Correzione:** Ridurre il numero di agent concorrenti in `config/nim_config.yaml`:
  ```yaml
  max_concurrent_agents: 2  # invece di 4
  ```

#### "Ho perso il file .geneclone originale"
- **Causa:** Cancellazione accidentale.
- **Correzione:** Contattare il supporto GeneForge fornendo **client ID** e **data di consegna**. Manteniamo backup crittografati per 90 giorni.

#### "La verifica checksum fallisce ogni volta che riscarico"
- **Causa:** Cache CDN che serve file vecchio, o antivirus che mette in quarantena parte dell'archivio.
- **Correzione:**
  1. Disabilita temporaneamente l'antivirus e riscarica.
  2. Prova un browser diverso o usa `wget` / `curl` direttamente:
     ```bash
     wget https://your-delivery-url/GeneForge-Custom-*.geneclone
     wget https://your-delivery-url/checksum.sha256
     sha256sum -c checksum.sha256
     ```
  3. Se continua a fallire, richiedi un nuovo upload dal supporto GeneForge.

#### "Il wizard si avvia ma non riesco a caricare file"
- **Causa:** Permessi del browser o sandbox di Firefox Snap.
- **Correzione:** Usa Chrome/Chromium. Se su DGX Spark con Firefox Snap, vedi [firefox-snap-upload-fix](https://github.com/geneforge-ai/firefox-snap-upload-fix).

| Problema | Causa | Soluzione |
|---------|-------|----------|
| `unzip: cannot find` | Estensione del file nascosta | Rinominare: `mv file.geneclone file.zip` ed estrarre |
| `ModuleNotFoundError: streamlit` | Dipendenze non installate | Eseguire `pip install -r requirements.txt` |
| `Address already in use` | Porta 8501 occupata | Cambiare porta: `--server.port 8502` |
| La wizard si carica ma mostra errori | Blocco da parte di Firefox Snap | Utilizzare Chrome/Chromium |
| `Permission denied` su `.sh` | Script non eseguibili | `chmod +x restore-geneclone.sh` |
| Prestazioni lente | Nessuna GPU / solo CPU | Comportamento atteso su sistemi senza GPU; ridurre la concorrenza degli agent |
| I prompt degli agent non vengono caricati | Directory `agents/` mancante | Estrarre nuovamente il pacchetto; verificare la struttura delle directory |

---

## 9. Note di Sicurezza

- **Nessun blocco hardware**: Il pacchetto `.geneclone` è portatile. Proteggerlo come qualsiasi asset aziendale sensibile.
- **Nessuna dipendenza dal cloud**: Tutti gli agent AI vengono eseguiti in locale tramite Ollama. Nessun dato lascia la macchina, salvo configurazione diversa.
- **Permessi dei file**: Assicurarsi che le directory `agents/` e `config/` siano leggibili solo dall'utente del servizio.

---

## 10. Scheda di Riferimento Rapido

```bash
# --- Deploy in 30 secondi ---
mkdir -p ~/geneforge-clone && cd ~/geneforge-clone
unzip ~/Downloads/GeneForge-Custom-*-v1.0.geneclone
bash wizard/launch_onboarding.sh

# --- Accesso ---
open http://localhost:8501

# --- Arresto ---
pkill -f streamlit

# --- Aggiornamento ---
# Backup → Estrazione nuovo → Migrazione config → Riavvio
```

---

*Per il manuale completo del motore interno, vedere [MANUALE.md](MANUALE.md).*  
*Per le note di sviluppo specifiche per CUDA, vedere [CUDA_DEVELOPMENT_GUIDE.md](CUDA_DEVELOPMENT_GUIDE.md).*  
*Per il percorso aziendale, vedere [CUSTOMER_JOURNEY_GUIDE.md](CUSTOMER_JOURNEY_GUIDE.md).*  
*Piattaforma: GeneForge AI Clone Deployment*  
*Ultimo aggiornamento: 2026-04-16*
