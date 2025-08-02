# Recap Giorno 6

## Obiettivo
Separare il microservizio prodotti in una propria cartella e iniziare la progettazione del microservizio di autenticazione (auth service).

## Attività svolte

- **Refactoring struttura progetto**:  
  - Creato la cartella `products/` dedicata al microservizio prodotti.
  - Spostati all’interno della cartella tutti i file relativi al servizio prodotti: `server.js`, script di inizializzazione del database, `package.json`, `node_modules`, ecc.
  - Ogni microservizio ora ha la propria struttura indipendente e può essere gestito separatamente.

- **Preparazione auth service**:  
  - Avviata la creazione della cartella `auth-service/` per il microservizio di autenticazione.
  - Prevista l’inizializzazione di un nuovo progetto Express dedicato all’auth service.
  - In programma la creazione dello scheletro base:  
    - Installazione delle dipendenze (`express`, `pg`, `helmet`, `morgan`, `dotenv`)
    - Installazione di nodemod come dev-dependency con:
    ```sh
    npm install --save-dev nodemon
    ```
    - Configurazione del database utenti
    - Preparazione degli script di inizializzazione delle tabelle utenti

## Prossimi passi

- [x] Completare lo scheletro del microservizio di autenticazione.
- [x] Suddividere il microservizio auth-service in routes,controllers per rendere il progetto modulare e ampliabile in futuro
- [x] Testare le prime rotte per la registrazione e il login con dei console.log
- [x] Implementare per la rotta /signup la validazione del body con libreria `joi`
- [x] Implementare l'hashing della password con `bcrypt`
- [x] Implementare una query preventiva per controllare che non esista un utente con lo stesso user e/o email associato
- [x] Eseguire la query per salvare username,email,password_hastata nel db
- [ ] Implementare la rotta /login 
- [ ] Integrare la generazione e la validazione dei JWT per la protezione delle API.

## Risultato

La struttura del progetto ora è pronta per gestire più microservizi in modo modulare e scalabile. Il microservizio prodotti è stato isolato e si sta avviando la base per il microservizio auth.