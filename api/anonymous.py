from flask import request

from lib.views.crud import CrudViews
from utils.auth import login
from logs.log import logger

from .base import FacadeBase


class AnonymousFacade(FacadeBase):
    """Facade class for anonymous-specific operations."""

    @staticmethod
    def login():
        new_path = 'user/flights'
        request.url = FacadeBase.edit_url(request.url, new_path)
        response = login()
        return response

    @staticmethod
    def add_customer():
        """
        Add a customer entity.

        Returns:
            The response from the add_entity function.
        """
        model = 'Customers'
        FacadeBase.edit_add_entity_request(model)
        try:
            response = CrudViews.add_entity()
        except Exception as e:
            logger.error(e)
        return response