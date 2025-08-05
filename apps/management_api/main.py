from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Management API is running"}

@app.get("/status")
def get_status():
    return {"status": "ok", "version": "v1"}
