from .anonymousFacade import AnonymousFacade
from flask_login import login_required
from flask import redirect, url_for
from views.crudView import add_entity_endpoint

class AdministratorFacade(AnonymousFacade):
    def __init__(self):
        super().__init__()


    @classmethod
    @login_required
    def get_all_customers(self):
        return redirect(url_for('get.get_all_entities'))
    
    @classmethod
    @login_required
    def add_airline(self):
        model= 'AirlineCompanies'
        AnonymousFacade.edit_add_entity_request(model)
        response = add_entity_endpoint()
        return response

    @classmethod
    @login_required
    def add_administrator(self):
        model= 'Administrators'
        AnonymousFacade.edit_add_entity_request(model)
        response = add_entity_endpoint()
        return response

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

