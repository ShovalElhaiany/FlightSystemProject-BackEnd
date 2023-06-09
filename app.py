from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Shoval963654@localhost:3306/flights_system_db'  # Replace with your MySQL database credentials
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Register routes
from routes import setup_routes
setup_routes(app)

if __name__ == '__main__':
    app.run()
