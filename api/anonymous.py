from flask import redirect, url_for

from lib.views.crud import CrudViews
from logs.log import logger

from .base import FacadeBase, edit_add_entity_request


class AnonymousFacade(FacadeBase):
    """Facade class for anonymous-specific operations."""

    @staticmethod
    def login():
        return redirect(url_for('user.login'))

    @staticmethod
    def add_customer():
        """
        Add a customer entity.

        Returns:
            The response from the add_entity function.
        """
        model = 'Customers'
        edit_add_entity_request(model)
        try:
            response = CrudViews.add_entity()
        except Exception as e:
            logger.error(e)
        return response