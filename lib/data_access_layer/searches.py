from datetime import datetime, timedelta

from .models import (AirlineCompanies, Countries, Customers, Flights, Tickets,
                    Users)

from logs.log import log_and_raise
from src.my_app import db


def get_flights_by_parameters(origin_country_id, destination_country_id, date):
    """Retrieve flights based on origin country, destination country, and date."""
    return Flights.query.filter_by(origin_country_id=origin_country_id,
                                   destination_country_id=destination_country_id,
                                   departure_time=date).all()

def get_flights_by_airline_id(airline_id):
    """Retrieve flights based on airline ID."""
    try:    
        return Flights.query.filter_by(airline_company_id=airline_id).all()
    except Exception as e:
        log_and_raise(e, 'error')

def get_flights_by_origin_country_id(country_id):
    """Retrieve flights based on origin country ID."""
    try:
        return (Flights.query.join(Countries, Flights.origin_country_id == Countries.id)
            .filter_by(id=country_id).all())
    except Exception as e:
        log_and_raise(e, 'error')

def get_flights_by_destination_country_id(country_id):
    """Retrieve flights based on destination country ID."""
    try:
        return (Flights.query.join(Countries, Flights.destination_country_id == Countries.id)
            .filter_by(id=country_id).all())
    except Exception as e:
        log_and_raise(e, 'error')

def get_flights_by_departure_date(date):
    """Retrieve flights based on departure date."""
    try:
        return Flights.query.filter_by(departure_time=date).all()
    except Exception as e:
        log_and_raise(e, 'error')

def get_flights_by_landing_date(date):
    """Retrieve flights based on landing date."""
    try:
        return Flights.query.filter_by(landing_time=date).all()
    except Exception as e:
        log_and_raise(e, 'error')

def get_arrival_flights(country_id):
    """Retrieve arrival flights for a given country within the next 12 hours."""
    try:
        current_time = datetime.utcnow()
        time_12_hours_later = current_time + timedelta(hours=12)
        
        return (db.session.query(Flights)
                .filter(Flights.destination_country_id == country_id,
                        Flights.landing_time >= current_time,
                        Flights.landing_time < time_12_hours_later).all())
    except Exception as e:
        log_and_raise(e, 'error')

def get_departure_flights(country_id):
    """Retrieve departure flights for a given country within the next 12 hours."""
    try:
        current_time = datetime.utcnow()
        time_12_hours_later = current_time + timedelta(hours=12)

        return (db.session.query(Flights)
                .filter(Flights.origin_country_id == country_id,
                        Flights.departure_time >= current_time,
                        Flights.departure_time < time_12_hours_later).all())
    except Exception as e:
        log_and_raise(e, 'error')

def get_airline_by_username(username):
    """Retrieve an airline company based on the username."""
    try:
        return AirlineCompanies.query.join(Users).filter_by(username=username).first()
    except Exception as e:
        log_and_raise(e, 'error')

def get_airlines_by_country(country_id):
    """Retrieve airlines based on country ID."""
    try:
        return AirlineCompanies.query.join(Countries).filter_by(id=country_id).all()
    except Exception as e:
        log_and_raise(e, 'error')

def get_user_by_username(username):
    """Retrieve a user based on the username."""
    try: 
        return Users.query.filter_by(username=username).first()
    except Exception as e:
        log_and_raise(e, 'error')

def get_tickets_by_customer(customer_id):
    """Retrieve tickets based on customer ID."""
    try:
        return Tickets.query.filter_by(customer_id=customer_id).all()
    except Exception as e:
        log_and_raise(e, 'error')

def get_customer_by_username(username):
    """Retrieve a customer based on the username."""
    try:
        return Customers.query.join(Users).filter(Users.username == username).first()
    except Exception as e:
        log_and_raise(e, 'error')

def get_flights_by_customer(customer_id):
    """Retrieve flights based on customer ID."""
    try:
        customer_tickets = Tickets.query.join(Customers).filter_by(id=customer_id).all()
        flights =[]
        for ticket in customer_tickets:
            flight = Flights.query.filter_by(id=ticket.flight_id).first()
            flights.append(flight)
        return flights
    except Exception as e:
        log_and_raise(e, 'error')

def get_airline_by_parameters(name, country_id):
    """Retrieve airline companies based on name and country ID."""
    try:    
        airlines = AirlineCompanies.query.filter_by(name=name, country_id=country_id).all()
        return airlines
    except Exception as e:
        log_and_raise(e, 'error')