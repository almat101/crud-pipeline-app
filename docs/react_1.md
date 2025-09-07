## Cos’è React e Principi Base

**React** è una libreria JavaScript per la costruzione di UI interattive a partire da “componenti” riutilizzabili che gestiscono dati, stato e rendering dichiarativo. Ogni componente è tipicamente una funzione che restituisce JSX (un superset XML-like per scrivere HTML con JavaScript), e può ricevere input tramite le proprie "props" (proprietà).[^8][^10][^12]

## Struttura delle Applicazioni React

- Ogni app React è composta da **componenti** (Funzioni o Classi, ma con React 19 si usano solo funzioni).[^6][^8]
- I componenti ricevano i dati tramite le **props** e ragionano sul rendering tramite lo **stato locale** (useState, useReducer).
- Per visualizzare il risultato si usa l’elemento root nel DOM, solitamente chiamato `root`.

```jsx
function Saluto(props) {
  return <h1>Ciao, {props.nome}</h1>;
}
```


## Novità e Workflow con React 19

### API di Mount/Unmount

- È stato **rimosso ReactDOM.render** in favore di `createRoot` da `react-dom/client`, per un mounting più efficiente e granulare dell’applicazione.[^3][^5]

```jsx
import { createRoot } from 'react-dom/client';
const root = createRoot(document.getElementById('root'));
root.render(<App />);
```

- **Scorretto:**
`ReactDOM.render(<App />, document.getElementById('root'))`
**Corretto:**
`root.render(<App />)`
- Per smontare un componente dal DOM ora si usa `root.unmount()` invece di `ReactDOM.unmountComponentAtNode`.[^3]


### Actions e Nuovi Hooks

- React 19 introduce le **Actions** per la gestione asincrona delle interazioni (mutazioni dati, invio form).[^5][^7][^9]
- Nuovi hooks come `useActionState`, `useFormStatus`, `useOptimistic` semplificano la gestione di stato pending, errori, ed optimistic update nelle UI.

```jsx
const [error, submitAction, isPending] = useActionState(
  async (prev, formData) => {
    const error = await updateName(formData.get("name"));
    return error ? error : null;
  }, null
);
return (
  <form action={submitAction}>
    <input name="name" />
    <button disabled={isPending}>Aggiorna</button>
    {error && <p>{error}</p>}
  </form>
);
```


### Gestione Form e Stato

- Il nuovo supporto alle form consente di **associare una funzione asincrona direttamente all’action** del form, rendendo la gestione e il reset automatico.[^5]
- Il hook `useFormStatus` consente di abilitare/disabilitare pulsanti e visualizzare loading sulla base dello stato form.[^5]


### React Server Components \& Server Actions

- React 19 stabilizza il supporto ai **Server Components** e introduce le **Server Actions**, facilitando il rendering e la gestione delle mutazioni lato server in ambienti come Next.js e Remix.[^9][^5]
- Questo migliora le performance e semplifica la condivisione logica tra frontend e backend.


## Compilatore React 19

- Il nuovo **React Compiler** trasforma il codice React in JavaScript ottimizzato già in fase di build, migliorando la rapidità di caricamento e la performance delle applicazioni.[^1][^13][^7]
- Si promettono performance anche doppie rispetto alle versioni precedenti grazie a questa ottimizzazione.[^7]


## Sintesi: Cosa Devi Sapere per Iniziare

- Usa solo **componenti funzione** con hooks come `useState`, `useEffect`, `useActionState`.
- Monta il tuo componente root con l’API `createRoot`.
- Sfrutta le nuove **Actions** e **Server Actions** per gestire le interazioni asincrone.
- Sfrutta il compilatore per performance migliori e minor boilerplate.
- La struttura degli import in React 19 sarà:

```jsx
import { createRoot } from 'react-dom/client';
// Hooks come useState, useActionState da 'react'
```


## Risorse Consigliate

- Documentazione ufficiale React 19
- Guide e tutorial aggiornati su HTML.it, freeCodeCamp e Hostinger[^2][^18][^8]
- Video tutorial introduttivi (es. Corso React in Italiano)[^6][^10]

Questa panoramica ti consente di cominciare o aggiornare i tuoi progetti React con le basi e gli standard moderni della versione 19. Per approfondimenti su specifiche aree (routing, Redux, performance, testing), consulta le guide aggiornate e la documentazione ufficiale.[^11][^17]
<span style="display:none">[^14][^15][^16][^4]</span>

<div style="text-align: center">⁂</div>

[^1]: https://tech.neosperience.com/blog/react-19

[^2]: https://www.html.it/magazine/react-19-rilasciata-la-versione-stabile/

[^3]: https://kinsta.com/it/blog/react-19-wordpress/

[^4]: https://www.youtube.com/watch?v=__7zfliVOHk

[^5]: https://innovaformazione.net/novita-in-react-19/

[^6]: https://www.youtube.com/watch?v=3edF3beLm-k

[^7]: https://neosyn.it/react-19-rivoluzione-o-evoluzione/

[^8]: https://www.hostinger.com/it/tutorial/cose-react

[^9]: https://quinck.io/it/blog/react-server-components-server-actions-novita-react-19

[^10]: https://www.youtube.com/watch?v=WCaPTprOuL8

[^11]: https://react-guida-pratica.it/blog/2025-aggiornamento-react-19/

[^12]: https://it.legacy.reactjs.org/tutorial/tutorial.html

[^13]: https://www.html.it/magazine/react-19-un-compilatore-per-le-performance/

[^14]: https://www.freecodecamp.org/italian/news/buone-pratiche-di-react-suggerimenti-per-scrivere-del-codice-react-migliore-nel-2022/

[^15]: https://www.reddit.com/r/webdev/comments/1h7z9v3/react_19_is_officially_out/

[^16]: https://www.youtube.com/watch?v=eXefBs-RWrY

[^17]: https://aulab.it/categorie-guide-avanzate/guida-react-in-italiano

[^18]: https://www.freecodecamp.org/italian/news/la-guida-per-principianti-a-react/

