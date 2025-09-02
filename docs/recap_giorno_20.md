# Recap Giorno 20

## Obiettivo
Automatizzare ulteriormente l’esecuzione della pipeline dati, rendendo il processo completamente schedulato e indipendente dall’intervento manuale.

## Checklist attività previste

- [x] **Automazione tramite cron**
      - Creare un nuovo container dedicato con `cron` installato.
      - All’avvio del container, il servizio cron effettuerà una chiamata HTTP all’endpoint `/orchestrate` dell’orchestrator-service per avviare la pipeline.
      - La chiamata verrà effettuata alla partenza del cron-service e poi ripetuta automaticamente ogni ora, garantendo l’esecuzione periodica e regolare della pipeline dati.

- [x] **Visualizzazione prodotti scraped su React**
      - Implementare la visualizzazione dei prodotti inseriti in PostgreSQL nella tabella `scraped_products` anche nell’interfaccia React.
      - Attualmente, su React visualizzo solo i prodotti su cui posso effettuare operazioni CRUD; sarà necessario aggiungere una sezione o una vista dedicata ai prodotti provenienti dalla pipeline di scraping e trasformazione.

- [ ] **Valutazione di Apache Airflow**
      - Valutare l’utilizzo di Apache Airflow per gestire la pipeline.
      - Airflow permetterebbe di creare workflow più robusti, monitorabili e professionali.
      - Potrei definire dipendenze tra task, gestire retry, logging avanzato e visualizzare lo stato delle esecuzioni tramite interfaccia web.

---

## Note
- L’obiettivo è rendere la pipeline dati completamente automatica e schedulata, pronta per ambienti di produzione.
- L’approccio con cron è semplice e immediato; Airflow rappresenta una possibile evoluzione verso una soluzione enterprise.
- L’integrazione della visualizzazione dei prodotti scraped su React migliorerà la trasparenza e l’usabilità del sistema.

---

**Con questo recap si apre la fase di automazione periodica e avanzata della pipeline dati, con attenzione anche alla visualizzazione dei