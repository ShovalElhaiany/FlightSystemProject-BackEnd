from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta
from flask import jsonify

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flight_system.db'
db = SQLAlchemy(app)

class Flights(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    airline_company_id = db.Column(db.BigInteger, db.ForeignKey('airline_companies.id'))
    origin_country_id = db.Column(db.Integer, db.ForeignKey('countries.id'))
    destination_country_id = db.Column(db.Integer, db.ForeignKey('countries.id'))
    departure_time = db.Column(db.DateTime)
    landing_time = db.Column(db.DateTime)
    remaining_tickets = db.Column(db.Integer)

class AirlineCompanies(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), unique=True)
    country_id = db.Column(db.Integer, db.ForeignKey('countries.id'))
    user_id = db.Column(db.BigInteger, db.ForeignKey('users.id'), unique=True)

class Users(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    username = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True)
    user_role = db.Column(db.Integer, db.ForeignKey('user_roles.id'))

class Countries(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), unique=True)

class Tickets(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    flight_id = db.Column(db.BigInteger, db.ForeignKey('flights.id'), unique=True)
    customer_id = db.Column(db.BigInteger, db.ForeignKey('customers.id'), unique=True)

class Customers(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    address = db.Column(db.String(255))
    phone_no = db.Column(db.String(255), unique=True)
    credit_card_no = db.Column(db.String(255), unique=True)
    user_id = db.Column(db.BigInteger, db.ForeignKey('users.id'), unique=True)

class UserRoles(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    role_name = db.Column(db.String(255), unique=True)

class Administrators(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    user_id = db.Column(db.BigInteger, db.ForeignKey('users.id'), unique=True)

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

db.create_all()

if __name__ == '__main__':
    app.run(debug=True)