from flask import request

from lib.views.crud import CrudViews
from lib.views.searches import SearchesView
from logs.log import logger
from utils.user_manage import create_user


class FacadeBase():
    """Base class for facade pattern implementation."""
    
    @staticmethod
    def get_all_flights():
        new_path = 'get/flights'
        request.url = request.url = f'{request.host_url}{new_path}'
        response = CrudViews.get_entities()
        return response


    @staticmethod
    def get_flight_by_id(flight_id):
        new_path = 'get/flights'
        request.url = request.url = f'{request.host_url}{new_path}/{flight_id}'
        response = CrudViews.get_entity(flight_id)
        return response

    @staticmethod
    def get_flights_by_parameters():
        new_path = 'flights/parameters'
        request.url = request.url = f'{request.host_url}{new_path}'
        response = SearchesView.get_flights_by_parameters()
        return response

    @staticmethod
    def get_all_airlines():
        new_path = 'get/airlinecompanies'
        request.url = request.url = f'{request.host_url}{new_path}'
        response = CrudViews.get_entities()
        return response

    @staticmethod
    def get_airline_by_id(airline_id):
        new_path = 'get/airlinecompanies'
        request.url = request.url = f'{request.host_url}{new_path}/{airline_id}'
        response = CrudViews.get_entity(airline_id)
        return response

    @staticmethod
    def get_airline_by_parameters():
        new_path = 'airlines/parameters'
        request.url = request.url = f'{request.host_url}{new_path}'
        response = SearchesView.get_airlines_by_parameters()
        return response

    @staticmethod
    def get_all_countries():
        new_path = 'get/countries'
        request.url = request.url = f'{request.host_url}{new_path}'
        response = CrudViews.get_entities()
        return response

    @staticmethod
    def get_country_by_id(country_id):
        new_path = 'get/countries'
        request.url = request.url = f'{request.host_url}{new_path}/{country_id}'
        response = CrudViews.get_entity(country_id)
        return response

    @staticmethod
    def edit_add_entity_request():
        """
        Edit the request URL and data for adding an entity.

        Returns:
            None
        """
        data = request.json
        user_role = data.get('user_role')
        
        new_path = f"add/add_{user_role}".lower()
        request.url = f'{request.host_url}{new_path}'

        user_id = create_user(user_role)
        data['user_id'] = user_id

        keys_to_remove = ['username', 'password', 'email']
        for key in keys_to_remove:
            if key in data:
                del data[key]
        request.data = data
        
        logger.info('The request was successfully updated!')