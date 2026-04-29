# Studio Legale AI — Manuale Utente

**Versione:** 1.0  
**Data:** 29 Aprile 2026  
**Progetto:** GeneForge AI — Studio Legale AI  
**Destinatari:** Avv. Marco della Luna, collaboratori e segretarie dello studio  

---

## 1. Introduzione

### Cos’è Studio Legale AI

**Studio Legale AI** è una piattaforma completa di gestione dello studio legale che unisce strumenti di organizzazione pratiche, generazione automatica di documenti giuridici e ricerca legale avanzata.

Tutto gira su server locali. Nessun dato dei clienti lascia mai il tuo computer.

### A cosa serve

- **Organizzare clienti e pratiche** in un unico sistema
- **Generare documenti giuridici** in pochi minuti anziché ore
- **Cercare norme, giurisprudenza e dottrina** senza cambiare sito
- **Tracciare scadenze, udienze e termini** processuali
- **Esportare e inviare documenti** in PDF, DOCX o via email

### Vantaggi principali

| Vantaggio | Descrizione |
|-----------|-------------|
| **Privacy totale** | I modelli AI girano localmente. Nessun dato in cloud |
| **Risparmio di tempo** | Un atto di citazione si genera in 2–3 minuti |
| **Protocollo automatico** | I documenti si numerano da soli (es. 2026/001) |
| **Verifica citazioni** | L’AI controlla che le sentenze della Cassazione esistano davvero |
| **Multi-formato** | PDF per la stampa, DOCX per le modifiche, MD per l’archivio |

### Come accedere

Apri il browser e digita:

```
http://localhost:8506
```

Se usi il tunnel Cloudflare:

```
https://studio-legale.tuo-dominio.workers.dev
```

Non serve password. L’applicazione è pronta all’uso.

---

## 2. Dashboard

### Panoramica della home page

La **Dashboard** è la prima pagina che vedi dopo l’accesso. Ti dà un quadro immediato della situazione dello studio.

### Cosa mostra

In alto trovi una riga di **contatori colorati**:

- **Clienti totali** — Quanti clienti hai in anagrafica
- **Pratiche aperte** — Casi attualmente in corso
- **Pratiche in scadenza** — Casi con data chiusura imminente (entro 30 giorni)
- **Pratiche chiuse** — Casi archiviati
- **Documenti prodotti** — Totale documenti generati finora
- **Scadenze imminenti** — Prossime udienze, termini e appuntamenti

### Menu di navigazione

Sulla sinistra (o in alto, a seconda dello schermo) trovi il menu principale:

1. **Dashboard** — Panoramica
2. **Clienti** — Anagrafica
3. **Pratiche** — Gestione casi
4. **Documenti** — Generazione e archivio
5. **Ricerca** — Ricerca giuridica
6. **Calendario** — Scadenze
7. **Impostazioni** — Configurazione

> 💡 **Suggerimento:** Clicca sempre su **Dashboard** quando vuoi tornare alla home.

---

## 3. Gestione Clienti

### Creare un nuovo cliente

1. Clicca su **Clienti** nel menu
2. Clicca sul pulsante **"➕ Nuovo Cliente"**
3. Compila il modulo che appare:

| Campo | Esempio | Obbligatorio |
|-------|---------|--------------|
| Nome | Mario Rossi Srl | Sì |
| Email | info@mariorossi.it | No |
| Telefono | 02 12345678 | No |
| Indirizzo | Via Roma 1, Milano | No |
| P.IVA / CF | 12345678901 | No |
| Tipo cliente | Azienda | Sì (default: Privato) |
| Avvertenze | Pagamento dilazionato | No |
| Note | Cliente acquisito da referenza | No |

4. Clicca su **"Salva"**

Il cliente apparirà subito nella lista.

### Esempio concreto

> **Caso:** Devi inserire una nuova azienda cliente.
>
> Compila così:
> - **Nome:** Mario Rossi Srl
> - **Email:** info@mariorossi.it
> - **Telefono:** 02 12345678
> - **Tipo cliente:** Azienda
> - **Avvertenze:** "Fattura mensile, pagamento a 60 giorni"
>
> Clicca **Salva**. Il cliente è pronto per essere collegato a una pratica.

