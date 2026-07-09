# Piano di implementazione — PEC e Deposito Telematico / E-filing

**Studio Legale AI · GeneForge · Luglio 2026**

---

## 1. Obiettivo

Aggiungere a Studio Legale AI:

1. **PEC professionale**: invio e ricezione di posta certificata, con associazione automatica a clienti/pratiche e archiviazione delle ricevute.
2. **Deposito telematico / e-filing**: predisposizione connettori per PCT civile, UNEP, ReGIndE e piattaforme commerciali (Polisweb, TrialOnline, eDepart, Altalex Studio Legale), con generazione del pacchetto di deposito e link rapidi ai portali.

Tutto rimane **on-premise**: credenziali, ricevute, metadati e documenti restano nel DGX Spark dello studio.

---

## 2. Perché serve

La tabella comparativa del mercato italiano mostra che i gestionali legali (AvvoDesk, LexDoctor, Legal360) e i competitor cloud integrano già PEC/PCT. Senza queste funzioni, gli avvocati devono usare strumenti esterni per atti processuali e notifiche, riducendo l'adozione di Studio Legale AI.

---

## 3. PEC — Requisiti funzionali

### 3.1 Provider target (fase 1)

| Provider | Protocolli | Note |
|---|---|---|
| **Aruba PEC** | SMTP/IMAP/POP3 SSL | Caselle `pec.it`, `arubapec.it`, domini custom |
| **Legalmail** | SMTP/IMAP/POP3 SSL | Provider giuridico italiano |
| **PEC.it / PosteCert** | SMTP/IMAP/POP3 SSL | Poste Italiane e altri provider |
| **Generico PEC** | SMTP/IMAP/POP3 SSL | Per caselle di altri provider |

### 3.2 Funzionalità

1. **Invio PEC**
   - Compilazione destinatario, oggetto, corpo, allegati (PDF/DOCX/MD).
   - Header PEC conformi (`X-Ricevuta-PDF`, `X-TipoRicevuta`, ecc. gestiti dal provider).
   - Salvataggio nella pratica associata.

2. **Ricezione PEC**
   - Polling casella IMAP ogni N minuti (configurabile).
   - Scaricamento messaggi, allegati e ricevute (`daticert.xml`, `postacert.eml`, `smime.p7s`).
   - Associazione automatica a pratica tramite numero pratica nell'oggetto o indirizzo mittente/destinatario.

3. **Ricevute**
   - Accettazione, consegna, errore, avvenuta lettura.
   - Visualizzazione stato di ogni PEC inviata.

4. **Notifiche**
   - Notifica in-app per nuovi messaggi in ingresso.
   - Avviso se PEC in uscita non ha ricevuta di consegna entro termine.

---

## 4. Deposito telematico / E-filing — Requisiti funzionali

### 4.1 Sistemi target

| Sistema | Tipo | Stato previsto | Note |
|---|---|---|---|
| **PCT — Processo Civile Telematico** | Ministero Giustizia | Placeholder + link rapido | Richiede firma digitale/smart card e software PCT del MJ |
| **UNEP** | Cassazione / Consiglio di Stato / TAR | Placeholder + link rapido | Richiede credenziali UNEP e firma digitale |
| **ReGIndE** | Registro Generale Indice Elettronico | Placeholder + link rapido | Per atti telematici presso alcuni uffici giudiziari |
| **Polisweb** | Piattaforma commerciale | Connettore placeholder | API su richiesta |
| **TrialOnline** | Piattaforma commerciale | Connettore placeholder | API su richiesta |
| **eDepart** | Piattaforma commerciale | Connettore placeholder | API su richiesta |
| **Altalex Studio Legale** | Piattaforma commerciale | Connettore placeholder | API su richiesta |

### 4.2 Funzionalità

1. **Generazione pacchetto di deposito**
   - PDF/A dell'atto con metadati.
   - File XML metadati secondo schemi PCT/UNEP (ove possibile).
   - Verifica pre-deposito (vocatio, avvertimenti, struttura, valore causa).

2. **Link rapidi ai portali**
   - Apertura browser direttamente sul portale corretto con dati precompilati quando possibile.

