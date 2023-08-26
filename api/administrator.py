from flask import request
from flask_login import login_required

from lib.views.crud import CrudViews
from logs.log import logger
from utils.auth import role_required

from .anonymous import AnonymousFacade


class AdministratorFacade(AnonymousFacade):
    """Facade class for admin-specific operations."""

    @staticmethod
    #@login_required
    #@role_required('Administrators')
    def get_all_customers():
        new_path = 'get/customers'
        request.url = request.url = f'{request.host_url}{new_path}'
        response = CrudViews.get_entities()
        return response

    @staticmethod
    #@login_required
    #@role_required('Administrators')
    def get_customer(customer_id):
        new_path = 'get/customers'
        request.url = request.url = f'{request.host_url}{new_path}/{customer_id}'
        response = CrudViews.get_entity(customer_id)
        return response
    
    @staticmethod
    #@login_required
    #@role_required('Administrators')
    def add_airline():
        """S
        Add a airline entity.

        Returns:
            The response from the add_entity function.
        """
        AnonymousFacade.edit_add_entity_request()
        try:
            response = CrudViews.add_entity()
        except Exception as e:
            logger.error(e)
        return response
    
    @staticmethod
    #@login_required
    #@role_required('Administrators')
    def get_all_administrators():
        new_path = 'get/administrators'
        request.url = request.url = f'{request.host_url}{new_path}'
        response = CrudViews.get_entities()
        return response
    
    @staticmethod
    #@login_required
    #@role_required('Administrators')
    def get_administrator(admin_id):
        new_path = 'get/administrators'
        request.url = request.url = f'{request.host_url}{new_path}/{admin_id}'
        response = CrudViews.get_entity(admin_id)
        return response

    @staticmethod
    #@login_required
    #@role_required('Administrators')
    def add_administrator():
        """
        Add a administrator entity.

        Returns:
            The response from the add_entity function.
        """
        AnonymousFacade.edit_add_entity_request()
        try:
            response = CrudViews.add_entity()
        except Exception as e:
            logger.error(e)
        return response

    @staticmethod
    #@login_required
    #@role_required('Administrators')
    def delete_airline(airline_id):
        new_path = 'delete/airlinecompanies'
        request.url = request.url = f'{request.host_url}{new_path}/{airline_id}'
        response = CrudViews.delete_entity(airline_id)
        return response

    @staticmethod
    #@login_required
    #@role_required('Administrators')
    def delete_customer(customer_id):
        new_path = 'delete/customers'
        request.url = request.url = f'{request.host_url}{new_path}/{customer_id}'
        response = CrudViews.delete_entity(customer_id)
        return response

    @staticmethod
    #@login_required
    #@role_required('Administrators')
    def delete_administrator(admin_id):
        new_path = 'delete/administrators'
        request.url = request.url = f'{request.host_url}{new_path}/{admin_id}'
        response = CrudViews.delete_entity(admin_id)
        return response