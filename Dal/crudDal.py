from .models import *

def get_entity(model, entity_id):
    return model.query.get(entity_id)

def get_all_entities(model):
    return model.query.all()

def add_entity(model, entity_data):
    entity = model(**entity_data)
    db.session.add(entity)
    db.session.commit()

def add_entities(model, entities_data):
    entities = [model(**entity_data) for entity_data in entities_data]
    db.session.bulk_save_objects(entities)
    db.session.commit()

def update_entity(entity, entity_data):
    for key, value in entity_data.items():
        setattr(entity, key, value)
    db.session.commit()

def remove_entity(entity):
    db.session.delete(entity)
    db.session.commit()

def remove_all_entities(model):
    model.query.delete()
    db.session.commit()
