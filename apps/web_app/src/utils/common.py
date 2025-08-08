import  os

BACKEND_HOST:str = os.getenv("BACKEND_HOST", "management_api")
BACKEND_PORT:int = int(os.getenv("BACKEND_PORT", "5000"))
PORT:int = int(os.getenv("PORT", "8501"))
API_URL = f"http://{BACKEND_HOST}:{BACKEND_PORT}"