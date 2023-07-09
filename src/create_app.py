"""
This module initializes the Flask application, configures it, and registers routes and blueprints.
"""

from routes.csuRoutes import setup_csuRoutes
from routes.facadesRoutes import setup_facadesRoutes
from bluePrints.facadesBp import setup_FacadesBp
from bluePrints.csuBp import setup_csuBp

from src.config import Config
from src.myApp import app, db, bcrypt, login_manager
from logs.log import logger

def init_app():
    """
    Initializes the Flask application, configures it, and registers routes and blueprints.
    """
    # App configuration 
    app.config.from_object(Config)
    
    # Initialize extensions
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    
    # Register routes and blueprints
    setup_csuRoutes()
    setup_facadesRoutes()
    setup_FacadesBp()
    setup_csuBp()

    login_manager.login_view = 'csuRoutes.login'

    app.app_context().push()

    logger.info('The app has been successfully configured!')
