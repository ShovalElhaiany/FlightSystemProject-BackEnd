from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from bluePrints.facadesBp import setup_FacadesBp
from bluePrints.csuBp import setup_csuBp
from config import Config
from create_db import db

bcrypt = Bcrypt()
login_manager = LoginManager()

def create_app():
    # App configuration
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Initialize extensions
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    
    # Register routes and blueprints
    from routes.csuRoutes import setup_csuRoutes
    from routes.facadesRoutes import setup_facadesRoutes

    setup_csuRoutes(app)
    setup_facadesRoutes(app)
    setup_FacadesBp(app)
    setup_csuBp(app)

    login_manager.login_view = 'csuRoutes.login'

    app.app_context().push()
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)