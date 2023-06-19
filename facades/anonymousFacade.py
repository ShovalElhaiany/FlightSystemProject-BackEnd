from .facadeBase import FacadeBase
from flask import redirect, url_for

class AnonymousFacade(FacadeBase):
    def __init__(self):
        super().__init__(None)

    @classmethod
    def login(self):
       return redirect(url_for('user.login'))

    @classmethod
    def add_customer(self):
        return redirect(url_for('add.add_entity_endpoint'))

