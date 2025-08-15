# Recap Giorno 14

## Obiettivo
Inserire i dati grezzi (raw data) ottenuti dallo scraper nel database MongoDB in modalità locale.

## Attività completate

- **Connessione a MongoDB**:
    - Configurata la connessione a un'istanza locale di MongoDB utilizzando la libreria `pymongo`.
    - Verificata la connessione al database `scraping_db` e alla collezione `products`.

- **Inserimento dei dati nel database**:
    - Implementata la logica per salvare i dati scansionati (risultato JSON dello scraper) nel database MongoDB.
    - ~~Utilizzato il metodo `insert_many` per inserire tutti i prodotti in un'unica operazione.~~
  
    - Utilizzato il metodo `update_one` per inserire un prodotto alla volta e implementata una pulizia dei dati basilare prima di inserirli nel db.
    Il metodo `update_one` accetta un filtro per trovare il documento da aggiornare, un dizionario di aggiornamento (spesso con l'operatore `$set` per modificare solo i campi specificati) e il parametro opzionale `upsert` che, se True, crea il documento se non esiste già. `$set` serve ad aggiornare o aggiungere solo i campi indicati senza sovrascrivere l'intero documento.

- **Gestione degli errori**:
    - Aggiunto un blocco `try-except` per gestire eventuali errori durante l'inserimento dei dati nel database.
    - Log degli errori configurato per facilitare il debugging in caso di problemi.

- **Verifica dei dati salvati**:
    - Utilizzato il client MongoDB (`mongosh`) per verificare che i dati siano stati salvati correttamente nella collezione `raw_products`.

## Risultato atteso

Al termine della giornata, il progetto include:

- Una connessione stabile e funzionante a un'istanza locale di MongoDB.
- La possibilità di salvare i dati scansionati  dallo scraper e successivamente puliti nel database MongoDB.
- Una gestione robusta degli errori durante il processo di salvataggio.
- Dati verificati e correttamente salvati nella collezione `raw_products` del db.
- Aggiunta documentazione di base per fast_api e mongo con qualche comando per mongosh.