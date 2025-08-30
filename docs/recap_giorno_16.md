# Recap Giorno 16

## Obiettivo
Riorganizzare l’architettura del progetto per garantire l’immutabilità dei dati raccolti dallo scraper e separare le responsabilità tra scraping e trasformazione/cleaning dei dati.

## Pipeline dati: Extract-Load-Transform-Load (ELTL) vs ETL

Sto strutturando una pipeline dati secondo il paradigma **ELTL (Extract, Load, Transform, Load)**, una variante moderna rispetto al classico ETL:

- **ETL (Extract, Transform, Load):**  
  I dati vengono estratti, trasformati subito e poi caricati nel database finale.  
  Questo approccio non conserva i dati raw e rende più difficile rielaborare i dati se cambiano le regole di cleaning.

- **ELTL (Extract, Load, Transform, Load):**  
  I dati vengono prima estratti e caricati **grezzi** (raw) in un database (nel mio caso MongoDB), mantenendo così l’immutabilità e la tracciabilità.  
  Successivamente, un microservizio dedicato (`transformer-service`) legge i dati raw, li trasforma (cleaning, normalizzazione, filtri) e li carica in un database strutturato (PostgreSQL).  
  Questo approccio è più moderno e flessibile: permette di conservare sempre i dati originali, di aggiornare la logica di cleaning senza riscraping, e di scalare facilmente ogni fase della pipeline.

Questa architettura è ideale per progetti di data engineering, data analytics e machine learning, perché permette di:
- Conservare sempre i dati originali per eventuali rielaborazioni o audit.
- Aggiornare o migliorare la logica di trasformazione senza dover riscrapare i dati.
- Scalare e manutenere facilmente ogni fase della pipeline.

## Attività completate e migliorie apportate

1. **Rinominato il microservizio di scraping**
   - Il servizio FastAPI dedicato allo scraping è stato rinominato in `scraper-service` per riflettere meglio il suo ruolo specifico di raccolta dati grezzi.

2. **Immutabilità dei dati raccolti**
   - Lo scraper ora salva su MongoDB i dati esattamente come vengono estratti dal sito, senza alcuna logica di pulizia, normalizzazione o filtro. Questo garantisce la tracciabilità e la possibilità di riutilizzare i dati grezzi per future elaborazioni.

3. **Separazione delle responsabilità**
   - Tutta la logica di cleaning, normalizzazione e filtraggio verrà implementata in un futuro microservizio chiamato `transformer-service`, che utilizzerà strumenti come Pandas e Numpy per processare i dati raw e salvarli in PostgreSQL.

4. **Migliorie tecniche apportate**
   - Aggiunte le Chrome options al webdriver per eseguire lo scraping in modalità headless (senza apertura della finestra del browser).
   - Impostato uno user-agent reale e una dimensione finestra standard per ridurre il rischio di blocco anti-bot.
   - Commentate e documentate opzioni aggiuntive (`--no-sandbox`, `--disable-dev-shm-usage`, `--disable-blink-features=AutomationControlled`) per una futura esecuzione stabile in ambienti Docker o CI/CD.
   - Migliorata la documentazione interna tramite docstring e commenti esplicativi.

### Esempio di documento raw salvato in mongodb

```json
{
  "_id": ObjectId('689f0033db2204130ffb4d4a'),
  "title": "Iphone 15 PRO max 256GB",
  "city": "Cornaredo",
  "province": "(MI)",
  "price": "500€ Spedizione disponibile",
  "date_scraped": ISODate('2025-08-16T00:37:03.765Z'),
  "url": "https://www.subito.it/..."
}