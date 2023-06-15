from app import db

# Import your models here
from Dal.models import *

# Create the database tables
db.create_all()

# Perform any additional setup tasks, if needed
