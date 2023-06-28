from .anonymousFacade import AnonymousFacade
from flask_login import login_required
from flask import redirect, url_for
from src.config import USER_ROLES

class AdministratorFacade(AnonymousFacade):
    def __init__(self, user):
        super().__init__()
        self.user = user

    @classmethod
    @login_required
    def get_all_customers(self):
        return redirect(url_for('get.get_all_entities'))
    
    @classmethod
    @login_required
    def add_airline(self):
        user_role = USER_ROLES['AirlineCompanies']
        AnonymousFacade.create_new_user(user_role)
        return redirect(url_for('add.add_entity_endpoint'))

    @classmethod
    @login_required
    def add_administrator(self):
        user_role = USER_ROLES['Administrators']
        AnonymousFacade.create_new_user(user_role)
        return redirect(url_for('add.add_entity_endpoint'))

    @classmethod
    @login_required
    def remove_airline(self, airline_id):
        return redirect(url_for('remove.remove_entity_endpoint', entity_id=airline_id))

    @classmethod
    @login_required
    def remove_customer(self, customer_id):
        return redirect(url_for('remove.remove_entity_endpoint', entity_id=customer_id))

    
    @classmethod
    @login_required
    def remove_administrator(self, admin_id):
        return redirect(url_for('remove.remove_entity_endpoint', entity_id=admin_id))

