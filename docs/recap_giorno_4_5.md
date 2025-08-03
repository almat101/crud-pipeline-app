# Recap Giorno 4 e 5

## Obiettivo
Implementare la connessione al database PostgreSQL e gestire le operazioni CRUD di base tramite Express e la libreria `pg`.

## Attività svolte

- **Configurazione ambiente**:  
  - Creato file `.env` per gestire le variabili di connessione al database.
  - Utilizzato `dotenv` per caricare le variabili d’ambiente.

- **Connessione a PostgreSQL**:  
  - Importata la libreria `pg` e configurato il `Pool` per la gestione delle connessioni.
  - Testata la connessione con una query di base tramite `pool.query`.

- **Implementazione CRUD**:  
  - Creato il file `products.js` con le rotte Express per gestire prodotti.
  - Implementate le rotte:
    - `GET /api/products` per recuperare tutti i prodotti.
    - `GET /api/products/:id` per recuperare un prodotto specifico.
    - `POST /api/products` per creare un nuovo prodotto.
    - `PATCH /api/products/:id` per aggiornare un prodotto.
    - `DELETE /api/products/:id` per cancellare un prodotto.
  - Gestione degli errori e delle risposte HTTP appropriate.

- **Validazione dati**:  
  - Aggiunti controlli sui parametri ricevuti (es. id numerico, campi obbligatori).

## Risultato

Il backend ora è in grado di interagire con PostgreSQL tramite chiamate asincrone con `pool.query`, gestendo tutte le operazioni CRUD sui prodotti in modo sicuro