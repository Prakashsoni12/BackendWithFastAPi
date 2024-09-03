from typing import Dict
import json

Database = {}

def store_content(chat_id: str, content: str) -> None:
    Database[chat_id] = {"content": content}

def retrive_content(chat_id: str) -> Dict[str, str]:
    return Database.get(chat_id)