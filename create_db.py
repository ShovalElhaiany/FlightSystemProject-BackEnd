from flask_sqlalchemy import SQLAlchemy
import os
import json

db = SQLAlchemy()

def create_tables(app):
    """Creates tables and inserts data."""
    db.init_app(app)
    db.create_all()
    print("Tables created successfully!")

def insert_data(app):
    # Insert data into multiple tables
    from config import MODELS, DATA_FOLDER

    for model in MODELS:
        model_name = model.__name__
        model_file = f"{model_name[0].lower() + model_name[1:]}Data.json"
        json_path = os.path.join(DATA_FOLDER, model_file)

        with open(json_path, 'r') as file:
            data = json.load(file)

        # Insert data into table
        for item in data:
            record = model(**item)
            db.session.add(record)

        db.session.commit()
        print(f"Data inserted into {model_name} successfully!")
