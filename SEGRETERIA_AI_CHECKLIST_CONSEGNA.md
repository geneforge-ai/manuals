# Checklist di Consegna - Segreteria AI On-Premise
**Versione:** 2.0  
**Data:** 10 Maggio 2026  
**Studio:** Studio Legale Della Luna, Novi Ligure (AL)

---

## Consegna del Sistema

| # | Item | Stato | Note |
|---|------|-------|------|
| 1 | Server installato e configurato | ⬜ | Modello, RAM, storage verificati |
| 2 | Ubuntu 24.04 LTS installato | ⬜ | Aggiornamenti eseguiti |
| 3 | Utente `segreteria` creato | ⬜ | Permessi corretti |
| 4 | Codice sorgente copiato in `/opt/segreteria-ai` | ⬜ | Versione 2.0 |
| 5 | Virtual environment creato | ⬜ | Dipendenze installate |

---

## Canale Telefono (Asterisk)

| # | Item | Stato | Note |
|---|------|-------|------|
| 6 | Asterisk 20.6 installato | ⬜ | `asterisk -rx "core show version"` |
| 7 | PJSIP configurato | ⬜ | Endpoint e trunk definiti |
| 8 | SIP Trunk attivo | ⬜ | Provider: _______________ |
| 9 | Numero DID configurato | ⬜ | Numero: _______________ |
| 10 | Dialplan `segreteria-ai` attivo | ⬜ | Estensioni 100/101 definite |
| 11 | AGI script funzionante | ⬜ | Test chiamata simulata OK |
| 12 | Codec alaw/ulaw configurati | ⬜ | |
| 13 | RTP range 10000-20000 aperto | ⬜ | Firewall verificato |
| 14 | Test chiamata in entrata | ⬜ | Audio OK, risposta AI OK |
| 15 | Test chiamata in uscita | ⬜ | Transfer a 100/101 OK |

---

## Canale WhatsApp

| # | Item | Stato | Note |
|---|------|-------|------|
| 16 | Business Account Meta creato | ⬜ | business.facebook.com |
| 17 | Numero verificato | ⬜ | Numero: _______________ |
| 18 | Access Token generato | ⬜ | Token permanent OK |
| 19 | APP_SECRET configurato | ⬜ | In secrets.yaml |
| 20 | Webhook configurato su Meta | ⬜ | URL HTTPS: _______________ |
| 21 | Verifica firma HMAC OK | ⬜ | Test webhook passato |
| 22 | Template creati (7/7) | ⬜ | appointment_confirmation |
| 23 | Template approvati da Meta | ⬜ | appointment_reminder |
| | | | appointment_cancellation |
| | | | document_received |
| | | | human_transfer |
| | | | welcome_new_contact |
| | | | out_of_hours |
| 24 | Test messaggio in entrata | ⬜ | AI risponde correttamente |
| 25 | Test template inviato | ⬜ | Cliente riceve messaggio |

---

## Canale Email

| # | Item | Stato | Note |
|---|------|-------|------|
| 26 | Casella info@ configurata | ⬜ | Server IMAP: _______________ |
| 27 | Casella segreteria@ configurata | ⬜ | Server SMTP: _______________ |
| 28 | Credenziali IMAP testate | ⬜ | Porta 993 SSL |
| 29 | Credenziali SMTP testate | ⬜ | Porta 587 STARTTLS |
| 30 | Listener IMAP avviato | ⬜ | `systemctl status segreteria-email` |
| 31 | Test invio email | ⬜ | Firma e formattazione OK |
| 32 | Test ricezione email | ⬜ | Parsing e thread OK |
| 33 | Test inoltro ad umano | ⬜ | Forward a segreteria OK |

---

## Dashboard Web

| # | Item | Stato | Note |
|---|------|-------|------|
| 34 | Dashboard avviata su porta 8513 | ⬜ | `systemctl status segreteria-ai` |
| 35 | Cloudflare Tunnel attivo | ⬜ | Hostname: _______________ |
| 36 | Accesso HTTPS funzionante | ⬜ | Certificato valido |
| 37 | Login con credenziali testato | ⬜ | Username: _______________ |
| 38 | Pagina Overview caricata | ⬜ | KPI visibili |
| 39 | Pagina Appuntamenti funzionante | ⬜ | CRUD testato |
| 40 | Pagina Analytics caricata | ⬜ | Grafici visibili |
| 41 | Pagina System Health verde | ⬜ | Tutti i servizi OK |
| 42 | Pagina Logs accessibile | ⬜ | Ricerca funzionante |
| 43 | Pagina Configurazione accessibile | ⬜ | Orari e regole visibili |

