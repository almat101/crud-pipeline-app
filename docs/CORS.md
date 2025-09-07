## CORS (Cross-Origin Resource Sharing)
 
**CORS** è una protezione di sicurezza implementata dai browser che blocca, per impostazione predefinita, le richieste HTTP fatte da una pagina web verso un dominio diverso da quello da cui la pagina è stata caricata.

**In pratica:**
- Se il tuo frontend gira su http://localhost:3000 e il backend su http://localhost:3040, il browser considera questi come origini diverse.
- Senza CORS abilitato sul backend, il browser blocca le richieste fatte dal frontend al backend, mostrando un errore di tipo "CORS policy".
**Perché esiste?**
- Serve a proteggere l’utente da richieste non autorizzate verso altri siti (Cross-Site Request Forgery, CSRF).
- Permette al backend di decidere quali origini (domini) sono autorizzate a comunicare con lui.
**Come si risolve?**
- Si configura il backend (con CORS middleware) per autorizzare le richieste provenienti dal dominio del frontend.
**In sintesi**:
CORS è una misura di sicurezza del browser che blocca le chiamate tra origini diverse, a meno che il backend non autorizzi esplicitamente quelle richieste.