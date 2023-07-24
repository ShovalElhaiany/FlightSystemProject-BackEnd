from logs.log import LogLevel, log_and_raise
from src.my_app import db


def get_entity(model, entity_id):
    """Retrieve a specific entity from the database based on its ID."""
    try:
        return model.query.get(entity_id)
    except Exception as e:
        log_and_raise(e, LogLevel.ERROR)
def get_entities(model):
    """Retrieve all entities of a specific model from the database."""
    try:
        return model.query.all()
    except Exception as e:
        log_and_raise(e, LogLevel.ERROR)

def add_entity(model, entity_data):
    """
    Create a new entity of a specific model and add it to the database.
    
    Args:
        model: The model class representing the entity.
        entity_data: A dictionary containing the data for the entity.
    """
    try:
        entity = model(**entity_data)
        db.session.add(entity)
        db.session.commit()
    except Exception as e:
        log_and_raise(e, LogLevel.ERROR)

def add_entities(model, entities_data):
    """
    Create multiple entities of a specific model and add them to the database.
    
    Args:
        model: The model class representing the entities.
        entities_data: A list of dictionaries, where each dictionary contains the data for an entity.
    """
    try:
        entities = [model(**entity_data) for entity_data in entities_data]
        db.session.bulk_save_objects(entities)
        db.session.commit()
    except Exception as e:
        log_and_raise(e, LogLevel.ERROR)

def update_entity(entity, entity_data):
    """
    Update the properties of an existing entity.
    
    Args:
        entity: The entity object to be updated.
        entity_data: A dictionary containing the updated data for the entity.
    """
    try:
        for key, value in entity_data.items():
            setattr(entity, key, value)
        db.session.commit()
    except Exception as e:
        log_and_raise(e, LogLevel.ERROR)

def remove_entity(entity):
    """
    Remove an entity from the database.
    
    Args:
        entity: The entity object to be removed.
    """
    try:
        db.session.delete(entity)
        db.session.commit()
    except Exception as e:
        log_and_raise(e, LogLevel.ERROR)

def remove_entities(model):
    """
    Remove all entities of a specific model from the database.
    
    Args:
        model: The model class representing the entities to be removed.
    """
    try:
        model.query.delete()
        db.session.commit()
    except Exception as e:
        log_and_raise(e, LogLevel.ERROR)