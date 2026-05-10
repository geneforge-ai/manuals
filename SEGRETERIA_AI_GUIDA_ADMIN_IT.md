# Guida Amministratore - Segreteria AI On-Premise
**Versione:** 2.0  
**Data:** 10 Maggio 2026  
**Prodotto:** GeneForge Segreteria AI Multi-Channel  
**Destinatario:** Amministratori di sistema / Tecnici

---

## 1. Architettura del Sistema

```
┌─────────────────────────────────────────────────────────────┐
│                        INTERNET                              │
└──────────────┬──────────────────────────────┬───────────────┘
               │                              │
      ┌────────▼─────────┐        ┌──────────▼─────────┐
      │  SIP Trunk VoIP  │        │ Cloudflare Tunnel  │
      │  (Provider)      │        │ (HTTPS :443)       │
      └────────┬─────────┘        └──────────┬─────────┘
               │                              │
      ┌────────▼──────────────────────────────▼─────────┐
      │              SERVER ON-PREMISE                   │
      │                                                  │
      │  ┌─────────────┐  ┌─────────────┐  ┌──────────┐ │
      │  │  Asterisk   │  │   Segreteria│  │ Dashboard│ │
      │  │  PBX        │  │   AI Core   │  │ NiceGUI  │ │
      │  │  (porta     │  │   (Python)  │  │ (porta   │ │
      │  │   5060)     │  │             │  │  8513)   │ │
      │  └──────┬──────┘  └──────┬──────┘  └────┬─────┘ │
      │         │                │              │       │
      │  ┌──────▼──────┐  ┌──────▼──────┐  ┌────▼────┐ │
      │  │  WhatsApp   │  │    Email    │  │ SQLite  │ │
      │  │  Webhook    │  │  IMAP/SMTP  │  │   DB    │ │
      │  │  (porta     │  │  (porta     │  │         │ │
      │  │   8702)     │  │   993/587)  │  │         │ │
      │  └─────────────┘  └─────────────┘  └─────────┘ │
      │                                                  │
      └──────────────────────────────────────────────────┘
```

---

## 2. Installazione

### 2.1 Requisiti Hardware

| Componente | Minimo | Consigliato |
|------------|--------|-------------|
| CPU | 8 core x86_64 | 16 core (o ARM64 con GPU) |
| RAM | 16 GB | 32-64 GB |
| Storage | 100 GB SSD | 250 GB NVMe |
| GPU | Opzionale | NVIDIA con CUDA (per STT/LLM) |
| Rete | 100 Mbps | 1 Gbps |

### 2.2 Requisiti Software

- Ubuntu 24.04 LTS (o 22.04)
- Python 3.12
- Asterisk 20.6+ con PJSIP
- SQLite 3 (incluso in Ubuntu)
- Cloudflared (per tunnel)

### 2.3 Procedura Installazione

```bash
# 1. Scaricare il repository
git clone https://github.com/geneforge/segreteria-ai.git /opt/segreteria-ai
cd /opt/segreteria-ai

# 2. Eseguire lo script di installazione
sudo bash deploy/scripts/install.sh

# 3. Configurare secrets
cp config/secrets.yaml.example config/secrets.yaml
nano config/secrets.yaml

# 4. Configurare servizi esterni (vedi sezioni 3-5)

# 5. Avviare i servizi
sudo systemctl start segreteria-ai
sudo systemctl start segreteria-whatsapp
sudo systemctl start segreteria-email
sudo systemctl start segreteria-tunnel
```

### 2.4 Struttura Directory

```
/opt/segreteria-ai/
├── core/                    # Orchestrator, intent classifier, entity extractor
├── flows/                   # Phone, WhatsApp, Email flows
├── voice/                   # AGI, STT, TTS engines
├── whatsapp/                # WhatsApp gateway + webhook server
├── mail_gateway/            # Email IMAP/SMTP gateway
├── tools/                   # Calendar, appointment manager, notifications
├── web/                     # Dashboard NiceGUI
├── connectors/              # Studio Legale AI connector
├── config/                  # Configurazioni YAML
├── data/                    # Database SQLite
├── logs/                    # Log applicazione
├── deploy/                  # Script di deploy e documentazione
│   ├── systemd/             # Service files
│   ├── scripts/             # Backup, install, utilities
│   ├── cloudflare/          # Tunnel setup
│   └── docs/                # Documentazione
├── tests/                   # Test suite
└── .venv/                   # Virtual environment Python
```

---

## 3. Configurazione Asterisk (Telefono)

### 3.1 SIP Trunk

Editare `/etc/asterisk/pjsip.conf`:

