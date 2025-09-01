# Recap Giorno 19

## Obiettivo
Completare l’automazione della pipeline dati tramite la realizzazione di un microservizio orchestratore, in modo da gestire l’intero flusso end-to-end senza intervento manuale.

## Attività svolte

### 1. **Creazione del microservizio orchestrator**
- [x] Creato un nuovo microservizio `orchestrator-service` utilizzando FastAPI.
- [x] Implementato un endpoint `/orchestrate` che, quando chiamato, esegue in sequenza:
    - Una richiesta al microservizio `scraper-service` per avviare lo scraping e il salvataggio dei dati raw su MongoDB.
    - Una richiesta al microservizio `transformer-service` per avviare la trasformazione e il caricamento dei dati puliti su PostgreSQL.
- [x] Gestita la comunicazione tra i servizi tramite chiamate HTTP, utilizzando i nomi dei servizi Docker Compose per garantire la corretta risoluzione tra container.
- [x] Implementata una gestione degli errori dettagliata, che permette di sapere esattamente quale servizio ha fallito e perché.


### 2. **Prossimi step: scelta se creazione cron, automazione con compose, sistemazione healthcheck dei servizi nel compose**
- Valutare la possibilità di **automatizzare l’esecuzione periodica della pipeline** tramite uno scheduler:
    - Utilizzo di `cron` all’interno di uno dei container o direttamente sull’host per chiamare periodicamente l’endpoint `/orchestrate` dell’orchestrator-service.
    - In alternativa, valutare l’uso di strumenti di orchestrazione più avanzati (es. Apache Airflow, Prefect) per gestire la schedulazione e il monitoraggio dei job.
- Considerare l’automazione tramite **Docker Compose**:
    - Analizzare se è possibile sfruttare le dipendenze tra servizi (`depends_on`) e i comandi di avvio per rendere ancora più fluido il flusso di esecuzione all’interno dello stack Compose.
    - Integrare eventuali script di startup o entrypoint personalizzati per avviare la pipeline in modo automatico al deploy.
- **Migliorare i healthcheck dei servizi** nel file `docker-compose.yml`

### 3. **Risultato**
- Ora l’intera pipeline può essere eseguita automaticamente chiamando un solo endpoint (`/orchestrate`) dell’orchestrator-service.
- L’automazione è completamente integrata nella struttura a microservizi e containerizzata.

---

## Note
- Questo step rappresenta il completamento della pipeline dati automatizzata, pronta per essere lanciata e monitorata in modo semplice e ripetibile.
- Eventuali miglioramenti futuri potranno riguardare la schedulazione automatica, il monitoraggio avanzato o l’integrazione con strumenti di workflow più complessi.

---

**Con questo recap si conclude la fase di automazione della pipeline dati tramite orchestrazione