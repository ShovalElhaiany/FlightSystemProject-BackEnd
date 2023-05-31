from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'your_database_uri_here'
db = SQLAlchemy(app)

class AirlineCompanies(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), unique=True)
    country_id = db.Column(db.Integer, db.ForeignKey('countries.id'))
    user_id = db.Column(db.BigInteger, db.ForeignKey('users.id'), unique=True)

class Customers(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    address = db.Column(db.String(255))
    phone_no = db.Column(db.String(255), unique=True)
    credit_card_no = db.Column(db.String(255), unique=True)
    user_id = db.Column(db.BigInteger, db.ForeignKey('users.id'), unique=True)

class Users(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    username = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True)
    user_role = db.Column(db.Integer, db.ForeignKey('user_roles.id'))

class Flights(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    airline_company_id = db.Column(db.BigInteger, db.ForeignKey('airline_companies.id'))
    origin_country_id = db.Column(db.Integer, db.ForeignKey('countries.id'))
    destination_country_id = db.Column(db.Integer, db.ForeignKey('countries.id'))
    departure_time = db.Column(db.DateTime)
    landing_time = db.Column(db.DateTime)
    remaining_tickets = db.Column(db.Integer)

class Tickets(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    flight_id = db.Column(db.BigInteger, db.ForeignKey('flights.id'))
    customer_id = db.Column(db.BigInteger, db.ForeignKey('customers.id'))

class Countries(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), unique=True)

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

def get_flights_by_parameters(_origin_counry_id, _destination_country_id, _date):
    return Flights.query.filter_by(origin_country_id=_origin_counry_id, 
                                    destination_country_id=_destination_country_id, 
                                    departure_time=_date).all()

def get_flights_by_airline_id(_airline_id):
    return Flights.query.filter_by(airline_company_id=_airline_id).all()

def get_arrival_flights(_country_id):
    import datetime
    time_threshold = datetime.datetime.now() + datetime