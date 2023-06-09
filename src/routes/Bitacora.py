from flask import Blueprint, jsonify, request
import uuid
from models.entities.Bitacora import Bitacora
#Models
from models.BitacoraModel import BitacoraModel


main = Blueprint('bitacora_blueprint', __name__)

@main.route('/')
def get_bitacora():
    try:
        bitacora = BitacoraModel.get_bitacora()
        return jsonify(bitacora)
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
    
@main.route('/<id>')
def get_bitacora(id):
    try:
        bitacora = BitacoraModel.get_bitacora(id)
        if bitacora != None:
            return jsonify(bitacora)
        else:
            return jsonify({}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
    
@main.route('/add', methods=['POST'])
def add_bitacora():
    try:
        id = request.json['id']
        fechahora = request.json['fechahora']
        accion = request.json['accion']
        nombre_tabla = request.json['nombre_tabla']

        bitacora = Bitacora(id, fechahora, accion, nombre_tabla)
        
        affected_rows = BitacoraModel.add_bitacora(bitacora)

        if affected_rows == 1:
            return jsonify(bitacora.id)
        else:
            return jsonify({'message': "Error on insert"}), 500
        ############# validar datos ######################
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
    
@main.route('/update/<id>', methods=['PUT'])
def update_bitacora(id):
    try:
        id = request.json['id']
        fechahora = request.json['fechahora']
        accion = request.json['accion']
        nombre_tabla = request.json['nombre_tabla']
        
        bitacora = Bitacora(id, fechahora, accion, nombre_tabla)
        
        affected_rows = BitacoraModel.update_bitacora(bitacora)

        if affected_rows == 1:
            return jsonify(bitacora.id)
        else:
            return jsonify({'message': "No paciente updated"}), 404
        ############# validar datos ######################
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
