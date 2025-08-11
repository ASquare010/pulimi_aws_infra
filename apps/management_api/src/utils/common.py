import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..')))
from shared_lib.logger import logger

PORT:int = int(os.getenv("PORT", "5000"))


def load_system_message(dir_path: str = "../agent_prompt") -> dict:
    messages = {}

    for file_name in os.listdir(dir_path):
        if file_name.endswith(".md"): 
            file_path = os.path.join(dir_path, file_name)
            
            with open(file_path, "r", encoding="utf-8") as file:
                content = file.read()
                messages[os.path.splitext(file_name)[0]] = content
    
    return messages