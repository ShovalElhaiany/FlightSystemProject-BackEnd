from abc import ABC, abstractmethod
from flask import redirect, url_for


class FacadeBase(ABC):
    @abstractmethod
    def __init__(self, user):
        pass

    @classmethod
    @abstractmethod
    def get_all_flights(self):
        return redirect(url_for('get.get_all_entities'))

    @classmethod
    @abstractmethod
    def get_flight_by_id(self, flight_id):
        return redirect(url_for('get.get_entity_endpoint', entity_id=flight_id))

    @classmethod
    @abstractmethod
    def get_flights_by_parameters(self):
        return redirect(url_for('search.get_flights_by_parameters'))

    @classmethod
    @abstractmethod
    def get_all_airlines(self):
        return redirect(url_for('get.get_all_entities'))

    @classmethod
    @abstractmethod
    def get_airline_by_id(self, airline_id):
        return redirect(url_for('get.get_entity_endpoint', entity_id=airline_id))

    @classmethod
    @abstractmethod
    def get_airline_by_parameters(self):
        return redirect(url_for('search.get_airlines_by_parameters'))
    
    @classmethod
    @abstractmethod
    def get_all_countries(self):
        return redirect(url_for('get.get_all_entities'))

    @classmethod
    @abstractmethod
    def get_country_by_id(self, country_id):
        return redirect(url_for('get.get_entity_endpoint', entity_id=country_id))

    @classmethod
    @abstractmethod
    def create_new_user(self):
        return redirect(url_for('add.add_entity_endpoint'))

        


