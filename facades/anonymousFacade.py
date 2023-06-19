from .facadeBase import FacadeBase
from flask import redirect, url_for

class AnonymousFacade(FacadeBase):
    def __init__(self):
        super().__init__(None)

    @classmethod
    def login(self, username, password):
       return redirect(url_for('user.login', 
                               username=username, 
                               password=password))

    @classmethod
    def add_customer(self):
        return redirect(url_for('add.add_entity_endpoint'))

