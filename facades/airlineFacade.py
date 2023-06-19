from .anonymousFacade import AnonymousFacade
from flask_login import login_required
from flask import redirect, url_for

class AirlineFacade(AnonymousFacade):
    def __init__(self, user):
        super().__init__()
        self.user = user

    @classmethod
    @login_required
    def update_airline(self, airline_id):
        return redirect(url_for('update.update_entity_endpoint', entity_id=airline_id))

    @classmethod
    @login_required
    def add_flight(self):
        return redirect(url_for('add.add_entity_endpoint'))
     
    @classmethod
    @login_required
    def update_flight(self,flight_id):
        return redirect(url_for('update.update_entity_endpoint', entity_id=flight_id))


    @classmethod
    @login_required
    def remove_flight(self, flight_id):
        return redirect(url_for('remove.remove_entity_endpoint', entity_id=flight_id))


    @classmethod
    @login_required
    def get_my_flights(self, customer_id):
        pass



 
   