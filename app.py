import os

from logs.log import logger
from src.create_app import init_app
from src.create_db import create_tables, insert_data
from src.my_app import app

LOCK_FILE = 'temp/lock'

def deploy():
    """Deploys the application by initializing the app, creating tables, and inserting data."""
    try:
        init_app()
        create_tables()
        insert_data()
    except Exception as e:
        logger.critical(e)

if __name__ == '__main__':
    if not os.path.exists(LOCK_FILE):
        deploy()
        open(LOCK_FILE, 'w').close()
        logger.info('deploy was executed successfully!')
        app.run(debug=True)
    else:
        init_app()
        app.run(debug=True)
