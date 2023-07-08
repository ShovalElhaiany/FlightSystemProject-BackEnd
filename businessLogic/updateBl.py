from dataAccessLayer.crudDal import *
from dataAccessLayer.searchesDal import *

def update_entity_data(entity_id, entity_data, entity_fields):
    if 'id' not in entity_data:
        return {'error': 'Missing required field: id'}

    entity = get_entity(entity_fields['model'], entity_id)
    if entity:
        entity_data_filtered = {field: entity_data[field] for field in entity_fields['fields'] if field != 'id'}
        update_entity(entity, entity_data_filtered)
        return {'message': f'{entity_fields["name"]} updated successfully'}
    else:
        return {'error': f'{entity_fields["name"]} not found'}

def update_entities_data(entities_data, entity_fields):
    responses = []
    for entity_data in entities_data:
        entity_id = entity_data.get('id')
        if entity_id is None:
            responses.append({'error': 'Missing required field: id'})
            continue

        response = update_entity_data(entity_id, entity_data, entity_fields)
        responses.append(response)

    return {'responses': responses}