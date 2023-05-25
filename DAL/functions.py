from models import AirlineCompanies, Customers, Users, Flights, Tickets, db
from datetime import datetime, timedelta
from flask import jsonify

def get_airline_by_username(_username):
    return AirlineCompanies.query.join(Users).filter_by(username=_username).first()

def get_customer_by_username(_username):
    return Customers.query.join(Users).filter_by(username=_username).first()

def get_user_by_username(_username):
    return Users.query.filter_by(username=_username).first()

def get_flights_by_parameters(_origin_counry_id: int, _destination_country_id: int, _date):
    return Flights.query.filter_by(origin_country_id=_origin_counry_id, 
                                    destination_country_id=_destination_country_id, 
                                    departure_time=_date).all()

def get_flights_by_airline_id(_airline_id):
    return Flights.query.filter_by(airline_company_id=_airline_id).all()

def get_arrival_flights(_country_id: int):
    # Get current time and time 12 hours from now
    current_time = datetime.utcnow()
    time_12_hours_later = current_time + timedelta(hours=12)
    
    # Query for flights landing in the next 12 hours in the given country
    flights = db.session.query(Flights).filter(Flights.destination_country_id == _country_id,
                                               Flights.landing_time.between(current_time, time_12_hours_later)).all()
    
    # Convert flights to a list of dictionaries and return as JSON
    flights_list = [{'id': flight.id,
                     'airline_company_id': flight.airline_company_id,
                     'origin_country_id': flight.origin_country_id,
                     'destination_country_id': flight.destination_country_id,
                     'departure_time': flight.departure_time.isoformat(),
                     'landing_time': flight.landing_time.isoformat(),
                     'remaining_tickets': flight.remaining_tickets} for flight in flights]
    return jsonify(flights_list)

def get_departure_flights(_country_id):
    # Get current time and time 12 hours from now
    current_time = datetime.utcnow()
    time_12_hours_later = current_time + timedelta(hours=12)
    
    # Query for flights departing in the next 12 hours from the given country
    flights = db.session.query(Flights).filter(Flights.origin_country_id == _country_id,
                                               Flights.departure_time.between(current_time, time_12_hours_later)).all()
    
    # Convert flights to a list of dictionaries and return as JSON
    flights_list = [{'id': flight.id,
                     'airline_company_id': flight.airline_company_id,
                     'origin_country_id': flight.origin_country_id,
                     'destination_country_id': flight.destination_country_id,
                     'departure_time': flight.departure_time.isoformat(),
                     'landing_time': flight.landing_time.isoformat(),
                     'remaining_tickets': flight.remaining_tickets} for flight in flights]
    return jsonify(flights_list)

def get_tickets_by_customer(_customer_id):
    # Query for flight tickets belonging to the given customer
    tickets = db.session.query(Tickets).filter(Tickets.customer_id == _customer_id).all()
    
    # Convert tickets to a list of dictionaries and return as JSON
    tickets_list = [{'id': ticket.id,
                     'flight_id': ticket.flight_id,
                     'customer_id': ticket.customer_id} for ticket in tickets]
    return jsonify(tickets_list)