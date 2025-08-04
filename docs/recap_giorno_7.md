# Recap Giorno 7

## Obiettivo
Implementare una base di frontend per interagire con i microservizi `auth-service` e `products-service`. Creare pagine per la registrazione, il login e la visualizzazione dei prodotti.

## Attività previste

- **Setup del progetto frontend**:
  - Creare una nuova cartella `frontend/` per il progetto.
  - Inizializzare il progetto con `npx create-react-app . ` e installare le dipendenze necessarie:
    - Librerie consigliate:
      - `axios` per le richieste HTTP
      - ~~`dotenv`~~ i file .env vengono gestiti da create-react-app usando questa sintassi `REACT_APP_NOME=valore`.
      - `react-router-dom`: Per la gestione delle pagine/rotte (Login, Signup, Prodotti...).
      - `jwt-decode`: Se vuoi leggere dati dal token JWT sul frontend (ad esempio per sapere l’ID utente loggato).
    
- **Creazione delle pagine principali**:
  - **Pagina di Signup**:
    - Form con campi: `username`, `email`, `password`, `repeat_password`.
    - Inviare i dati al microservizio `auth-service` tramite una richiesta POST a `/signup`.
    - Mostrare messaggi di successo o errore.
  - **Pagina di Login**:
    - Form con campi: `email`, `password`.
    - Inviare i dati al microservizio `auth-service` tramite una richiesta POST a `/login`.
    - Salvare il token JWT nel `localStorage` o `sessionStorage`.
  - **Pagina Prodotti**:
    - Recuperare i prodotti dal microservizio `products-service` tramite una richiesta GET.
    - Includere il token JWT nell'header `Authorization` per autenticare la richiesta.
    - Mostrare i prodotti in una lista o tabella.

- **Gestione del token JWT**:
  - Salvare il token JWT dopo il login.
  - Includere automaticamente il token nelle richieste HTTP verso i microservizi.
  - Implementare un semplice meccanismo di logout eliminando il token.

## Prossimi passi

- [x] Creare la struttura base del progetto frontend.
- [x] Installare dipendenze necessarie
- [x] Abilitare CORS
- [x] Implementare la pagina di Signup con validazione lato client.
- [x] Collegare il frontend ai microservizi `auth-service` e `products-service`.
- [x] Creare dockerfile per frontend e backend
- [x] Creare Nginx e configurarlo per usarlo come reverse-proxy per collegare frontend con il backend
## Risultato atteso

Al termine della giornata, il progetto avrà un frontend funzionante con:
- Pagine per Signup, Login e Prodotti.
- Integrazione con i microservizi per autenticazione e gestione dei prodotti.
- Gestione del token JWT