```ini
; Trunk VoIP (esempio VoIPVoice)
[voipvoice_trunk]
type=registration
transport=transport-udp
outbound_auth=voipvoice_auth
server_uri=sip:voip.voipvoice.it:5060
client_uri=sip:NUMERO@sip:voip.voipvoice.it:5060

[voipvoice_auth]
type=auth
auth_type=userpass
password=TUA_PASSWORD
username=NUMERO

[voipvoice_endpoint]
type=endpoint
transport=transport-udp
context=from-trunk
disallow=all
allow=alaw,ulaw
direct_media=no
from_user=NUMERO
outbound_auth=voipvoice_auth
aors=voipvoice_aor

[voipvoice_aor]
type=aor
contact=sip:voip.voipvoice.it:5060
```

### 3.2 Dialplan per AI

In `/etc/asterisk/extensions.conf`:

```ini
[segreteria-ai]
exten => _X.,1,NoOp(Incoming call to AI receptionist)
 same => n,Answer()
 same => n,Set(CALLERID_NUM=${CALLERID(num)})
 same => n,AGI(/opt/segreteria-ai/voice/agi_handler.py)
 same => n,Hangup()

; Transfer to human
exten => 100,1,NoOp(Transfer to human secretary)
 same => n,Dial(PJSIP/segretaria)

; Urgency transfer
exten => 101,1,NoOp(Urgency transfer to lawyer)
 same => n,Dial(PJSIP/avvocato)
```

### 3.3 Riavvio Asterisk

```bash
sudo asterisk -rx "core reload"
sudo asterisk -rx "pjsip show endpoints"
```

---

## 4. Configurazione WhatsApp Business API

### 4.1 Prerequisiti Meta

