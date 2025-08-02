## Frontend:

- L’utente compila il form di login (es: email/username e password).
- Quando invii il form, raccogli i dati in un oggetto JavaScript, ad esempio:
```javascript
const payload = {  email: "user@example.com",  password: "mypassword"};
```
- Prima di inviare la richiesta, l’oggetto viene convertito in JSON (la maggior parte delle librerie come fetch o axios lo fanno automaticamente).
- Invia una richiesta POST all’endpoint /auth/login con il payload nel body:
```javascript
fetch('/auth/login', {  method: 'POST',  headers: { 'Content-Type': 'application/json' },  body: JSON.stringify(payload)});
```

## Backend (Express):

- La rotta /auth/login riceve la richiesta POST.
- Express, grazie a express.json() come middleware, parsa automaticamente il body JSON e lo rende disponibile come oggetto JS in req.body.
- Nel controller (login), puoi accedere ai dati con req.body.email e req.body.password.

## Riassunto:

Il form crea un oggetto JS → viene convertito in JSON → inviato via POST → Express lo riceve e lo trasforma di nuovo in oggetto JS (req.body).
Questo è il flusso tipico di una rotta di login POST tra frontend e backend.