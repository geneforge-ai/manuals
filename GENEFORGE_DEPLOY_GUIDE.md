# GeneForge Deploy Guide — `.geneclone` Package

This guide covers how to receive, extract, deploy, and run a **GeneForge Custom Clone** packaged as a `.geneclone` artifact.

---

## 1. What is a `.geneclone` package?

A `.geneclone` file is a **renamed ZIP archive** containing a fully personalized AI clone:

```
GeneForge-Custom-<CompanyName>-v1.0.geneclone
├── agents/                     # Personalized AI agent prompts
├── config/                     # Configuration files (YAML, JSON)
├── restore-geneclone.sh        # Automated restore script
└── wizard/
    ├── app_onboarding.py       # Streamlit onboarding wizard
    ├── launch_onboarding.sh    # Launch helper
    └── requirements.txt        # Python dependencies
```

> **Note:** The package is **hardware-agnostic**. It is not locked to a specific machine. You can deploy it on any Linux system that meets the requirements below.

---

## 2. System Requirements

### Minimum Requirements
| Component | Requirement |
|-----------|-------------|
| **OS** | Linux (Ubuntu 22.04+ recommended) |
| **Python** | 3.10 or higher |
| **Bash** | GNU bash 4.0+ |
| **Memory** | 4 GB RAM (8 GB recommended) |
| **Storage** | 2 GB free space |
| **Network** | Internet access for first-time dependency install |

### Recommended for Full Experience
| Component | Requirement |
|-----------|-------------|
| **GPU** | NVIDIA GPU with CUDA 11.8+ (optional — CPU mode works) |
| **OS** | DGX OS 7.x / Ubuntu 24.04 |
| **Browser** | Chrome, Chromium, or Firefox (non-Snap) |
| **Python Environment** | `venv` or `conda` |

---

## 3. Deployment Steps

### Step 1 — Receive the Package

The `.geneclone` file is delivered by the GeneForge team via:
- Secure file transfer (SFTP, encrypted email)
- Shared storage (S3, Google Drive, internal NAS)
- Physical media (USB drive)

Place the file in a working directory:
```bash
mkdir -p ~/geneforge-deploy
cp /path/to/GeneForge-Custom-*-v1.0.geneclone ~/geneforge-deploy/
```

### Step 2 — Extract the Package

A `.geneclone` is a standard ZIP file. Extract it with any of these methods:

> **✅ Recommended: Option B — Restore script** (handles directory structure and permissions automatically).

**Option A — Restore script (recommended ⭐)**
```bash
cd ~/geneforge-deploy
bash restore-geneclone.sh ~/my-clone
```

The restore script automatically:
- Creates the target directory structure
- Copies agents, config, and wizard files
- Sets executable permissions on `.sh` files
- Checks for a Python virtual environment
- Verifies critical files are present

**Option B — Unzip (manual)**
```bash
cd ~/geneforge-deploy
unzip GeneForge-Custom-*-v1.0.geneclone -d my-clone/
```

> ⚠️ Manual unzip skips permission checks. You may need to run `chmod +x` on scripts afterwards.

The restore script:
- Creates the target directory structure
- Copies agents, config, and wizard files
- Sets executable permissions on `.sh` files
- Checks for a Python virtual environment

### Step 3 — Verify Package Integrity ✅

**Always verify before installing.** This ensures the package was not corrupted or tampered with during transfer.

```bash
cd ~/geneforge-deploy
sha256sum -c checksum.sha256
```

**Expected output:**
```
GeneForge-Custom-*-v1.0.geneclone: OK
```

**If you see `FAILED`:**
```
GeneForge-Custom-*-v1.0.geneclone: FAILED
sha256sum: WARNING: 1 computed checksum did NOT match
```

> 🛑 **Do not proceed.** The package may be corrupted, incomplete, or tampered with. Contact GeneForge support immediately with your client ID and delivery date.

**What the checksum protects against:**
- Partial downloads or network interruptions
- File corruption during transfer
- Unauthorized modifications
- Bit-rot on storage media

### Step 4 — Install Dependencies