1. Creare Business Account su [business.facebook.com](https://business.facebook.com)
2. Aggiungere numero di telefono dello studio
3. Verificare numero via SMS/chiamata

### 4.2 App Developer

1. Andare su [developers.facebook.com](https://developers.facebook.com)
2. Creare nuova app → tipo "Business"
3. Aggiungere prodotto "WhatsApp"
4. Copiare:
   - `Phone Number ID`
   - `WhatsApp Business Account ID`
   - Generare `Permanent Access Token`
   - Copiare `APP_SECRET`

### 4.3 Configurazione Webhook

1. In Meta Dashboard, configurare webhook:
   - Callback URL: `https://TUO-DOMINIO/whatsapp/webhook`
   - Verify Token: generare token casuale
   - Sottoscrivere: `messages`

2. Aggiornare `config/secrets.yaml`:

```yaml
whatsapp:
  phone_number_id: "1234567890"
  business_account_id: "9876543210"
  access_token: "EAAB..."
  app_secret: "abc123..."
  verify_token: "segreteria_webhook_2026"
```

### 4.4 Template

I 7 template predefiniti vanno creati su Meta Dashboard e inviati per approvazione:
- `appointment_confirmation`
- `appointment_reminder`
- `appointment_cancellation`
- `document_received`
- `human_transfer`
- `welcome_new_contact`
- `out_of_hours`

Tempo di approvazione: 1-24 ore.

---

## 5. Configurazione Email

### 5.1 Caselle Email

Configurare due caselle (o alias):
- `info@studiolegaledellaluna.it`
- `segreteria@studiolegaledellaluna.it`

### 5.2 Configurazione IMAP/SMTP

Aggiornare `config/config.yaml`:

```yaml
email:
  enabled: true
  polling_interval: 60
  use_idle: true
  max_attachment_size: 10485760
  accounts:
    info:
      enabled: true
      address: "info@studiolegaledellaluna.it"
      username: "info@studiolegaledellaluna.it"
      password: "${EMAIL_INFO_PASSWORD}"
      imap_server: "imap.provider.it"
      imap_port: 993
      smtp_server: "smtp.provider.it"
      smtp_port: 587
    segreteria:
      enabled: true
      address: "segreteria@studiolegaledellaluna.it"
      username: "segreteria@studiolegaledellaluna.it"
      password: "${EMAIL_SEGRETERIA_PASSWORD}"
      imap_server: "imap.provider.it"
      imap_port: 993
      smtp_server: "smtp.provider.it"
      smtp_port: 587
```

---

## 6. Cloudflare Tunnel (Accesso Esterno)

### 6.1 Installazione

```bash
# Eseguire lo script incluso
sudo bash deploy/cloudflare/setup_tunnel.sh

# O manualmente:
curl -L --output /tmp/cloudflared.deb https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64.deb
dpkg -i /tmp/cloudflared.deb
cloudflared tunnel login
cloudflared tunnel create segreteria-ai-dashboard
```

### 6.2 Autenticazione Aggiuntiva (Consigliata)

Su [dash.teams.cloudflare.com](https://dash.teams.cloudflare.com):
1. Access → Applications → Add
2. Inserire dominio: `segreteria.studiolegaledellaluna.it`
3. Configurare policy:
   - Allow: email `marco.dellaluna@studiolegaledellaluna.it`
   - Allow: email `segreteria@studiolegaledellaluna.it`
4. Salva

---

## 7. Gestione e Monitoraggio

### 7.1 Comandi Utili

```bash
# Stato servizi
systemctl status segreteria-ai segreteria-whatsapp segreteria-email segreteria-tunnel

# Log in tempo reale
journalctl -u segreteria-ai -f
journalctl -u segreteria-whatsapp -f
journalctl -u segreteria-email -f

# Riavvio
systemctl restart segreteria-ai

# Backup manuale
/opt/segreteria-ai/deploy/scripts/backup.sh

# Verifica Asterisk
asterisk -rx "core show version"
asterisk -rx "pjsip show endpoints"
asterisk -rx "core show calls"
```

### 7.2 Backup e Ripristino

**Backup automatico**: ogni giorno alle 3:00 AM in `/opt/backups/segreteria-ai/`

**Ripristino da backup:**

```bash
# 1. Identificare il backup
cd /opt/backups/segreteria-ai
ls -la

# 2. Estrarre
mkdir /tmp/restore
tar -xzf segreteria-ai_backup_YYYYMMDD_HHMMSS.tar.gz -C /tmp/restore

# 3. Ripristinare database
sudo systemctl stop segreteria-ai
cp /tmp/restore/segreteria_ai.db /opt/segreteria-ai/data/

# 4. Ripristinare configurazioni
cp -r /tmp/restore/config/* /opt/segreteria-ai/config/

# 5. Riavviare
sudo systemctl start segreteria-ai
```

### 7.3 Aggiornamento del Sistema

```bash
# 1. Backup prima di aggiornare
/opt/segreteria-ai/deploy/scripts/backup.sh

# 2. Scaricare nuova versione
cd /opt/segreteria-ai
git pull origin main

# 3. Aggiornare dipendenze
source .venv/bin/activate
pip install -r requirements.txt

# 4. Riavviare
sudo systemctl restart segreteria-ai segreteria-whatsapp segreteria-email
```

---

## 8. Troubleshooting

### 8.1 Asterisk

| Problema | Comando Diagnostico | Soluzione |
|----------|---------------------|-----------|
| Non risponde | `systemctl status asterisk` | `systemctl restart asterisk` |
| Errore PJSIP | `asterisk -rx "pjsip show endpoints"` | Verificare `pjsip.conf` |
| Codec non supportato | `asterisk -rx "core show translations"` | Aggiungere `allow=alaw,ulaw` |
| Chiamata cade | `/var/log/asterisk/messages` | Verificare NAT e firewall |

### 8.2 AI / Dashboard

| Problema | Comando Diagnostico | Soluzione |
|----------|---------------------|-----------|
| Dashboard non risponde | `systemctl status segreteria-ai` | Riavviare servizio |
| LLM non risponde | `curl http://localhost:8080/health` | Verificare LLM Router |
| STT lento | Controllare CPU/GPU | Passare a CUDA se disponibile |
| Errore database | `sqlite3 data/segreteria_ai.db ".tables"` | Verificare permessi file |

### 8.3 WhatsApp

| Problema | Comando Diagnostico | Soluzione |
|----------|---------------------|-----------|
| Webhook non riceve | `journalctl -u segreteria-whatsapp -f` | Verificare URL webhook su Meta |
| Template rifiutati | Meta Dashboard | Modificare template e re-inviare |
| Rate limit | Log webhook | Ridurre frequenza messaggi |

### 8.4 Email

| Problema | Comando Diagnostico | Soluzione |
|----------|---------------------|-----------|
| Non legge email | `journalctl -u segreteria-email -f` | Verificare credenziali IMAP |
| Non invia email | Log email gateway | Verificare SMTP e credenziali |
| Allegati bloccati | Config `max_attachment_size` | Aumentare limite se necessario |

---

## 9. Sicurezza

### 9.1 Firewall (UFW)

Porte aperte:
- 22/tcp (SSH) — limitare a IP specifici se possibile
- 5060/udp (SIP)
- 10000-20000/udp (RTP)

Porte localhost solo:
- 5038 (AMI)
- 8513 (Dashboard)
- 8702 (WhatsApp webhook)

### 9.2 Fail2Ban

Monitora:
- SSH (tentativi di accesso)
- Asterisk (registrazioni fallite)

### 9.3 Backup Crittografati (Consigliato)

Aggiungere al backup script:

```bash
# Crittografa backup con GPG
gpg --symmetric --cipher-algo AES256 \
    --output "${BACKUP_PATH}.tar.gz.gpg" \
    "${BACKUP_PATH}.tar.gz"
rm "${BACKUP_PATH}.tar.gz"
```

---

## 10. Contatti e Supporto

**GeneForge AI Team**
- Email: support@geneforge.eu
- Telefono: +39 0143 123456
- Orari: Lun-Ven 9:00-18:00

**Documentazione Online:**
- https://docs.geneforge.eu/segreteria-ai

---

**GeneForge AI Team**  
10 Maggio 2026
