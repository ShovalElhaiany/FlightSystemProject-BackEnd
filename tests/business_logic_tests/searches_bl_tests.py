from unittest.mock import patch

import pytest

from lib.business_logic.searches.additional_searches import \
    BusinessLogicAdditionalSearches
from lib.business_logic.searches.airlines import BusinessLogicAirlinesSearches
from lib.business_logic.searches.flights import BusinessLogicFlightsSearches


@pytest.fixture
def mock_log_data():
    with patch('logs.log.log_data') as mock_log_data:
        yield mock_log_data


@pytest.fixture
def mock_get_flights_by_parameters():
    with patch('bl.get_flights_by_parameters') as mock_get_flights_by_parameters:
        yield mock_get_flights_by_parameters


@pytest.fixture
def mock_get_flights_by_customer():
    with patch('bl.get_flights_by_customer') as mock_get_flights_by_customer:
        yield mock_get_flights_by_customer


@pytest.fixture
def mock_get_airline_by_parameters():
    with patch('bl.get_airline_by_parameters') as mock_get_airline_by_parameters:
        yield mock_get_airline_by_parameters


@pytest.fixture
def mock_get_airlines_by_country():
    with patch('bl.get_airlines_by_country') as mock_get_airlines_by_country:
        yield mock_get_airlines_by_country


@pytest.fixture
def mock_get_customer_by_username():
    with patch('bl.get_customer_by_username') as mock_get_customer_by_username:
        yield mock_get_customer_by_username


@pytest.fixture
def mock_get_tickets_by_customer():
    with patch('bl.get_tickets_by_customer') as mock_get_tickets_by_customer:
        yield mock_get_tickets_by_customer


@pytest.fixture
def mock_get_user_by_username():
    with patch('bl.get_user_by_username') as mock_get_user_by_username:
        yield mock_get_user_by_username


def generic_test_function(mock_log_data, bl_func, dal_func, *args, expected_result):
    dal_func.return_value = expected_result

    result = bl_func(*args)

    dal_func.assert_called_once_with(*args)
    mock_log_data.assert_called_once_with(expected_result)
    assert result == expected_result


def test_get_flights_by_parameters(mock_log_data, mock_get_flights_by_parameters):
    # Test get_flights_by_parameters function
    origin_country_id = 1
    destination_country_id = 2
    date = '2023-07-18'
    expected_result = [{'id': 1, 'origin_country_id': 1, 'destination_country_id': 2}]

    generic_test_function(mock_log_data, BusinessLogicFlightsSearches.get_flights_by_parameters, mock_get_flights_by_parameters,
                          origin_country_id, destination_country_id, date, expected_result)


def test_get_flights_by_customer(mock_log_data, mock_get_flights_by_customer):
    # Test get_flights_by_customer function
    customer_id = 1
    expected_result = [{'id': 1, 'origin_country_id': 1, 'destination_country_id': 2}]

    generic_test_function(mock_log_data, BusinessLogicFlightsSearches.get_flights_by_customer, mock_get_flights_by_customer,
                          customer_id, expected_result)

def test_get_flights_by_customer(mock_log_data, mock_get_flights_by_customer):
    # Test get_flights_by_customer function
    customer_id = 1
    expected_result = [
        {'id': 1, 'airline_company_id': 1, 'origin_country_id': 2, 'destination_country_id': 3,
         'departure_time': '2023-07-18T10:00:00', 'landing_time': '2023-07-18T12:00:00', 'remaining_tickets': 100},
        {'id': 2, 'airline_company_id': 2, 'origin_country_id': 3, 'destination_country_id': 2,
         'departure_time': '2023-07-18T13:00:00', 'landing_time': '2023-07-18T15:00:00', 'remaining_tickets': 50},
    ]

    generic_test_function(mock_log_data, BusinessLogicFlightsSearches.get_flights_by_customer, mock_get_flights_by_customer,
                          customer_id, expected_result)

def test_get_airline_by_parameters(mock_log_data, mock_get_airline_by_parameters):
    # Test get_airline_by_parameters function
    name = "Test Airline"
    country_id = 1
    expected_result = [{'id': 1, 'name': 'Test Airline', 'country_id': 1}]

    generic_test_function(mock_log_data, BusinessLogicAirlinesSearches.get_airline_by_parameters, mock_get_airline_by_parameters,
                          name, country_id, expected_result)


def test_get_airlines_by_country(mock_log_data, mock_get_airlines_by_country):
    # Test get_airlines_by_country function
    country_id = 1
    expected_result = [{'id': 1, 'name': 'Test Airline', 'country_id': 1}]

    generic_test_function(mock_log_data, BusinessLogicAirlinesSearches.get_airlines_by_country, mock_get_airlines_by_country,
                          country_id, expected_result)

def test_get_airline_by_parameters(mock_log_data, mock_get_airline_by_parameters):
    # Test get_airline_by_parameters function
    name = "Test Airline"
    country_id = 1
    expected_result = [
        {'id': 1, 'name': 'Test Airline', 'country_id': 1, 'user_id': 1},
        {'id': 2, 'name': 'Another Airline', 'country_id': 1, 'user_id': 2},
    ]

    generic_test_function(mock_log_data, BusinessLogicAirlinesSearches.get_airline_by_parameters, mock_get_airline_by_parameters,
                          name, country_id, expected_result)


def test_get_airlines_by_country(mock_log_data, mock_get_airlines_by_country):
    # Test get_airlines_by_country function
    country_id = 1
    expected_result = [
        {'id': 1, 'name': 'Airline A', 'country_id': 1, 'user_id': 1},
        {'id': 2, 'name': 'Airline B', 'country_id': 1, 'user_id': 2},
    ]

    generic_test_function(mock_log_data, BusinessLogicAirlinesSearches.get_airlines_by_country, mock_get_airlines_by_country,
                          country_id, expected_result)


def test_get_tickets_by_customer(mock_log_data, mock_get_tickets_by_customer):
    # Test get_tickets_by_customer function
    customer_id = 1
    expected_result = [
        {'id': 1, 'flight_id': 101, 'customer_id': 1},
        {'id': 2, 'flight_id': 102, 'customer_id': 1},
    ]

    generic_test_function(mock_log_data, BusinessLogicAdditionalSearches.get_tickets_by_customer, mock_get_tickets_by_customer,
                          customer_id, expected_result)


def test_get_user_by_username(mock_log_data, mock_get_user_by_username):
    # Test get_user_by_username function
    username = "testuser"
    expected_result = {
        'id': 1,
        'username': 'testuser',
        'password': 'hashed_password',
        'email': 'testuser@example.com',
        'user_role': 'customer'
    }

    generic_test_function(mock_log_data, BusinessLogicAdditionalSearches.get_user_by_username, mock_get_user_by_username,
                          username, expected_result)

def test_get_customer_by_username(mock_log_data, mock_get_customer_by_username):
    # Test get_customer_by_username function
    username = "test_customer"
    expected_result = {'id': 1, 'first_name': 'John', 'last_name': 'Doe', 'address': '123 Main St',
                       'phone_no': '555-1234', 'credit_card_no': '1234567890', 'user_id': 1}

    generic_test_function(mock_log_data, BusinessLogicAdditionalSearches.get_customer_by_username, mock_get_customer_by_username,
                          username, expected_result)