```bash
cd ~/my-clone/wizard

# Option 1 — System Python
pip install -r requirements.txt

# Option 2 — Virtual environment (recommended)
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Typical dependencies:
- `streamlit`
- `plotly`
- `pandas`
- `numpy`

### Step 5 — Launch the Onboarding Wizard

```bash
cd ~/my-clone/wizard
source venv/bin/activate  # if using venv

# Launch
streamlit run app_onboarding.py \
  --server.port 8501 \
  --server.address 0.0.0.0 \
  --server.headless true
```

The wizard will be available at:
```
http://localhost:8501
```

If deploying on a remote server, access it via:
```
http://<server-ip>:8501
```

### Step 6 — Complete Onboarding

Open the wizard in your browser and follow the guided steps:
1. **Health Check** — Verify system compatibility
2. **Agent Activation** — Initialize the personalized AI agents
3. **Integration Test** — Validate connections to your data sources
4. **Go Live** — Start using the clone

---

## 4. Directory Structure After Deploy

```
~/my-clone/
├── agents/
│   ├── ceo-meta/
│   │   └── system-prompt.md
│   ├── cloner/
│   ├── compliance-ai-act/
│   └── ... (personalized per client)
├── config/
│   ├── nim_config.yaml
│   └── ollama_config.yaml
├── wizard/
│   ├── app_onboarding.py
│   ├── launch_onboarding.sh
│   └── requirements.txt
└── logs/                     # Generated at runtime
```

---

## 5. Running the Clone (Headless / Production)

For production deployment without the wizard:

```bash
cd ~/my-clone

# Activate environment
source venv/bin/activate

# Run the main application (if applicable)
python3 -m agents.intake_analysis

# Or use the provided launcher
bash wizard/launch_onboarding.sh --headless
```

---

## 6. Updating the Clone

When you receive an updated `.geneclone` package:

```bash
# 1. Backup current deployment
cp -r ~/my-clone ~/my-clone-backup-$(date +%Y%m%d)

# 2. Stop running services
pkill -f streamlit
pkill -f app_onboarding.py

# 3. Extract new package
unzip GeneForge-Custom-*-v2.0.geneclone -d my-clone-new/

# 4. Migrate custom configs (if any)
cp ~/my-clone/config/custom.yaml ~/my-clone-new/config/

# 5. Replace old with new
mv ~/my-clone ~/my-clone-old
mv ~/my-clone-new ~/my-clone

# 6. Restart
bash ~/my-clone/wizard/launch_onboarding.sh
```

---

## 7. Rollback

If the new version causes issues:

```bash
# Stop current
pkill -f streamlit

# Restore backup
rm -rf ~/my-clone
mv ~/my-clone-backup-20260416 ~/my-clone

