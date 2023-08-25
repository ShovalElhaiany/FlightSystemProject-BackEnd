from flask import request
from flask_login import login_required

from lib.views.searches import SearchesView
from utils.auth import role_required

from .anonymous import AnonymousFacade
from lib.views.crud import CrudViews


class CustomerFacade(AnonymousFacade):
    """Facade class for customer-specific operations."""

    @staticmethod
    #@login_required
    #@role_required('Customers')
    def get_customer(customer_id):
        new_path = 'get/customers'
        request.url = request.url = f'{request.host_url}{new_path}/{customer_id}'
        response = CrudViews.get_entity(customer_id)
        return response
    
    @staticmethod
    #@login_required
    #@role_required('Customers')
    def update_customer(customer_id):
        new_path = 'update/customers'
        request.url = request.url = f'{request.host_url}{new_path}/{customer_id}'
        response = CrudViews.update_entity(customer_id)
        return response

    @staticmethod
    #@login_required
    #@role_required('Customers')
    def add_ticket():
        new_path = 'add/add_tickets'
        request.url = request.url = f'{request.host_url}{new_path}'
        response = CrudViews.add_entity()
        return response

    @staticmethod
    #@login_required
    #@role_required('Customers')
    def delete_ticket(ticket_id):
        new_path = 'delete/tickets'
        request.url = request.url = f'{request.host_url}{new_path}/{ticket_id}'
        response = CrudViews.delete_entities(ticket_id)
        return response

    @staticmethod
    #@login_required
    #@role_required('Customers')
    def get_all_tickets():
        new_path = 'get/tickets'
        request.url = request.url = f'{request.host_url}{new_path}'
        response = CrudViews.get_entities()
        return response
    
    @staticmethod
    #@login_required
    #@role_required('Customers')
    def get_my_tickets(customer_id):
        new_path = 'tickets/customer'
        request.url = request.url = f'{request.host_url}{new_path}/{customer_id}'
        response = SearchesView.get_tickets_by_customer(customer_id)
        return response