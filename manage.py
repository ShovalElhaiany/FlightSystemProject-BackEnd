import os
import subprocess
from app import create_app
from create_db import create_tables, insert_data

def deploy():
    # def setup_environment():
    #     if not os.path.exists("venv"):
    #         subprocess.run(["python3", "-m", "venv", "venv"])
    #         subprocess.run(['pip', 'install', '-r', 'requirements.txt'])
            
    # setup_environment()
    app = create_app()
    create_tables(app)
    insert_data(app)

deploy()
# if __name__ == '__main__':
#     app = create_app()
#     try:
#         app.run(debug=True)
#     except ImportError:
#         from manage import deploy
#         deploy()
