from flask import jsonify, request
from flask_jwt_extended import create_access_token

def login_user(email, password):
    # Aquí debes validar el usuario con la base de datos
    # Si es válido, genera un token
    token = create_access_token(identity=email)
    return jsonify(access_token=token), 200
