from flask import redirect, request, url_for
from views.userManageView import create_user_with_random_data
from src.config import USER_ROLES

class FacadeBase():

    def get_all_flights(self):
        return redirect(url_for('get.get_all_entities'))

    def get_flight_by_id(self, flight_id):
        return redirect(url_for('get.get_entity_endpoint', entity_id=flight_id))

    def get_flights_by_parameters(self):
        return redirect(url_for('search.get_flights_by_parameters'))

    def get_all_airlines(self):
        return redirect(url_for('get.get_all_entities'))

    def get_airline_by_id(self, airline_id):
        return redirect(url_for('get.get_entity_endpoint', entity_id=airline_id))

    def get_airline_by_parameters(self):
        return redirect(url_for('search.get_airlines_by_parameters'))
    
    def get_all_countries(self):
        return redirect(url_for('get.get_all_entities'))

    def get_country_by_id(self, country_id):
        return redirect(url_for('get.get_entity_endpoint', entity_id=country_id))
   
    @classmethod
    def create_new_user(self, user_role):
        new_user = create_user_with_random_data(user_role)
        updated_data = request.get_json()
        updated_data['user_id'] = new_user.id

        return updated_data

    def edit_add_entity_request(model):
        url_model = f'add_{model.lower()}'
        role = USER_ROLES[model]
        
        def edit_url(url_model):
            url = request.url
            url_bp = 'add'
            url = url.split("/")
            if len(url) >= 4:
                url[3]=url_bp
                url[4]=url_model
                new_url = "/".join(url)
                return new_url
            
        new_url = edit_url(url_model)
        updated_data = FacadeBase.create_new_user(role) 
        
        request.url = new_url
        request.data = updated_data
        
        print('The request was successfully updated!')