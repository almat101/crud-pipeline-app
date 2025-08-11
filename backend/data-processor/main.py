from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/scrape")
def scrape():
    return {"message": "Scrape success"}
