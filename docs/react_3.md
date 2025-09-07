In React 19, le **Actions** e i **Server Components** rappresentano due delle innovazioni più importanti per migliorare performance, semplicità e integrare frontend e backend in modo moderno.[^1][^2][^3][^4]

## Actions: gestione moderna delle interazioni e mutazioni

Le **Actions** permettono di centralizzare e semplificare la gestione di mutazioni di stato e submission dei form, sia lato client che lato server:

- Con Actions, puoi associare direttamente una funzione asincrona all’attributo `action` del `<form>`, senza più dover usare onSubmit, fetch o API custom.[^5][^6][^7]
- React si occupa dello stato "pending", del reset automatico del form a successo e della gestione di errori "user-friendly".


### Esempio base di Action

```jsx
import { useActionState } from "react";

async function aggiornaNome(prev, formData) {
  const nome = formData.get("nome");
  // Esegui update su DB, validazione ecc.
  await new Promise(r => setTimeout(r, 2000)); // simula async
  if (!nome) return {error: "Nome obbligatorio"};
  return {data: "ok", error: null};
}
function UpdateNameForm() {
  const [state, submit, isPending] = useActionState(aggiornaNome, {data: null, error: null});
  return (
    <form action={submit}>
      <input name="nome" />
      <button disabled={isPending}>Salva</button>
      {state.error && <p>{state.error}</p>}
    </form>
  );
}
```

- Il codice business del submit resta separato dagli effetti UI, e lo stato (pending/caricamento/errori) è gestito per default dai nuovi hooks.
- Puoi passare una Server Action anche direttamente al form, e React esegue la funzione sul server (se usi Next.js, Remix o ambienti compatibili).[^3][^7][^6]


## React Server Components

I **Server Components** (RSC) sono componenti che vengono eseguiti e renderizzati completamente sul server, restituendo solamente HTML al client:

- Risolvono il data-fetching o la logica pesante prima che la pagina venga caricata.[^8][^9][^1][^3]
- Il codice JS del componente non viene mai scaricato dal browser: la UI arriva già pronta, riducendo il bundle JS e migliorando i tempi di caricamento.
- Puoi mescolare Server e Client Components in un’unica app: la UI statica o non interattiva viene generata lato server, mentre l’interattività rimane gestita dai Client Components.[^9][^3]


### Esempio Server Component

```js
// Users.server.jsx
export default async function Users() {
  const res = await fetch("https://api.example.com/users");
  const users = await res.json();
  return (
    <div>
      <h1>Utenti</h1>
      {users.map(u => <div key={u.id}>{u.name}</div>)}
    </div>
  );
}
```

- Lato client ricevi solo HTML, non la logica JS.
- Perfetto per performance, SEO e data-fetching centralizzato.


## Server Actions

Le **Server Actions** sono funzioni asincrone definite sul server, a cui puoi passare direttamente i tuoi dati dai Client Components o dai form:

- Non serve più scrivere API REST o GraphQL custom.[^7][^6][^3]
- Ideale per submit di form che modificano risorse, login, CRUD, ecc.

```js
// actions.js
"use server";
export async function creaPost(formData) {
  // logica server, validazione, DB...
}

import { creaPost } from "./actions";
function NewPostPage() {
  return (
    <form action={creaPost}>
      <input name="title" />
      <button>Salva</button>
    </form>
  );
}
```

- La funzione viene eseguita direttamente sul server, React si occupa di orchestrare chiamata, stato e reset.


## Miglioramenti e vantaggi

- Performance eccellenti: meno JavaScript, data-fetching ottimizzato, caricamento rapido.[^4][^3]
- Sviluppo più semplice: meno boilerplate, separazione naturale tra UI e logica server.
- SEO migliorata: HTML renderizzato lato server, contenuti subito visibili ai motori di ricerca.

Queste tecnologie segnano il passaggio a una piattaforma React molto più integrata con il backend, scalabile e performante, specialmente se usata con Next.js.[^1][^4][^3]
<span style="display:none">[^10][^11][^12][^13][^14][^15][^16][^17][^18][^19][^20]</span>

<div style="text-align: center">⁂</div>

[^1]: https://it.linkedin.com/pulse/react-19-levoluzione-verso-unarchitettura-web-moderna-quinck-mqelf

[^2]: https://tech.neosperience.com/blog/react-19

[^3]: https://www.geeksforgeeks.org/reactjs/react-19-new-features-and-updates/

[^4]: https://www.html.it/magazine/react-19-rilasciata-la-versione-stabile/

[^5]: https://diegobetto.com/react-useactionstate-useformstatus

[^6]: https://react.dev/reference/rsc/server-functions

[^7]: https://devmy.it/blog/article/nextjs-v14-quando-il-client-ed-il-server-diventano-ununica-astrazione-22

[^8]: https://react.dev/blog/2024/12/05/react-19

[^9]: https://react.dev/reference/rsc/server-components

[^10]: https://www.reddit.com/r/webdev/comments/1h7z9v3/react_19_is_officially_out/

[^11]: https://www.html.it/magazine/react-19-un-compilatore-per-le-performance/

[^12]: https://it.linkedin.com/pulse/creare-robust-action-handlers-react-con-hero-actions-e-peqpf

[^13]: https://kinsta.com/it/blog/react-19-wordpress/

[^14]: https://innovaformazione.net/novita-in-react-19/

[^15]: https://www.reddit.com/r/nextjs/comments/1h3crfy/what_is_server_in_server_action/

[^16]: https://www.youtube.com/watch?v=__7zfliVOHk

[^17]: https://www.youtube.com/watch?v=lM8Zm5pRT88

[^18]: https://neosyn.it/react-19-rivoluzione-o-evoluzione/

[^19]: https://dev.to/a1guy/react-19-server-components-deep-dive-what-they-are-how-they-work-and-when-to-use-them-2h2e

[^20]: https://www.reddit.com/r/reactjs/comments/1gwszdu/how_does_react_19_execute_server_components_and/

