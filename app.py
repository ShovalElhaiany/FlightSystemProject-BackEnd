from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
login_manager= LoginManager()
bcrypt = Bcrypt()

def create_app():
    app = Flask(__name__)
    app.secret_key = 'flaskey'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Shoval963654@localhost:3306/Flights_System_BD'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    login_manager.init_app(app)
    bcrypt.init_app(app)

    return app