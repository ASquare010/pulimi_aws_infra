from fastapi import FastAPI
from src.utils.pymodels import Item
from src.utils.common import PORT
from shared_lib.logger import logger 

# -----------------------------------

app = FastAPI()

# In-memory list of items
items = []


@app.get("/")
def read_root():
    logger.info("Root endpoint hit.")
    return {"message": "Management API is running"}

@app.get("/items")
def get_items():
    logger.info("Retrieving items.")
    return items

@app.post("/items")
def add_item(item: Item):
    logger.info(f"Adding item: {item.item}")
    items.append(item.item)
    return {"status": "added", "item": item.item}

@app.get("/status")
def get_status():
    return {"status": "ok", "version": "v1"}


if __name__ == "__main__":
    import uvicorn
    logger.info("Starting Management API on port 5000")
    uvicorn.run(app, host="0.0.0.0", port=PORT)
