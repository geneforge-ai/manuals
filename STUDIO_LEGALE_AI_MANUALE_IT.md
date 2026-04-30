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
- **Generare documenti giuridici** con agenti AI specializzati
- **Cercare norme, giurisprudenza e dottrina** con ricercatori AI dedicati
- **Tracciare scadenze, udienze e termini** con promemoria automatici
- **Esportare e inviare documenti** in PDF, DOCX o via email
- **Verificare citazioni** della Cassazione con un clic

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

La **Dashboard** è la prima pagina che vedi dopo l’accesso. Ti dà un quadro immediato della situazione dello studio ed è anche il punto di contatto con l’**Avvocato Generico**, l’agente AI per domande rapide.

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

1. **Dashboard** — Panoramica + chat con l'Avvocato Generico
2. **Clienti** — Anagrafica
3. **Pratiche** — Gestione casi
4. **Documenti** — Generazione con Documentalista e Segretaria
5. **Ricerca** — Ricerca con Ricercatore Giuridico e Cassazione
6. **Calendario** — Scadenze e promemoria
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

### Gli agenti del modulo Documenti

Quando generi un documento, non parli con un "generico AI". Parli con agenti specializzati:

| Agente | Ruolo | Quando usarlo |
|--------|-------|---------------|
| **Documentalista Legale** | Genera atti giuridici formali | Memorie, contratti, ricorsi, pareri |
| **Segretaria Legale** | Documenti amministrativi | Note di trasmissione, promemoria, solleciti |

Il sistema **sceglie automaticamente** l'agente giusto in base al tipo di documento.

---

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
6. Il sistema **seleziona automaticamente l'agente**:
   - Se scegli "Nota di trasmissione" → interviene la **Segretaria Legale** (veloce, ~10s)
   - Se scegli qualsiasi altro atto → interviene il **Documentalista Legale** (~30-60s)
7. Il documento apparirà nell’editor

### 🏛️ Verifica citazioni della Cassazione

Dopo aver generato un documento che cita sentenze, puoi verificarne l'esistenza:

1. Clicca su **"🏛️ Verifica Cassazione"**
2. Il **Ricercatore Cassazione** estrae ogni citazione "Cass., Sez. X, n. ..."
3. Cerca su Internet se la sentenza esiste
4. Ti mostra un report: ✅ verificata, ⚠️ non verificata, ❌ probabilmente inventata

> ⚠️ **Attenzione:** la verifica automatica è accurata all'~85%. Per documenti importanti, verifica sempre sulla banca dati ufficiale.

---

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

### Gli agenti del modulo Ricerca

La sezione **Ricerca** è gestita da due agenti specializzati:

| Agente | Modello | Temperatura | Specializzazione |
|--------|---------|-------------|------------------|
| **Ricercatore Giuridico** | Nemotron-70B | 0.3 | Normativa, giurisprudenza, dottrina |
| **Ricercatore Cassazione** | Nemotron-70B | 0.1 | Solo Corte di Cassazione — zero tolleranza per errori |

Il **Ricercatore Cassazione** è il più "rigoroso" del sistema. La sua temperatura è 0.1 (la minima possibile) perché non può permettersi di inventare sentenze. Se non è certo di una pronuncia, dichiara esplicitamente: *"Non verificato"*.

---

### I 6 motori di ricerca

Oltre agli agenti AI, puoi cercare contemporaneamente su più fonti giuridiche:

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
- L’agente **Ricercatore Cassazione** estrae ogni citazione "Cassazione, Sez. X, n. ..."
- Cerca su Internet se la sentenza esiste davvero
- Segna con ✅ le verificate e ⚠️ le non verificate

> ⚠️ **Attenzione:** la verifica automatica è accurata all’~85%. Per documenti importanti, verifica sempre manualmente le citazioni sulla banca dati ufficiale.

---

## 8. Calendario Scadenze

### Promemoria automatici con la Segretaria Legale

Ogni scadenza nel calendario ha un pulsante **"📋"** che attiva la **Segretaria Legale**.

La Segretaria può generare:
- **Promemoria** — Ricorda cosa fare e quanti giorni mancano
- **Sollecito** — Tono più deciso per scadenze già passate o imminenti

Il tono è automaticamente graduato:
- Se mancano > 7 giorni → educato e professionale
- Se mancano 3-7 giorni → fermo ma cortese
- Se la scadenza è passata → deciso, con azioni concrete richieste

---

### Aggiungere udienze e termini

1. Vai su **Calendario** nel menu
2. Clicca su **"➕ Nuova Scadenza"
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

### Configurazione degli agenti AI

