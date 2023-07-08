from dataAccessLayer.crudDal import *
from dataAccessLayer.searchesDal import *

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