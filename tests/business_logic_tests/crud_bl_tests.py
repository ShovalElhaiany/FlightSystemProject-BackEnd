import pytest
from lib.business_logic.crud.add import BusinessLogicAdd
from lib.business_logic.crud.delete import BusinessLogicRemove
from lib.business_logic.crud.get import BusinessLogicGet
from lib.business_logic.crud.update import BusinessLogicUpdate


def test_add_entity_data(caplog):
    # Test adding a single entity

    entity_data = {'field1': 'value1', 'field2': 'value2'}
    entity_fields = {'model': 'TestModel', 'fields': ['field1', 'field2'], 'name': 'TestEntity'}

    expected_result = {'TestEntity added successfully'}

    result = BusinessLogicAdd.add_entity_data(entity_data, entity_fields)

    assert result == expected_result
    assert 'TestEntity added successfully' in caplog.text


def test_add_entities_data(caplog):
    # Test adding multiple entities

    entities_data = [{'field1': 'value1', 'field2': 'value2'}, {'field1': 'value3', 'field2': 'value4'}]
    entity_fields = {'model': 'TestModel', 'fields': ['field1', 'field2'], 'name': 'TestEntity'}

    expected_result = {'TestEntities successfully added'}

    result = BusinessLogicAdd.add_entities_data(entities_data, entity_fields)

    assert result == expected_result
    assert 'TestEntities successfully added' in caplog.text


def test_remove_entity_data(caplog):
    # Test removing a specific entity

    entity_id = 1
    entity_fields = {'model': 'TestModel', 'name': 'TestEntity'}

    expected_result = {'TestEntity removed successfully'}

    result = BusinessLogicRemove.remove_entity_data(entity_id, entity_fields)

    assert result == expected_result
    assert 'TestEntity removed successfully' in caplog.text


def test_remove_entities_data(caplog):
    # Test removing all entities of a specific type

    entity_fields = {'model': 'TestModel', 'name': 'TestEntity'}

    expected_result = {'All TestEntities removed successfully'}

    result = BusinessLogicRemove.remove_entities_data(entity_fields)

    assert result == expected_result
    assert 'All TestEntities removed successfully' in caplog.text


def test_get_entity_data(caplog):
    # Test retrieving data for a specific entity

    entity_id = 1
    entity_fields = {'model': 'TestModel', 'name': 'TestEntity', 'fields': ['field1', 'field2']}

    expected_result = {'field1': 'value1', 'field2': 'value2'}

    result = BusinessLogicGet.get_entity_data(entity_id, entity_fields)

    assert result == expected_result
    assert 'TestEntity is found' in caplog.text


def test_get_entities_data(caplog):
    # Test retrieving data for all entities of a specific type

    entity_fields = {'model': 'TestModel', 'name': 'TestEntity', 'fields': ['field1', 'field2']}

    expected_result = [
        {'field1': 'value1', 'field2': 'value2'},
        {'field1': 'value3', 'field2': 'value4'}
    ]

    result = BusinessLogicGet.get_entities_data(entity_fields)

    assert result == expected_result
    assert 'All entities are found' in caplog.text


def test_update_entity_data(caplog):
    # Test updating a specific entity

    entity_id = 1
    entity_data = {'field1': 'new_value1', 'field2': 'new_value2', 'id': 1}
    entity_fields = {'model': 'TestModel', 'name': 'TestEntity', 'fields': ['field1', 'field2']}

    expected_result = {'TestEntity updated successfully'}

    result = BusinessLogicUpdate.update_entity_data(entity_id, entity_data, entity_fields)

    assert result == expected_result
    assert 'TestEntity updated successfully' in caplog.text


def test_update_entities_data(caplog):
    # Test updating multiple entities

    entities_data = [
        {'field1': 'new_value1', 'field2': 'new_value2', 'id': 1},
        {'field1': 'new_value3', 'field2': 'new_value4', 'id': 2}
    ]
    entity_fields = {'model': 'TestModel', 'name': 'TestEntity', 'fields': ['field1', 'field2']}

    expected_result = {
        'responses': [
            {'TestEntity1 updated successfully'},
            {'TestEntity2 updated successfully'}
        ]
    }

    result = BusinessLogicUpdate.update_entities_data(entities_data, entity_fields)

    assert result == expected_result
    assert 'The entities have been successfully updated!' in caplog.text
