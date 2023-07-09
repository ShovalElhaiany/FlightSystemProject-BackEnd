from flask import jsonify, request
from lib.businessLogic.searchesBl import *
from logs.log import logger

def log_and_return_json(data):
    """
    Logs the given data and returns it as a JSON response.

    Args:
        data: The data to be logged and returned as JSON.

    Returns:
        A JSON response containing the logged data.
    """
    logger.info(data)
    return jsonify(data)

def get_flights_by_parameters_view():
    """
    Retrieves flights based on the provided parameters and returns them as a JSON response.

    Returns:
        A JSON response containing the retrieved flights.
    """
    data = request.get_json()
    origin_country_id = data.get('origin_country_id')
    destination_country_id = data.get('destination_country_id')
    date = data.get('date')
    flights_list = get_flights_by_parameters_bl(origin_country_id, destination_country_id, date)
    return log_and_return_json(flights_list)

def get_flights_by_airline_id_view(airline_id):
    flights_list = get_flights_by_airline_id_bl(airline_id)
    return log_and_return_json(flights_list)

def get_flights_by_origin_country_id_view(country_id):
    flights_list = get_flights_by_origin_country_id_bl(country_id)
    return log_and_return_json(flights_list)

def get_flights_by_destination_country_id_view(country_id):
    flights_list = get_flights_by_destination_country_id_bl(country_id)
    return log_and_return_json(flights_list)

def get_flights_by_departure_date_view(date):
    flights_list = get_flights_by_departure_date_bl(date)
    return log_and_return_json(flights_list)

def get_flights_by_landing_date_view(date):
    flights_list = get_flights_by_landing_date_bl(date)
    return log_and_return_json(flights_list)

def get_arrival_flights_view(country_id):
    flights_list = get_arrival_flights_bl(country_id)
    return log_and_return_json(flights_list)

def get_departure_flights_view(country_id):
    flights_list = get_departure_flights_bl(country_id)
    return log_and_return_json(flights_list)

def get_airline_by_username_view(username):
    airline_data = get_airline_by_username_bl(username)
    return log_and_return_json(airline_data)

def get_airlines_by_country_view(country_id):
    airlines_list = get_airlines_by_country_bl(country_id)
    return log_and_return_json(airlines_list)

def get_user_by_username_view(username):
    user_data = get_user_by_username_bl(username)
    return log_and_return_json(user_data)

def get_tickets_by_customer_view(customer_id):
    tickets_list = get_tickets_by_customer_bl(customer_id)
    return log_and_return_json(tickets_list)

def get_customer_by_username_view(username):
    customer_data = get_customer_by_username_bl(username)
    return log_and_return_json(customer_data)

def get_flights_by_customer_view(customer_id):
    flights_list = get_flights_by_customer_bl(customer_id)
    return log_and_return_json(flights_list)

def get_airlines_by_parameters_view():
    """
    Retrieves airlines based on the provided parameters and returns them as a JSON response.

    Returns:
        A JSON response containing the retrieved airlines.
    """
    data = request.get_json()
    name = data.get('name')
    country_id = data.get('country_id')
    airlines_list = get_airline_by_parameters_bl(name, country_id)
    return log_and_return_json(airlines_list)
