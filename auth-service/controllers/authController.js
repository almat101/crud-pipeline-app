import Joi from 'joi';
import bcrypt from 'bcrypt';
import { Pool } from 'pg'
import dotenv from 'dotenv'

dotenv.config({ path: '/home/ale/Desktop/express_project_1/.env' })
console.log(process.env)

const pool = new Pool({
  host: process.env.POSTGRES_HOST_AUTH,
  user:  process.env.POSTGRES_USER_AUTH,
  database: process.env.POSTGRES_DB_AUTH,
  password: process.env.POSTGRES_PASSWORD_AUTH,
  port: process.env.POSTGRES_PORT_AUTH,
  max: 20,
  idleTimeoutMillis: 30000,
  connectionTimeoutMillis: 2000,
  maxLifetimeSeconds: 60
});

const schema = Joi.object({
    username: Joi.string()
        .alphanum()
        .min(3)
        .max(30)
        .required(),

    password: Joi.string()
        .pattern(new RegExp('^[a-zA-Z0-9]{3,30}$')),

    repeat_password: Joi.ref('password'),

    email: Joi.string()
        .email({ minDomainSegments: 2, tlds: { allow: ['com', 'net','org','edu','gov', 'io', 'co', 'it', 'us', 'uk'] } })
})
    .with('password', 'repeat_password');



// funzione che gestisce la logica di registrazione utente
// riceve dati dal fronted trasformati da oggetto JS a oggetto JSON con AXIOS 
// valida i dati con la libreria JOI
// se i dati sono ok (cripta la password)
// eseque una query sql per inserirli nel db
export const signup = async (req, res) => {
    // Primo try catch usato per validate il body con la libreria joi
    let validateUser;
    try {
        console.log("Validation with Joi")
        let userJoi = req.body;
        validateUser = await schema.validateAsync(userJoi);
        // console.log(validateUser)
        // res.status(201).json({message: "validation ok", body: validateUser})
    }
    catch (err) { 
        res.status(400).json({message : "Validation Error", error: err.details })
    }
    
    // Secondo try catch per criptare la password e salvare tutto lo user  nel DB
    try {
        // Per prima cosa geniaramo un Salt ( che e' una stringa causale che andra aggiunta alla password prima di hasharla)
        const saltRounds = 10;
        const salt = await bcrypt.genSalt(saltRounds); // Generate salt
        const hash = await bcrypt.hash(validateUser.password, salt); // adesso abbiamo la password hashata e la possiamo salvare nel db
        // prev_query e' una query preventiva che serve a controllare se un utente o emai e' gia esistente 
        const prev_query = await pool.query('SELECT * FROM users WHERE username = $1 OR email = $2', [ validateUser.username , validateUser.email ])
        if (prev_query.rowCount == 1) // prev_query.rowCount ritorna uno se c'e una corrispondenza, ossia se esiste gia un utente con lo stesso user e/o email
            return res.status(400).json({ message : "Username or Email already exists" })
        // Inserimento dello user nel db con una query protetta dai placeholder della libreria pg
        const text = `INSERT INTO users (username, email, password_hash) VALUES ($1 ,$2 ,$3 ) returning *`;
        const values = [ validateUser.username, validateUser.email, hash]
        const result = await pool.query( text, values); 
        return res.status(201).send({ message: "User created" , product: result.rows[0] });
    } catch (error) {
        res.status(500).json({message: "Internal server error"})
    }
}

// funzione che gestisce la logica di login utente (riceve credenziali dal fronted, valida dati, cerca utente nel db eseguendo una query, se le credenziali sono corrette genera e restituisce un token JWT e risponde con successo o con errore 401)
export const login = async (req, res) => {
    //testing route
    try {
        console.log("test login")
        console.log(req.body);
        res.status(200).json({message: "body received" , body_richiesta: req.body})
    } catch (error) {
        res.status(500).json({message: "Internal server error"})
    }
}