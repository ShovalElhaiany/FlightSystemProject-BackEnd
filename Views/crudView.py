from flask import jsonify, request
from businessLogic.getBl import *
from businessLogic.addBl import *
from businessLogic.updateBl import *
from businessLogic.deleteBl import *
from businessLogic.searchesBl import *
from .entityFields import *

def get_entity_endpoint(entity_id):
    entity_data = get_entity_data(entity_id, entity_fields)
    return jsonify(entity_data)

def get_all_entities_endpoint():
    entities_data = get_all_entities_data(entity_fields)
    return jsonify(entities_data)

def add_entity_endpoint():
    entity_data = request.get_json()
    response = add_entity_data(entity_data, entity_fields)
    return jsonify(response)

def add_entities_endpoint():
    entities_data = request.get_json()
    response = add_entities_data(entities_data, entity_fields)
    return jsonify(response)

def update_entity_endpoint(entity_id):
    entity_data = request.get_json()
    response = update_entity_data(entity_id, entity_data, entity_fields)
    return jsonify(response)

def update_entities_endpoint():
    entities_data = request.get_json()
    response = update_entities_data(entities_data, entity_fields)
    return jsonify(response)

def remove_entity_endpoint(entity_id):
    response = remove_entity_data(entity_id, entity_fields)
    return jsonify(response)

def remove_all_entities_endpoint():
    response = remove_all_entities_data(entity_fields)
    return jsonify(response)