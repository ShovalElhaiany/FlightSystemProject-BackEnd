from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

app = Flask(__name__)

bcrypt = Bcrypt()
login_manager = LoginManager()

# App configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Shoval963654@localhost:3306/flights_system_db'  # Replace with your MySQL database credentials
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'flaskey'

# Init App
db = SQLAlchemy(app)
bcrypt.init_app(app)
login_manager.init_app(app)

# Register routes and blueprints
from routes import *
setup_routes(app)
setup_blueprints(app)

login_manager.login_view = 'routes.login'

if __name__ == '__main__':
    app.run()