3. **Tracciamento stato**
   - Bozza → Pronto per deposito → Depositato → Esito ricevuto.
   - Associazione alla pratica e alla scadenza.

4. **Notifiche ex L. 53/1994**
   - Generazione pacchetto notifica via PEC con allegati e verbale.

---

## 5. Architettura tecnica

```
Studio Legale AI (NiceGUI + FastAPI)
├── core/connectors/pec.py          # Invio/ricezione PEC via SMTP/IMAP
├── core/connectors/efiling.py      # Registry deposito telematico
├── web-ui/studio_legale_app.py     # UI Impostazioni + Pannello PEC + Azioni documento
├── database/pec_messages.json      # Messaggi PEC in ingresso/uscita
└── database/efiling_tracking.json  # Stati depositi telematici
```

### Componenti da aggiungere

| Componente | Scopo |
|---|---|
| `PECConnector` | Invio SMTP, ricezione IMAP, parsing ricevute |
| `PECMail` | Modello dati per messaggio PEC |
| `EFILING_PROVIDERS` | Registro sistemi di deposito |
| `EFilingConnector` | Placeholder con metadati e link rapidi |
| `pec_settings_page` | UI configurazione provider PEC |
| `efiling_settings_page` | UI configurazione e-filing |
| `send_pec_dialog` | Dialog invio PEC da documento/pratica |

---

## 6. Piano di lavoro

### Fase 1 — PEC base (settimana 1)

1. Implementare `core/connectors/pec.py`:
   - `send_pec()` via `smtplib`.
   - `fetch_inbox()` via `imaplib`.
   - Parser ricevute (`daticert.xml`, `postacert.eml`).
2. Aggiungere UI in Impostazioni per configurare provider SMTP/IMAP.
3. Aggiungere dialog "Invia PEC" in Documenti e Pratiche.
4. Salvare messaggi in `database/pec_messages.json`.
5. Test unitari per invio/ricezione con server di test/mock.

### Fase 2 — Integrazione pratiche (settimana 2)

1. Associazione automatica PEC↔pratica per numero pratica nell'oggetto.
2. Visualizzazione cronologia PEC dentro la scheda pratica.
3. Notifiche in-app per nuovi messaggi.
4. Polling automatico casella in entrata.

### Fase 3 — E-filing placeholder (settimana 2-3)

1. Implementare `core/connectors/efiling.py` con registry provider.
2. UI in Impostazioni per abilitare provider e inserire credenziali/firma.
3. Azione "Prepara pacchetto deposito" sui documenti processuali.
4. Link rapidi a PCT/UNEP/ReGIndE con query/dati precompilati.
5. Tracciamento stati in `database/efiling_tracking.json`.

### Fase 4 — Integrazioni dirette su richiesta (futuro)

1. Connettori reali per Polisweb/TrialOnline/eDepart (API su richiesta).
2. Integrazione con smart card/firma digitale remota (OTP/aruba sign).
3. Automazione PCT tramite software ministeriale installato in locale.

---

## 7. Sicurezza e conformità

- **Credenziali**: salvate in `database/settings.json` e mai trasmesse a GeneForge.
- **Messaggi PEC**: archiviati localmente, con backup nelle procedure esistenti.
- **Firma digitale**: rimane sul client o su dispositivo HSM/smart card; il sistema genera il pacchetto, la firma avviene esternamente o tramite modulo futuro.
- **GDPR/segreto professionale**: nessun dato lascia lo studio; la PEC è gestita direttamente via protocolli standard tra il DGX Spark e il provider PEC.

---

## 8. Metriche di successo

- Invio PEC riuscito con ricevuta archiviata.
- Ricezione PEC associata correttamente alla pratica nel 90% dei casi.
- Generazione pacchetto e-filing per PCT/UNEP in un clic.
- Riduzione tempi di gestione atti processuali rispetto all'uso di strumenti separati.

---

## 9. Output attesi

- `core/connectors/pec.py`
- `core/connectors/efiling.py`
- `tests/test_pec.py`
- `tests/test_efiling.py`
- Sezione manuale utente "PEC e Deposito Telematico"
- Aggiornamento tabella gap in `valutazione_concorrenza_mercato_italiano.md`

---

*Redatto per Studio Legale AI — GeneForge*
