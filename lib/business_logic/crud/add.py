from lib.data_access_layer.crud import add_entities, add_entity
from logs.log import logger


class BusinessLogicAdd():
    
    @staticmethod
    def add_entity_data(entity_data, entity_fields):
        """
        Adds a single entity to the database.

        Args:
            entity_data (dict): The data of the entity to be added.
            entity_fields (dict): Information about the entity's fields and model.

        Returns:
            dict: A dictionary with a success message or an error message if an ID is specified.

        Raises:
            None
        """
        if 'id' in entity_data:
            logger.warning('Cannot specify id when creating a new entity')
            return {'error': 'Cannot specify id when creating a new entity'}

        entity_data_filtered = {field: entity_data[field] for field in entity_fields['fields'] if field != 'id'}
        add_entity(entity_fields['model'], entity_data_filtered)
        logger.debug(f'{entity_fields["name"]} added successfully')
        return {f'{entity_fields["name"]} added successfully'}

    @staticmethod
    def add_entities_data(entities_data, entity_fields):
        """
        Adds multiple entities to the database.

        Args:
            entities_data (list): A list of entity data dictionaries.
            entity_fields (dict): Information about the entity's fields and model.

        Returns:
            dict: A dictionary with a success message or an error message if an ID is specified.

        Raises:
            None
        """
        entities_data_filtered = [
            {field: entity_data[field] for field in entity_fields['fields'] if field != 'id'}
            for entity_data in entities_data
            if 'id' not in entity_data
        ]

        if any('id' in entity_data for entity_data in entities_data):
            logger.warning('Cannot specify id when creating a new entity')
            return {'error': 'Cannot specify id when creating a new entity'}

        add_entities(entity_fields['model'], entities_data_filtered)
        logger.debug(f'{entity_fields["name"]}s successfully added')
        return {f'{entity_fields["name"]}s successfully added'}
