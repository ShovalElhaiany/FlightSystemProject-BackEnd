import subprocess
import venv

from src.myApp import app
from src.create_app import init_app
from src.create_db import create_tables, insert_data
import os
LOCK_FILE = "./lock"



def setup_env():
    venv_path = '.venv'
    requirements_file = 'requirements.txt'

    venv.create(venv_path, with_pip=True)
    activate_script = 'Scripts\\activate.bat'
    activate_path = f'{venv_path}/{activate_script}'

    subprocess.call(f'call {activate_path} && pip install -r {requirements_file}', shell=True)

def deploy():
    setup_env()
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