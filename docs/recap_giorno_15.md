# Recap Giorno 15

## Obiettivo
Migliorare ulteriormente la qualità e la struttura dei dati salvati nel database MongoDB, partendo dai dati già puliti ottenuti dallo scraper.

## Attività completate e suggerimenti di miglioramento

1. **Campo titolo**
   - **Prima:** `"title": "Iphone 15 PRO max 256GB"`
   - **Dopo:** Uniformata la capitalizzazione a lowercase. Sono stati validati solo i prodotti che contengono `iphone 15` nel titolo e creata una lista di parole indesiderate (es. cover, case) che, se presenti nel titolo, fanno scartare il prodotto.

2. **Campo Price**
   - **Prima:** `"price": "500$ Venduto"` oppure `"price": "500$ Spedizione disponibile"`
   - **Dopo:** Uniformata la capitalizzazione a lowercase. Se è presente la parola `venduto`, il prodotto viene scartato. Se è presente la parola `spedizione disponibile`, il campo `shipping_available` viene impostato a `True` (default `False`). Dal campo price viene estratta solo la prima parola e convertita in float (`"price": 500.00`) per facilitare ordinamenti, filtri e calcoli direttamente su MongoDB o nell'applicazione. Vengono inoltre rimossi i prodotti con prezzo inferiore o uguale a una certa soglia, ad esempio `<= 150.00`.

3. **Campo Province**
   - **Prima:** `"province": "(MI)"`
   - **Dopo:** Rimosse le parentesi per rendere più semplice la ricerca e la gestione (`"province": "MI"`).

4. **Formattazione Consistente di City**
   - Uniformata la capitalizzazione del campo city per garantire coerenza nei dati.

5. **Campi Aggiuntivi**
   - Considerata l'aggiunta di campi come `date_scraped` impostando la data con datetime in python e come ISOdate in mongo e `url` selezionando href di ogni prodotto per una migliore tracciabilità e analisi futura.

### Esempio di documento ancora più pulito

```json
{
  "_id": ObjectId('689f0033db2204130ffb4d4a'),
  "title": "iphone 15",
  "city": "cornaredo",
  "date_scraped": ISODate('2025-08-16T00:37:03.765Z'),
  "province": "MI",
  "price": 500.0,
  "shipping_available": true,
}
```
  