# Restart
bash ~/my-clone/wizard/launch_onboarding.sh
```

---

## 8. Troubleshooting

| Problem | Cause | Solution |
|---------|-------|----------|
| `unzip: cannot find` | File extension hidden | Rename: `mv file.geneclone file.zip` then unzip |
| `ModuleNotFoundError: streamlit` | Dependencies not installed | Run `pip install -r requirements.txt` |
| `Address already in use` | Port 8501 occupied | Change port: `--server.port 8502` |
| Wizard loads but shows errors | Firefox Snap blocking | Use Chrome/Chromium |
| `Permission denied` on `.sh` | Scripts not executable | `chmod +x restore-geneclone.sh` |
| Slow performance | No GPU / CPU only | Expected on non-GPU systems; reduce agent concurrency |
| Agent prompts not loading | Missing `agents/` directory | Re-extract package; verify directory structure |
| Checksum verification fails | Corrupted or tampered package | 🛑 Do not install. Contact GeneForge support immediately |
| `restore-geneclone.sh: not found` | Script not extracted | Re-extract with Option A (restore script) |
| Wizard shows blank page after login | Browser cache issue | Hard-refresh: `Ctrl+Shift+R` or try incognito mode |
| High CPU usage after launch | Too many agents active | Edit `config/nim_config.yaml`: set `max_concurrent_agents: 2` |

### Extended Troubleshooting

#### "The restore script fails with 'directory not found'"
- **Cause:** You ran `restore-geneclone.sh` from inside the zip without extracting first.
- **Fix:** Extract the `.geneclone` first, then run the script from the extracted folder:
  ```bash
  unzip GeneForge-Custom-*-v1.0.geneclone -d temp/
  bash temp/restore-geneclone.sh ~/my-clone
  ```

#### "Streamlit starts but the page is blank"
- **Cause:** Firewall blocking port 8501, or browser cache issue.
- **Fix:**
  ```bash
  # Try a different port
  streamlit run app_onboarding.py --server.port 8502
  # Or access via IP instead of localhost
  streamlit run app_onboarding.py --server.address $(hostname -I | awk '{print $1}')
  ```

#### "I see '404: Not Found' for static assets"
- **Cause:** The `agents/` or `config/` folder is missing from the extraction.
- **Fix:** Re-extract using the restore script (Option B) instead of manual unzip.

#### "The clone responds slowly or times out"
- **Cause:** Running on CPU-only machine with default settings.
- **Fix:** Reduce the number of concurrent agents in `config/nim_config.yaml`:
  ```yaml
  max_concurrent_agents: 2  # instead of 4
  ```

#### "I lost my original .geneclone file"
- **Cause:** Accidental deletion.
- **Fix:** Contact GeneForge support with your **client ID** and **delivery date**. We keep encrypted backups for 90 days.

#### "Checksum verification fails every time I re-download"
- **Cause:** CDN cache serving stale file, or antivirus quarantining part of the archive.
- **Fix:**
  1. Disable antivirus temporarily and re-download.
  2. Try a different browser or use `wget` / `curl` directly:
     ```bash
     wget https://your-delivery-url/GeneForge-Custom-*.geneclone
     wget https://your-delivery-url/checksum.sha256
     sha256sum -c checksum.sha256
     ```
  3. If still failing, request a fresh upload from GeneForge support.

#### "The wizard starts but I can't upload files"
- **Cause:** Browser permissions or Firefox Snap sandbox.
- **Fix:** Use Chrome/Chromium. If on DGX Spark with Firefox Snap, see [firefox-snap-upload-fix](https://github.com/geneforge-ai/firefox-snap-upload-fix).

| Problem | Cause | Solution |
|---------|-------|----------|
| `unzip: cannot find` | File extension hidden | Rename: `mv file.geneclone file.zip` then unzip |
| `ModuleNotFoundError: streamlit` | Dependencies not installed | Run `pip install -r requirements.txt` |
| `Address already in use` | Port 8501 occupied | Change port: `--server.port 8502` |
| Wizard loads but shows errors | Firefox Snap blocking | Use Chrome/Chromium |
| `Permission denied` on `.sh` | Scripts not executable | `chmod +x restore-geneclone.sh` |
| Slow performance | No GPU / CPU only | Expected on non-GPU systems; reduce agent concurrency |
| Agent prompts not loading | Missing `agents/` directory | Re-extract package; verify directory structure |

---

## 9. Security Notes

- **No hardware lock**: The `.geneclone` package is portable. Protect it as you would any sensitive company asset.
- **No cloud dependency**: All AI agents run locally via Ollama. No data leaves your machine unless configured.
- **File permissions**: Ensure `agents/` and `config/` are readable only by the service user.

---

## 10. Quick Reference Card

```bash
# --- Deploy in 30 seconds ---
mkdir -p ~/geneforge-clone && cd ~/geneforge-clone
unzip ~/Downloads/GeneForge-Custom-*-v1.0.geneclone
bash wizard/launch_onboarding.sh

# --- Access ---
open http://localhost:8501

# --- Stop ---
pkill -f streamlit

# --- Update ---
# Backup → Extract new → Migrate configs → Restart
```

---

*For the full internal engine manual, see [MANUALE.md](MANUALE.md).*  
*For CUDA-specific development notes, see [CUDA_DEVELOPMENT_GUIDE.md](CUDA_DEVELOPMENT_GUIDE.md).*  
*For the business journey, see [CUSTOMER_JOURNEY_GUIDE.md](CUSTOMER_JOURNEY_GUIDE.md).*  
*Platform: GeneForge AI Clone Deployment*  
*Last updated: 2026-04-16*
