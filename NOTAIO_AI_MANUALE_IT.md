# Notaio AI — Manuale Utente

**Versione:** 1.0  
**Data:** 3 Maggio 2026  
**Progetto:** GeneForge AI — Notaio AI  
**Destinatari:** Notai, collaboratori e segretarie degli Studi Notarili

---

## 1. Introduzione

### Cos’è Notaio AI

**Notaio AI** è un pacchetto on-premise di agenti AI specializzati per la professione notarile italiana. Il sistema assiste il Notaio e i collaboratori nella stesura, verifica, conformità e gestione degli atti notarili.

Tutto gira su server locali. Nessun dato dei clienti lascia mai il tuo studio.

### A cosa serve

- **Stesura atti notarili** con agenti AI specializzati (compravendite, società, testamenti, mutui)
- **Verifica catastale** con report strutturati e checklist
- **Conformità urbanistica, edilizia e fiscale** con verifica agevolazioni
- **Controllo documenti** e coerenza dati prima del rogito
- **Cronoprogramma scadenze** con termini perentori calcolati automaticamente
- **Ricerca normativa** notarile, circolari CNN, giurisprudenza
- **Supporto firma digitale** InfoCert, Aruba, Namirial

### Vantaggi principali

| Vantaggio | Descrizione |
|-----------|-------------|
| **Privacy totale** | I modelli AI girano localmente. Nessun dato in cloud |
| **Risparmio di tempo** | Un atto di compravendita si genera in 2-3 minuti |
| **Zero errori formali** | Intestazione e firma pre-compilate dal codice, non dall'AI |
| **Conformità garantita** | Verifica automatica documenti, agevolazioni, scadenze |
| **Multi-formato** | PDF per la stampa, DOCX per le modifiche, MD per l'archivio |

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

## 4. Workflow Compravendita — Guida Passo-passo

### Panoramica del flusso

```
Inserimento dati → Verifica Catastale → Conformità → Stesura Atto → Controllo → Scadenze
```

### Passo 1 — Inserimento dati

1. Apri Notaio AI su `http://localhost:8507` (o `https://notaio-ai.geneforge.eu` se online)
2. Compila il form in 4 sezioni:
   - **Dati Venditore**: Nome, Cognome, CF, Nato a, Residente in
   - **Dati Acquirente**: Nome, Cognome, CF, Nato a, Residente in, Età, ISEE
   - **Dati Immobile**: Comune, Indirizzo, Foglio, Mappa, Sub, Categoria, Consistenza, Rendita
   - **Dati Economici**: Prezzo, Onorario Notaio, Clausole particolari

> 💡 **Suggerimento:** Seleziona il cliente dall'anagrafica (se disponibile) per pre-compilare i dati.

### Passo 2 — Generazione

1. Clicca su **"⚖️ Genera Atto di Compravendita"**
2. Il sistema esegue 5 fasi in sequenza:
   - **Fase 1/5: Verifica Catastale** (~15-20s)
   - **Fase 2/5: Verifica Conformità** (~50-70s)
   - **Fase 3/5: Stesura Atto** (~50-70s)
   - **Fase 4/5: Controllo Documenti** (~15-20s)
   - **Fase 5/5: Cronoprogramma Scadenze** (~15-20s)

3. Il documento completo apparirà nell'area risultato

### Passo 3 — Revisione

1. **Leggi il report catastale**: verifica che i dati siano coerenti con la visura reale
2. **Leggi il report conformità**: controlla i documenti mancanti evidenziati (es. APE, agibilità)
3. **Leggi l'atto**: verifica che il corpo giuridico sia corretto
4. **Leggi il controllo**: assicurati che tutti i documenti obbligatori siano presenti
5. **Leggi le scadenze**: verifica le date calcolate

> ⚠️ **Attenzione:** L'AI genera SOLO il corpo giuridico. Intestazione, procura e firma sono pre-compilate dal codice Python in modo deterministico.

### Passo 4 — Export

1. Clicca su **"📄 Scarica PDF"** per la stampa
2. Clicca su **"📄 Scarica DOCX"** per modifiche in Word/LibreOffice
3. Clicca su **"📧 Invia per Email"** per inviare al cliente

---

## 5. Esempio concreto: Prima Casa Under 36

