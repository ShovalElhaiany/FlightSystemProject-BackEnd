from flask import redirect, url_for
from flask_login import login_required

from lib.views.crud import CrudViews
from logs.log import logger

from .anonymous import AnonymousFacade
from .base import edit_add_entity_request


class AdministratorFacade(AnonymousFacade):
    """Facade class for admin-specific operations."""

    @staticmethod
    @login_required
    def get_all_customers():
        return redirect(url_for('get.get_all_entities'))

    @staticmethod
    @login_required
    def add_airline():
        """
        Add a airline entity.

        Returns:
            The response from the add_entity function.
        """
        model = 'AirlineCompanies'
        edit_add_entity_request(model)
        try:
            response = CrudViews.add_entity()
        except Exception as e:
            logger.error(e)
        return response

    @staticmethod
    @login_required
    def add_administrator():
        """
        Add a administrator entity.

        Returns:
            The response from the add_entity function.
        """
        model = 'Administrators'
        edit_add_entity_request(model)
        try:
            response = CrudViews.add_entity()
        except Exception as e:
            logger.error(e)

        return response

    @staticmethod
    @login_required
    def remove_airline(airline_id):
        return redirect(url_for('remove.remove_entity_endpoint', entity_id=airline_id))

    @staticmethod
    @login_required
    def remove_customer(customer_id):
        return redirect(url_for('remove.remove_entity_endpoint', entity_id=customer_id))

    @staticmethod
    @login_required
    def remove_administrator(admin_id):
        return redirect(url_for('remove.remove_entity_endpoint', entity_id=admin_id))