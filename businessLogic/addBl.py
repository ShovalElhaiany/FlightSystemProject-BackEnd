from dal.crudDal import *
from dal.searchesDal import *

def add_entity_data(entity_data, entity_fields):
    if 'id' in entity_data:
        return {'error': 'Cannot specify id when creating a new entity'}

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

