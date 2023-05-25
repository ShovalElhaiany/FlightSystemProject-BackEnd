from flask import Flask
from configuration import Configuration
from data import db_session
from api import blueprint


app = Flask(__name__)
app.config.from_object(Configuration)

app.register_blueprint(blueprint)

if __name__ == '__main__':
    db_session.global_init(app.config['DATABASE_URI'])
    app.run()