---

## Modulo Appuntamenti

| # | Item | Stato | Note |
|---|------|-------|------|
| 44 | Database SQLite creato | ⬜ | `/opt/segreteria-ai/data/segreteria_ai.db` |
| 45 | Tabelle e indici creati | ⬜ | appointments + indici |
| 46 | Creazione appuntamento testata | ⬜ | Via telefono/WhatsApp/email |
| 47 | Modifica appuntamento testata | ⬜ | Cambio data/ora |
| 48 | Cancellazione testata | ⬜ | Soft delete + notifica |
| 49 | Slot disponibili calcolati | ⬜ | Orari di apertura rispettati |
| 50 | Conflitti bloccati | ⬜ | Sovrapposizioni impedite |
| 51 | Promemoria automatico testato | ⬜ | 24h prima |
| 52 | Conferma automatica testata | ⬜ | Dopo creazione |
| 53 | Notifica modifica testata | ⬜ | Dopo aggiornamento |
| 54 | Notifica cancellazione testata | ⬜ | D dopo cancellazione |

---

## Sicurezza

| # | Item | Stato | Note |
|---|------|-------|------|
| 55 | Firewall UFW attivo | ⬜ | `ufw status` |
| 56 | Porte non necessarie chiuse | ⬜ | Solo 22, 5060, 10000-20000 |
| 57 | Dashboard accessibile solo via tunnel | ⬜ | No esposizione diretta |
| 58 | Fail2Ban attivo | ⬜ | SSH + Asterisk |
| 59 | Password di default cambiate | ⬜ | AMI, dashboard, sistema |
| 60 | Backup automatico configurato | ⬜ | Ogni giorno alle 3:00 AM |
| 61 | Log di sistema attivi | ⬜ | journald configurato |
| 62 | Servizi systemd abilitati | ⬜ | Avvio automatico |

---

## Documentazione Consegnata

| # | Item | Stato | Note |
|---|------|-------|------|
| 63 | Manuale Utente v1.0 | ⬜ | File: `Manuale_Utente_Segreteria_AI_v1.0.pdf` |
| 64 | Guida Amministratore v1.0 | ⬜ | File: `Guida_Amministratore_Segreteria_AI_v1.0.pdf` |
| 65 | README Tecnico | ⬜ | File: `README.md` |
| 66 | Checklist di consegna (questo file) | ⬜ | Firmata |

---

## Test Finali

| # | Test | Stato | Note |
|---|------|-------|------|
| 67 | Test end-to-end: prenotazione telefono | ⬜ | |
| 68 | Test end-to-end: modifica WhatsApp | ⬜ | |
| 69 | Test end-to-end: cancellazione email | ⬜ | |
| 70 | Test end-to-end: urgenza → transfer | ⬜ | |
| 71 | Test end-to-end: fuori orario | ⬜ | |
| 72 | Test end-to-end: multi-canale | ⬜ | |
| 73 | Test limite massimo appuntamenti | ⬜ | |
| 74 | Test conflitto/prevenzione doppia | ⬜ | |
| 75 | Stress test: 20 appuntamenti | ⬜ | |

---

## Formazione Cliente

| # | Item | Stato | Note |
|---|------|-------|------|
| 76 | Dashboard spiegata al cliente | ⬜ | |
| 77 | Accesso dashboard consegnato | ⬜ | Username/password |
| 78 | App mobile/dashboard testata | ⬜ | Da smartphone |
| 79 | Procedure di backup spiegate | ⬜ | |
| 80 | Contatti supporto consegnati | ⬜ | Email/telefono GeneForge |

---

## Firme

**Consegnato da:**
- Nome: _______________________
- Ruolo: ______________________
- Data: _______________________
- Firma: ______________________

**Ricevuto da (Studio Legale Della Luna):**
- Nome: Avv. Marco della Luna
- Ruolo: Titolare Studio
- Data: _______________________
- Firma: ______________________

---

**Totale items completati:** ____ / 80

**Stato complessivo:** ⬜ In corso / ⬜ Completato con riserve / ⬜ Completato

**Note finali:**
_________________________________________________________________
_________________________________________________________________
_________________________________________________________________

---

**GeneForge AI Team**  
10 Maggio 2026
