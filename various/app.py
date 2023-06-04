from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from routes import flights_routes, airline_routes, users_routes, countries_routes, tickets_routes, customers_routes, user_roles_routes, administrators_routes
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
bcrypt = Bcrypt()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'your_database_uri'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    bcrypt.init_app(app)

    # Initialize the database
    db.init_app(app)

    # Register the API routes
    app.register_blueprint(flights_routes)
    app.register_blueprint(airline_routes)
    app.register_blueprint(users_routes)
    app.register_blueprint(countries_routes)
    app.register_blueprint(tickets_routes)
    app.register_blueprint(customers_routes)
    app.register_blueprint(user_roles_routes)
    app.register_blueprint(administrators_routes)

    return app


if __name__ == '__main__':
    app = create_app()
    app.run()
