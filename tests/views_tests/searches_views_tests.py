import pytest
from flask import Response, request

from lib.views.searches import SearchesView


@pytest.fixture
def json_data():
    return {
        'origin_country_id': 1,
        'destination_country_id': 2,
        'date': '2023-07-20',
    }

@pytest.fixture
def mock_function():
    return []

@pytest.fixture
def json_response():
    return lambda data: Response(str(data))

@pytest.mark.parametrize(
    "filter_key, view_function",
    [
        ((1, 2, '2023-07-20'), SearchesView.get_flights_by_parameters),
        (123, SearchesView.get_flights_by_airline_id),
        (456, SearchesView.get_flights_by_origin_country_id),
        (789, SearchesView.get_flights_by_destination_country_id),
        ('2023-07-20', SearchesView.get_flights_by_departure_date),
        ('2023-07-20', SearchesView.get_flights_by_landing_date),
        (111, SearchesView.get_arrival_flights),
        (222, SearchesView.get_departure_flights),
        ('sample_username', SearchesView.get_airline_by_username),
        (333, SearchesView.get_airlines_by_country),
        ('sample_username', SearchesView.get_user_by_username),
        (444, SearchesView.get_tickets_by_customer),
        ('sample_username', SearchesView.get_customer_by_username),
        (555, SearchesView.get_flights_by_customer),
        ({'name': 'sample_airline', 'country_id': 666}, SearchesView.get_airlines_by_parameters),
    ]
)
def test_searches(
        filter_key,
        view_function,
        json_data,
        mock_function,
        json_response,
        monkeypatch
):
    monkeypatch.setattr(request, 'get_json', lambda: json_data)
    monkeypatch.setattr(SearchesView.get_flights_by_parameters, 'side_effect', mock_function)

    response = view_function(filter_key)

    assert response.status_code == 200
