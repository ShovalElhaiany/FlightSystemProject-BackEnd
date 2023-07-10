from lib.dataAccessLayer.crudDal import remove_entity, remove_all_entities, get_entity
from logs.log import logger

def remove_entity_data(entity_id, entity_fields):
    """
    Removes a specific entity from the database.

    Parameters:
    - entity_id (int): The ID of the entity to be removed.
    - entity_fields (dict): A dictionary containing information about the entity, including the model and name.

    Returns:
    - dict: A dictionary with a success message if the entity is successfully removed, or an error message if the entity is not found.
    """
    entity_model = entity_fields['model']
    entity_name = entity_fields['name']
    entity = get_entity(entity_model, entity_id)
    if entity:
        remove_entity(entity)
        logger.debug(f'{entity_name} removed successfully')
        return {f'{entity_name} removed successfully'}
    else:
        logger.warning(f'{entity_name} not found')
        return {'error': f'{entity_name} not found'}

def remove_all_entities_data(entity_fields):
    """
    Removes all entities of a specific type from the database.

    Parameters:
    - entity_fields (dict): A dictionary containing information about the entity, including the model and name.

    Returns:
    - dict: A dictionary with a success message indicating that all entities have been removed.
    """
    entity_model = entity_fields['model']
    entity_name = entity_fields['name']
    remove_all_entities(entity_model)
    logger.debug(f'All {entity_name}s removed successfully')
    return {f'All {entity_name}s removed successfully'}
