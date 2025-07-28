import express from 'express'
import morgan from 'morgan';
import helmet from 'helmet';
import dotenv from 'dotenv'

const app = express();
const port = 3000;

//libreria di node per leggere i file .env ( su python si usa os.environ.get("ENV_VARIABLE"))
dotenv.config({ path: '~/Desktop/express_project_1/.env' })
console.log(process.env) // stampa tutto l'env compresi i valori che ho aggiunto al .env


//                                                             ":method :url :status :response-time ms\ - :res[content-length]"
// middleware logger utile per stampare info sulla richiesta es "GET /about 200 1.896 ms - 34" 
app.use(morgan('dev'));

// middleware che aggiunge vari header di sicurezza alla risposta HTTP
app.use(helmet())


// middleware impostato a livello globale
// serve per parsare il corpo(body) delle richieste in entrata quando sono in formato JSON
app.use(express.json());

app.get('/', (req, res) => {
  res.send('Hello World!')
})

//Query string con /user/search va messo prima di req.parmas ( /user/:id)  per evitare che express esequa prima la rotta con il parametro
//La query string sono coppie chiave valore che vengono aggiunte dopo un '?' e separati tramite '&' es /products/search?chiave=valore&chiave2=valore2 
app.get('/products/search', (req,res) =>
{
  console.log(req.query)
  res.send(`req.query.name ${req.query.name} req.query.category ${req.query.category} req.query.price ${req.query.price}`)
})

// Parametro nella richiesta (req.params) questo parametro e' un valore dinamico che puo' essere catturato con req.params
app.get('/products/:id', (req,res) => 
{
  let id = req.params.id;
  let isDigit = /^[0-9]+$/.test(id);
  let type = typeof req.params.id;
  if (isDigit) {
    res.send(`req.params is: ${req.params.id}, type is ${type}, is digit? ${isDigit}`)
  } else {
    res.status(400).send("Error ID is not a digit!")
  }
})

app.get('/about',(req,res)=>
{
  // richiesta GET qui res.json e' usato per Serializzare JSON per la Risposta (Output) (prende un oggeto javascript e lo serializza in un JSON)
  // (il JSON e' hardcodato direttamente, in realta' andrebbe preso da un database)
  res.json({message : "success", test : "lol"}) 
})

app.get('/plain',(req,res) =>
{
  //  res.set modifca l'header e lo cambia in text/plain
  res.set('Content-Type','text/plain');
  // res.send invia semplice testo (se imoposta nell header) puo anche inviare oggetti JSON 
  res.send('Plain text sended!');
})

// test prima POST
app.post('/data', (req,res) =>
{
  // richiesta POST 
  // dentro express.json() ce del codice che intercetta la richiesta HTTP che contiene anche il body come oggetto JSON, legge il corpo e lo parsa in oggetto javascript 
  // e lo inserisce dentro req.body, dopo questo chiama next() per passare al prossimo middleware. req.body diventa un oggetto javascript grazie ad express.json().
  // se non viene usato express.json() con app.use(express.json()); il body sara' undefined.
  // Anche in questa POST il codice e' hardcoded, in realta' andrebbero effettuati controlli sul tipo di oggetto, se ha i campi necessari ecc e poi aggiunto al database.
  console.log('Dati ricevuti nel corpo della richiesta:', req.body);
  res.status(201);
  res.json({
    message: "dati ricevuti",
    data: req.body
  });
});

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`)
  console.log(`
  Route available:
  '/'                 (GET) return a string
  '/products/search'  (GET) return the query srting parameters searched
  '/products/:id'     (GET) return the 'id'(accept only digit or return 400)
  '/about'            (GET) return a JSON object
  '/plain'            (GET) return a string with Content-type set to plain/text
  '/data'             (POST) send JSON data
  `)
})


// my logger tolto 
// funzione custom per stampare a schermo info utile ( custom logger tipo morgan) 
//const myLogger = function (req, res, next) {
  //console.log('--- MIDDLEWARE LOG TEST ---');
  //console.log(`Richiesta in arrivo: ${req.method} ${req.originalUrl}`);
  //console.log(`Timestamp: ${new Date().toISOString()}`); // Preferibile ISO string per standardizzazione
  //console.log(`IP client: ${req.ip}`);
  //console.log(`User-Agent: ${req.get('User-Agent') || 'N/A'}`); // User-Agent è un header di RICHIESTA, corretto
//
  //// Leggi il Content-Type dalla RICHIESTA
  //// Sarà undefined per GET/DELETE, presente per POST/PUT/PATCH
  //console.log(`Content-Type della Richiesta: ${req.get('Content-Type') || 'N/A (Nessun corpo o header)'}`);
//
  //// Leggi l'Host dalla RICHIESTA (è un header di richiesta!)
  //console.log(`Host della Richiesta: ${req.get('Host') || 'N/A'}`);
//
  //// Puoi anche leggere req.hostname che è una proprietà più comoda
  //console.log(`Hostname: ${req.hostname}`);
//
  //next();
//};

// usiamo il custom middleware myLogger 
//app.use(myLogger);
