from flask import jsonify, request
from lib.businessLogic.getBl import *
from lib.businessLogic.addBl import *
from lib.businessLogic.updateBl import *
from lib.businessLogic.deleteBl import *
from .entityFields import *

# Retrieves and returns data for a specific entity
def get_entity_view(entity_id):
    try:
        entity_fields = extracts_entity_fields(request)
        entity_data = get_entity_data(entity_id, entity_fields)

        logger.info(entity_data)
        return jsonify(entity_data)
    except Exception as e:
        logger.error(e)
        return jsonify({'error': 'Failed to retrieve entity data.'}), 500

# Retrieves and returns data for all entities
def get_all_entities_view():
    try:
        entity_fields = extracts_entity_fields(request)
        entities_data = get_all_entities_data(entity_fields)

        logger.info(entities_data)
        return jsonify(entities_data)
    except Exception as e:
        logger.error(e)
        return jsonify({'error': 'Failed to retrieve entities data.'}), 500

# Adds a new entity to the system
def add_entity_view():
    try:
        entity_data = request.get_json()
        entity_fields = extracts_entity_fields(request)
        response = add_entity_data(entity_data, entity_fields)

        logger.info(response)
        return jsonify(response)
    except Exception as e:
        logger.error(e)
        return jsonify({'error': 'Failed to add entity.'}), 500

# Adds multiple entities to the system
def add_entities_view():
    try:
        entity_fields = extracts_entity_fields(request)
        entities_data = request.get_json()
        response = add_entities_data(entities_data, entity_fields)

        logger.info(response)
        return jsonify(response)
    except Exception as e:
        logger.error(e)
        return jsonify({'error': 'Failed to add entities.'}), 500

# Updates data for a specific entity
def update_entity_view(entity_id):
    try:
        entity_fields = extracts_entity_fields(request)
        entity_data = request.get_json()
        response = update_entity_data(entity_id, entity_data, entity_fields)

        logger.info(response)
        return jsonify(response)
    except Exception as e:
        logger.error(e)
        return jsonify({'error': 'Failed to update entity.'}), 500

# Updates data for multiple entities
def update_entities_view():
    try:
        entity_fields = extracts_entity_fields(request)
        entities_data = request.get_json()
        response = update_entities_data(entities_data, entity_fields)

        logger.info(response)
        return jsonify(response)
    except Exception as e:
        logger.error(e)
        return jsonify({'error': 'Failed to update entities.'}), 500

# Removes a specific entity from the system
def remove_entity_view(entity_id):
    try:
        entity_fields = extracts_entity_fields(request)
        response = remove_entity_data(entity_id, entity_fields)

        logger.info(response)
        return jsonify(response)
    except Exception as e:
        logger.error(e)
        return jsonify({'error': 'Failed to remove entity.'}), 500

# Removes all entities from the system
def remove_all_entities_view():
    try:
        entity_fields = extracts_entity_fields(request)
        response = remove_all_entities_data(entity_fields)

        logger.info(response)
        return jsonify(response)
    except Exception as e:
        logger.error(e)
        return jsonify({'error': 'Failed to remove entities.'}), 500
