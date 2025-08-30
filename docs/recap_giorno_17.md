# Recap Giorno 17

## Obiettivo
Progettare e iniziare l’implementazione del microservizio `transformer-service`, responsabile della pulizia, normalizzazione e trasformazione dei dati raw provenienti da MongoDB, e del caricamento dei dati puliti in PostgreSQL.

## Guida e checklist per implementare `transformer-service`

### 1. **Setup del progetto**
- [x] Crea una nuova cartella/progetto per `transformer-service`.
- [x] Inizializza un ambiente Python dedicato (virtualenv/venv).
- [x] Installa le dipendenze principali:  
  - `pandas`  
  - `numpy`  
  - `pymongo` (per leggere da MongoDB)  
  - `sqlalchemy` e `psycopg2` (per scrivere su PostgreSQL)  
  - (opzionale) `fastapi` se vuoi esporre API di controllo.

### 2. **Connessione ai database**
- [x] Configura la connessione a MongoDB.

### 3. **Estrazione dei dati raw e caricamento in pandas**
- [x] Leggi i dati raw dalla collezione MongoDB (`raw_products`).
- [x] Carica i dati in un DataFrame Pandas per facilitarne la manipolazione.

### 4. **Pulizia e trasformazione dei dati**
- [x] Applica filtri sui titoli (es: solo prodotti che contengono "iphone 15").
- [x] Normalizza i campi testuali (es: lowercase, rimozione spazi, formattazione province/città).
- [x] Estrai e converti il prezzo in formato numerico.
- [x] Gestisci i campi mancanti o non validi.
- [x] Aggiungi/aggiorna eventuali campi utili (es: `shipping_available`, `price_not_specified`).

### 5 **Connessione a postgreSQL**
- [x] Configura la connessione a PostgreSQL ( eseguendo un semplice SELECT 1)

### 6. **Caricamento su PostgreSQL**
- [x] Definisci la struttura della tabella prodotti in PostgreSQL.
- [x] Usa SQLAlchemy per creare la connessione al database postgreSQL `create_engine(..)`
- [x] Scrivi i dati puliti dal DataFrame Pandas nella tabella con Pandas usando  `df.to_sql(..., if_exists='replace') la struttura viene creata automaticamente e rispecchia quella del DataFrame (quindi, dei dati MongoDB)`

### 7. **Testing e validazione**
- [x] Verifica che i dati puliti siano corretti e coerenti.
- [x] Esegui test di integrazione tra MongoDB e PostgreSQL.
(validazione manuale tramite log, print, e controlli diretti su MongoDB con mongosh e PostgreSQL con psql)

### 8. **Gestione errori di connessione a MongoDB e PostgreSQL**
- [x] Il programma gestisce correttamente errori se uno o entrambi i container sono spenti e quindi non raggiungibili.

### 9. **Automazione e scheduling**
- [ ] (Opzionale) Prepara uno script o una funzione schedulabile per eseguire periodicamente la trasformazione.

---

## Note aggiuntive
- Documenta bene ogni funzione con docstring.
- Prepara log e gestione degli errori per ogni fase.
- Mantieni la pipeline modulare per facilitare futuri miglioramenti.

---

**Questa checklist ti guiderà passo passo nella realizzazione di un microservizio transformer-service robusto, scalabile e facilmente