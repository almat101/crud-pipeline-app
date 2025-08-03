# Recap Giorno 7

## Obiettivo
Implementare una base di frontend per interagire con i microservizi `auth-service` e `products-service`. Creare pagine per la registrazione, il login e la visualizzazione dei prodotti.

## Attività previste

- **Setup del progetto frontend**:
  - Creare una nuova cartella `frontend/` per il progetto.
  - Inizializzare il progetto con `npx create-react-app . ` e installare le dipendenze necessarie:
    - Librerie consigliate: `axios` per le richieste HTTP, `dotenv` per la configurazione.
    - Framework opzionale: `React`

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
- [ ] Installare dipendenze necessarie
- [ ] Implementare la pagina di Signup con validazione lato client.
- [ ] Implementare la pagina di Login e salvare il token JWT.
- [ ] Creare la pagina Prodotti e testare l'accesso autenticato.
- [ ] Collegare il frontend ai microservizi `auth-service` e `products-service`.

## Risultato atteso

Al termine della giornata, il progetto avrà un frontend funzionante con:
- Pagine per Signup, Login e Prodotti.
- Integrazione con i microservizi per autenticazione e gestione dei prodotti.
- Gestione del token JWT