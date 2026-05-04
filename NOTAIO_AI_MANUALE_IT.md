# Notaio AI — Manuale Utente

**Versione:** 1.2
**Data:** 4 Maggio 2026
**Progetto:** GeneForge AI — Notaio AI
**Destinatari:** Notai, collaboratori e segretarie degli Studi Notarili

---

## 1. Introduzione

### Cos’è Notaio AI

**Notaio AI** è un pacchetto on-premise di agenti AI specializzati per la professione notarile italiana. Il sistema assiste il Notaio e i collaboratori nella stesura, verifica, conformità e gestione degli atti notarili.

Tutto gira su server locali. Nessun dato dei clienti lascia mai il tuo studio.

### A cosa serve

- **Stesura atti notarili** con agenti AI specializzati per 7 tipi di atto
- **Verifica catastale** con report strutturati e checklist (atti immobiliari)
- **Conformità urbanistica, edilizia e fiscale** con verifica agevolazioni (atti immobiliari)
- **Controllo documenti** e coerenza dati prima del rogito
- **Cronoprogramma scadenze** con termini perentori calcolati automaticamente
- **Ricerca normativa** notarile, circolari CNN, giurisprudenza
- **Supporto firma digitale** InfoCert, Aruba, Namirial
- **Notaio Sintetico** — consulenza strategica in chat per ogni dubbio di procedura

### Vantaggi principali

| Vantaggio | Descrizione |
|-----------|-------------|
| **Privacy totale** | I modelli AI girano localmente. Nessun dato in cloud |
| **Risparmio di tempo** | Un atto si genera in 2–3 minuti (5 fasi) o 1–2 minuti (3 fasi) |
| **Zero errori formali** | Intestazione e firma pre-compilate dal codice, non dall'AI |
| **Conformità garantita** | Verifica automatica documenti, agevolazioni, scadenze |
| **Multi-formato** | PDF per la stampa, DOCX per le modifiche, MD per l'archivio |
| **Responsive** | Funziona su desktop, tablet e smartphone |
| **Dark mode** | Interfaccia scura ottimizzata per lunghe sessioni di lavoro |

### Come accedere

Apri il browser e digita:

```
http://localhost:8507
```

Se usi il tunnel Cloudflare (accesso online):

```
https://notaio-ai.geneforge.eu
```

Non serve password. L'applicazione è pronta all'uso.

---

## 2. Avvio e Installazione

### Prerequisiti hardware

- **NVIDIA DGX SPARK** (prerequisito — da acquistare dai distributori NVIDIA autorizzati)
- GPU NVIDIA GB10 Grace Blackwell Superchip
- 128 GB unified memory
- 4 TB NVMe SSD

### Avvio

1. Accendi il DGX SPARK
2. Apri il terminale nella cartella `notaio-ai/web-ui/`
3. Esegui:
   ```bash
   ./launch_notaio_ai.sh
   ```
4. Apri il browser all'indirizzo indicato (`http://localhost:8507` o `https://notaio-ai.geneforge.eu` se online)

---

## 3. Gli 7 Agenti Notarili

Quando generi un documento, non parli con un "generico AI". Parli con agenti specializzati:

| Agente | Ruolo | Quando usarlo |
|--------|-------|---------------|
| **Attista** | Stesura atti notarili | Compravendite, società, testamenti, mutui |
| **Catasto** | Verifica dati catastali | Visure, planimetrie, anomalie |
| **Conformità** | Conformità urbanistica/edilizia/fiscale | Verifica documenti, agevolazioni, criticità |
| **Controllo** | Controllo documenti | Checklist completezza, coerenza dati, firme |
| **Scadenze** | Gestione termini e scadenze | Cronoprogramma post-stipula |
| **Ricercatore** | Ricerca normativa | Leggi, circolari CNN, giurisprudenza |
| **Firma** | Supporto firma digitale | InfoCert, Aruba, Namirial |

Il sistema **sceglie automaticamente** l'agente giusto in base al task.

---

## 4. Selettore Tipo Atto e Form Dedicate

### Panoramica

