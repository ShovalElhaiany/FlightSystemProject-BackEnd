from flask import redirect, request, url_for
from flask_login import login_required

from lib.views.crud import CrudViews
from logs.log import logger
from utils.auth import role_required

from .anonymous import AnonymousFacade


class AdministratorFacade(AnonymousFacade):
    """Facade class for admin-specific operations."""

    @staticmethod
    @login_required
    @role_required('Administrator')
    def get_all_customers():
        new_path = 'get/customers'
        request.url = request.url = f'{request.host_url}{new_path}'
        response = CrudViews.get_entities()
        return response
    

    @staticmethod
    @login_required
    @role_required('Administrator')
    def add_airline():
        """
        Add a airline entity.

        Returns:
            The response from the add_entity function.
        """
        model = 'AirlineCompanies'
        AnonymousFacade.edit_add_entity_request(model)
        try:
            response = CrudViews.add_entity()
        except Exception as e:
            logger.error(e)
        return response

    @staticmethod
    @login_required
    @role_required('Administrator')
    def add_administrator():
        """
        Add a administrator entity.

        Returns:
            The response from the add_entity function.
        """
        model = 'Administrators'
        AnonymousFacade.edit_add_entity_request(model)
        try:
            response = CrudViews.add_entity()
        except Exception as e:
            logger.error(e)
        return response

    @staticmethod
    @login_required
    @role_required('Administrator')
    def delete_airline(airline_id):
        return redirect(url_for('delete.delete_entity', entity_id=airline_id))

    @staticmethod
    @login_required
    @role_required('Administrator')
    def delete_customer(customer_id):
        return redirect(url_for('delete.delete_entity', entity_id=customer_id))

    @staticmethod
    @login_required
    @role_required('Administrator')
    def delete_administrator(admin_id):
        return redirect(url_for('delete.delete_entity', entity_id=admin_id))