### Modificare i dati di un cliente

1. Nella lista clienti, clicca su **"✏️ Modifica"** accanto al cliente
2. Modifica i campi desiderati
3. Clicca **"Salva"**

### Aggiungere avvertenze

Le **avvertenze** sono note speciali visibili in prima pagina quando apri il cliente.

Esempi utili:
- "Cliente allergico alle formalità — usare tono informale"
- "Pagamento sempre in ritardo — richiedere acconto"
- "Preferisce contatti telefonici, non email"

### Visualizzare pratiche e documenti associati

Clicca su **"🔽 Espandi"** accanto al nome del cliente. Vedrai:

- **Pratiche** — Lista dei casi collegati a quel cliente
- **Documenti** — Tutti i documenti generati per lui, con numero di protocollo

> 💡 **Suggerimento:** Se un cliente ha molte pratiche, usa la barra di ricerca in alto per filtrare per nome.

---

## 4. Gestione Casi / Pratiche

### Creare una nuova pratica

1. Clicca su **Pratiche** nel menu
2. Clicca su **"➕ Nuova Pratica"**
3. Compila il modulo:

| Campo | Esempio | Obbligatorio |
|-------|---------|--------------|
| Titolo | Recupero crediti fornitura | Sì |
| Cliente | Mario Rossi Srl | Sì |
| Numero pratica | 2025/042 | No |
| Tipo pratica | Commerciale | No |
| Area giuridica | Diritto commerciale | No |
| Data apertura | 15/01/2025 | No |
| Data chiusura prevista | 30/06/2025 | No |
| Avvocato assegnato | Avv. Marco della Luna | Sì (default) |
| Note | Fornitura non pagata, fattura n. 123 | No |

4. Clicca **"Salva"**

### Se il cliente non esiste ancora

Se il cliente non è in anagrafica:

1. Nel campo **Cliente**, clicca su **"➕ Crea nuovo cliente"**
2. Si apre una finestra popup
3. Compila i dati del nuovo cliente
4. Clicca **"Salva e seleziona"**
5. Il cliente viene creato e subito selezionato nella pratica

### Esempio concreto

> **Caso:** Nuova pratica per Mario Rossi Srl.
>
> Compila così:
> - **Titolo:** Recupero crediti fornitura non pagata
> - **Cliente:** Mario Rossi Srl
> - **Numero pratica:** 2025/042
> - **Tipo pratica:** Commerciale
> - **Data apertura:** 15/01/2025
> - **Data chiusura prevista:** 30/06/2025
> - **Note:** Controversia per fornitura software non pagata, fattura n. 123 del 10/12/2024
>
> Clicca **Salva**. La pratica è aperta.

### Cambiare lo stato di una pratica

Ogni pratica ha uno stato:

| Stato | Significato |
|-------|-------------|
| **Aperta** | Pratica in corso |
| **In attesa** | In attesa di documenti o decisioni |
| **In scadenza** | Scadenza imminente |
| **Chiusa** | Pratica conclusa |

Per cambiare stato:
1. Nella lista pratiche, clicca su **"✏️ Modifica"**
2. Seleziona il nuovo stato dal menu a tendina
3. Clicca **"Salva"**

### Visualizzare scadenze e documenti

Clicca su **"🔽 Espandi"** accanto alla pratica. Vedrai:
- **Scadenze collegate** — Udienze, termini, appuntamenti
- **Documenti collegati** — Atti, memorie, lettere generate

### Filtrare le pratiche

Usa i filtri sopra la tabella:
- **Stato** — Mostra solo aperte, chiuse, ecc.
- **Tipo pratica** — Civile, Penale, Amministrativo, ecc.
- **Area giuridica** — Filtra per specializzazione
- **Avvocato** — Se ci sono più professionisti

---

## 5. Generazione Documenti

### I 11 tipi di documento disponibili

Studio Legale AI può generare i seguenti documenti giuridici:

