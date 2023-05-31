from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
engine = None
Session = sessionmaker()


def global_init(db_file):
    global engine
    engine = create_engine(db_file)
    Session.configure(bind=engine)
    Base.metadata.create_all(engine)
