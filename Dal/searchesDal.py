from .models import *
from datetime import datetime, timedelta

def get_flights_by_parameters_dal(origin_country_id, destination_country_id, date):
    return Flights.query.filter_by(origin_country_id=origin_country_id,
                                      destination_country_id=destination_country_id,
                                      departure_time=date).all()

def get_flights_by_airline_id_dal(airline_id):
    return Flights.query.filter_by(airline_company_id=airline_id).all()

def get_flights_by_origin_country_id_dal(country_id):
    return (Flights.query.join(Countries, Flights.origin_country_id == Countries.id).filter_by(id=country_id).all())

def get_flights_by_destination_country_id_dal(country_id):
    return (Flights.query.join(Countries, Flights.destination_country_id == Countries.id).filter_by(id=country_id).all())

def get_flights_by_departure_date_dal(date):
    return Flights.query.filter_by(departure_time=date).all()

def get_flights_by_landing_date_dal(date):
    return Flights.query.filter_by(landing_time=date).all()

def get_arrival_flights_dal(country_id):
    current_time = datetime.utcnow()
    time_12_hours_later = current_time + timedelta(hours=12)
    
    return db.session.query(Flights).filter(Flights.destination_country_id == country_id,
                                            Flights.landing_time >= current_time,
                                            Flights.landing_time < time_12_hours_later).all()

def get_departure_flights_dal(country_id):
    current_time = datetime.utcnow()
    time_12_hours_later = current_time + timedelta(hours=12)

    return db.session.query(Flights).filter(Flights.origin_country_id == country_id,
                                            Flights.departure_time >= current_time,
                                            Flights.departure_time < time_12_hours_later).all()

def get_airline_by_username_dal(username):
    return AirlineCompanies.query.join(Users).filter_by(username=username).first()

def get_airlines_by_country_dal(country_id):
    return AirlineCompanies.query.join(Countries).filter_by(id=country_id).all()

def get_user_by_username_dal(username):
    return Users.query.filter_by(username=username).first()

def get_tickets_by_customer_dal(customer_id):
    return Tickets.query.filter_by(customer_id=customer_id).all()

def get_customer_by_username_dal(username):
    return Customers.query.join(Users).filter(Users.username == username).first()

def get_flights_by_customer_dal(customer_id):
    customer_tickets = Tickets.query.join(Customers).filter_by(id=customer_id).all()
    flights =[]
    for ticket in customer_tickets:
        flight = Flights.query.filter_by(id = ticket.flight_id).first()
        flights.append(flight)
    return flights

def get_airline_by_parameters_dal(name, country_id):
    airlines = AirlineCompanies.query.filter_by(name=name,
                                                country_id=country_id).all()
    return airlines