| # | Tipologia | Quando usarlo |
|---|-----------|---------------|
| 1 | **Lettera formale** | Comunicazioni ufficiali a clienti o avversari |
| 2 | **Atto di citazione** | Avvio giudizio civile |
| 3 | **Lettera di messa in mora** | Diffida ad adempiere |
| 4 | **Preventivo** | Offerta economica per prestazioni |
| 5 | **Parcella** | Nota di spettanze professionali |
| 6 | **Ricorso** | Ricorso amministrativo o tributario |
| 7 | **Contratto** | Contratto di assistenza legale |
| 8 | **Memoria difensiva** | Atto difensivo in giudizio |
| 9 | **Parere scritto** | Consulenza giuridica motivata |
| 10 | **Nota di trasmissione** | Accompagnamento documenti |
| 11 | **Ricerca su tema giuridico** | Studio approfondito con fonti |

### Come generare un documento

1. Vai su **Documenti** nel menu
2. Seleziona la **Tipologia** dal menu a tendina
3. Compila i campi richiesti (variano in base al tipo)
4. Seleziona il **Cliente** e la **Pratica** (facoltativo ma consigliato)
5. Clicca su **"⚡ Genera Documento"**
6. Attendi 30–60 secondi
7. Il documento apparirà nell’editor

### Esempio: generare una Lettera di messa in mora

> **Caso:** Mario Rossi Srl deve inviare una diffida al debitore.
>
> 1. Seleziona **Tipologia:** Lettera di messa in mora
> 2. Compila:
>    - **Oggetto:** Mancato pagamento fattura n. 123
>    - **Destinatario:** Bianchi Srl
>    - **Importo:** € 15.000,00
>    - **Termine:** 15 giorni
>    - **Cliente:** Mario Rossi Srl
>    - **Pratica:** Recupero crediti fornitura
> 3. Clicca **"⚡ Genera Documento"**
> 4. L’AI produce una lettera professionale con:
>    - Riferimenti normativi (art. 1218 e 1223 c.c.)
>    - Preavviso di azione legale
>    - Intestazione dello studio
> 5. Rivedi il testo nell’editor
> 6. Se va bene, clicca **"💾 Salva"**

### Collegare a cliente e pratica

Sempre nella pagina Documenti, trovi due menu a tendina:
- **Cliente** — Pre-compila i dati dell’intestazione
- **Pratica** — Collega il documento alla cartella del caso

Quando selezioni un cliente, l’AI inserisce automaticamente i suoi dati nel documento:
- Nome e indirizzo
- P.IVA / CF
- Riferimenti telefonici

### Preventivo e Parcella — Calcoli automatici

Per **Preventivo** e **Parcella**, scegli una delle 4 modalità:

#### Modalità 1: Percentuale sul valore
- **Valore controversia:** € 100.000
- **Percentuale:** 10%
- **Imponibile:** € 10.000
- **IVA (22%):** € 2.200
- **Ritenuta (20% su 50%):** € 1.000
- **Totale:** € 11.200

#### Modalità 2: Tariffa oraria
- **Tariffa oraria:** € 250
- **Ore stimate:** 20
- **Imponibile:** € 5.000
- *IVA e ritenuta calcolate automaticamente*

#### Modalità 3: Forfait
- Inserisci direttamente l’importo totale

#### Modalità 4: Tariffa parametri forensi
- L’AI calcola secondo il D.M. parametri forensi

> ✅ **Nota:** I calcoli sono eseguiti da Python prima di generare il testo. L’AI riceve i numeri già corretti.

### Salvare un documento

Dopo la generazione:
1. Rivedi il testo nell’editor (puoi modificarlo a mano)
2. Clicca **"💾 Salva"**
3. Il documento viene salvato con un numero di protocollo automatico:
   ```
   2026/001, 2026/002, ...
   ```
4. Il file viene archiviato nella cartella `database/documents/`

---

## 6. Esportazione e Invio

### Come scaricare in PDF

1. Genera o apri un documento
2. Clicca su **"📄 Scarica PDF"**
3. Il browser scarica un file PDF con:
   - Intestazione "Studio Legale AI"
   - Nome dell’avvocato
   - Corpo formattato
   - Firma in calce

### Come scaricare in DOCX

1. Clicca su **"📄 Scarica DOCX"**
2. Il browser scarica un file Word editabile
3. Puoi aprirlo in Microsoft Word o LibreOffice
4. Il formato è professionale, con font Times New Roman 12pt

### Come scaricare in Markdown

