from .facadeBase import FacadeBase
from flask import redirect, url_for
from src.config import USER_ROLES
from flask import request

class AnonymousFacade(FacadeBase):
    def __init__(self):
        super().__init__(None)

    @classmethod
    def login(self):
       return redirect(url_for('user.login'))

    @classmethod
    def add_customer(self):
        user_role = USER_ROLES['Customers']
        updated_request = FacadeBase.create_new_user(user_role)
        # request.data = updated_request
        return redirect(url_for('add.add_entity_endpoint'))