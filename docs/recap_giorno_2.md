### **Recap Giorno 2: Costruire un Server Web con Express.js**

Il "Giorno 2" è stato il tuo primo passo pratico nella creazione di un backend web. Abbiamo introdotto Express.js, il framework più popolare per Node.js, e abbiamo iniziato a costruire le fondamenta della tua API.

#### **1\. Introduzione a Express.js**

Abbiamo iniziato a capire cos'è Express.js e perché è così ampiamente utilizzato per lo sviluppo di applicazioni web e API con Node.js.

* **Cos'è Express.js:** Un framework web minimalista e flessibile per Node.js che fornisce un robusto set di funzionalità per lo sviluppo di applicazioni web e API.  
* **Installazione:** Abbiamo visto come installare Express.js nel tuo progetto (npm install express).  
* **Server Base:** Hai creato il tuo primo server "Hello World", imparando la struttura minima di un'applicazione Express (const app \= express(); app.listen(...)).

#### **2\. Routing**

Il routing è il modo in cui il tuo server risponde a diverse richieste HTTP basate sul loro URL e metodo.

* **Definizione di Route Semplici:** Hai imparato a definire route per diversi metodi HTTP:  
  * app.get(): Per richieste di recupero dati.  
  * app.post(): Per richieste di invio dati (creazione).  
  * app.put(): Per richieste di aggiornamento completo.  
  * app.patch(): Per richieste di aggiornamento parziale.  
  * app.delete(): Per richieste di eliminazione.  
* **Parametri di Rotta (es. /users/:id):** Hai visto come catturare valori dinamici dall'URL (es. l'ID di un utente) usando i parametri di rotta e accedendovi tramite req.params 
  * Cosa sono: Sono segmenti dinamici dell'URL che fanno parte del percorso della rotta.
    Vengono usati per identificare una risorsa specifica o una sottorisorsa.
  * Come si definiscono: Li definisci nella tua rotta Express usando i due punti (:).
  * Come si accede: Sono disponibili come proprietà dell'oggetto req.params.id
* **Gestione delle Query String:** Hai imparato come accedere ai parametri aggiunti all'URL dopo un '?' e separati da '&' (es. /search?q=nodejs&framework=express) tramite req.query.q 
    e req.query.framework in questo esempio.
  * Non sono definiti nella rotta; il client li aggiunge dinamicamente dopo il ?.

  * Sono usati per filtrare, ordinare, paginare o passare opzioni aggiuntive.

  * Sono generalmente opzionali. Se un parametro non è presente nella query string, la sua proprietà in req.query sarà undefined.

  * Esempio: /api/products/search?q=laptop&sort=price_asc (qui q e sort sono parametri di query).
  
  * Questa flessibilità di req.query lo rende estremamente utile per le funzionalità di ricerca, filtro e ordinamento nelle API RESTful.

#### **3\. Middleware**

I middleware sono il cuore della modularità e della flessibilità di Express.js.

* **Cos'è un Middleware:** Una funzione che ha accesso all'oggetto richiesta (req), all'oggetto risposta (res) e alla funzione next() nel ciclo richiesta-risposta.  
* **Funzionamento:** I middleware possono eseguire qualsiasi codice, modificare gli oggetti req e res, terminare il ciclo inviando una risposta, o passare il controllo al middleware successivo con next().  
* **Tipi di Middleware:**  
  * **A livello di Applicazione (app.use()):** Applicato a tutte le richieste o a un gruppo di percorsi.  
  * **A livello di Rotta:** Applicato solo a specifiche route.  
  * **Di Gestione degli Errori:** Con una firma speciale (err, req, res, next) per catturare e gestire gli errori.  
* **Middleware Integrato express.json():**  
  * **Ruolo Cruciale:** Fondamentale per le API RESTful che ricevono dati JSON. Parsifica il corpo delle richieste POST, PUT, PATCH con Content-Type: application/json, rendendo i dati disponibili come oggetto JavaScript su req.body.  
  * **Necessità:** Senza di esso, req.body sarebbe undefined per le richieste JSON.  
  * **Posizionamento:** Deve essere applicato con app.use(express.json()); **prima** delle route che si aspettano di ricevere JSON.  
* **Middleware Personalizzato (myLogger):** Hai creato un semplice middleware per il logging (console.log('LOGGED')) per capire il flusso e l'uso di next().  
* **Middleware di Terze Parti (Introdotti):**  
  * **morgan:** Per il logging dettagliato delle richieste HTTP nel terminale.  
    per esempio:
    GET /plain 200 1.149 ms - 18
    GET / 200 0.363 ms - 12

  * **helmet:** Per impostare header di sicurezza HTTP, proteggendo l'applicazione da vulnerabilità comuni.
  * Helmet is a middleware function that sets security-related HTTP response headers. Helmet sets the following headers by default:

  * Content-Security-Policy: A powerful allow-list of what can happen on your page which mitigates many attacks
  * Cross-Origin-Opener-Policy: Helps process-isolate your page
  * Cross-Origin-Resource-Policy: Blocks others from loading your resources cross-origin
  * Origin-Agent-Cluster: Changes process isolation to be origin-based
  * Referrer-Policy: Controls the Referer header
  *Strict-Transport-Security: Tells browsers to prefer HTTPS
  * X-Content-Type-Options: Avoids MIME sniffing
  * X-DNS-Prefetch-Control: Controls DNS prefetching
  * X-Download-Options: Forces downloads to be saved (Internet Explorer only)
  * X-Frame-Options: Legacy header that mitigates Clickjacking attacks
  *  X-Permitted-Cross-Domain-Policies: Controls cross-domain behavior for Adobe products, like * Acrobat
  * X-Powered-By: Info about the web server. Removed because it could be used in simple attacks
  * X-XSS-Protection: Legacy header that tries to mitigate XSS attacks, but makes things worse, so Helmet disables it

#### **4\. Gestione Richieste e Risposte**

Hai imparato a interagire con i dati in entrata e a inviare risposte corrette.

* **Accesso ai Dati della Richiesta:** Hai usato req.body (grazie a express.json()), req.params e req.query per accedere ai dati inviati dal client.  
* **Invio di Risposte:**  
  * res.send(): Per inviare risposte in plain text o HTML.  
  * res.json(): Per serializzare oggetti JavaScript in JSON e inviarli come risposta. Questo è il metodo standard per le API RESTful.  
  * res.status(): Per impostare il codice di stato HTTP della risposta (es. 200 OK, 201 Created, 404 Not Found).  
* **Ciclo Richiesta-Risposta:** Hai compreso che ogni richiesta deve essere terminata con una risposta (tramite res.send(), res.json(), ecc.) per evitare che il client vada in timeout.

Il "Giorno 2" ti ha fornito gli strumenti per creare un server web funzionale e iniziare a costruire le tue API RESTful, gestendo sia l'input che l'output di dati in formato JSON. Sei pronto per connetterti a un database\!
