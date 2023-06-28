from routes.csuRoutes import setup_csuRoutes
from routes.facadesRoutes import setup_facadesRoutes
from bluePrints.facadesBp import setup_FacadesBp
from bluePrints.csuBp import setup_csuBp

from src.config import Config
from src.myApp import app, db, bcrypt, login_manager

def init_app():
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