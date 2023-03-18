#!/usr/bin/python3
"""
    Create a python class State that inherits
    from Base class and links it to the MySQL
    table
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from relationship_city import City, Base


class State(Base):
    """
        This is a sql query representation
        in the for of a class
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="all, delete", backref="state")
