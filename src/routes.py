from flask import jsonify, request
from models import create_user, create_department, create_project, get_all_users, get_departments, calculate_average_salary, count_employees_by_department, get_birthdays_this_month
from auth import login_user # Importa la función de autenticación
from validations import validate_email, validate_password
from flask_jwt_extended import jwt_required

def init_routes(app):
    @app.route('/users', methods=['POST'])
    def register_user():
        data = request.get_json()

        # Validaciones
        if not validate_email(data['email']):
            return jsonify({"message": "Email inválido."}), 400
        if not validate_password(data['password']):
            return jsonify({"message": "La contraseña debe tener al menos 8 caracteres, incluir una letra mayúscula y un número."}), 400
        
        create_user(data['name'], data['email'], data['password'], data['role'], data['salary'], data['hire_date'], data['birth_date'])
        return jsonify({"message": "Usuario registrado exitosamente."}), 201

    # Endpoint para inicio de sesion
    @app.route('/login', methods=['POST'])
    def login():
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')
        # Aquí debes implementar la lógica para validar el usuario
        # Por simplicidad, aquí solo llamamos a la función login_user
        # Deberías agregar validación real (comparar email y password con la base de datos)
        if email and password:
            users = get_all_users()  # Obtén todos los usuarios
            for user in users:
                if user[2] == email and user[3] == password:  # Comparar el email y la contraseña
                    return login_user(email, password)  # Si coinciden, genera el token
            return jsonify({"message": "Credenciales inválidas."}), 401  # Si no coinciden, devuelve un error

    @app.route('/departments', methods=['POST'])
    @jwt_required()
    def register_department():
        data = request.get_json()
        create_department(data['name'], data['manager'])
        return jsonify({"message": "Departamento creado exitosamente."}), 201

    @app.route('/projects', methods=['POST'])
    @jwt_required()
    def register_project():
        data = request.get_json()
        create_project(data['name'], data['start_date'], data['end_date'], data['department_id'])
        return jsonify({"message": "Proyecto creado exitosamente."}), 201

    @app.route('/users', methods=['GET'])
    @jwt_required()
    def get_users():
        users = get_all_users()
        return jsonify(users), 200

    @app.route('/departments', methods=['GET'])
    @jwt_required()
    def list_departments():
        departments = get_departments()
        return jsonify(departments), 200

    @app.route('/average-salary', methods=['GET'])
    @jwt_required()
    def average_salary():
        average = calculate_average_salary()
        return jsonify({"average_salary": average[0]}), 200

    @app.route('/count-employees', methods=['GET'])
    @jwt_required()
    def count_employees():
        counts = count_employees_by_department()
        return jsonify(counts), 200

    @app.route('/birthdays', methods=['GET'])
    @jwt_required()
    def birthdays():
        birthdays = get_birthdays_this_month()
        return jsonify(birthdays), 200
