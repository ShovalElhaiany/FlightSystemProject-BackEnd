from flask import Blueprint
from src.myApp import app

facadeBase = Blueprint('facadeBase', __name__)
anonymousFacade = Blueprint('anonymousFacade', __name__)
airlineFacade = Blueprint('airlineFacade', __name__)
administratorFacade = Blueprint('administratorFacade', __name__)
customerFacade = Blueprint('customerFacade', __name__)


def setup_FacadesBp():
    app.register_blueprint(facadeBase, url_prefix = '/facadeBase')
    app.register_blueprint(anonymousFacade, url_prefix = '/anonymousFacade')
    app.register_blueprint(airlineFacade, url_prefix = '/airlineFacade')
    app.register_blueprint(administratorFacade, url_prefix = '/administratorFacade')
    app.register_blueprint(customerFacade, url_prefix = '/customerFacade')