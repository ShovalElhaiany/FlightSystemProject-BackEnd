from flask import request
from flask_login import login_required

from utils.auth import role_required
from lib.views.crud import CrudViews
from lib.views.searches import SearchesView
from .anonymous import AnonymousFacade


class AirlineFacade(AnonymousFacade):
    """Facade class for airline-specific operations."""

    @staticmethod
    #@login_required
    #@role_required('AirlineCompanies')
    def update_airline(airline_id):
        new_path = 'update/airlinecompanies'
        request.url = request.url = f'{request.host_url}{new_path}/{airline_id}'
        response = CrudViews.update_entity(airline_id)
        return response

    @staticmethod
    #@login_required
    #@role_required('AirlineCompanies')
    def add_flight():
        new_path = 'add/flights'
        request.url = request.url = f'{request.host_url}{new_path}'
        response = CrudViews.add_entity()
        return response

    @staticmethod
    #@login_required
    #@role_required('AirlineCompanies')
    def update_flight(flight_id):
        new_path = 'update/flights'
        request.url = request.url = f'{request.host_url}{new_path}/{flight_id}'
        response = CrudViews.update_entity(flight_id)
        return response

    @staticmethod
    #@login_required
    #@role_required('AirlineCompanies')
    def delete_flight(flight_id):
        new_path = 'delete/flights'
        request.url = request.url = f'{request.host_url}{new_path}/{flight_id}'
        response = CrudViews.delete_entity(flight_id)
        return response

    @staticmethod
    #@login_required
    #@role_required('AirlineCompanies')
    def get_my_flights(airline_id):
        new_path = 'search/flights/airline'
        request.url = request.url = f'{request.host_url}{new_path}/{airline_id}'
        response = SearchesView.get_flights_by_airline_id(airline_id)
        return response