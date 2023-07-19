import json
import os

from logs.log import log_and_raise, logger
from src.my_app import db

from .config import DATA_FOLDER, MODELS


def create_tables():
    """
    Creates database tables.

    This function creates tables in the database using SQLAlchemy's `create_all` method.
    It assumes that the database is already initiated to the Flask app.

    Args:
        app (Flask): The Flask app to create tables for.
    """
    try:
        db.create_all()
        logger.info('Tables created successfully!')
    except Exception as e:
        log_and_raise(e, 'critical')


def insert_data():
    """
    Inserts data into database tables.

    This function inserts data into multiple tables specified in the `MODELS` list.
    It reads JSON files containing data for each table and inserts the data into the respective table.

    Raises:
        Exception: If an error occurs during the insertion process.
    """
    for model in MODELS:
        model_name = model.__name__
        model_file = f'{model_name[0].lower() + model_name[1:]}Data.json'
        json_path = os.path.join(DATA_FOLDER, model_file)

        try:
            with open(json_path, 'r') as file:
                data = json.load(file)

            # Insert data into table
            for item in data:
                record = model(**item)
                db.session.add(record)

            db.session.commit()
            logger.info(f'Data inserted into {model_name} successfully!')

        except Exception as e:
            log_and_raise(e, 'critical')
