from flask import Flask
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app: Flask = Flask(__name__)
db: SQLAlchemy = SQLAlchemy()
cors: CORS = CORS()
bcrypt: Bcrypt = Bcrypt()
login_manager: LoginManager = LoginManager()