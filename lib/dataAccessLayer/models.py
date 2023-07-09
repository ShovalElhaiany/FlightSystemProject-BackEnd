from flask_login import UserMixin
from sqlalchemy.orm import relationship

from src.myApp import db


class Flights(db.Model):
    """Model representing flights."""

    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    airline_company_id = db.Column(db.BigInteger, db.ForeignKey('airline_companies.id', ondelete='CASCADE'))
    origin_country_id = db.Column(db.Integer, db.ForeignKey('countries.id', ondelete='CASCADE'))
    destination_country_id = db.Column(db.Integer, db.ForeignKey('countries.id', ondelete='CASCADE'))
    departure_time = db.Column(db.DateTime)
    landing_time = db.Column(db.DateTime)
    remaining_tickets = db.Column(db.Integer)


class AirlineCompanies(db.Model):
    """Model representing airline companies."""

    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), unique=True)
    country_id = db.Column(db.Integer, db.ForeignKey('countries.id', ondelete='CASCADE'))
    user_id = db.Column(db.BigInteger, db.ForeignKey('users.id', ondelete='CASCADE'), unique=True)

    # Relationships with Flights and AirlineCompanies cascade deletion
    flight = relationship('Flights', backref='airlinecompany', cascade='all, delete')


class Users(UserMixin, db.Model):
    """Model representing users."""

    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    username = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True)
    user_role = db.Column(db.Integer, db.ForeignKey('user_roles.id', ondelete='CASCADE'))

    # Relationships with Customers, AirlineCompanies and Administrators, cascade deletion
    customer = relationship('Customers', backref='user', cascade='all, delete')
    airline = relationship('AirlineCompanies', backref='user', cascade='all, delete')
    admin = relationship('Administrators', backref='user', cascade='all, delete')


class Countries(db.Model):
    """Model representing countries."""

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), unique=True)

    # Relationships with Flights and AirlineCompanies cascade deletion
    flight_origin = relationship('Flights', foreign_keys=[Flights.origin_country_id], backref='origin_country', cascade='all, delete')
    flight_destination = relationship('Flights', foreign_keys=[Flights.destination_country_id], backref='destination_country', cascade='all, delete')
    airline = relationship('AirlineCompanies', backref='country', cascade='all, delete')


class Tickets(db.Model):
    """Model representing tickets."""

    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    flight_id = db.Column(db.BigInteger, db.ForeignKey('flights.id'))
    customer_id = db.Column(db.BigInteger, db.ForeignKey('customers.id'))

    __table_args__ = (db.UniqueConstraint('flight_id', 'customer_id', name='uq_flight_customer'),)


class Customers(db.Model):
    """Model representing customers."""

    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    address = db.Column(db.String(255))
    phone_no = db.Column(db.String(255), unique=True)
    credit_card_no = db.Column(db.String(255), unique=True)
    user_id = db.Column(db.BigInteger, db.ForeignKey('users.id', ondelete='CASCADE'), unique=True)


class UserRoles(db.Model):
    """Model representing user roles."""

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    role_name = db.Column(db.String(255), unique=True)

    # Relationships with Users, cascade deletion
    user = relationship('Users', backref='userrole', cascade='all, delete')


class Administrators(db.Model):
    """Model representing administrators."""

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    user_id = db.Column(db.BigInteger, db.ForeignKey('users.id', ondelete='CASCADE'), unique=True)
