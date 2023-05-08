from flask import Blueprint, jsonify, request
import uuid
from models.entities.Medicos import Medicos
#Models
from models.MedicosModel import MedicosModel


main = Blueprint('medicos_blueprint', __name__)

@main.route('/')
def get_medicos():
    try:
        medicos = MedicosModel.get_medicos()
        return jsonify(medicos)
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
    
@main.route('/<id_medico>')
def get_medicos(id_medico):
    try:
        medicos = MedicosModel.get_medicos(id_medico)
        if medicos != None:
            return jsonify(medicos)
        else:
            return jsonify({}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
    
@main.route('/add', methods=['POST'])
def add_medicos():
    try:
        id_medico = request.json['id_paciente']
        dpi = request.json['dpi']
        nombre = request.json['nombre']
        telefono = request.json['telefono']
        direccion = request.json['direccion']
        num_colegiado = request.json['num_colegiado']
        especialidades = request.json['especialidades']
        hospital = request.json['hospital']
        fecha_contratacion = request.json['fecha_contratacion']
        correo = request.json['correo']
        contrasena = request.json['contrasena']

        medicos = Medicos(id_medico, dpi, nombre, telefono, direccion, num_colegiado, especialidades, hospital, fecha_contratacion, correo, contrasena)
        
        affected_rows = MedicosModel.add_medicos(medicos)

        if affected_rows == 1:
            return jsonify(medicos.id_medico)
        else:
            return jsonify({'message': "Error on insert"}), 500
        ############# validar datos ######################
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
    
@main.route('/update/<id_medico>', methods=['PUT'])
def update_medicos(id_medico):
    try:
        id_medico = request.json['id_paciente']
        dpi = request.json['dpi']
        nombre = request.json['nombre']
        telefono = request.json['telefono']
        direccion = request.json['direccion']
        num_colegiado = request.json['num_colegiado']
        especialidades = request.json['especialidades']
        hospital = request.json['hospital']
        fecha_contratacion = request.json['fecha_contratacion']
        correo = request.json['correo']
        contrasena = request.json['contrasena']
        
        medicos = Medicos(id_medico, dpi, nombre, telefono, direccion, num_colegiado, especialidades, hospital, fecha_contratacion, correo, contrasena)
        
        affected_rows = MedicosModel.update_medicos(medicos)

        if affected_rows == 1:
            return jsonify(medicos.id_medico)
        else:
            return jsonify({'message': "No paciente updated"}), 404
        ############# validar datos ######################
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
    
@main.route('/delete/<id_medico>', methods=['DELETE'])
def delete_medicos(id_medico):
    try:

        medicos = Medicos(id_medico)

        affected_rows = MedicosModel.delete_medicos(medicos)

        if affected_rows == 1:
            return jsonify(medicos.id_medico)
        else:
            return jsonify({'message': "No movie deleted"}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500