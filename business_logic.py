from dal import (
    get_entity,
    get_all_entities,
    add_entity,
    add_entities,
    update_entity,
    remove_entity,
    remove_all_entities
)

def get_entity_data(entity_id, entity_fields):
    entity = get_entity(entity_fields['model'], entity_id)
    if entity:
        return {field: getattr(entity, field) for field in entity_fields['fields']}
    else:
        return {'error': f'{entity_fields["name"]} not found'}

def get_all_entities_data(entity_fields):
    entities = get_all_entities(entity_fields['model'])
    return [
        {field: getattr(entity, field) for field in entity_fields['fields']}
        for entity in entities
    ]

def add_entity_data(entity_data, entity_fields):
    if 'id' in entity_data:
        return {'error': 'Cannot specify id when creating a new entity'}

    # Exclude 'id' field from entity_data
    entity_data_filtered = {field: entity_data[field] for field in entity_fields['fields'] if field != 'id'}

    add_entity(entity_fields['model'], entity_data_filtered)
    return {'message': f'{entity_fields["name"]} added successfully'}

def add_entities_data(entities_data, entity_fields):
    entities_data_filtered = []
    for entity_data in entities_data:
        if 'id' in entity_data:
            return {'error': 'Cannot specify id when creating a new entity'}
        entity_data_filtered = {field: entity_data[field] for field in entity_fields['fields'] if field != 'id'}
        entities_data_filtered.append(entity_data_filtered)

    add_entities(entity_fields['model'], entities_data_filtered)
    return {'message': f'{entity_fields["name"]}s successfully added'}


def update_entity_data(entity_id, entity_data, entity_fields):
    if 'id' not in entity_data:
        return {'error': 'Missing required field: id'}

    entity = get_entity(entity_fields['model'], entity_id)
    if entity:
        # Exclude 'id' field from entity_data
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

def remove_entity_data(entity_id, entity_fields):
    entity = get_entity(entity_fields['model'], entity_id)
    if entity:
        remove_entity(entity)
        return {'message': f'{entity_fields["name"]} removed successfully'}
    else:
        return {'error': f'{entity_fields["name"]} not found'}

def remove_all_entities_data(entity_fields):
    remove_all_entities(entity_fields['model'])
    return {'message': f'All {entity_fields["name"]}s removed successfully'}
