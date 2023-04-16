from flask_login import login_user, logout_user, login_required
from flask import Blueprint, jsonify, request
from models.entities.User import User
from models.UserModel import UserModel
import uuid

main = Blueprint('movie_blueprint', __name__)

@main.route('/signup', methods=['POST'])
def signup():
    # Aquí se debe escribir el código para registrar a un nuevo usuario en la base de datos
    try:
        email = request.json['email']
        nombre = request.json['nombre']
        apellido=request.json['apellido']        
        contrasena = request.json['contrasena']

        usuario = User(email, nombre, apellido, contrasena)
        
        affected_rows = UserModel.add_user(usuario)

        if affected_rows == 1:
            return jsonify({'message': 'El usuario ha sido registrado exitosamente.'}), 201
        else:
            return jsonify({'message': "Error on insert"}), 500
        ############# validar datos ######################
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@main.route('/login', methods=['POST'])
def login():
    email = request.json.get('email', None)
    password = request.json.get('password', None)

    # Verifica las credenciales de inicio de sesión
    user = User.query.filter_by(email=email).first()
    if user is None or not user.check_password(password):
        return jsonify({'message': 'Credenciales inválidas.'}), 401

    # Inicia sesión con Flask-Login
    login_user(user)

    return jsonify({'message': 'Sesión iniciada exitosamente.'}), 200

@main.route('/logout')
@login_required
def logout():
    # Cierra la sesión con Flask-Login
    logout_user()

    return jsonify({'message': 'Sesión cerrada exitosamente.'}), 200
