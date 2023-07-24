from unittest.mock import MagicMock

import pytest
from lib.views.crud import CrudViews
from src.my_app import app


@pytest.fixture
def client():
    return app.test_client()


@pytest.fixture
def mock_function():
    return lambda response_data: lambda *args, **kwargs: response_data


@pytest.fixture
def mock_request_context():
    return lambda json_data: lambda *args, **kwargs: MagicMock(get_json=lambda: json_data)


def test_generic(client, mock_function, mock_request_context):
    view_functions = [
        (CrudViews.get_entity, 'get_entity_data'),
        (CrudViews.get_entities, 'get_entities_data'),
        (CrudViews.add_entity, 'add_entity_data'),
        (CrudViews.add_entities, 'add_entities_data'),
        (CrudViews.update_entity, 'update_entity_data'),
        (CrudViews.update_entities, 'update_entities_data'),
        (CrudViews.remove_entity, 'remove_entity_data'),
        (CrudViews.remove_entities, 'remove_entities_data'),
    ]
    json_data = {
        "field1": "value1",
        "field2": "value2",
    }

    for view_function, bl_function in view_functions:
        with pytest.patch('lib.businessLogic.getBl.' + bl_function, mock_function(json_data)):
            with app.test_request_context(json=json_data):
                response = client.post('/api/' + view_function.__name__.replace('', ''), json=json_data)
                assert response.status_code == 200
