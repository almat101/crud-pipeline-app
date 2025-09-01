import pandas as pd
import numpy as np
from pymongo import MongoClient
import logging
import re
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import text
from dotenv import load_dotenv
import os

from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/")
def hello():
    return {"message": "Hello from trasformer-service!"}


#TODO remove it when I launch from docker-compose
load_dotenv()

POSTGRES_USER_PRODUCTS = os.getenv("POSTGRES_USER_PRODUCTS")
POSTGRES_PASSWORD_PRODUCTS = os.getenv("POSTGRES_PASSWORD_PRODUCTS")
POSTGRES_HOST_PRODUCTS = os.getenv("POSTGRES_HOST_PRODUCTS")
POSTGRES_PORT_PRODUCTS = os.getenv("POSTGRES_PORT_PRODUCTS")
POSTGRES_DB_PRODUCTS = os.getenv("POSTGRES_DB_PRODUCTS")

PRODUCT_NAME_FILTERED = "iphone 15"
PRDODUCT_MIN_PRICE = 200.00

#### MONGO DB constant ####
#aggiunta timeout all URI per evitare che il programma resti in attessa infinita aspettando la connessione
MONGO_URI = "mongodb://mongodb:27017/?timeoutMS=10000"
MONGO_DB = "products_db"
MONGO_COLLECTION = "raw_products"

# Configure logging to display messages at the INFO level
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)  # Create a logger instance for this module

# Imposta Pandas per visualizzare tutte le colonne
pd.set_option('display.max_columns', None)
# Imposta Pandas per visualizzare tutte le colonne
pd.set_option('display.max_rows', None)


def get_products_from_mongo():
    """
    Connects to MongoDB, retrieves all documents from the specified collection,
    and returns them as a list of dictionaries.

    Returns:
        list: A list of product documents (dicts) from MongoDB, or None if an error occurs.

    Notes:
        - The MongoDB connection is always closed after the operation.
        - If an error occurs, it is logged and None is returned.
    """
    client = None
    product_list = None
    try:
        #### MONGO DB connection creation ####
        client = MongoClient(MONGO_URI)
        db = client[MONGO_DB]
        collection = db[MONGO_COLLECTION]
        cursor = collection.find({}) # un oggetto cursor in MongoDB/Python è simile a un "iteratore" che ti permette di scorrere i risultati di una query, leggerli uno alla volta o convertirli in una lista list(cursor)
        product_list = list(cursor)
    except Exception as e:
        logger.error(f"error getting product from mongo: {e} ")
    finally:
        if client:
            client.close()
    return product_list

def clean_data(df):
    """
    Cleans and transforms the raw product DataFrame.

    Operations performed:
        - Converts MongoDB ObjectId to string to avoid writing errors.
        - Converts all text fields to lowercase for normalization.
        - Filters products to keep only those whose title contains 'iphone 15'.
        - Removes emojis from the title field using a regular expression.
        - Cleans up the 'city' and 'province' fields (lowercase, removes parentheses from province).
        - Creates a 'shipping_available' boolean column based on the presence of 'Spedizione disponibile' in the price field.
        - Extracts numeric values from the 'price' field and converts them to numeric type (non-numeric values become NaN).
        - Filters out products with price less than or equal to 200.
        - Adds a 'price_not_specified' boolean column indicating if the price is missing (NaN).
        - Resets the DataFrame index after filtering.

    Args:
        df (pd.DataFrame): The raw products DataFrame.

    Returns:
        pd.DataFrame: The cleaned and transformed DataFrame.
    """
    try:
        #ObjectId of mongo is an invalid value that gives writing errors now is a str
        df['_id'] = df['_id'].astype(str)
        # print(df.dtypes)
        #uniformazione dei dati, tutti i campi del dataframe a lowercase
        df['title'] = df['title'].str.lower()
        # filtraggio del df usando una maschera che prende solo i prodotti che hanno iphone 15 nel title
        # aggiunta del .copy per evitare warning su pandas in modo da usare una copia del df e non una vista (una vista e come lavorare su una reference, questo dava il warning 'SettingWithCopyWarning')
        df = df[df['title'].str.contains(PRODUCT_NAME_FILTERED)].copy()
        #filtraggio emoji
        EMOJI_PATTERN = re.compile(
        "["
        "\U0001F1E0-\U0001F1FF"  # flags (iOS)
        "\U0001F300-\U0001F5FF"  # symbols & pictographs
        "\U0001F600-\U0001F64F"  # emoticons
        "\U0001F680-\U0001F6FF"  # transport & map symbols
        "\U0001F700-\U0001F77F"  # alchemical symbols
        "\U0001F780-\U0001F7FF"  # Geometric Shapes Extended
        "\U0001F800-\U0001F8FF"  # Supplemental Arrows-C
        "\U0001F900-\U0001F9FF"  # Supplemental Symbols and Pictographs
        "\U0001FA00-\U0001FA6F"  # Chess Symbols
        "\U0001FA70-\U0001FAFF"  # Symbols and Pictographs Extended-A
        "\U00002702-\U000027B0"  # Dingbats
        "\U000024C2-\U0001F251" 
        "]+")

        df['title'] = df['title'].str.replace(EMOJI_PATTERN, '', regex=True)

        df['city'] = df['city'].str.lower()

        df['province'] = df['province'].str.lower().str.replace( r'[\(\)]', '',regex=True)

        # creazione di nuova colonna impostata a false (non serve)
        # df['shipping_available'] = False
        # questa linea di codice crea una nuova colonna e restituisce una nuova Series di booleani, quindi inserisce automaticamente i valori true e false se price contiene "Spedizione disponibile"
        df['shipping_available'] = df['price'].str.contains('Spedizione disponibile')

        #esecuzione di un espressione regolare che filtra solo i numeri e dopo casta le stringhe che contengono numeri in valori numerici e le stringhe di testo in NaN automaticamente.
        df['price'] = df['price'].str.replace(r'\D', '', regex=True)
        df['price'] = pd.to_numeric(df['price'], errors="coerce")
        # quando si filtra e si riassegna con una maschera non serve il to_copy()
        df = df[df['price'] > PRDODUCT_MIN_PRICE]

        # creazione colonna 'price_not_specified' che genera una Series di booleani che contiene True se il prezzo e NaN o false altrimenti
        df['price_not_specified'] = df['price'].isnull()
        # reset dell indice del dataframe con nuovi valori da 0 a X e drop della colonna con i vecchi indici (es vecchi indici 0 2 4 5, si resetta e diventa 0 1 2 3)
        df = df.reset_index(drop = True)
        return df
    except Exception as e:
        logger.error(f"Pandas error on cleaning data: {e}")

