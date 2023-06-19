from flask import Blueprint

get=Blueprint('get', __name__)
add=Blueprint('add', __name__)
update=Blueprint('update', __name__)
remove=Blueprint('remove', __name__)
searche=Blueprint('searches', __name__)
user = Blueprint('/user', __name__)
facade = Blueprint('/facade', __name__)


def setup_blueprints(app):
    app.register_blueprint(add, url_prefix = '/add')
    app.register_blueprint(get, url_prefix = '/get')
    app.register_blueprint(update, url_prefix = '/update')
    app.register_blueprint(remove, url_prefix = '/remove')
    app.register_blueprint(searche, url_prefix = '/searche')
    app.register_blueprint(user, url_prefix = '/user')
    app.register_blueprint(facade, url_prefix = '/facade')