Notaio AI supporta **7 tipi di atto notarile**. Al centro della schermata principale trovi il selettore **⚖️ Tipo di Atto** — scegli quello che ti serve e il form si adatta automaticamente.

| # | Tipo di Atto | Form dedicate | Fasi workflow |
|---|--------------|---------------|---------------|
| 1 | **Compravendita immobiliare** | Venditore, Acquirente, Immobile, Economico | 5 fasi |
| 2 | **Costituzione SRL** | Soci, Denominazione, Sede, Oggetto, Capitale, Amministratore, Statuto | 3 fasi |
| 3 | **Testamento** | Testatore, Eredi, Legati, Esecutore, Disposizioni | 3 fasi |
| 4 | **Patto di famiglia** | Contraenti, Bene, Regime, Durata, Successori | 3 fasi |
| 5 | **Mutuo ipotecario** | Mutuatario, Istituto, Importo, Tasso, Durata, Immobile garanzia | 5 fasi |
| 6 | **Divisione** | Coeredi, Bene, Quote, Modalità | 5 fasi |
| 7 | **Donazione** | Donante, Donatario, Bene, Regime fiscale, Oneri | 5 fasi |

> 💡 **Come funziona:** quando cambi tipo di atto, le card del form appaiono e scompaiono automaticamente. Compila solo i campi visibili.

---

## 5. Workflow per Tipo di Atto — Guida Passo-passo

### Panoramica del flusso

**Atti immobiliari** (Compravendita, Mutuo, Divisione, Donazione):

```
Inserimento dati → Verifica Catastale → Conformità → Stesura Atto → Controllo → Scadenze
                              ↑_____________↑
                        (solo per atti con immobile)
```

**Atti non immobiliari** (Costituzione SRL, Testamento, Patto di famiglia):

```
Inserimento dati → Stesura Atto → Controllo → Scadenze
```

### Passo 1 — Selezione e inserimento dati

1. Apri Notaio AI su `http://localhost:8507`
2. Seleziona il **Tipo di Atto** dal menu a tendina in cima alla colonna sinistra
3. Compila le card dedicate che compaiono:
   - **Compravendita**: Dati Venditore, Acquirente, Immobile, Economico
   - **Costituzione SRL**: Dati Società (soci, denominazione, sede, oggetto, capitale, amministratore, statuto)
   - **Testamento**: Dati Testatore, Eredi, Legati, Esecutore, Disposizioni
   - **Patto di famiglia**: Dati Contraenti, Bene, Regime, Durata, Successori
   - **Mutuo ipotecario**: Dati Mutuo (mutuatario, istituto, importo, tasso, durata, immobile garanzia)
   - **Divisione**: Dati Divisione (coeredi, bene, quote, modalità)
   - **Donazione**: Dati Donazione (donante, donatario, bene, regime fiscale, oneri)
4. Compila sempre la card **💶 Dati Economici e Clausole** (condivisa per tutti i tipi)

> 💡 **Suggerimento:** Seleziona il cliente dall'anagrafica (se disponibile) per pre-compilare i dati.

### Passo 2 — Generazione

1. Clicca su **"⚖️ Genera Atto: [Tipo selezionato]"**
2. Il sistema esegue le fasi in sequenza:

   **Per atti immobiliari (5 fasi):**
   - **Fase 1/5: Verifica Catastale** (~15–20s)
   - **Fase 2/5: Verifica Conformità** (~50–70s)
   - **Fase 3/5: Stesura Atto** (~50–70s)
   - **Fase 4/5: Controllo Documenti** (~15–20s)
   - **Fase 5/5: Cronoprogramma Scadenze** (~15–20s)

   **Per atti non immobiliari (3 fasi):**
   - **Fase 1/3: Stesura Atto** (~50–70s)
   - **Fase 2/3: Controllo Documenti** (~15–20s)
   - **Fase 3/3: Cronoprogramma Scadenze** (~15–20s)

3. Il documento completo apparirà nell'area risultato

### Passo 3 — Revisione

1. **Leggi i report preliminari** (catasto e conformità, se presenti): verifica coerenza con i dati reali
2. **Leggi l'atto**: verifica che il corpo giuridico sia corretto per il tipo di atto selezionato
3. **Leggi il controllo**: assicurati che tutti i documenti obbligatori siano presenti
4. **Leggi le scadenze**: verifica le date calcolate

