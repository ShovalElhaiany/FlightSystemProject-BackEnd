from dal.models import *

class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql://root:Shoval963654@localhost:3306/flights_system_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'flaskey'

MODELS = [ UserRoles, Users, Administrators, Customers, Countries, AirlineCompanies, Flights, Tickets ]

MODELS_NAMES = [ MODEL.__name__ for MODEL in MODELS ]

DATA_FOLDER = "data/"