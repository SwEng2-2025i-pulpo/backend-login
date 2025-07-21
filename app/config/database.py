from pymongo import MongoClient
from app.core.config import get_settings

settings = get_settings()

# Conectar a MongoDB usando la URI del .env
client = MongoClient(settings.mongo_uri)

# Seleccionar la base de datos
db = client["conectacare_caretaker"]

# Colección principal de usuarios
user_collection = db["caretaker"]