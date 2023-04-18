from flask import Blueprint, jsonify, request
import uuid
from models.entities.Paciente import Paciente
#Models
from models.PacienteModel import PacienteModel


main = Blueprint('paciente_blueprint', __name__)

@main.route('/')
def get_pacientes():
    try:
        pacientes = PacienteModel.get_pacientes()
        return jsonify(pacientes)
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
    
@main.route('/<id_paciente>')
def get_paciente(id_paciente):
    try:
        paciente = PacienteModel.get_paciente(id_paciente)
        if paciente != None:
            return jsonify(paciente)
        else:
            return jsonify({}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
    
@main.route('/add', methods=['POST'])
def add_paciente():
    try:
        id_paciente = request.json['id_paciente']
        dpi = request.json['dpi']
        nombre=request.json['nombre']
        telefono = request.json['telefono']
        direccion = request.json['direccion']
        imc = request.json['imc']
        altura = request.json['altura']
        peso = request.json['peso']
        adiccion = request.json['adiccion']
        enfermedades_hereditarias = request.json['enfermedades_hereditarias']
        tratamientos = request.json['tratamientos']
        medico_asignado = request.json['medico_asignado']
        hospital_asignado = request.json['hospital_asignado']
        enfermedades = request.json['enfermedades']
        evolucion_enfermedad = request.json['evolucion_enfermedad']
        fecha_ingreso = request.json['fecha_ingreso']
        fecha_salida = request.json['fecha_salida']
        correo = request.json['correo']
        contrasena = request.json['contrasena']

        paciente = Paciente(id_paciente, dpi, nombre, telefono, direccion, imc, altura, peso, adiccion, enfermedades_hereditarias, tratamientos, medico_asignado, hospital_asignado, enfermedades, evolucion_enfermedad, fecha_ingreso, fecha_salida, correo, contrasena)
        
        affected_rows = PacienteModel.add_paciente(paciente)

        if affected_rows == 1:
            return jsonify(paciente.id_paciente)
        else:
            return jsonify({'message': "Error on insert"}), 500
        ############# validar datos ######################
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
    
@main.route('/update/<id_paciente>', methods=['PUT'])
def update_paciente(id_paciente):
    try:
        id_paciente = request.json['id_paciente']
        dpi = request.json['dpi']
        nombre=request.json['nombre']
        telefono = request.json['telefono']
        direccion = request.json['direccion']
        imc = request.json['imc']
        altura = request.json['altura']
        peso = request.json['peso']
        adiccion = request.json['adiccion']
        enfermedades_hereditarias = request.json['enfermedades_hereditarias']
        tratamientos = request.json['tratamientos']
        medico_asignado = request.json['medico_asignado']
        hospital_asignado = request.json['hospital_asignado']
        enfermedades = request.json['enfermedades']
        evolucion_enfermedad = request.json['evolucion_enfermedad']
        fecha_ingreso = request.json['fecha_ingreso']
        fecha_salida = request.json['fecha_salida']
        correo = request.json['correo']
        contrasena = request.json['contrasena']
        
        paciente = Paciente(id_paciente, dpi, nombre, telefono, direccion, imc, altura, peso, adiccion, enfermedades_hereditarias, tratamientos, medico_asignado, hospital_asignado, enfermedades, evolucion_enfermedad, fecha_ingreso, fecha_salida, correo, contrasena)
        
        affected_rows = PacienteModel.update_paciente(paciente)

        if affected_rows == 1:
            return jsonify(paciente.id_paciente)
        else:
            return jsonify({'message': "No paciente updated"}), 404
        ############# validar datos ######################
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
    
@main.route('/delete/<id_paciente>', methods=['DELETE'])
def delete_paciente(id_paciente):
    try:

        paciente = Paciente(id_paciente)

        affected_rows = PacienteModel.delete_paciente(paciente)

        if affected_rows == 1:
            return jsonify(paciente.id_paciente)
        else:
            return jsonify({'message': "No movie deleted"}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
