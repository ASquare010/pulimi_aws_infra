import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..')))
from shared_lib.logger import logger

BACKEND_HOST:str = os.getenv("BACKEND_HOST", "localhost")
BACKEND_PORT:int = int(os.getenv("BACKEND_PORT", "5000"))
PORT:int = int(os.getenv("PORT", "8501"))
API_URL = f"http://{BACKEND_HOST}:{BACKEND_PORT}"