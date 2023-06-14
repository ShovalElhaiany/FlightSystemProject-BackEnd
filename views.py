from flask import jsonify, request
from business_logic import *

entity_fields = {
    # 'Administrators': {
    #     'model': Administrators,
    #     'name': 'Administrator',
    #     'fields': ['id', 'first_name', 'last_name', 'user_id']
    # },
    # 'Flights': {
    #     'model': Flights,
    #     'name': 'Flight',
    #     'fields': ['id', 'airline_company_id', 'origin_country_id', 'destination_country_id', 'departure_time', 'landing_time', 'remaining_tickets']
    # },
    # 'AirlineCompanies': {
    #     'model': AirlineCompanies,
    #     'name': 'Airline Company',
    #     'fields': ['id', 'name', 'country_id', 'user_id']
    # },
    # 'Users': {
        'model': Users,
        'name': 'User',
        'fields': ['id', 'username', 'password', 'email', 'user_role']
    # },
    # 'Countries': {
    #     'model': Countries,
    #     'name': 'Country',
    #     'fields': ['id', 'name']
    # },
    # 'Tickets': {
    #     'model': Tickets,
    #     'name': 'Ticket',
    #     'fields': ['id', 'flight_id', 'customer_id']
    # },
    # 'Customers': {
    #     'model': Customers,
    #     'name': 'Customer',
    #     'fields': ['id', 'first_name', 'last_name', 'address', 'phone_no', 'credit_card_no', 'user_id']
    # },
    # 'UserRoles': {
    #     'model': UserRoles,
    #     'name': 'User Role',
    #     'fields': ['id', 'role_name']
    # }
}

def get_entity_endpoint(entity_id):
    entity_data = get_entity_data(entity_id, entity_fields)
    return jsonify(entity_data)

def get_all_entities_endpoint():
    entities_data = get_all_entities_data(entity_fields)
    return jsonify(entities_data)

def add_entity_endpoint():
    entity_data = request.get_json()
    response = add_entity_data(entity_data, entity_fields)
    return jsonify(response)

def add_entities_endpoint():
    entities_data = request.get_json()
    response = add_entities_data(entities_data, entity_fields)
    return jsonify(response)

def update_entity_endpoint(entity_id):
    entity_data = request.get_json()
    response = update_entity_data(entity_id, entity_data, entity_fields)
    return jsonify(response)

def update_entities_endpoint():
    entities_data = request.get_json()
    response = update_entities_data(entities_data, entity_fields)
    return jsonify(response)

def remove_entity_endpoint(entity_id):
    response = remove_entity_data(entity_id, entity_fields)
    return jsonify(response)

def remove_all_entities_endpoint():
    response = remove_all_entities_data(entity_fields)
    return jsonify(response)

#**********************************************************************************************************************************

def get_flights_by_parameters():
    origin_country_id = request.get_json().get('origin_country_id')
    destination_country_id = request.get_json().get('destination_country_id')
    date = request.get_json().get('date')

    flights_list = get_flights_by_parameters_bl(origin_country_id, destination_country_id, date)

    return jsonify(flights_list)

def get_flights_by_airline_id(airline_id):
    flights_list = get_flights_by_airline_id_bl(airline_id)

    return jsonify(flights_list)

def get_flights_by_origin_country_id(country_id):
    flights_list = get_flights_by_origin_country_id_bl(country_id)
    return jsonify(flights_list)

def get_flights_by_destination_country_id(country_id):
    flights_list = get_flights_by_destination_country_id_bl(country_id)
    return jsonify(flights_list)

def get_flights_by_departure_date(date):
    flights_list = get_flights_by_departure_date_bl(date)
    return jsonify(flights_list)

def get_flights_by_landing_date(date):
    flights_list = get_flights_by_landing_date_bl(date)
    return jsonify(flights_list)

def get_arrival_flights(country_id):
    flights_list = get_arrival_flights_bl(country_id)
    return jsonify(flights_list)

def get_departure_flights(country_id):
    flights_list = get_departure_flights_bl(country_id)
    return jsonify(flights_list)

def get_airline_by_username(username):
    airline_data = get_airline_by_username_bl(username)
    return jsonify(airline_data)

def get_airlines_by_country(country_id):
    airlines_list = get_airlines_by_country_bl(country_id)
    return jsonify(airlines_list)

def get_user_by_username(username):
    user_data = get_user_by_username_bl(username)
    return jsonify(user_data)

def get_tickets_by_customer(customer_id):
    tickets_list = get_tickets_by_customer_bl(customer_id)
    return jsonify(tickets_list)

def get_customer_by_username(username):
    customer_data = get_customer_by_username_bl(username)
    return jsonify(customer_data)
