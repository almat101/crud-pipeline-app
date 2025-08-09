# Recap Giorno 9

## Obiettivo
Completare le attività rimaste in sospeso dal giorno 8, con particolare attenzione alla gestione del token JWT nel frontend e alla risoluzione del problema del refresh della pagina prodotti.

## Attività previste

- **Migliorare la gestione del token JWT nel frontend**:

    - Implementare una soluzione per garantire che il token JWT sia sempre disponibile e utilizzabile senza dover ricaricare manualmente la pagina prodotti.
    - Valutare e scegliere tra:
        - Creare un servizio centralizzato per gestire il token.
        - Configurare un interceptor Axios per automatizzare l'invio del token nelle richieste HTTP.
        - Utilizzare uno stato globale (ad esempio, React Context o Redux) per sincronizzare il token tra i componenti.

- **Test e Debug**:

    - Testare la pagina prodotti per verificare che il token venga inviato correttamente e che il problema del refresh sia risolto.
    - Assicurarsi che il middleware nel backend gestisca correttamente i token JWT e restituisca un errore 401 Unauthorized in caso di token mancante o non valido.
    
- **Ottimizzare il flusso di autenticazione**:

    - Garantire che il login reindirizzi correttamente alla pagina prodotti solo dopo che il token è stato salvato.
    - Verificare che il logout svuoti correttamente il localStorage e reindirizzi alla pagina di login.

## Prossimi passi
- [x] Creazione di uno stato globale con react Context per gestire il token
- [x] Risolvere il problema del refresh della pagina prodotti.
- [x] Configurazione di un interceptor axios che aggiunge il token JWT ad ogni richiesta che necessita autenticazione.
- [x] Implementare una gestione centralizzata del token JWT nel frontend.
- [x] Testare e verificare tutte le funzionalità del frontend e del backend.
- [X] Creazione di un file docker-compose.dev.yml per lo sviluppo locale, configurato per abilitare l'hot reload grazie al montaggio dei volumi. La directory /app è montata all'interno dei container, consentendo di applicare automaticamente le modifiche al codice senza dover ricostruire manualmente le immagini Docker ogni volta.

## Risultato atteso

Al termine della giornata, il progetto avrà:

- Una gestione migliorata del token JWT nel frontend.
Una soluzione per evitare il refresh manuale della pagina prodotti.
- Un flusso di autenticazione più fluido e affidabile.
- La creazione dell'interceptor ha reso superfluo l'uso dello stato globale