1. Clicca su **"📄 Scarica MD"**
2. Utile per l’archiviazione testuale o il versionamento con Git

### Come inviare per email

1. Genera o seleziona un documento dall’archivio
2. Clicca su **"📧 Invia per Email"**
3. Si apre una finestra:

   | Campo | Valore |
   |-------|--------|
   | **Destinatario** | Auto-filled dall’email del cliente |
   | **Oggetto** | Titolo del documento |
   | **Corpo** | Messaggio pre-compilato |
   | **Allegati** | ☑️ DOCX ☑️ PDF ☑️ MD |

4. Modifica i campi se necessario
5. Seleziona gli allegati desiderati
6. Clicca **"📧 Invia"**

> ⚠️ **Prima di inviare:** assicurati di aver configurato l’SMTP in **Impostazioni** (vedi Sezione 9).

### Esempio concreto

> **Caso:** Invio della memoria difensiva al cliente Mario Rossi Srl.
>
> 1. Genera la memoria difensiva
> 2. Clicca **"📧 Invia per Email"**
> 3. Verifica che il destinatario sia: `info@mariorossi.it`
> 4. Oggetto: "Memoria difensiva — Pratica 2025/042"
> 5. Seleziona allegati:
>    - ☑️ DOCX (per eventuali modifiche)
>    - ☑️ PDF (per la stampa)
> 6. Clicca **Invia**
> 7. Riceverai una notifica: "Email inviata con successo"

---

## 7. Ricerca Legale Avanzata

### I 6 motori di ricerca

La sezione **Ricerca** consente di cercare contemporaneamente su più fonti giuridiche:

| Motore | Cosa cerca | Fonte |
|--------|-----------|-------|
| **Normattiva** | Leggi, decreti, regolamenti italiani | Normattiva.it |
| **Giustizia Amministrativa** | Sentenze TAR e Consiglio di Stato | DDG search |
| **CEDU** | Sentenze Corte Europea Diritti Uomo | DDG search |
| **EUR-Lex** | Direttive, regolamenti, decisioni UE | EUR-Lex + DDG |
| **CURIA** | Sentenze Corte di Giustizia UE | DDG search |
| **Dottrina** | Articoli scientifici e riviste | CrossRef + DDG |

### Come fare una ricerca

1. Vai su **Ricerca** nel menu
2. Scrivi il tema nella casella di ricerca
3. Clicca su uno o più pulsanti dei motori (es. **"🔍 Normattiva"**, **"🔍 Dottrina"**)
4. Attendi i risultati
5. Ogni motore mostra una lista di risultati con:
   - **Titolo**
   - **Riassunto**
   - **URL** per approfondire

### Esempio concreto

> **Caso:** Devi cercare fonti per una memoria su responsabilità civile medica.
>
> 1. Scrivi: `responsabilità civile medica art. 2043`
> 2. Clicca **"🔍 Normattiva"** per trovare le norme
> 3. Clicca **"🔍 Dottrina"** per trovare articoli scientifici
> 4. Clicca **"🔍 Giustizia Amministrativa"** per sentenze dei TAR
>
> I risultati appariranno divisi per sezione.

### Selezionare le fonti

Accanto a ogni risultato trovi il pulsante **"➕ Aggiungi"**.

1. Clicca **"➕ Aggiungi"** sui risultati che ti interessano
2. Le fonti selezionate compaiono in una lista laterale
3. Puoi rimuovere una fonte cliccando **"❌ Rimuovi"**

### Generare documento dalle fonti

Dopo aver selezionato le fonti:

1. Clicca su **"📄 Genera Documento con queste fonti"**
2. Si apre una finestra:
   - Seleziona **Tipologia documento** (es. Parere scritto)
   - Seleziona **Cliente** (opzionale)
   - Seleziona **Pratica** (opzionale)
3. Clicca **"Genera"**
4. L’AI crea un documento con:
   - Introduzione al tema
   - Analisi delle norme trovate
   - Riferimenti alla giurisprudenza
   - Conclusioni
   - **Bibliografia** con le fonti selezionate

### Verifica automatica delle citazioni

Quando generi una ricerca, l’AI cerca di inserire sentenze della Cassazione.

