from app import db

class Flights(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    airline_company_id = db.Column(db.BigInteger, db.ForeignKey('airline_companies.id', nullable=False))
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