from .facadeBase import FacadeBase
from flask import redirect, url_for
from views.crudView import add_entity_endpoint


class AnonymousFacade(FacadeBase):
    def __init__(self):
        super().__init__(None)

    @classmethod
    def login(self):
       return redirect(url_for('user.login'))

    @classmethod
    def add_customer(self):
        model = 'Customers'
        FacadeBase.edit_add_entity_request(model)
        response = add_entity_endpoint()
        return response