Per evitare **citazioni inventate** (allucinazioni):
- L’applicazione estrae ogni citazione "Cassazione, Sez. X, n. ..."
- Cerca su Internet se la sentenza esiste davvero
- Segna con ✅ le verificate e ⚠️ le non verificate

> ⚠️ **Attenzione:** la verifica automatica è accurata all’~80%. Per documenti importanti, verifica sempre manualmente le citazioni sulla banca dati ufficiale.

---

## 8. Calendario Scadenze

### Aggiungere udienze e termini

1. Vai su **Calendario** nel menu
2. Clicca su **"➕ Nuova Scadenza"**
3. Compila:

| Campo | Esempio |
|-------|---------|
| Titolo | Udienza di comparizione |
| Data | 15/05/2026 |
| Tipo | Udienza |
| Pratica collegata | Recupero crediti fornitura |

4. Clicca **"Salva"**

### Tipi di scadenza

| Tipo | Quando usarlo |
|------|---------------|
| **Udienza** | Appuntamento in tribunale |
| **Termine** | Scadenza per presentare atti (es. termine a difesa) |
| **Scadenza** | Data limite generica (es. scadenza contratto) |
| **Appuntamento** | Incontro con cliente o collega |

### Toggle completamento

Quando una scadenza è svolta:
1. Nella lista, clicca sulla casella di spunta ✅
2. La scadenza verrà barrata e spostata in fondo
3. Puoi ripristinarla togliendo la spunta

### Filtrare le scadenze

Usa i filtri sopra la tabella:
- **Tipo** — Mostra solo udienze, termini, ecc.
- **Pratica** — Filtra per caso specifico
- **Stato** — Mostra solo aperte o completate

### Visualizzazione dalla pratica

Quando guardi una pratica espansa (in pagina **Pratiche**), vedrai automaticamente tutte le scadenze collegate a quel caso.

---

## 9. Impostazioni

### Configurazione SMTP (Email)

Per inviare email con allegati, devi configurare l’account SMTP:

1. Vai su **Impostazioni**
2. Scorri fino alla sezione **"📧 Configurazione SMTP"**
3. Compila i campi:

| Campo | Esempio Gmail | Esempio Aruba |
|-------|---------------|---------------|
| Server SMTP | `smtp.gmail.com` | `smtp.aruba.it` |
| Porta SMTP | `587` | `587` |
| Username | `tuaemail@gmail.com` | `studio@tuodominio.it` |
| Password | *App Password* | *Password email* |
| Nome mittente | `Studio Legale AI` | `Studio Legale AI` |

4. Clicca **"💾 Salva SMTP"**
5. Clicca **"🧪 Test invio"** per verificare che funzioni

> 🔐 **Importante per Gmail:** devi usare una **App Password** (non la password normale). Crealà su https://myaccount.google.com/apppasswords

> 🔐 **Sicurezza:** le credenziali sono salvate solo sul tuo computer, nel file `database/settings.json`.

### Modello documento

Nelle impostazioni puoi anche configurare:
- **Modello AI primario** — Default: Nemotron-70B
- **Modello AI secondario** — Default: Qwen-72B
- **Temperatura** — Più bassa = più preciso, più alta = più creativo

Per la produzione di atti giuridici, lascia la temperatura su **0.3–0.5**.

---

## 10. Flusso di Lavoro Consigliato

### Esempio pratico completo

> **Caso:** Recupero crediti fornitura non pagata — Mario Rossi Srl vs Bianchi Srl
>
> **Pratica:** 2025/042

#### Passo 1 — Ricerca giuridica
1. Vai su **Ricerca**
2. Cerca: `messa in mora recupero crediti art. 1218 1223 codice civile`
3. Clicca **Normattiva** e **Dottrina**
4. Seleziona 3–4 fonti rilevanti
5. Clicca **"Genera Documento con queste fonti"**
6. Seleziona tipologia: **Parere scritto**
7. Collega cliente: **Mario Rossi Srl**, pratica: **2025/042**
8. Clicca **Genera**

