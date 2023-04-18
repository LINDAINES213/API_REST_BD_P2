from flask import Blueprint, jsonify, request, session
from database.db import get_connection
from models.entities.User import User
from models.ModelUser import UserModel
from werkzeug.security import check_password_hash


main = Blueprint('paciente_blueprint', __name__)

@main.route('/signup', methods=['POST'])
def signup():
    # Aquí se debe escribir el código para registrar a un nuevo usuario en la base de datos
    try:
        email = request.json['email']
        username = request.json['username']
        contrasena = request.json['contrasena']

        usuario = User(email, username, contrasena)
        
        affected_rows = UserModel.signup(usuario)

        if affected_rows == 1:
            return jsonify({'message': 'El usuario ha sido registrado exitosamente.'}), 201
        else:
            return jsonify({'message': "Error on insert"}), 500
        ############# validar datos ######################
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500