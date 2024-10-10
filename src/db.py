import MySQLdb
import os
from dotenv import load_dotenv

# Cargar las variables de entorno del archivo .env
load_dotenv()

def get_db():
    db = MySQLdb.connect(
        host=os.getenv("DB_HOST"),          # Cargar el host desde las variables de entorno
        user=os.getenv("DB_USER"),          # Cargar el usuario desde las variables de entorno
        password=os.getenv("DB_PASSWORD"),  # Cargar la contraseña desde las variables de entorno
        database=os.getenv("DB_NAME")       # Cargar el nombre de la base de datos desde las variables de entorno
    )
    return db