> **Caso:** Laura Verdi, 28 anni, ISEE €22.000, acquista la sua prima casa da Mario Rossi per €180.000.
>
> **Agevolazione:** art. 1 commi 67-71 L. 234/2021 (prima casa under 36)
>
> 1. Inserisci i dati nel form
> 2. Clicca **"Genera Atto di Compravendita"**
> 3. Il sistema genera:
>    - Report catastale con checklist
>    - Report conformità che evidenzia APE mancante e verifica l'ammissibilità under 36
>    - Corpo giuridico con normativa citata
>    - Checklist documenti
>    - Cronoprogramma scadenze
> 4. Rivedi il documento
> 5. Scarica in PDF o DOCX

---

## 6. Verifica e Controllo Qualità

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

## 7. FAQ e Troubleshooting

### Domande frequenti

**D: I dati dei clienti finiscono su Internet?**
> R: **No.** Gli agenti AI girano sul tuo server locale. Nessun dato lascia il computer, eccetto le ricerche normative dove viene trasmesso *solo il testo della query*, mai dati delle pratiche.

**D: Posso usare il software senza connessione?**
> R: Sì per la stesura atti, verifica catastale (con placeholder), controllo documenti e scadenze. **No** per la ricerca normativa e la verifica via web, che richiedono Internet.

**D: Gli atti generati dall'AI hanno valore legale?**
> R: Sono **bozze professionali** generate da agenti AI specializzati, ma devono sempre essere **revisionati e sottoscritti** dal Notaio prima del rogito.

**D: L'AI inventa clausole o dati catastali?**
> R: I nostri agenti hanno regole ferree: non inventano mai. Se manca un dato, usano placeholder o indicano "da verificare".

**D: Quanti documenti posso generare?**
> R: Nel pacchetto **Base**: fino a 50/mese. **Professional**: fino a 200/mese. **Enterprise**: illimitati.

**D: Posso modificare un atto dopo la generazione?**
> R: Sì. Scaricalo in DOCX, modificalo in Word/LibreOffice, e caricalo nuovamente se necessario.

**D: Qual è il tempo medio di generazione?**
> R: 2-3 minuti per un atto di compravendita completo (5 fasi). La stesura dell'atto da sola richiede 50-70 secondi.

### Errori comuni e soluzioni

| Errore | Causa | Soluzione |
|--------|-------|-----------|
| "LLM non risponde" | Il servizio AI è spento | Verifica: `curl http://localhost:8081/health` |
| "Timeout generazione" | Nemtron sovraccarico | Aspetta 30 secondi e riprova |
| "Placeholder non sostituiti" | Dati mancanti nel form | Compila tutti i campi obbligatori |
| "Documento incompleto" | Campi obbligatori vuoti | Verifica Venditore, Acquirente, Comune, Prezzo |
| "Pagina bianca" | Browser datato | Aggiorna Chrome/Firefox |

---

## 8. Prezzi e Servizi Commerciali

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

## 9. Gli Agenti AI di Notaio AI — Dettaglio

### Panoramica

Notaio AI utilizza **7 agenti AI specializzati**, ciascuno con una propria identità, competenze e regole di comportamento. Il sistema sceglie automaticamente l'agente giusto per ogni compito.

### I 7 agenti

#### 📜 1. Attista
- **Ruolo:** Stesura di atti notarili
- **Modello:** Nemotron-70B
- **Temperatura:** 0.15 (molto conservativa)
- **Output:** Corpo giuridico con premesse, dispositive, clausole
- **Regole critiche:** Non inventa clausole, cita norma specifica, registro solenne

#### 🏠 2. Catasto
- **Ruolo:** Verifica dati catastali
- **Modello:** Nemotron-70B
- **Temperatura:** 0.1 (massima precisione)
- **Output:** Report con checklist e anomalie
- **Regole critiche:** Non inventa dati catastali, usa placeholder per verifiche esterne

#### ✅ 3. Conformità
- **Ruolo:** Conformità urbanistica, edilizia, fiscale
- **Modello:** Nemotron-70B
- **Temperatura:** 0.15
- **Output:** Report con documenti mancanti e agevolazioni
- **Regole critiche:** Non dà parere positivo assoluto se manca documentazione

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
*Versione 1.0 — 3 Maggio 2026*
