from flask import Blueprint

from src.my_app import app

# Create blueprint instances for each functionality
base = Blueprint('base', __name__)
anonymous = Blueprint('anonymous', __name__)
airline = Blueprint('airline', __name__)
administrator = Blueprint('administrator', __name__)
customer = Blueprint('customer', __name__)

def setup_facades_bp():
    """
    Sets up and registers the blueprint objects for different facades in the Flask app.

    Each facade blueprint is registered with a specific URL prefix.

    """
    app.register_blueprint(base, url_prefix='/base')
    app.register_blueprint(anonymous, url_prefix='/anonymous')
    app.register_blueprint(airline, url_prefix='/airline')
    app.register_blueprint(administrator, url_prefix='/administrator')
    app.register_blueprint(customer, url_prefix='/customer')