> ⚠️ **Attenzione:** L'AI genera SOLO il corpo giuridico. Intestazione, procura e firma sono pre-compilate dal codice Python in modo deterministico.

### Passo 4 — Export

1. Clicca su **"📄 Scarica PDF"** per la stampa
2. Clicca su **"📄 Scarica DOCX"** per modifiche in Word/LibreOffice
3. Clicca su **"📧 Invia per Email"** per inviare al cliente

---

## 6. Notaio Sintetico — Consulenza Strategica

### Cos'è

Il **Notaio Sintetico** è un assistente AI in chat integrato nell'applicazione. Non sostituisce il Notaio, ma offre una **consulenza rapida** su:
- Quali documenti servono per un determinato atto
- Come procedere in casi particolari
- Quali norme si applicano
- Dubbi di procedura prima del rogito

### Come si usa

1. Compila il form con il tipo di atto che ti interessa
2. Clicca su **"💬 Chiedi al Notaio Sintetico"** (nella colonna destra, sopra il pulsante "Genera Atto")
3. Si apre una finestra a tutto schermo con la chat
4. Scrivi la tua domanda e premi **Invia**

> 🧘 **Meditazione in corso...** Mentre Nemotron elabora la risposta, vedrai questo indicatore. La risposta arriva in 30–60 secondi.

### Esempi di domande

- "Quali documenti servono per una procura in caso di compravendita?"
- "L'acquirente under 36 ha diritto all'imposta di bollo agevolata?"
- "Quanto tempo ho per registrare l'atto di costituzione SRL?"
- "Serve l'assenso del coniuge per la donazione di un immobile?"

> ⚠️ **Attenzione:** Il Notaio Sintetico fornisce indicazioni di massima. Per decisioni definitive, consulta sempre la normativa vigente e la giurisprudenza aggiornata.

---

## 7. Esempi Concreti

### 7.1 Prima Casa Under 36 — Compravendita

> **Caso:** Laura Verdi, 28 anni, ISEE €22.000, acquista la sua prima casa da Mario Rossi per €180.000.
>
> **Agevolazione:** art. 1 commi 67-71 L. 234/2021 (prima casa under 36)
>
> 1. Seleziona **"Compravendita immobiliare"**
> 2. Inserisci i dati nel form
> 3. Clicca **"Genera Atto"**
> 4. Il sistema genera 5 sezioni: Catasto, Conformità, Atto, Controllo, Scadenze
> 5. Rivedi il documento e scarica in PDF/DOCX

### 7.2 Costituzione SRL

> **Caso:** Marco Rossi (60%) e Paolo Bianchi (40%) costituiscono la "Rossi & Bianchi SRL" con capitale €10.000.
>
> 1. Seleziona **"Costituzione SRL"**
> 2. Compila: Soci, Denominazione, Sede, Oggetto, Capitale, Amministratore, Statuto
> 3. Clicca **"Genera Atto"**
> 4. Il sistema genera 3 sezioni: Atto di Costituzione SRL, Controllo Documenti, Scadenze (iscrizione REA, PEC, ecc.)

### 7.3 Testamento Olografo Pubblico

> **Caso:** Carlo Verdi, 70 anni, vuole lasciare i beni ai figli Marco e Anna in parti uguali.
>
> 1. Seleziona **"Testamento"**
> 2. Compila: Testatore, Eredi, Legati, Esecutore, Disposizioni
> 3. Clicca **"Genera Atto"**
> 4. Il sistema genera il corpo giuridico del testamento con normativa artt. 587-602 c.c.

---

## 8. Verifica e Controllo Qualità

### Placeholder e dati da verificare

Quando l'AI non ha accesso a una banca dati esterna, inserisce indicazioni di verifica:

- **Visura catastale**: richiede verifica su Agenzia Entrate
- **APE**: richiede commissione se mancante
- **Ipoteche**: richiede visura ipotecaria in Conservatoria

> ⚠️ **L'AI non inventa mai dati catastali, numeri di sentenza o norme.** Se non è certa, indica "da verificare".