Nelle impostazioni puoi anche visualizzare la configurazione degli agenti:
- **Avvocato Generico** — Modello: auto (router), Temp: 0.5
- **Analista Contrattuale** — Modello: Nemotron, Temp: 0.2
- **Ricercatore Giuridico** — Modello: Nemotron, Temp: 0.3
- **Ricercatore Cassazione** — Modello: Nemotron, Temp: 0.1
- **Documentalista Legale** — Modello: Nemotron, Temp: 0.2
- **Segretaria Legale** — Modello: Qwen, Temp: 0.3
- **Parerista** — Modello: Nemotron, Temp: 0.2

Ogni agente ha una **temperatura** ottimizzata per il suo compito. Non è consigliabile modificarle senza motivo.

Per la produzione di atti giuridici, il sistema usa temperature basse (0.1–0.3) per massimizzare la precisione.

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
> R: **No.** Gli agenti AI girano sul tuo server locale. Nessun dato lascia il computer, eccetto le ricerche avanzate (Nemotron API) dove viene trasmesso *solo il testo della query*, mai dati delle pratiche. Le ricerche sui motori giuridici (Normattiva, EUR-Lex, ecc.) sono pubbliche.

**D: Posso usare il software senza connessione?**
> R: Sì per la gestione clienti, pratiche, documenti e calendario. **No** per la ricerca giuridica e la verifica citazioni, che richiedono Internet.

**D: I documenti generati dall’AI hanno valore legale?**
> R: Sono **bozze professionali** generate da agenti AI specializzati, ma devono sempre essere **revisionati e sottoscritti** dall’avvocato prima dell’uso processuale. L’agente è uno strumento, non un sostituto del professionista.

**D: Come faccio il backup?**
> R: Copia la cartella `database/` su un disco esterno o cloud personale. Contiene tutto: clienti, pratiche, documenti, impostazioni.

**D: Posso modificare un documento dopo averlo salvato?**
> R: Sì. Scaricalo in DOCX, modificalo in Word/LibreOffice, e caricalo nuovamente se necessario. Oppure rigeneralo dalla pagina Documenti.

**D: Quanti documenti posso generare?**
> R: Nel pacchetto **Base**: fino a 50/mese. **Professional**: fino a 200/mese. **Enterprise**: illimitati.

**D: Cos'è la temperatura di un agente?**
> R: È un parametro che regola la "creatività" dell'AI. I nostri agenti legali usano temperature molto basse (0.1–0.3) per essere precisi e conservativi. L'Avvocato Generico, che risponde a domande rapide, ha temperatura 0.5 per essere più conversazionale.

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
- **Email:** marco.saba@geneforge.eu
- **Documentazione aggiornata:** https://github.com/geneforge-ai/manuals

---

*Studio Legale AI — Powered by GeneForge AI*

*© 2026 — Tutti i diritti riservati*

*Manuale redatto per l’Avv. Marco della Luna e lo Studio Legale AI*


---

## 12. Gli Agenti AI di Studio Legale AI

### Panoramica

Studio Legale AI non usa un "unico chatbot" per tutto. Utilizza **7 agenti AI specializzati**, ciascuno con una propria identità, competenze e regole di comportamento. Il sistema sceglie automaticamente l'agente giusto per ogni compito.

### I 7 agenti

#### ⚖️ 1. Avvocato Generico
- **Ruolo:** Primo punto di contatto per domande legali rapide
- **Modello:** Auto (router sceglie il più veloce)
- **Temperatura:** 0.5
- **Quando usarlo:** Dashboard, domande di diritto generale, rimandi normativi
- **Regole critiche:**
  - Non inventa sentenze
  - Indica norme abrogate
  - Sempre disclaimer "verificare con professionista"

#### 📜 2. Analista Contrattuale
- **Ruolo:** Analisi approfondita di contratti
- **Modello:** Nemotron-70B
- **Temperatura:** 0.2
- **Quando usarlo:** Pagina Contratti — verifica di accordi commerciali
- **Output:** Executive Summary → Rischi → Mancanze → Modifiche suggerite
- **Regole critiche:**
  - Non inventa clausole
  - Distingue rischio cliente vs controparte
  - Indica grado di rischio (alto/medio/basso)

#### 🔍 3. Ricercatore Giuridico
- **Ruolo:** Ricerche multi-motore su normativa e giurisprudenza
- **Modello:** Nemotron-70B
- **Temperatura:** 0.3
- **Quando usarlo:** Pagina Ricerca — tema generico
- **Output:** Normativa vigente + giurisprudenza + dottrina
- **Regole critiche:**
  - Cita fonti precise
  - Distingue vigente / abrogata / in riforma
  - Indica data di pubblicazione delle fonti

