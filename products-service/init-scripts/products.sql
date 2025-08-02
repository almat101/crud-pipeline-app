-- Inizializzazione tabella products
CREATE TABLE products (  
    id SERIAL PRIMARY KEY,  
    name VARCHAR(255) NOT NULL,  
    price NUMERIC(10, 2) NOT NULL,  
    category VARCHAR(100),
    user_id INTEGER NOT NULL
);




-- Se avessi usato un solo DATABASE per contenere entrambe le tabelle prodotti e utenti avrei potuto usare
-- una foreign key per collegare la tabella products con un utente specifico tramite il suo id
-- Nelle app a microservizi basta usare un ID per mantenere la logica tra la tabella products e il suo ID utente apposito