def check_connection_to_pg():
    logger.info('Checking connection to postgres...')
    try:
        engine = create_engine(f"postgresql+psycopg2://{POSTGRES_USER_PRODUCTS}:{POSTGRES_PASSWORD_PRODUCTS}@{POSTGRES_HOST_PRODUCTS}:{POSTGRES_PORT_PRODUCTS}/{POSTGRES_DB_PRODUCTS}", echo=True)
        Session = sessionmaker(bind=engine)
        session = Session()
        session.execute(text("SELECT 1"))
        logger.info("PostgreSQL connection successful!")
    except Exception as e:
       logger.error(f"PostgreSQL connection error: {e}")
    finally:
        session.close()

def writing_dataframe_to_pg(df):
    """
    Writes the provided DataFrame to a PostgreSQL database table.

    The function creates a SQLAlchemy engine using environment variables for connection parameters,
    and writes the DataFrame to the 'scraped_products' table using the pandas to_sql() method.
    If the table already exists, it will be replaced. Logs success or error messages.

    Args:
        df (pd.DataFrame): The cleaned DataFrame to be written to PostgreSQL.

    Returns:
        None
    """

    logger.info('Writing dataframe to postgres...')
    try:
        # Create the database connection engine inside the function
        engine = create_engine(f"postgresql+psycopg2://{POSTGRES_USER_PRODUCTS}:{POSTGRES_PASSWORD_PRODUCTS}@{POSTGRES_HOST_PRODUCTS}:{POSTGRES_PORT_PRODUCTS}/{POSTGRES_DB_PRODUCTS}")
        # Use the to_sql() method to write the DataFrame
        df.to_sql(name='scraped_products', con=engine, if_exists='replace', index=False)
        logger.info("Successfully wrote data to PostgreSQL.")

    except Exception as e:
        logger.error(f"PostgreSQL writing error: {e}")
    # print(df)

@app.post("/transform")
def exec_trasform():
    try:
        # Entry point of the transformer-service script
        logger.info("Starting trasformer-service...")
        # 1. Connect to MongoDB for reading data.
        list = get_products_from_mongo()
        # 2. Create a dataframe object from the list retured by mongo
        df = pd.DataFrame(list)
        if df is not None and not df.empty:
            # 2. Clean and transform data using Pandas e NumPy.
            df = clean_data(df)
            # 3. Test connection to PostgreSQL
            check_connection_to_pg()
            # 4. write cleaned data to PostgresSQL
            writing_dataframe_to_pg(df)
            # 5. Convert to json and return
            # obj = df.to_json()
            obj = df.to_dict('records')
            logger.info("Finished job trasformer-service.")
            return {"Status": "success, trasformation and loading completed.", "data cleaned" : obj}
        else:
            return {"status": "no_data", "message": "No data found in MongoDB."}
            # print(df)
    except Exception as e:
        logger.error(f"Main program error: {e}")
        return {"status": "error", "message": str(e)}

if __name__ == "__main__":
    exec_trasform()