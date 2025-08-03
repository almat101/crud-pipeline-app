import express from 'express';
import morgan from 'morgan';
import helmet from 'helmet';
// import dotenv from 'dotenv'
// import { Pool } from 'pg'

import authRoutes from './routes/authRoutes.js'

const app = express();
const PORT = 3030;

// dotenv.config({ path: '/home/ale/Desktop/express_project_1/.env' })
// console.log(process.env)

// const pool = new Pool({
//   host: process.env.POSTGRES_HOST_AUTH,
//   user:  process.env.POSTGRES_USER_AUTH,
//   database: process.env.POSTGRES_DB_AUTH,
//   password: process.env.POSTGRES_PASSWORD_AUTH,
//   port: process.env.POSTGRES_PORT_AUTH,
//   max: 20,
//   idleTimeoutMillis: 30000,
//   connectionTimeoutMillis: 2000,
//   maxLifetimeSeconds: 60
// });

// middleware logger utile per stampare info sulla richiesta es "GET /about 200 1.896 ms - 34" 
app.use(morgan('dev'));

// middleware che aggiunge vari header di sicurezza alla risposta HTTP
app.use(helmet());

// Parsail corpo(body) delle richieste in entrata quando sono in formato JSON
app.use(express.json());

//rotta test
app.get('/', (req, res) => {
  res.send('Hello auth-service!');
});

// Collego il router di autenticazione aggiungo /auth in modo da dover chiamare solo /auth/signup e auth/login
app.use('/auth', authRoutes);

app.listen(PORT, () => {
  console.log(`Auth app listening on port ${PORT}`)
      console.log(`
        Route available:
        '/' return Hello auth-service!
        '/auth/signup (POST)
        '/auth/login' (POST)
    `)
});
