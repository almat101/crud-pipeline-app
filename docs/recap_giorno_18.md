# Recap Giorno 18

## Obiettivo
Automatizzare l’intera pipeline dati tramite containerizzazione e orchestrazione, così da poter eseguire in modo automatico sia lo scraping che la trasformazione dei dati.

## Attività svolte

### 1. **Containerizzazione dei microservizi**
- [x] Creato un `Dockerfile` per il microservizio `scraper-service`.
- [x] Creato un `Dockerfile` per il microservizio `transformer-service`.

### 2. **Orchestrazione con Docker Compose**
- [x] Creati i servizi `scraper-service` e `transformer-service` all’interno del file `docker-compose.yml`, insieme ai servizi per MongoDB e PostgreSQL.
- [x] Gestite le variabili d’ambiente tramite il file `.env`.

### 3. **Automazione della pipeline (stato attuale)**
- [x] La pipeline è completamente containerizzata e funzionante: posso avviare tutti i servizi con Docker Compose.
- [x] L’esecuzione della pipeline è però ancora **manuale**: devo chiamare io gli endpoint dei microservizi (`scraper-service` e `transformer-service`) per avviare rispettivamente lo scraping e la trasformazione/caricamento dei dati.

### 4. **Prossimi step: orchestrazione automatica**
- [ ] Creare un nuovo microservizio che fungerà da orchestratore della pipeline.
    - Questo servizio si occuperà di chiamare automaticamente gli endpoint dei microservizi nell’ordine corretto, gestendo il flusso end-to-end senza intervento manuale.
    - Valutare se implementare l’orchestratore come microservizio FastAPI, script Python, o altro strumento di workflow.

---

## Note
- L’obiettivo resta avere una pipeline completamente automatizzata e ripetibile, lanciabile con un solo comando o una singola chiamata.
- In questa fase ho risolto tutte le problematiche di containerizzazione e orchestrazione base, ma la gestione del flusso è ancora manuale.
- Il prossimo passo sarà fondamentale per rendere la pipeline davvero scalabile, automatica e pronta per la produzione.

---

**Questo recap documenta il completamento della containerizzazione e orchestrazione manuale della pipeline dati, e introduce il prossimo step: la realizzazione di un orchestratore