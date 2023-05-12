from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from data import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, unique=True)
    password = Column(String)

    __mapper_args__ = {
        'polymorphic_identity': 'users',
        'polymorphic_on': type
    }


class Customer(User):
    __tablename__ = 'customers'

    id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    name = Column(String)
    email = Column(String)
    phone = Column(String)

    tickets = relationship('Ticket', back_populates='customer')

    __mapper_args__ = {
        'polymorphic_identity': 'customers'
    }

    def to_dict(self
