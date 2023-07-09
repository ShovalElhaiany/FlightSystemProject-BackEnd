from .anonymousFacade import AnonymousFacade
from flask_login import login_required
from flask import redirect, url_for

class CustomerFacade(AnonymousFacade):
    """Facade class for customer-specific operations."""

    def __init__(self, user):
        super().__init__()
        self.user = user

    @classmethod
    @login_required
    def update_customer(self, customer_id):
        return redirect(url_for('update.update_entity_endpoint', entity_id=customer_id))

    @classmethod
    @login_required
    def add_ticket(self):
        return redirect(url_for('add.add_entity_endpoint'))

    @classmethod
    @login_required
    def remove_ticket(self, ticket_id):
        return redirect(url_for('remove.remove_entity_endpoint', entity_id=ticket_id))

    @classmethod
    @login_required
    def get_my_tickets(self, customer_id):
        return redirect(url_for('search.get_tickets_by_customer', customer_id=customer_id))
