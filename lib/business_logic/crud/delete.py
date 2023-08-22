from lib.data_access_layer.crud import (get_entity, delete_entities,
                                        delete_entity)
from logs.log import logger


class BusinessLogicDelete():

    @staticmethod
    def delete_entity_data(entity_id, entity_fields):
        """
        Deletes a specific entity from the database.

        Parameters:
        - entity_id (int): The ID of the entity to be deleted.
        - entity_fields (dict): A dictionary containing information about the entity, including the model and name.

        Returns:
        - dict: A dictionary with a success message if the entity is successfully deleted, or an error message if the entity is not found.
        """
        entity_model = entity_fields['model']
        entity_name = entity_fields['name']
        entity = get_entity(entity_model, entity_id)
        if entity:
            delete_entity(entity)
            logger.debug(f'{entity_name} deleted successfully')
            return {'msg': f'{entity_name} deleted successfully'}
        else:
            logger.warning(f'{entity_name} not found')
            return {'error': f'{entity_name} not found'}

    @staticmethod
    def delete_entities_data(entity_fields):
        """
        Deletes all entities of a specific type from the database.

        Parameters:
        - entity_fields (dict): A dictionary containing information about the entity, including the model and name.

        Returns:
        - dict: A dictionary with a success message indicating that all entities have been deleted.
        """
        entity_model = entity_fields['model']
        entity_name = entity_fields['name']
        delete_entities(entity_model)
        logger.debug(f'All {entity_name}s deleted successfully')
        return {'msg': f'All {entity_name}s deleted successfully'}
