from dataAccessLayer.crudDal import *
from dataAccessLayer.searchesDal import *

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
