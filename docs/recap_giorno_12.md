# Recap Giorno 12

## Obiettivo
Aggiungere un endpoint basato su Selenium per lo scraping dei dati utilizzando **FastAPI**.

## Attività completate

- **Implementazione dell'endpoint `/scrape`**:
    - Creato un endpoint utilizzando FastAPI e Selenium, basato sulla documentazione ufficiale di Selenium.
    - Aggiunta la funzionalità per interagire con un form Web **come da esempio della documentazione ufficiale**:
        - Navigazione verso l'URL target.
        - Compilazione di un campo di input e invio del modulo.
        - Recupero e restituzione del messaggio visualizzato dopo l'invio.

- **Configurazione del logging**:
    - Configurato il logging per migliorare il debugging e il monitoraggio.

- **Aggiunta di funzioni helper**:
    - Implementate funzioni per l'inizializzazione (`setup`) e la chiusura (`teardown`) del WebDriver.

## Risultato atteso

Al termine della giornata, il progetto include:

- Un endpoint `/scrape` funzionante per lo scraping dei dati tramite Selenium.
- Un sistema di logging configurato per tracciare gli eventi e facilitare il debugging.
- Funzioni helper per gestire l'inizializzazione e la chiusura del WebDriver in