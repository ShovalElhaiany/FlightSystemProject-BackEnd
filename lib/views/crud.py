from venv import logger

from flask import jsonify, request

from lib.business_logic.crud.add import BusinessLogicAdd
from lib.business_logic.crud.delete import BusinessLogicRemove
from lib.business_logic.crud.get import BusinessLogicGet
from lib.business_logic.crud.update import BusinessLogicUpdate
from utils.entity_fields import extracts_entity_fields
from utils.user_manage import create_user


class CrudViews():
        
    # Retrieves and returns data for a specific entity
    @staticmethod
    def get_entity(entity_id):
        try:
            entity_fields = extracts_entity_fields(request)
            entity_data = BusinessLogicGet.get_entity_data(entity_id, entity_fields)

            logger.info(entity_data)
            return jsonify(entity_data)
        except Exception as e:
            logger.error(e)
            return jsonify({'error': 'Failed to retrieve entity data.'}), 500

    # Retrieves and returns data for all entities
    @staticmethod    
    def get_entities():
        try:
            entity_fields = extracts_entity_fields(request)
            entities_data = BusinessLogicGet.get_entities_data(entity_fields)

            logger.info(entities_data)
            return jsonify(entities_data)
        except Exception as e:
            logger.error(e)
            return jsonify({'error': 'Failed to retrieve entities data.'}), 500

    # Adds a new entity to the system
    @staticmethod
    def add_entity():
        try:
            entity_data = request.get_json()
            entity_fields = extracts_entity_fields(request)
            entity_name = entity_fields['name']
            if entity_name in ['Customers', 'AirlineCompanies', 'Administrators']:
                create_user(entity_name)
            response = BusinessLogicAdd.add_entity_data(entity_data, entity_fields)

            logger.info(response)
            return jsonify(response)
        except Exception as e:
            logger.error(e)
            return jsonify({'error': 'Failed to add entity.'}), 500

    # Adds multiple entities to the system
    @staticmethod
    def add_entities():
        try:
            entity_fields = extracts_entity_fields(request)
            entities_data = request.get_json()
            entity_name = entity_fields['name']
            if entity_name in ['Customers', 'AirlineCompanies', 'Administrators']:
                create_user(entity_name)
            response = BusinessLogicAdd.add_entities_data(entities_data, entity_fields)

            logger.info(response)
            return jsonify(response)
        except Exception as e:
            logger.error(e)
            return jsonify({'error': 'Failed to add entities.'}), 500

    # Updates data for a specific entity
    @staticmethod
    def update_entity(entity_id):
        try:
            entity_fields = extracts_entity_fields(request)
            entity_data = request.get_json()
            response = BusinessLogicUpdate.update_entity_data(entity_id, entity_data, entity_fields)

            logger.info(response)
            return jsonify(response)
        except Exception as e:
            logger.error(e)
            return jsonify({'error': 'Failed to update entity.'}), 500

    # Updates data for multiple entities
    @staticmethod
    def update_entities():
        try:
            entity_fields = extracts_entity_fields(request)
            entities_data = request.get_json()
            response = BusinessLogicUpdate.update_entities_data(entities_data, entity_fields)

            logger.info(response)
            return jsonify(response)
        except Exception as e:
            logger.error(e)
            return jsonify({'error': 'Failed to update entities.'}), 500

    # Removes a specific entity from the system
    @staticmethod
    def remove_entity(entity_id):
        try:
            entity_fields = extracts_entity_fields(request)
            response = BusinessLogicRemove.remove_entity_data(entity_id, entity_fields)

            logger.info(response)
            return jsonify(response)
        except Exception as e:
            logger.error(e)
            return jsonify({'error': 'Failed to remove entity.'}), 500

    # Removes all entities from the system
    @staticmethod
    def remove_entities():
        try:
            entity_fields = extracts_entity_fields(request)
            response = BusinessLogicRemove.remove_entities_data(entity_fields)

            logger.info(response)
            return jsonify(response)
        except Exception as e:
            logger.error(e)
            return jsonify({'error': 'Failed to remove entities.'}), 500