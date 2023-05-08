from flask import Blueprint, jsonify, request
import uuid
from models.entities.Medicamentos import Medicamentos
#Models
from models.MedicamentosModel import MedicamentosModel


main = Blueprint('medicamentos_blueprint', __name__)

@main.route('/')
def get_medicamentos():
    try:
        medicamentos = MedicamentosModel.get_medicamentos()
        return jsonify(medicamentos)
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
    
@main.route('/<id>')
def get_medicamentos(id):
    try:
        medicamentos = MedicamentosModel.get_medicamentos(id)
        if medicamentos != None:
            return jsonify(medicamentos)
        else:
            return jsonify({}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
    
@main.route('/add', methods=['POST'])
def add_medicamentos():
    try:
        id = request.json['id']
        nombre = request.json['nombre']
        cantidad_actual = request.json['cantidad_actual']
        cantidad_necesaria = request.json['cantidad_necesaria']
        necesita_compra = request.json['necesita_compra']
        hospital = request.json['hospital']

        medicamentos = Medicamentos(id, nombre, cantidad_actual, cantidad_necesaria, necesita_compra, hospital)
        
        affected_rows = MedicamentosModel.add_medicamentos(medicamentos)

        if affected_rows == 1:
            return jsonify(medicamentos.id)
        else:
            return jsonify({'message': "Error on insert"}), 500
        ############# validar datos ######################
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
    
@main.route('/update/<id>', methods=['PUT'])
def update_medicamentos(id):
    try:
        id = request.json['id']
        nombre = request.json['nombre']
        cantidad_actual = request.json['cantidad_actual']
        cantidad_necesaria = request.json['cantidad_necesaria']
        necesita_compra = request.json['necesita_compra']
        hospital = request.json['hospital']
        
        medicamentos = Medicamentos(id, nombre, cantidad_actual, cantidad_necesaria, necesita_compra, hospital)
        
        affected_rows = MedicamentosModel.update_medicamentos(medicamentos)

        if affected_rows == 1:
            return jsonify(medicamentos.id)
        else:
            return jsonify({'message': "No paciente updated"}), 404
        ############# validar datos ######################
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
    
@main.route('/delete/<id>', methods=['DELETE'])
def delete_medicamentos(id):
    try:

        medicamentos = Medicamentos(id)

        affected_rows = MedicamentosModel.delete_medicamentos(medicamentos)

        if affected_rows == 1:
            return jsonify(medicamentos.id)
        else:
            return jsonify({'message': "No movie deleted"}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500