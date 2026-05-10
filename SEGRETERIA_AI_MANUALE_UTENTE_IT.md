# Manuale Utente - Segreteria AI On-Premise
**Versione:** 2.0  
**Data:** 10 Maggio 2026  
**Prodotto:** GeneForge Segreteria AI Multi-Channel  
**Studio:** Studio Legale Della Luna, Novi Ligure (AL)

---

## 1. Introduzione

La **Segreteria AI** è un assistente virtuale intelligente che gestisce le comunicazioni in entrata dello Studio Legale Della Luna su tre canali:

- **Telefono** — risponde alle chiamate, prenota appuntamenti, fornisce informazioni
- **WhatsApp** — risponde ai messaggi, invia conferme e promemoria
- **Email** — legge le email in arrivo e risponde automaticamente

Il sistema è completamente **on-premise** (tutti i dati restano nel vostro server) e utilizza intelligenza artificiale locale per garantire massima privacy e conformità al segreto professionale.

---

## 2. Come Funziona

### 2.1 Telefono

Quando un cliente chiama lo studio:

1. L'AI risponde con un saluto professionale
2. Ascolta la richiesta del cliente
3. Capisce l'intento (prenotazione, informazioni, urgenza...)
4. Risponde o prende l'appuntamento
5. Se necessario, trasferisce alla segreteria umana

**Esempio di conversazione:**

> **AI:** "Buongiorno, Studio Legale Della Luna. Sono l'assistente virtuale. Come posso aiutarla?"
>
> **Cliente:** "Vorrei fissare un appuntamento per la prossima settimana."
>
> **AI:** "Certamente. Per quale servizio ha bisogno? Offriamo consulenza generale, consulenza strategica, redazione atti, udienze e mediazioni."
>
> **Cliente:** "Una consulenza generale."
>
> **AI:** "Perfetto. Ho trovato questi slot disponibili per martedì prossimo: 9:00, 10:30, 15:00. Quale preferisce?"
>
> **Cliente:** "Le 10:30."
>
> **AI:** "Appuntamento confermato! Martedì alle 10:30 per consulenza generale. Le invierò una conferma via WhatsApp. A presto!"

### 2.2 WhatsApp

I clienti possono scrivere allo studio su WhatsApp:

- **Comandi rapidi**: il sistema riconosce automaticamente richieste di appuntamento, informazioni, urgenze
- **Conferme**: dopo ogni prenotazione, l'invio di una conferma con tutti i dettagli
- **Promemoria**: 24 ore prima dell'appuntamento, un promemoria automatico
- **Documenti**: i clienti possono inviare documenti che vengono archiviati automaticamente

**Esempi di messaggi che l'AI capisce:**
- "Vorrei prenotare un appuntamento"
- "Posso spostare l'appuntamento di domani?"
- "A che ora apre lo studio?"
- "Ho bisogno di parlare con l'avvocato urgentemente"
- "Cancello l'appuntamento del 15"

### 2.3 Email

L'AI controlla periodicamente le caselle di posta:

- **info@studiolegaledellaluna.it** — per richieste generali
- **segreteria@studiolegaledellaluna.it** — per appuntamenti e pratiche

Per ogni email ricevuta:
1. Legge il contenuto
2. Classifica l'intento
3. Risponde automaticamente (conferme, informazioni, inoltro)
4. Per email complesse o urgenti, inoltra alla segreteria umana

---

## 3. Dashboard Web

La **Dashboard** è accessibile dal browser all'indirizzo fornito dallo staff tecnico (es. `https://segreteria.studiolegaledellaluna.it`).

### 3.1 Login

Usare le credenziali fornite dallo staff di GeneForge.

### 3.2 Pagina Overview

La pagina principale mostra:
- **Appuntamenti di oggi** — quanti e chi
- **Appuntamenti questa settimana**
- **Totali confermati**
- **Cancellazioni**
- **Distribuzione per canale** (telefono, WhatsApp, email)

### 3.3 Pagina Appuntamenti

Qui potete:
- Vedere tutti gli appuntamenti in una tabella
- Cercare per nome cliente
- Modificare data/ora di un appuntamento
- Cancellare un appuntamento
- Aggiungere note

**Per modificare un appuntamento:**
1. Cercare il cliente nella tabella
2. Cliccare su "Modifica"
3. Cambiare data o ora
4. Salvare

