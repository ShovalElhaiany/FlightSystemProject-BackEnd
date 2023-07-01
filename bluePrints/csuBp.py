from flask import Blueprint
from src.myApp import app

get=Blueprint('get', __name__)
add=Blueprint('add', __name__)
update=Blueprint('update', __name__)
remove=Blueprint('remove', __name__)
search=Blueprint('search', __name__)
user = Blueprint('user', __name__)

def setup_csuBp():
    app.register_blueprint(add, url_prefix = '/add')
    app.register_blueprint(get, url_prefix = '/get')
    app.register_blueprint(update, url_prefix = '/update')
    app.register_blueprint(remove, url_prefix = '/remove')
    app.register_blueprint(search, url_prefix = '/search')
    app.register_blueprint(user, url_prefix = '/user')