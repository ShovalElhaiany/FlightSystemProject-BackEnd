from urllib.parse import urlparse, urlunparse

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
        request.url = FacadeBase.edit_url(request.url, new_path)
        response = CrudViews.get_entities()
        return response


    @staticmethod
    def get_flight_by_id(flight_id):
        new_path = 'get/flights'
        request.url = FacadeBase.edit_url(request.url, new_path)
        response = CrudViews.get_entity(flight_id)
        return response

    @staticmethod
    def get_flights_by_parameters():
        new_path = 'flights/parameters'
        request.url = FacadeBase.edit_url(request.url, new_path)
        response = SearchesView.get_flights_by_parameters()
        return response

    @staticmethod
    def get_all_airlines():
        new_path = 'get/airlinecompanies'
        request.url = FacadeBase.edit_url(request.url, new_path)
        response = CrudViews.get_entities()
        return response

    @staticmethod
    def get_airline_by_id(airline_id):
        new_path = 'get/airlinecompanies'
        request.url = FacadeBase.edit_url(request.url, new_path)
        response = CrudViews.get_entity(airline_id)
        return response

    @staticmethod
    def get_airline_by_parameters():
        new_path = 'airlines/parameters'
        request.url = FacadeBase.edit_url(request.url, new_path)
        response = SearchesView.get_airlines_by_parameters()
        return response

    @staticmethod
    def get_all_countries():
        new_path = 'get/countries'
        request.url = FacadeBase.edit_url(request.url, new_path)
        response = CrudViews.get_entities()
        return response

    @staticmethod
    def get_country_by_id(country_id):
        new_path = 'get/countries'
        request.url = FacadeBase.edit_url(request.url, new_path)
        response = CrudViews.get_entity(country_id)
        return response

    @staticmethod
    def create_new_user(user_role):
        """
        Creates a new user with random data and assigns a user role.

        Args:
            user_role (str): The user role for the new user.

        Returns:
            dict: Updated user data.

        """
        new_user = create_user(user_role)
        updated_data = request.get_json()
        updated_data['user_id'] = new_user.id

        logger.info('A new user has been created')
        return updated_data

    @staticmethod
    def edit_add_entity_request(model):
        """
        Edit the request URL and data for adding an entity.

        Args:
            model (str): The model of the entity to be added.

        Returns:
            None
        """
        new_path = f"add/add_{model}".lower()
        request.url = FacadeBase.edit_url(request.url, new_path)

        updated_data = FacadeBase.create_new_user(model)
        request.data = updated_data

        logger.info('The request was successfully updated!')

    @staticmethod
    def edit_url(original_url, new_path):
        """
        Edit the path of a URL.

        Args:
            original_url (str): The original URL to be edited.
            new_path (str): The new path to replace the existing path in the URL.

        Returns:
            str: The edited URL with the new path.
        """
        parsed_url = urlparse(original_url)
        new_parsed_url = parsed_url._replace(path=new_path)
        edited_url = urlunparse(new_parsed_url)
        return edited_url
