from lib.data_access_layer.crud import get_entities, get_entity
from logs.log import logger


class BusinessLogicGet():

    @staticmethod
    def get_entity_data(entity_id, entity_fields):
        """
        Retrieves data for a specific entity.

        Args:
            entity_id (int): The ID of the entity to retrieve.
            entity_fields (dict): A dictionary containing information about the entity.

        Returns:
            dict: A dictionary containing the entity data.
        """
        entity = get_entity(entity_fields['model'], entity_id)
        if entity:
            logger.debug(f'{entity_fields["name"]} is found')
            return {field: getattr(entity, field) for field in entity_fields['fields']}
        else:
            logger.warning(f'{entity_fields["name"]} not found')
            return {'error': f'{entity_fields["name"]} not found'}

    @staticmethod
    def get_entities_data(entity_fields):
        """
        Retrieves data for all entities of a specific type.

        Args:
            entity_fields (dict): A dictionary containing information about the entity.

        Returns:
            list or dict: A list of dictionaries containing the entity data, or an error dictionary if no entities are found.
        """
        entities = get_entities(entity_fields['model'])
        if entities:
            logger.debug('All entities are found')
            return [{field: getattr(entity, field) for field in entity_fields['fields']} for entity in entities]
        else:
            logger.warning('Entities are not found')
            return {'error': 'Entities are not found'}
