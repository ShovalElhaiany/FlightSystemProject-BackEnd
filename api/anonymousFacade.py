from .facadeBase import FacadeBase
from flask import redirect, url_for
from lib.views.crudView import add_entity_view
from logs.log import logger


class AnonymousFacade(FacadeBase):
    """Facade class for anonymous-specific operations."""

    def __init__(self):
        super().__init__(None)

    @classmethod
    def login(self):
        return redirect(url_for('user.login'))

    @classmethod
    def add_customer(self):
        """
        Add a customer entity.

        Returns:
            The response from the add_entity_view function.
        """
        model = 'Customers'
        FacadeBase.edit_add_entity_request(model)
        try:
            response = add_entity_view()
        except Exception as e:
            logger.error(e)
        return response