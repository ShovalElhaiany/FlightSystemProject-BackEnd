from src.myApp import app
from src.create_app import init_app
from src.create_db import create_tables, insert_data
import os
LOCK_FILE = "./lock"

def deploy():
    init_app()
    create_tables()
    insert_data()

if __name__ == '__main__':
    if not os.path.exists(LOCK_FILE):
        deploy()
        open(LOCK_FILE, 'w').close()
    else:
        init_app()
        app.run(debug=True)