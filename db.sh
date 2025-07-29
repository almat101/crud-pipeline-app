#!/bin/sh

# Nome del container PostgreSQL definito in docker-compose.yml
CONTAINER_NAME="postgres_database_express"

# Carica le variabili d'ambiente dal file .env
# Questo è importante se esegui lo script direttamente.
# Se lo esegui tramite `docker-compose exec`, le variabili potrebbero essere già disponibili.
# Assicurati che il tuo file .env contenga POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_DB.
if [ -f .env ]; then
  export $(grep -v '^#' .env | xargs)
fi

# Controlla se le variabili d'ambiente necessarie sono impostate
if [ -z "$POSTGRES_USER" ] || [ -z "$POSTGRES_PASSWORD" ] || [ -z "$POSTGRES_DB" ]; then
  echo "Errore: Le variabili d'ambiente POSTGRES_USER, POSTGRES_PASSWORD o POSTGRES_DB non sono impostate nel file .env."
  echo "Assicurati che il file .env esista e contenga queste variabili."
  exit 1
fi

echo "Tentativo di connessione al container PostgreSQL: $CONTAINER_NAME"
echo "Utente: $POSTGRES_USER, Database: $POSTGRES_DB"

# Comandi SQL da eseguire
# Abbiamo aggiunto 'IF NOT EXISTS' per la creazione della tabella per renderla idempotente
# (puoi eseguire lo script più volte senza errori se la tabella esiste già).
# Abbiamo aggiunto 'UNIQUE' al nome e 'ON CONFLICT (name) DO NOTHING' per gli INSERT
# per evitare di inserire duplicati se lo script viene eseguito più volte.
SQL_COMMANDS="
CREATE TABLE IF NOT EXISTS products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) UNIQUE NOT NULL,
    price NUMERIC(10, 2) NOT NULL,
    category VARCHAR(100)
);

INSERT INTO products (name, price, category) VALUES ('Iphone 14', 1299.99, 'Electronics') ON CONFLICT (name) DO NOTHING;
INSERT INTO products (name, price, category) VALUES ('Lenovo T14', 1499.99, 'Electronics') ON CONFLICT (name) DO NOTHING;
INSERT INTO products (name, price, category) VALUES ('Pixel 9', 899.99, 'Electronics') ON CONFLICT (name) DO NOTHING;
INSERT INTO products (name, price, category) VALUES ('Dyson v15', 899.99, 'Home') ON CONFLICT (name) DO NOTHING;
"

# Esegui i comandi SQL all'interno del container usando docker exec
# Usiamo PGPASSWORD per passare la password in modo sicuro.
# Il flag -w (o --no-password) impedisce a psql di chiedere la password interattivamente.
# Il flag -c esegue la stringa di comando SQL.
docker exec -e PGPASSWORD="$POSTGRES_PASSWORD" \
  "$CONTAINER_NAME" \
  psql -U "$POSTGRES_USER" -d "$POSTGRES_DB" -w -c "$SQL_COMMANDS"

# Controlla lo stato di uscita del comando docker exec
if [ $? -eq 0 ]; then
  echo "Comandi SQL eseguiti con successo."
else
  echo "Errore durante l'esecuzione dei comandi SQL. Controlla i log del container e la sintassi SQL."
fi

