## **1\. Cos'è FastAPI?**

FastAPI è un **framework web per Python** per creare API ad alte prestazioni in modo rapido. È stato progettato per essere intuitivo e veloce sia da usare che da imparare.

Le sue caratteristiche principali, che lo rendono molto attraente per chi viene da Express, sono:

* **Velocità:** È uno dei framework Python più veloci, con performance paragonabili a Node.js e Go, grazie all'uso di **Starlette** e **Uvicorn** (il suo server ASGI).  
* **Digressione da Node.js:** Node.js è un runtime, Express è un framework che ci gira sopra. In Python, il linguaggio stesso ha un focus maggiore sull'efficienza e le librerie come **Starlette** e **Pydantic** offrono una base molto solida per FastAPI.  
* **Tipizzazione (Type Hints):** Utilizza le annotazioni di tipo di Python. Questo permette agli editor di testo di darti un ottimo autocompletamento e di rilevare errori prima ancora che tu esegua il codice.  
* **Validazione automatica dei dati:** Grazie a **Pydantic**, FastAPI valida automaticamente i dati in entrata (sia dai parametri di percorso che dal body della richiesta). Non devi scrivere codice boilerplate per verificare che una stringa sia una stringa o un numero sia un numero.  
* **Documentazione automatica:** Genera in automatico una documentazione interattiva per la tua API (con Swagger UI e ReDoc), senza che tu debba scrivere una riga di codice in più. È una cosa che in Express richiederebbe librerie esterne e configurazione manuale.

## **2\. Punti in comune con Express**

Molti dei concetti fondamentali che conosci in Express si ritrovano in FastAPI.

* **Routing:** Come in Express, definisci gli "endpoint" della tua API usando decoratori (@app.get(), @app.post(), ecc.) e associandoli a una funzione.  
* **Middleware:** Entrambi i framework supportano il concetto di middleware per eseguire codice prima o dopo che una richiesta raggiunga il suo endpoint finale.  
* **Gestione della richiesta/risposta:** L'idea di base di prendere un oggetto request e restituire un oggetto response (spesso in formato JSON) è la stessa.  
* **Concetti di base:** L'approccio minimalista per la creazione di API, l'uso di un server (come Uvicorn per FastAPI e il server HTTP nativo di Node.js per Express) e la gestione delle richieste HTTP sono concetti che ti sentirai familiare.

## **3\. Le differenze chiave**

Nonostante le somiglianze, ci sono delle differenze sostanziali che migliorano l'esperienza di sviluppo.

* **Linguaggio:** Ovviamente, Python vs JavaScript. Con FastAPI sei nel mondo Python, con i suoi vantaggi (ecosistema di librerie scientifiche e di machine learning) e le sue sintassi.  
* **Asincronia (async/await):** Mentre Express usa un modello event-driven basato su callback e async/await (più tardi), **FastAPI è nativamente asincrono (async/await)** per impostazione predefinita, rendendo la gestione delle operazioni I/O (come le chiamate a un database) molto più efficiente e performante.  
* **Validazione dei dati (Pydantic):** Questa è una delle differenze più importanti. In Express, usi librerie come **Joi** o **yup** per validare il body di una richiesta. In FastAPI, la validazione è integrata. Basta definire un modello con Pydantic e usarlo come tipo per i parametri della funzione.  
* **Documentazione:** L'automazione della documentazione è una killer feature di FastAPI. In Express, Swagger o altre librerie simili richiedono configurazione e spesso non sono perfettamente sincronizzate con il codice. FastAPI lo fa per te, riducendo gli errori.  
* **Gestione degli errori:** FastAPI fornisce messaggi di errore automatici e chiari quando la validazione dei dati fallisce, cosa che in Express devi gestire manualmente.

## **4\. Esempi di codice a confronto**

Ecco un semplice esempio di "Hello World" con gestione dei parametri per farti capire meglio.

**Express**

main.js  
```javascript
const express = require('express');  
const app = express();  
const port = 3000;

app.use(express.json());

app.get('/', (req, res) => {  
  res.send('Ciao, mondo!');  
});

app.get('/items/:id', (req, res) => {  
  const itemId = req.params.id;  
  const query = req.query.q;  
  res.json({ item_id: itemId, query: query });  
});

app.listen(port, () => {  
  console.log(`Esempio app in ascolto sulla porta ${port}`);  
});
```
**FastAPI**

main.py  
```python
from fastapi import FastAPI  
from typing import Optional # Per i tipi opzionali

app = FastAPI()

@app.get("/")  
def read_root():  
    """Endpoint per la root."""  
    return {"message": "Ciao, mondo\!"}

@app.get("/items/{item_id}")  
async def read_item(item_id: int, q: Optional [str] = None):  
    """  
    Endpoint per un singolo item.  
    \- item\_id: viene automaticamente convertito in intero e validato.  
    \- q: parametro di query opzionale.  
    """  
    return {"item_id": item_id, "q": q}  
```



### FASTAPI use starlette to parse the response. 

In a FastAPI application, **the conversion from Python dictionaries (or lists of dictionaries) to JSON** for the HTTP response is handled by **Starlette**, which is the ASGI framework FastAPI is built on.

- Pydantic is used by FastAPI to validate and serialize/deserialize data models (for request and response models), but if you return a plain dictionary or list, FastAPI passes it directly to Starlette.

- Starlette uses Python’s standard json module to serialize the response data into JSON before sending it to the client.

**Summary**:

- If you return a Pydantic model, FastAPI uses Pydantic to convert it to a dict, then Starlette serializes it to JSON.

- If you return a dict or list, Starlette serializes it to JSON.
So:

Starlette is responsible for the final conversion to JSON in the HTTP response.
Pydantic is responsible for data validation and (optionally) serialization if you use Pydantic models.


1. Can I use a list of dictionaries in Python to return a format like a JSON object?
   Yes!
   In Python, a list of dictionaries is very similar to a JSON array of objects.
   When you return data from a FastAPI (or Flask) endpoint, Python will automatically convert (serialize) your list of dictionaries into a JSON array of objects for the HTTP response(using starlette).

   Example in Python:

   ```python
   data = [ 
      {"name": "Laptop", "price": 1000},
      {"name": "Monitor", "price": 200}
   ]

   # When returned from FastAPI, this becomes:
   # [
   # {"name": "Laptop", "price": 1000},
   # {"name": "Monitor", "price": 200}
   # ]
   ```
2. What is the difference between JSON and a list of dictionaries?
  - Python list of dictionaries:

    Native Python data structure.

    Not a string, but actual Python objects in memory.

    Example:
    ```python
    [{"name": "Laptop", "price": 1000}, {"name": "Monitor", "price": 200}]
    ```

  - JSON:

    A string format for data interchange (JavaScript Object Notation).
    Used to transmit data between systems (e.g., from server to browser).
    
    Example:
    ```json
    [  {"name": "Laptop", "price": 1000},  {"name": "Monitor", "price": 200}]
    ```

    In Python, you can convert a list of dictionaries to JSON using json.dumps() and parse JSON back to Python with json.loads().

3. NodeJS/Express and JSON
    In NodeJS, you often work with JavaScript objects and arrays.
    When you send a response with res.json(data), Express automatically converts your JS object/array into a JSON string for the HTTP response.
    This is similar to what FastAPI or Flask does in Python.

  In short:

  In Python, use a list of dictionaries for your data.
  **When you return it from an API, it will be automatically converted to JSON for the client.**
  JSON is just a string representation for data exchange.


