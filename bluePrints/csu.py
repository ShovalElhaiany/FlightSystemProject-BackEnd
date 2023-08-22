from flask import Blueprint

from src.my_app import app

# Create blueprint instances for each functionality
get = Blueprint('get', __name__)
add = Blueprint('add', __name__)
update = Blueprint('update', __name__)
delete = Blueprint('delete', __name__)
search = Blueprint('search', __name__)
user = Blueprint('user', __name__)

def setup_csu_bp():
    """
    Sets up and registers the blueprint objects for different facades in the Flask app.

    Each facade blueprint is registered with a specific URL prefix.

    """
    app.register_blueprint(add, url_prefix='/add')
    app.register_blueprint(get, url_prefix='/get')
    app.register_blueprint(update, url_prefix='/update')
    app.register_blueprint(delete, url_prefix='/delete')
    app.register_blueprint(search, url_prefix='/search')
    app.register_blueprint(user, url_prefix='/user')
