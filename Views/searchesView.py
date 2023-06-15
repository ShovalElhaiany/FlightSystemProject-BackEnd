from flask import jsonify, request
from businessLogic.getBl import *
from businessLogic.addBl import *
from businessLogic.updateBl import *
from businessLogic.deleteBl import *
from businessLogic.searchesBl import *
from .entityFields import *

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

def get_flights_by_customer(customer_id):
    flights_list = get_flights_by_customer(customer_id)
    return jsonify(flights_list)

def get_airlines_by_parameters():
    name = request.get_json().get('name')
    country_id = request.get_json().get('country_id')
    
    airlines_list = get_airline_by_parameters_bl(name, country_id)
   
    return jsonify(airlines_list)