#### 🏛️ 4. Ricercatore Cassazione
- **Ruolo:** Giurisprudenza della Corte di Cassazione
- **Modello:** Nemotron-70B
- **Temperatura:** 0.1 (la più bassa del sistema)
- **Quando usarlo:** Quando la tesi dipende criticamente dalla Cassazione
- **Output:** Orientamenti maggioritari/minoritari, grado consolidamento
- **Regole critiche:**
  - Se non certo → dichiara "non verificato"
  - Distingue Sezioni Unite / Semplici
  - Indica grado: consolidato / emergente / superato

#### 📄 5. Documentalista Legale
- **Ruolo:** Generazione di 11 tipi di atto giuridico
- **Modello:** Nemotron-70B
- **Temperatura:** 0.2
- **Quando usarlo:** Pagina Documenti — tutti gli atti tranne Nota di trasmissione
- **Output:** Documento strutturato con intestazione, protocollo, firma
- **Regole critiche:**
  - Non inventa dati cliente/protocollo
  - Cita norma specifica per tipo di atto
  - Formato pronto per la firma

#### 📋 6. Segretaria Legale
- **Ruolo:** Documenti amministrativi e promemoria
- **Modello:** Qwen-72B
- **Temperatura:** 0.3
- **Quando usarlo:** Note di trasmissione, promemoria scadenze, solleciti
- **Output:** Documento amministrativo professionale
- **Regole critiche:**
  - Calcola giorni rimanenti/trascorsi automaticamente
  - Tono graduato in base all'urgenza
  - **Blacklist:** NON fornisce consulenza legale sostanziale

#### 📖 7. Parerista
- **Ruolo:** Pareri legali formali strutturati
- **Modello:** Nemotron-70B
- **Temperatura:** 0.2
- **Quando usarlo:** Pagina Pareri — quando serve una risposta motivata
- **Output:** Quesito → Norma → Analisi → Conclusioni → Rischi
- **Regole critiche:**
  - Grado di certezza: "certa" / "probabile" / "possibile ma rischiosa"
  - Indica sempre le fonti
  - Non omette rischi connessi alla tesi sostenuta

### Fallback di sicurezza

Se il sistema di agenti non è disponibile (es. file YAML corrotti), l'applicazione **non si blocca**. Usa automaticamente i prompt "legacy" originali, salvaguardando la continuità del servizio.

---

## 13. Prezzi e Servizi Commerciali

### Modello di business

Studio Legale AI è offerto in modalità **on-premise**: il sistema viene installato fisicamente nello studio su hardware NVIDIA DGX SPARK. I dati non escono mai dall'ufficio.

### Pacchetti disponibili

| Pacchetto | Canone/mese | Setup | Destinatario |
|-----------|-------------|-------|--------------|
| **Base** | € 500 + IVA | € 990 | 1–3 avvocati |
| **Professional** | € 1.000 + IVA | € 990 | 4–8 avvocati |
| **Enterprise** | € 2.500 + IVA | € 1.990 | 10+ avvocati / Network |

### Cosa include ogni pacchetto

#### 🥉 Base — € 500/mese
- 7 agenti AI standard
- 50 documenti/mese
- 20 ricerche avanzate/mese
- Archivio fino a 1.000 documenti
- Supporto email (24h SLA)

#### 🥈 Professional — € 1.000/mese
- 7 agenti + 1 agente custom
- 200 documenti/mese
- 100 ricerche avanzate/mese
- Archivio illimitato
- Supporto telefonico (8h SLA)
- 2 sessioni di formazione

#### 🥇 Enterprise — € 2.500/mese
- 7 agenti + 3 agenti custom
- Documenti illimitati
- Ricerche avanzate illimitate
- Archivio illimitato + API REST
- Account Manager dedicato (4h SLA)
- Cluster HA (2 DGX SPARK)

### Hardware incluso

L'hardware NVIDIA DGX SPARK è incluso nel canone in comodato d'uso. Specifiche:
- GPU NVIDIA GB10 Grace Blackwell Superchip
- 128 GB unified memory
- 4 TB NVMe SSD
- < 35 dB in operazione (adatto a ufficio)

### ROI stimato

| Metrica | Valore |
|---------|--------|
| Tempo risparmiato su redazione atti | 60–70% |
| Tempo risparmiato su ricerche | 50–60% |
| Riduzione errori formali | 80%+ |
| **Payback stimato** | **1–2 mesi** (studio con 3+ avvocati) |

### Contatti commerciali

- **Demo:** info@geneforge.eu
- **Supporto tecnico:** info@geneforge.eu
- **Telefono:** +39 370 353 8535

---

*Studio Legale AI — Powered by GeneForge AI*

*© 2026 — Tutti i diritti riservati*

*Manuale redatto per l'Avv. Marco della Luna e lo Studio Legale AI*
*Versione 2.0 — 30 Aprile 2026*
