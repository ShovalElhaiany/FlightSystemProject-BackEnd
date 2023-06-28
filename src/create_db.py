from src.myApp import db
import os
import json

from .config import MODELS, DATA_FOLDER

def create_tables():
    """
    Creates the db

    Args:
        app (Flask): The flask app to create tables for. Assumes the db is already initiated to this app
    """    
    db.create_all()
    print("Tables created successfully!")

def insert_data():
    # Insert data into multiple tables
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
