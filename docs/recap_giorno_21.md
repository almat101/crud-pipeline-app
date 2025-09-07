# Recap Giorno 21

## Obiettivo
Modificare la pipeline dati introducendo una maggiore flessibilità e scalabilità tramite l’uso di parametri dinamici e query string.
Modificato il frontend con l’introduzione di un bottone che consente di avviare lo scraping, permettendo all’utente di cercare i prodotti in modo interattivo tramite un form (per il nome prodotto) e un menu a tendina (per la categoria), invece che in modo hardcoded come prima.

## Modifiche principali

- **Endpoint Scraper aggiornato**
  - L’endpoint `/scrape/{category}/` ora accetta sia un path parameter (`category`) sia una query string (`q`), permettendo ricerche più flessibili e dinamiche.
  - Viene così simulata la stessa ricerca che avviene su subito.it, ad esempio:
    - `"https://www.subito.it/annunci-italia/vendita/informatica/?q=thinkpad+t14"`
    - `"https://www.subito.it/annunci-italia/vendita/{category}/?q={q}"`
  - Esempio di chiamata all’API:
    - `GET /scrape/informatica/?q=iphone%2015`

  - **Modifica:** Lo scraper-service ora accetta `/scrape/{category}` come path parameter e una query string `q`.

- **Endpoint Transformer aggiornato**
  - Anche il transformer-service è stato modificato per accettare la query string `q` (ad esempio: `/transform?q=iphone%2015`), senza path parameter.

- **Orchestrator aggiornato**
  - L’orchestrator ora gestisce sia il path parameter `category` che la query string `q`, inoltrando questi parametri sia allo scraper-service che al transformer-service per mantenere coerenza nella pipeline.

- **Aggiornamento configurazione Nginx**
  - Ho aggiornato il file di configurazione di Nginx aggiungendo tutti i servizi della pipeline (scraper, transformer, orchestrator) che prima non erano presenti, così da permettere il corretto routing delle richieste verso tutti i microservizi.

- **Aggiornamento docker-compose.dev.yml**
  - Ho sistemato il `docker-compose.dev.yml` per includere anche l’hot reload dei microservizi della pipeline.
  - Ora i servizi partono con un comando specifico nel `docker-compose.dev.yml`, ovvero `uvicorn main:app --host 0.0.0.0 --port 30x0 --reload`, che sovrascrive il comando predefinito del Dockerfile. Questo facilita lo sviluppo e il testing grazie all’hot reload automatico delle modifiche al codice.

- **Aggiunta bottone frontend per avvio scraping**
  - È stato creato un bottone sul frontend che permette all’utente di avviare manualmente la pipeline di scraping.
  - Il bottone apre un form dove l’utente può inserire il nome del prodotto da cercare.
  - È stato aggiunto anche un menu a tendina per selezionare la categoria tra quelle disponibili.
  - Alla conferma, il frontend invia una richiesta all’orchestrator (endpoint `/scrape/{category}/?q=prodotto`), avviando così il processo di scraping in modo dinamico e personalizzato.

- **Aggiunta del supporto CORS nei backend FastAPI**
  - È stato aggiunto il middleware CORS all’interno dei microservizi FASTAPI scraper, transformer e orchestrator, permettendo così al frontend di comunicare correttamente con tutti i microservizi della pipeline anche da domini diversi.

## Checklist attività previste

- [x] Refactoring endpoint scraper per supportare path parameter e query string.
- [x] Modifica transformer-service per accettare la query string `q`.
- [x] Aggiornamento orchestrator per gestire il path param `category` e query string e passarli ai servizi downstream.
- [x] Aggiornamento della configurazione Nginx per includere tutti i servizi della pipeline.
- [x] Aggiornamento di docker-compose.dev.yml per garantire l'hot reload dei microservizi scraper, trasformer, orchestrator.
- [x] Creazione di un bottone e form frontend per avviare manualmente la pipeline di scraping.
- [x] Aggiunta del supporto CORS nei backend FastAPI (scraper, transformer, orchestrator).