#### Passo 2 — Generazione lettera di messa in mora
1. Vai su **Documenti**
2. Seleziona **Lettera di messa in mora**
3. Compila:
   - Oggetto: Mancato pagamento fattura n. 123
   - Destinatario: Bianchi Srl
   - Importo: € 15.000,00
   - Termine: 15 giorni
   - Cliente: Mario Rossi Srl
   - Pratica: 2025/042
4. Clicca **"⚡ Genera Documento"**
5. Rivedi il testo
6. Clicca **"💾 Salva"** — Protocollo: 2026/001

#### Passo 3 — Invio al cliente per approvazione
1. Clicca **"📧 Invia per Email"**
2. Destinatario: `info@mariorossi.it`
3. Oggetto: `Bozza lettera di messa in mora — Pratica 2025/042`
4. Seleziona allegato: ☑️ DOCX
5. Clicca **Invia**

#### Passo 4 — Tracciamento scadenza
1. Vai su **Calendario**
2. Clicca **"➕ Nuova Scadenza"**
3. Titolo: Termine per presentazione atto di citazione
4. Data: *15 giorni dopo la scadenza della mora*
5. Tipo: Termine
6. Pratica: 2025/042
7. Clicca **Salva**

#### Passo 5 — Archiviazione
Il documento 2026/001 è salvato automaticamente in `database/documents/` e visibile nell’archivio con tutti i metadati.

---

## 11. FAQ e Troubleshooting

### Domande frequenti

**D: I dati dei clienti finiscono su Internet?**
> R: **No.** I modelli AI (Nemotron e Qwen) girano sul tuo server locale. Nessun dato lascia il computer, eccetto le ricerche sui motori giuridici (Normattiva, EUR-Lex, ecc.) che sono pubbliche.

**D: Posso usare il software senza connessione?**
> R: Sì per la gestione clienti, pratiche, documenti e calendario. **No** per la ricerca giuridica e la verifica citazioni, che richiedono Internet.

**D: I documenti generati dall’AI hanno valore legale?**
> R: Sono **bozze professionali** ma devono sempre essere **revisionati e sottoscritti** dall’avvocato prima dell’uso processuale.

**D: Come faccio il backup?**
> R: Copia la cartella `database/` su un disco esterno o cloud personale. Contiene tutto: clienti, pratiche, documenti, impostazioni.

**D: Posso modificare un documento dopo averlo salvato?**
> R: Sì. Scaricalo in DOCX, modificalo in Word/LibreOffice, e caricalo nuovamente se necessario. Oppure rigeneralo dalla pagina Documenti.

**D: Quanti documenti posso generare?**
> R: Nessun limite. Il protocollo è progressivo annuale (2026/001, 2026/002, ...).

**D: Posso usare un altro modello AI?**
> R: Sì, se è compatibile con l’API OpenAI. Modifica l’endpoint in Impostazioni.

### Errori comuni e soluzioni

| Errore | Causa | Soluzione |
|--------|-------|-----------|
| "LLM non risponde" | Il servizio AI è spento | Apri il terminale e verifica: `curl http://localhost:8081/health` |
| "Configurazione SMTP incompleta" | Non hai salvato l’email | Vai su Impostazioni e compila i campi SMTP |
| "Errore invio email" | Password errata o server bloccato | Per Gmail usa App Password; per Aruba verifica la porta |
| "Ricerca EUR-Lex vuota" | Il server SPARQL è bloccato | Usa il risultato DuckDuckGo che appare sotto |
| "Timeout generazione" | Modello sovraccarico | Aspetta 30 secondi e riprova |
| "Citazioni non verificate" | DDG ha raggiunto il limite | Aspetta 2–3 minuti e rigenera il documento |
| "Pagina bianca" | Browser datato | Aggiorna Chrome/Firefox all’ultima versione |
| "Documento non si scarica" | Popup bloccati | Consenti i popup per localhost:8506 |

### Contatti e supporto

Per segnalazioni, richieste di funzionalità o assistenza:

- **Repository GitHub:** https://github.com/geneforge-ai/studio-legale-ai
- **Email:** support@geneforge-ai.it
- **Documentazione aggiornata:** https://github.com/geneforge-ai/manuals

---

*Studio Legale AI — Powered by GeneForge AI*

*© 2026 — Tutti i diritti riservati*

*Manuale redatto per l’Avv. Marco della Luna e lo Studio Legale AI*
