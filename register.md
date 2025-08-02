## Frontend:

L’utente compila il form di registrazione (es: username, email, password, ecc.).
I dati vengono raccolti in un oggetto JS, ad esempio:
```js
const payload = {  username: "newuser",  email: "newuser@example.com",  password: "mypassword"};
```
L’oggetto viene convertito in JSON e inviato tramite una richiesta POST all’endpoint /auth/register (o /signup), come per il login.

## Backend (Express):

- La rotta /auth/register riceve la richiesta POST.
- Express converte il body JSON in oggetto JS (req.body).
- Nel controller, validi i dati (es: email valida, password sicura).
- Cripti la password (con bcrypt).
- Salvi i dati dell’utente nel database.
- Rispondi con un messaggio di successo o errore.

## Riassunto:
Form → oggetto JS → JSON → POST → Express riceve → valida e salva nel DB → risposta al frontend.