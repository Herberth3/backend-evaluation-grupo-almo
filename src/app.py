from flask import Flask
from flask_jwt_extended import JWTManager
from db import get_db
from routes import init_routes

app = Flask(__name__)

# Configuración de JWT
app.config['JWT_SECRET_KEY'] = 'almo'  # Cambia esta clave por una segura

# Inicializar JWT
jwt = JWTManager(app)

# Inicializar la base de datos
db = get_db()

# Inicializar rutas
init_routes(app)

if __name__ == '__main__':
    app.run(debug=True)
