from unittest.mock import patch

import pytest

from lib.data_access_layer.crud import (add_entities, add_entity,
                                        get_entities, get_entity,
                                        remove_entities, remove_entity,
                                        update_entity)


class SampleModel:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    @pytest.fixture
    def mock_model():
        with patch('app.db.Model', new_callable=lambda: SampleModel) as mock:
            yield mock

    @pytest.fixture
    def mock_session(mock_model):
        with patch('app.db.session', new_callable=lambda: SampleModel()) as mock:
            yield mock

    def test_get_entity(mock_model, mock_session):
        mock_model.query.get.return_value = SampleModel(id=1, name='Entity 1')
        entity = get_entity(mock_model, 1)
        assert entity.id == 1
        assert entity.name == 'Entity 1'

    def test_get_entities(mock_model, mock_session):
        mock_model.query.all.return_value = [SampleModel(id=1, name='Entity 1'), SampleModel(id=2, name='Entity 2')]
        entities = get_entities(mock_model)
        assert len(entities) == 2
        assert entities[0].id == 1
        assert entities[1].id == 2

    def test_add_entity(mock_model, mock_session):
        entity_data = {'name': 'New Entity'}
        add_entity(mock_model, entity_data)
        mock_session.add.assert_called_once_with(SampleModel(name='New Entity'))

    def test_add_entities(mock_model, mock_session):
        entities_data = [{'name': 'Entity 1'}, {'name': 'Entity 2'}]
        add_entities(mock_model, entities_data)
        mock_session.bulk_save_objects.assert_called_once()

    def test_update_entity(mock_model, mock_session):
        entity = SampleModel(id=1, name='Old Name')
        entity_data = {'name': 'New Name'}
        update_entity(entity, entity_data)
        assert entity.name == 'New Name'

    def test_remove_entity(mock_model, mock_session):
        entity = SampleModel(id=1, name='Entity 1')
        remove_entity(entity)
        mock_session.delete.assert_called_once_with(entity)

    def test_remove_entities(mock_model, mock_session):
        remove_entities(mock_model)
        mock_model.query.delete.assert_called_once()
