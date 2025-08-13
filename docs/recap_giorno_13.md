# Recap Giorno 13

## Obiettivo
Implementare lo scraping dei dati dei prodotti utilizzando Selenium con l'esecuzione di JavaScript.

## Attività completate

- **Scraping dei dati dei prodotti**:
    - Aggiunta la funzionalità per estrarre i dati dei prodotti, inclusi:
        - **Titolo**: Nome del prodotto.
        - **Città**: Località del prodotto.
        - **Provincia**: Codice della provincia.
        - **Prezzo**: Prezzo del prodotto.

- **Miglioramento della logica di scraping**:
    - Utilizzata l'esecuzione di JavaScript per una manipolazione più veloce del DOM.
    - Estratti gli elementi dinamicamente utilizzando `querySelector` e gestiti i dati mancanti con stringhe vuote di default.

- **Logging dei risultati**:
    - Aggiunto il logging per facilitare il debugging e monitorare i risultati dello scraping.

- **Gestione del WebDriver**:
    - Assicurata la chiusura corretta del browser tramite una funzione di teardown.

- **Miglioramento della gestione degli errori**:
    - Introdotti blocchi `try-except` per gestire gli errori durante il processo di scraping.
    - Aggiunta logica per verificare l'assenza di prodotti (`if not products`) e restituire un messaggio appropriato.
    - Spostata la logica di cleanup del browser (`teardown(driver)`) nel blocco `finally` per garantire il rilascio corretto delle risorse in tutti gli scenari.
    - Migliorato il logging per un debugging e monitoraggio più efficaci.
    - Garantito che le eccezioni durante la configurazione o il teardown del WebDriver vengano registrate e rilanciate se necessario.

## Risultato atteso

Al termine della giornata, il progetto include:

- Una logica di scraping ottimizzata per estrarre dati dinamici tramite Selenium e JavaScript.
- Un sistema di logging configurato per tracciare i risultati e facilitare il debugging.
- Una gestione robusta del WebDriver per garantire la chiusura corretta del browser.
- Una gestione degli errori migliorata per garantire la stabilità e la manutenibilità del codice.