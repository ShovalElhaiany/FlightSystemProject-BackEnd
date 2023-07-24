from app import deploy

from .config import (DATA_FOLDER, MODELS, MODELS_NAMES, ROLES_PERMISSIONS,
                     USER_ROLES, Config, DatabaseUri)
from .create_app import init_app
from .create_db import create_tables, insert_data
from .my_app import app, bcrypt, db, login_manager
