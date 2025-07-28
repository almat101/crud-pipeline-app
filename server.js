import express from 'express'
import morgan from 'morgan';
import helmet from 'helmet';
import dotenv from 'dotenv'
import { Pool } from 'pg'

const app = express();
const port = 3000;

//libreria di node per leggere i file .env ( su python si usa os.environ.get("ENV_VARIABLE"))
dotenv.config()
console.log(process.env) // stampa tutto l'env compresi i valori che ho aggiunto al .env

const pool = new Pool({
  host: process.env.POSTGRES_HOST,
  user:  process.env.POSTGRES_USER,
  database: process.env.POSTGRES_DB,
  password: process.env.POSTGRES_PASSWORD,
  port: process.env.POSTGRES_PORT,
  max: 20,
  idleTimeoutMillis: 30000,
  connectionTimeoutMillis: 2000,
  maxLifetimeSeconds: 60
});

//                                                             ":method :url :status :response-time ms\ - :res[content-length]"
// middleware logger utile per stampare info sulla richiesta es "GET /about 200 1.896 ms - 34" 
app.use(morgan('dev'));

// middleware che aggiunge vari header di sicurezza alla risposta HTTP
app.use(helmet());


// middleware impostato a livello globale
// serve per parsare il corpo(body) delle richieste in entrata quando sono in formato JSON
app.use(express.json());

app.get('/', (req, res) => {
  res.send('Hello World!');
})

//Query string con /user/search va messo prima di req.parmas ( /user/:id)  per evitare che express esequa prima la rotta con il parametro
//La query string sono coppie chiave valore che vengono aggiunte dopo un '?' e separati tramite '&' es /products/search?chiave=valore&chiave2=valore2 
app.get('/products/search', (req,res) =>
{
  console.log(req.query);
  res.send(`req.query.name ${req.query.name} req.query.category ${req.query.category} req.query.price ${req.query.price}`);
})

// Parametro nella richiesta (req.params) questo parametro e' un valore dinamico che puo' essere catturato con req.params
app.get('/products/:id', (req,res) => 
{
  let id = req.params.id;
  let isDigit = /^[0-9]+$/.test(id);
  let type = typeof req.params.id;
  if (isDigit) {
    res.send(`req.params is: ${req.params.id}, type is ${type}, is digit? ${isDigit}`);
  } else {
    res.status(400).send("Error ID is not a digit!");
  }
})

app.get('/about',(req,res)=>
{
  // richiesta GET qui res.json e' usato per Serializzare JSON per la Risposta (Output) (prende un oggeto javascript e lo serializza in un JSON)
  // (il JSON e' hardcodato direttamente, in realta' andrebbe preso da un database)
  res.json({message : "success", test : "lol"});
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

async function testPool_startServer() {
  try {
    
    //const client = await pool.connect(); // Qui pool.connect() e usato per acqusire una connessione
    //const result = await client.query('SELECT NOW()') // viene eseguita una query che mostra l'ora attuale del db
    //console.log(result);
    //client.release(); //Necessario il rilascio del client al pool

    // Test con await pool.query():
    // Non ha bisogno di acquisire una connessione e di rilasciarla, per eseguire una semplice query.
    //const result = await pool.query('SELECT $1::text as name', ['Lenovo T14']);
    //const result = await pool.query('SELECT * FROM products WHERE id = $1', [2]);
    const result = await pool.query('SELECT * FROM products');
    console.log(result);

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
  } catch (err) {
    console.error('Errore critico all\'avvio del server o del database:', err.stack);
    process.exit(1); // Esci dal processo con un codice di errore
  }
};

testPool_startServer();
