from views import (
    get_entity_endpoint,
    get_all_entities_endpoint,
    add_entity_endpoint,
    add_entities_endpoint,
    update_entity_endpoint,
    update_entities_endpoint,
    remove_entity_endpoint,
    remove_all_entities_endpoint
)

def setup_routes(app):
    models = ['Flights', 'AirlineCompanies', 'Users', 'Countries', 'Tickets', 'Customers', 'UserRoles', 'Administrators']
    for model in models:
        app.add_url_rule(f'/{model.lower()}/<int:entity_id>', methods=['GET'], view_func=get_entity_endpoint)
        app.add_url_rule(f'/{model.lower()}', methods=['GET'], view_func=get_all_entities_endpoint)
        app.add_url_rule(f'/add_{model.lower()}', methods=['POST'], view_func=add_entity_endpoint)
        app.add_url_rule(f'/{model.lower()}', methods=['POST'], view_func=add_entities_endpoint)
        app.add_url_rule(f'/{model.lower()}/<int:entity_id>', methods=['PUT'], view_func=update_entity_endpoint)
        app.add_url_rule(f'/{model.lower()}', methods=['PUT'], view_func=update_entities_endpoint)
        app.add_url_rule(f'/{model.lower()}/<int:entity_id>', methods=['DELETE'], view_func=remove_entity_endpoint)
        app.add_url_rule(f'/{model.lower()}', methods=['DELETE'], view_func=remove_all_entities_endpoint)