### Regole di sicurezza

1. **Non firmare mai un atto senza revisione umana**
2. **Verificare sempre le citazioni giurisprudenziali** su database ufficiali
3. **Controllare i calcoli fiscali** con il proprio software contabile
4. **Validare le date delle scadenze** con il calendario notarile

---

## 9. FAQ e Troubleshooting

### Domande frequenti

**D: Quanti tipi di atto sono supportati?**
> R: **7 tipi**: Compravendita immobiliare, Costituzione SRL, Testamento, Patto di famiglia, Mutuo ipotecario, Divisione, Donazione.

**D: I dati dei clienti finiscono su Internet?**
> R: **No.** Gli agenti AI girano sul tuo server locale. Nessun dato lascia il computer, eccetto le ricerche normative dove viene trasmesso *solo il testo della query*, mai dati delle pratiche.

**D: Posso usare il software senza connessione?**
> R: Sì per la stesura atti, verifica catastale (con placeholder), controllo documenti, scadenze e Notaio Sintetico. **No** per la ricerca normativa e la verifica via web, che richiedono Internet.

**D: Gli atti generati dall'AI hanno valore legale?**
> R: Sono **bozze professionali** generate da agenti AI specializzati, ma devono sempre essere **revisionati e sottoscritti** dal Notaio prima del rogito.

**D: L'AI inventa clausole o dati catastali?**
> R: I nostri agenti hanno regole ferree: non inventano mai. Se manca un dato, usano placeholder o indicano "da verificare".

**D: Quanti documenti posso generare?**
> R: Nel pacchetto **Base**: fino a 50/mese. **Professional**: fino a 200/mese. **Enterprise**: illimitati.

**D: Posso modificare un atto dopo la generazione?**
> R: Sì. Scaricalo in DOCX, modificalo in Word/LibreOffice, e caricalo nuovamente se necessario.

**D: Qual è il tempo medio di generazione?**
> R: **Atti immobiliari** (5 fasi): 2–3 minuti. **Atti non immobiliari** (3 fasi): 1–2 minuti. La stesura dell'atto da sola richiede 50–70 secondi.

**D: Perché alcuni atti hanno 5 fasi e altri 3?**
> R: Gli atti che riguardano un immobile (Compravendita, Mutuo, Divisione, Donazione) richiedono Verifica Catastale e Conformità. Gli altri (SRL, Testamento, Patto di famiglia) non le richiedono.

**D: Il Notaio Sintetico sostituisce il parere del Notaio?**
> R: **No.** È uno strumento di supporto per dubbi procedurali. Le decisioni giuridiche definitive spettano sempre al Notaio.

### Errori comuni e soluzioni

| Errore | Causa | Soluzione |
|--------|-------|-----------|
| "LLM non risponde" | Il servizio AI è spento | Verifica: `curl http://localhost:8081/health` |
| "Timeout generazione" | Nemotron sovraccarico | Aspetta 30 secondi e riprova |
| "Placeholder non sostituiti" | Dati mancanti nel form | Compila tutti i campi del tipo di atto selezionato |
| "Documento incompleto" | Campi obbligatori vuoti | Verifica che la card dedicata al tipo di atto sia compilata |
| "Pagina bianca" | Browser datato | Aggiorna Chrome/Firefox |
| "Testo scuro su scuro" | CSS non caricato | Ricarica la pagina con cache vuota (Ctrl+F5) |
| "Dropdown bianco" | Tema chiaro di Quasar | Verifica che `ui.dark_mode().enable()` sia attivo |
| "Bottone non si aggiorna" | Cache del browser | Chiudi e riapri il browser |

---

## 10. Prezzi e Servizi Commerciali

### Modello di business

Notaio AI è offerto in modalità **on-premise**: il sistema viene installato fisicamente nello studio su hardware NVIDIA DGX SPARK (acquistato separatamente). I dati non escono mai dall'ufficio.

### Pacchetti disponibili

| Pacchetto | Canone/mese | Setup | Destinatario |
|-----------|-------------|-------|--------------|
| **Base** | € 500 + IVA | € 990 | 1-3 notai |
| **Professional** | € 1.000 + IVA | € 990 | 4-8 notai |
| **Enterprise** | € 2.500 + IVA | € 1.990 | 10+ notai / Network |

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

