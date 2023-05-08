from flask import Blueprint, jsonify, request
import uuid
from models.entities.Traslados import Traslados
#Models
from models.TrasladosModel import TrasladosModel


main = Blueprint('traslados_blueprint', __name__)

@main.route('/')
def get_traslados():
    try:
        traslados = TrasladosModel.get_traslados()
        return jsonify(traslados)
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
    
@main.route('/<id_traslados>')
def get_traslados(id_traslados):
    try:
        traslados = TrasladosModel.get_traslados(id_traslados)
        if traslados != None:
            return jsonify(traslados)
        else:
            return jsonify({}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
    
@main.route('/add', methods=['POST'])
def add_traslados():
    try:
        id_traslados = request.json['id_traslados']
        id_medico = request.json['id_medico']
        hospital_anterior = request.json['hospital_anterior']
        hospital_nuevo = request.json['hospital_nuevo']
        fecha_traslado = request.json['fecha_traslado']

        traslados = Traslados(id_traslados, id_medico, hospital_anterior, hospital_nuevo, fecha_traslado)
        
        affected_rows = TrasladosModel.add_traslados(traslados)

        if affected_rows == 1:
            return jsonify(traslados.id_traslados)
        else:
            return jsonify({'message': "Error on insert"}), 500
        ############# validar datos ######################
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
    
@main.route('/update/<id_traslados>', methods=['PUT'])
def update_traslados(id_traslados):
    try:
        id_traslados = request.json['id_traslados']
        id_medico = request.json['id_medico']
        hospital_anterior = request.json['hospital_anterior']
        hospital_nuevo = request.json['hospital_nuevo']
        fecha_traslado = request.json['fecha_traslado']
        
        traslados = Traslados(id_traslados, id_medico, hospital_anterior, hospital_nuevo, fecha_traslado)
        
        affected_rows = TrasladosModel.update_traslados(traslados)

        if affected_rows == 1:
            return jsonify(traslados.id_traslados)
        else:
            return jsonify({'message': "No paciente updated"}), 404
        ############# validar datos ######################
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@main.route('/<id_traslados>')
def get_traslados(id_traslados):
    try:
        traslados = TrasladosModel.get_traslados(id_traslados)
        if traslados != None:
            return jsonify(traslados)
        else:
            return jsonify({}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
    