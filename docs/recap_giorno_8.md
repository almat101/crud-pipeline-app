# Recap Giorno 8

## Obiettivo
Completare le funzionalità mancanti per il progetto, con particolare attenzione alla gestione del token JWT e alla protezione delle API del microservizio `products-service`. Migliorare l'integrazione tra frontend e backend.

## Attività previste

- **Completare la pagina di Login**:
  - Salvare il token JWT nel `localStorage` o `sessionStorage` dopo il login.
  - Mostrare un messaggio di errore in caso di credenziali errate.
  - Reindirizzare l'utente alla pagina dei prodotti dopo un login riuscito.

- **Creare la pagina Prodotti**:
  - Recuperare i prodotti dal microservizio `products-service` tramite una richiesta GET.
  - Includere il token JWT nell'header `Authorization` per autenticare la richiesta.
  - Mostrare i prodotti in una lista o tabella.
  - Implementare le funzionalità di aggiunta, modifica e cancellazione dei prodotti.

- **Implementare un middleware per il controllo del token JWT nel `products-service`**:
  - Verificare la validità del token JWT per ogni richiesta.
  - Restituire un errore 401 (Unauthorized) se il token è mancante o non valido.
  - Decodificare il token per ottenere l'ID utente e associarlo alle operazioni sui prodotti.

- **Migliorare la gestione del token JWT nel frontend**:
  - Creare una funzione centralizzata per includere automaticamente il token JWT nelle richieste HTTP.
  - Implementare un meccanismo di logout per eliminare il token JWT dal `localStorage` o `sessionStorage`.

- **Test e Debug**:
  - Testare tutte le funzionalità del frontend (Signup, Login, Prodotti).
  - Testare la protezione delle API del `products-service` con il middleware JWT.
  - Risolvere eventuali bug o problemi di integrazione.

## Prossimi passi

- [x] Completare la pagina di Login e salvare il token JWT.
- [x] Continuare la realizzazione della pagina Prodotti e testare l'accesso autenticato.
- [x] Implementare il middleware per il controllo del token JWT nel `products-service`.
- [x] Aggiunto bottone logout che svuola il localstorage.
- [ ] Migliorare la gestione del token JWT nel frontend.
- [ ] Testare e verificare tutte le funzionalità.

## Risultato atteso

Al termine della giornata, il progetto avrà:
- Una pagina di Login funzionante con salvataggio del token JWT.
- Una pagina Prodotti completa con accesso autenticato e funzionalità CRUD.
- Un middleware nel `products-service` per proteggere le API con il token JWT.
- Una gestione centralizzata del token JWT