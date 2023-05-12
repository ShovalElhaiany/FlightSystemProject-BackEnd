from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Flight(Base):
    __tablename__ = 'flights'
    id = Column(Integer, primary_key=True)
    airline_company_id = Column(Integer, ForeignKey('airline_companies.id'))
    origin_country_id = Column(Integer, ForeignKey('countries.id'))
    destination_country_id = Column(Integer, ForeignKey('countries.id'))
    departure_time = Column(DateTime)
    landing_time = Column(DateTime)
    remaining_tickets = Column(Integer)

class AirlineCompany(Base):
    __tablename__ = 'airline_companies'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    country_id = Column(Integer, ForeignKey('countries.id'))
    user_id = Column(Integer, ForeignKey('users.id'))
    flights = relationship('Flight', backref='airline_company')

class Customer(Base):
    __tablename__ = 'customers'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    address = Column(String(100))
    phone_no = Column(String(20), unique=True)
    credit_card_no = Column(String(20), unique=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    tickets = relationship('Ticket', backref='customer')

class Administrator(Base):
    __tablename__ = 'administrators'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    user_id = Column(Integer, ForeignKey('users.id'))

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True)
    password = Column(String(50))
    email = Column(String(50), unique=True)
    user_role = Column(Integer, ForeignKey('user_roles.id'))
    airline_companies = relationship('AirlineCompany', backref='user')
    customers = relationship('Customer', backref='user')
    administrators = relationship('Administrator', backref='user')

class Country(Base):
    __tablename__ = 'countries'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    airline_companies = relationship('AirlineCompany', backref='country')
    flights_origin = relationship('Flight', backref='origin_country', foreign_keys=[origin_country_id])
    flights_destination = relationship('Flight', backref='destination_country', foreign_keys=[destination_country_id])

class Ticket(Base):
    __tablename__ = 'tickets'
    id = Column(Integer, primary_key=True)
    flight_id = Column(Integer, ForeignKey('flights.id'))
    customer_id = Column(Integer, ForeignKey('customers.id'))
