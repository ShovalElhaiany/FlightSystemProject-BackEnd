from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import Flight, AirlineCompany, Customer, Administrator, User, Country, Ticket

class Repository:
    def __init__(self, db_uri):
        self.engine = create_engine(db_uri)
        self.Session = sessionmaker(bind=self.engine)
        
    def get_by_id(self, model_class, id):
        session = self.Session()
