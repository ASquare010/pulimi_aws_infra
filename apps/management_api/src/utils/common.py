import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..')))
from shared_lib.logger import logger

PORT:int = int(os.getenv("PORT", "5000"))