Il sistema invierà automaticamente una notifica al cliente.

### 3.4 Pagina Analytics

Grafici e statistiche:
- Appuntamenti per canale
- Appuntamenti per tipo di servizio
- Andamento nel tempo

### 3.5 Pagina System Health

Stato del sistema in tempo reale:
- Asterisk (telefono)
- STT (riconoscimento vocale)
- TTS (sintesi vocale)
- LLM (intelligenza artificiale)
- WhatsApp Gateway
- Email Gateway

Tutto verde = sistema funzionante.

### 3.6 Pagina Configurazione

Qui potete modificare:
- **Orari di apertura** dello studio
- **Regole appuntamenti** (durata, buffer, anticipo minimo)
- **Canali notifiche** attivi

**Attenzione**: le modifiche richiedono un riavvio del sistema. Contattare lo staff tecnico.

---

## 4. Regole di Utilizzo

### 4.1 Orari di Apertura

Lo studio è aperto:
- **Lunedì-Venerdì**: 9:00-13:00 / 15:00-19:00
- **Sabato-Domenica**: chiuso

L'AI risponde **24 ore su 24, 7 giorni su 7**, ma:
- Fuori orario: informa il cliente e prende nota
- In orario: gestisce appuntamenti e informazioni

### 4.2 Tipi di Servizio

| Servizio | Durata | Descrizione |
|----------|--------|-------------|
| Consulenza Generale | 30 min | Primo colloquio, informazioni |
| Consulenza Strategica | 60 min | Analisi approfondita |
| Redazione Atto | 60 min | Atti, contratti, ricorsi |
| Udienza | 120 min | Appuntamenti in tribunale |
| Mediazione | 90 min | Incontri di mediazione |
| Primo Colloquio | 45 min | Conoscenza iniziale |
| Revisione Contratto | 60 min | Analisi contratti |

### 4.3 Limiti del Sistema

L'AI è progettata per gestire:
- ✅ Prenotazione, modifica e cancellazione appuntamenti
- ✅ Informazioni generali sullo studio
- ✅ Inoltro di richieste urgenti alla segreteria
- ✅ Risposta a domande frequenti

L'AI **NON** può:
- ❌ Fornire pareri legali
- ❌ Accedere a pratiche esistenti senza autorizzazione
- ❌ Gestire casi complessi senza supervisione umana

**Per qualsiasi parere legale, l'AI trasferisce sempre alla segreteria umana.**

---

## 5. Come Contattare il Supporto

Se il sistema non funziona correttamente:

1. **Verificare la Dashboard** — pagina System Health
2. **Controllare i Log** — pagina Logs per errori recenti
3. **Contattare GeneForge**:
   - Email: support@geneforge.eu
   - Telefono: +39 0143 123456
   - Orari supporto: lun-ven 9:00-18:00

### 5.1 Problemi Comuni

| Problema | Soluzione |
|----------|-----------|
| L'AI non risponde al telefono | Verificare che Asterisk sia attivo (System Health) |
| Non arrivano messaggi WhatsApp | Verificare stato WhatsApp Gateway |
| Email non lette | Verificare configurazione IMAP |
| Dashboard non carica | Verificare connessione internet e Cloudflare Tunnel |
| Slot orari sbagliati | Verificare orari di apertura in Configurazione |

---

## 6. Sicurezza e Privacy

- Tutti i dati rimangono **nel vostro server** (on-premise)
- Nessun dato viene inviato a cloud esterni (eccetto WhatsApp Business API)
- Le chiamate telefoniche vengono trattate in locale
- Le conversazioni sono loggate per migliorare il servizio
- Accesso alla Dashboard protetto da password

---

## 7. Glossario

| Termine | Significato |
|---------|-------------|
| AI | Intelligenza Artificiale |
| STT | Speech-to-Text (voce → testo) |
| TTS | Text-to-Speech (testo → voce) |
| LLM | Large Language Model (modello linguistico) |
| IMAP | Protocollo per leggere email |
| SMTP | Protocollo per inviare email |
| SIP | Protocollo per telefonate VoIP |
| RAG | Retrieval-Augmented Generation (ricerca documenti) |

---

**GeneForge AI Team**  
10 Maggio 2026
