from lib.dataAccessLayer.crudDal import get_entity, update_entity
from logs.log import logger

def update_entity_data(entity_id, entity_data, entity_fields):
    """Updates entity data based on the given entity ID, data, and fields.

    Args:
        entity_id (int): The ID of the entity to be updated.
        entity_data (dict): The data containing the updates for the entity.
        entity_fields (dict): The fields associated with the entity.

    Returns:
        dict: A dictionary containing either an error message or a success message.

    Raises:
        None

    """
    if 'id' not in entity_data:
        logger.warning('Missing required field: id')
        return {'error': 'Missing required field: id'}

    entity = get_entity(entity_fields['model'], entity_id)
    if not entity:
        logger.warning(f'{entity_fields["name"]} not found')
        return {'error': f'{entity_fields["name"]} not found'}

    entity_data_filtered = {field: entity_data[field] for field in entity_fields['fields'] if field != 'id'}
    update_entity(entity, entity_data_filtered)

    logger.debug(f'{entity_fields["name"]} updated successfully')
    return {f'{entity_fields["name"]} updated successfully'}

def update_entities_data(entities_data, entity_fields):
    """Updates multiple entities' data based on the given entity data and fields.

    Args:
        entities_data (list): A list of dictionaries containing the data for multiple entities.
        entity_fields (dict): The fields associated with the entities.

    Returns:
        dict: A dictionary containing a list of responses for each entity update.

    Raises:
        None

    """
    responses = []
    for entity_data in entities_data:
        entity_id = entity_data.get('id')
        if entity_id is None:
            logger.warning('Missing required field: id')
            responses.append({'error': 'Missing required field: id'})
            continue

        response = update_entity_data(entity_id, entity_data, entity_fields)
        responses.append(response)

    logger.debug('The entities have been successfully updated!')
    return {'responses': responses}