### Hardware prerequisito

L'hardware NVIDIA DGX SPARK è un prerequisito. Il cliente lo acquista dai distributori NVIDIA autorizzati, con i quali GeneForge ha accordi di cooperazione. Specifiche:
- GPU NVIDIA GB10 Grace Blackwell Superchip
- 128 GB unified memory
- 4 TB NVMe SSD
- < 35 dB in operazione (adatto a ufficio)

### ROI stimato

| Metrica | Valore |
|---------|--------|
| Tempo risparmiato su redazione atti | 60–70% |
| Tempo risparmiato su verifiche | 50–60% |
| Riduzione errori formali | 80%+ |
| **Payback stimato** | **1–2 mesi** (studio con 2+ notai) |

### Contatti commerciali

- **Demo:** info@geneforge.eu
- **Supporto tecnico:** info@geneforge.eu
- **Telefono:** +39 370 353 8535

---

## 11. Gli Agenti AI di Notaio AI — Dettaglio

### Panoramica

Notaio AI utilizza **7 agenti AI specializzati**, ciascuno con una propria identità, competenze e regole di comportamento. Il sistema sceglie automaticamente l'agente giusto per ogni compito.

### I 7 agenti

#### 📜 1. Attista
- **Ruolo:** Stesura di atti notarili
- **Modello:** Nemotron-70B
- **Temperatura:** 0.15 (molto conservativa)
- **Output:** Corpo giuridico con premesse, dispositive, clausole
- **Regole critiche:** Non inventa clausole, cita norma specifica, registro solenne
- **Tipi supportati:** Compravendita, Costituzione SRL, Testamento, Patto di famiglia, Mutuo, Divisione, Donazione

#### 🏠 2. Catasto
- **Ruolo:** Verifica dati catastali
- **Modello:** Qwen-72B
- **Temperatura:** 0.1 (massima precisione)
- **Output:** Report con checklist e anomalie
- **Regole critiche:** Non inventa dati catastali, usa placeholder per verifiche esterne
- **Quando viene chiamato:** Solo per atti immobiliari (Compravendita, Mutuo, Divisione, Donazione)

#### ✅ 3. Conformità
- **Ruolo:** Conformità urbanistica, edilizia, fiscale
- **Modello:** Nemotron-70B
- **Temperatura:** 0.15
- **Output:** Report con documenti mancanti e agevolazioni
- **Regole critiche:** Non dà parere positivo assoluto se manca documentazione
- **Quando viene chiamato:** Solo per atti immobiliari

#### 📋 4. Controllo
- **Ruolo:** Controllo documenti e coerenza
- **Modello:** Qwen-72B
- **Temperatura:** 0.1
- **Output:** Checklist obbligatori/facoltativi, alert firme
- **Regole critiche:** Non dà OK definitivo, distingue obbligo da best practice

#### ⏰ 5. Scadenze
- **Ruolo:** Gestione termini e scadenze
- **Modello:** Qwen-72B
- **Temperatura:** 0.1
- **Output:** Cronoprogramma con date calcolate
- **Regole critiche:** Distingue perentori da ordinatori, calcola in giorni solari

#### 🔍 6. Ricercatore
- **Ruolo:** Ricerca normativa notarile
- **Modello:** Nemotron-70B
- **Temperatura:** 0.2
- **Output:** Quadro normativo, circolari CNN, giurisprudenza
- **Regole critiche:** Non inventa norme, distingue vigente da abrogata

#### ✍️ 7. Firma
- **Ruolo:** Supporto firma digitale
- **Modello:** Qwen-72B
- **Temperatura:** 0.1
- **Output:** Istruzioni passo-passo per provider
- **Regole critiche:** Non genera mai PIN o password, usa solo link ufficiali

---

*Notaio AI — Powered by GeneForge AI*
*© 2026 — Tutti i diritti riservati*
*Manuale redatto per i Notai e gli Studi Notarili italiani*
*Versione 1.2 — 4 Maggio 2026*
