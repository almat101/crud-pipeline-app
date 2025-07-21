# express_project_1
Some test with express framework

Express.js è un framework web minimale e flessibile per Node.js che fornisce un set robusto di funzionalità per costruire applicazioni web e API REST.

Perché usarlo?

- Semplifica lo Sviluppo Web: Node.js da solo offre API a basso livello per creare server HTTP. Express.js si basa su queste API e le semplifica enormemente, fornendo strumenti e convenzioni per gestire routing, middleware, richieste e risposte in modo molto più efficiente e organizzato.

- Veloce e Minimale: È "unopinionated", il che significa che non impone una struttura rigida o molte dipendenze. Questo ti dà la libertà di scegliere le librerie e gli strumenti che preferisci, mantenendo il tuo backend leggero e veloce.

- Gestione del Routing: Rende estremamente facile definire come il tuo server risponde a diverse richieste HTTP (GET, POST, PUT, DELETE) su vari URL (route).

- Middleware: Offre un potente sistema di middleware, che sono funzioni che possono eseguire compiti specifici (come il parsing del corpo delle richieste, l'autenticazione, il logging) prima che le richieste raggiungano la logica finale della tua applicazione.

- Grande Community ed Ecosistema: Essendo il framework più popolare per Node.js, ha una vasta community, tonnellate di risorse, tutorial e un enorme ecosistema di librerie e middleware di terze parti che possono estendere le sue funzionalità.

- Scalabilità: È progettato per essere scalabile e può gestire un gran numero di richieste simultanee, rendendolo adatto per applicazioni ad alto traffico.

In sintesi, Express.js è lo strumento che ti permette di passare dalla semplice creazione di un server HTTP con Node.js alla costruzione di API REST complesse e applicazioni web complete in modo strutturato ed efficiente.


Per creare un app express dalla documentazione ufficiale:

import express from 'express'

const app = express()
const port = 3000

app.get('/', (req, res) => {
  console.log(req);
  res.send('Hello World!')
})

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`)
  console.log(`Route available '/' e '/about'`)
})

possiamo aggiungere la creazione di un enpoint semplicemente cosi:

app.get('/about',(req,res)=>
{
  res.json({message : "success", test : "lol"})
})


Cosa fa res.json():

- Prende il valore JavaScript che gli hai passato.
- Lo converte in una stringa JSON (internamente usa JSON.stringify()).
- Imposta automaticamente l'header Content-Type della risposta HTTP a application/json.
- Invia la risposta al client.

in 3 righe abbiamo creato un endpoint che ritorna un oggetto JSON e imposta anche application/json nell header!

## BASIC ROUTING
Routing refers to determining how an application responds to a client request to a particular endpoint, which is a URI (or path) and a specific HTTP request method (GET, POST, and so on).

Each route can have one or more handler functions, which are executed when the route is matched.

Route definition takes the following structure:

app.METHOD(PATH, HANDLER)
Where:

app is an instance of express.
METHOD is an HTTP request method, in lowercase.
il metodo http get,post ecc
PATH is a path on the server.
il path e la rotta es '/'
HANDLER is the function executed when the route is matched.
l'handler e' una callback
es:
app.get('/',(req,res) =>
{
    res.send("lol");
})

## MIDDLEWARE

In Express.js, un middleware è una funzione che ha accesso all'oggetto della richiesta (req), all'oggetto della risposta (res) e alla funzione next() nel ciclo richiesta-risposta di un'applicazione.
