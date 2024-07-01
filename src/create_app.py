"""
This module initializes the Flask application, configures it, and registers routes and blueprints.
"""

from bluePrints.csu import setup_csu_bp
from bluePrints.facades import setup_facades_bp
from logs.log import logger
from routes.csu import setup_csu_routes
from routes.facades import setup_facades_routes
from src.config import Config
from src.my_app import app, bcrypt, db, login_manager, cors


def init_app():
    """
    Initializes the Flask application, configures it, and registers routes and blueprints.
    """
    # App configuration 
    app.config.from_object(Config)
    
    # Initialize extensions
    db.init_app(app)
    cors.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    # Register routes and blueprints
    setup_csu_routes()
    setup_facades_routes()
    setup_facades_bp()
    setup_csu_bp()

    login_manager.login = 'csuRoutes.login'

    app.app_context().push()

    logger.info('The app has been successfully configured!')
    
# def run_sql_file(filename):
#     with app.app_context():
#         with open(filename, 'r') as file:
#             sql_commands = file.read().split(';')
#             for command in sql_commands:
#                 if command.strip():
#                     db.session.execute(db.text(command))
#             db.session.commit()