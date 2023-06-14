from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Shoval963654@localhost:3306/flights_system_db'  # Replace with your MySQL database credentials
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'flaskey'

db = SQLAlchemy(app)
bcrypt = Bcrypt()
login_manager = LoginManager()

bcrypt.init_app(app)
login_manager.init_app(app)

login_manager.login_view = 'routes.login'

# Register routes and blueprints
from routes import(
    setup_routes,
    add,
    get,
    update,
    remove,
    searche,
    user
) 
setup_routes(app)
app.register_blueprint(add, url_prefix = '/add')
app.register_blueprint(get, url_prefix = '/get')
app.register_blueprint(update, url_prefix = '/update')
app.register_blueprint(remove, url_prefix = '/remove')
app.register_blueprint(searche, url_prefix = '/searche')
app.register_blueprint(user, url_prefix = '/user')

if __name__ == '__main__':
    app.run()
