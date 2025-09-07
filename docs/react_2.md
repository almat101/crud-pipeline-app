Ecco una panoramica dettagliata sui **componenti principali di React**, gli hook fondamentali (`useState`, `useEffect`, etc.) e sul funzionamento delle **props**, adatta a chi già programma backend e vuole consolidare la propria base frontend con React 19.

## Componenti React

### Componenti Funzionali

I componenti React sono funzioni JavaScript che ricevono come primo argomento un oggetto chiamato **props** (proprietà) e restituiscono elementi JSX (markup simile a HTML).[^2][^5][^7]

```jsx
function Saluto(props) {
  return <h1>Ciao, {props.nome}</h1>;
}
```

- Si utilizzano quasi esclusivamente **componenti funzione** nelle app moderne.
- Le props permettono di passare dati e callback ai componenti figli.


### Props

- Le **props** sono dati che si passano dal genitore al figlio, come attributi HTML.[^3][^6]
- Sono immutabili nel componente che le riceve.

```jsx
<UserInfo name="Marco" onLogout={() => console.log("Logout")} />
// Nel componente:
function UserInfo({ name, onLogout }) {
  return (
    <div>
      <p>{name}</p>
      <button onClick={onLogout}>Logout</button>
    </div>
  );
}
```

- Si possono passare anche elementi JSX come props, per comporre layout avanzati.


### Esempio di composizione

```jsx
function PageContainer({ header, content }) {
  return (
    <div>
      <header>{header}</header>
      <main>{content}</main>
    </div>
  );
}
// Uso:
<PageContainer 
  header={<h1>Titolo</h1>} 
  content={<p>Contenuto...</p>} 
/>
```


## useState

- **useState** è un hook per gestire lo stato locale del componente.
- Sintassi: `const [valore, setValore] = useState(valoreIniziale)`
- Aggiornare lo stato causa il re-render del componente.

```jsx
import { useState } from "react";
function Contatore() {
  const [conta, setConta] = useState(0);
  return (
    <button onClick={() => setConta(conta + 1)}>
      Clicca: {conta}
    </button>
  );
}
```


## useEffect

- **useEffect** consente di gestire effetti collaterali: chiamate API, aggiornamenti del DOM, timers, ecc.
- Sintassi base: `useEffect(callback, [dipendenze])`
- Viene eseguito dopo ogni render (o solo quando cambiano le dipendenze)

```jsx
import { useEffect } from "react";
useEffect(() => {
  // Operazione al mount
  document.title = "React App";
}, []); // Solo al primo render

useEffect(() => {
  // Operazione ad ogni cambio di 'conta'
  console.log(conta);
}, [conta]);
```


## Altri Hook Fondamentali

### useContext

- Permette la condivisione di dati tra componenti senza passare props manualmente.
- Utile per autenticazione, tema, lingua, ecc.

```jsx
import { useContext } from "react";
const AuthContext = React.createContext();
function Componente() {
  const auth = useContext(AuthContext);
}
```


### useReducer

- Gestisce stato complesso tramite logica simile a Redux.
- Sintassi: `const [state, dispatch] = useReducer(reducer, statoIniziale)`

```jsx
function reducer(state, action) {
  if (action.type === "increment") return state + 1;
  return state;
}
const [conto, dispatch] = useReducer(reducer, 0);
```


### useRef

- Crea un riferimento persistente tra i render, utile per input DOM o variabili non-reactive.

```jsx
import { useRef } from "react";
const inputRef = useRef();
<input ref={inputRef} />
```


## Nota su React 19

- In React 19 gli hooks hanno una gestione ottimizzata e sono alla base di tutto il workflow moderno, inclusa la gestione delle nuove **Actions** asyncrone, il supporto ai Server Components e i miglioramenti su refs e stato.[^4]

Questa base ti permette di lavorare in modo efficace con React e di scrivere componenti modulari, riutilizzabili e altamente dinamici.
<span style="display:none">[^1][^10][^8][^9]</span>

<div style="text-align: center">⁂</div>

[^1]: https://kinsta.com/it/blog/react-19-wordpress/

[^2]: https://it.react.dev/learn/your-first-component

[^3]: https://it.legacy.reactjs.org/docs/components-and-props.html

[^4]: https://tech.neosperience.com/blog/react-19

[^5]: https://www.mrw.it/lez/nostro-primo-react-component/

[^6]: https://www.manuelricci.com/guida/props-componenti-react

[^7]: https://www.manuelricci.com/guida/componenti-in-react

[^8]: https://www.mrw.it/lez/componenti-react-oggetto-props/

[^9]: https://kinsta.com/it/blog/libreria-componenti-react/

[^10]: https://www.youtube.com/watch?v=fl-43zv--9Q

