#!/usr/bin/python3
"""
contains the class definition
of a State and an
instance Base = declarative_base():
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sys import argv

Base = declarative_base()


class State(Base):
    """
    State class in db

    Attributes:
        __tablename__(str): db table name
        id (int): Primary key of state which is auto incremented
        name (str): state name 128 char max
    """

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, unique=True,
                nullable=False, autoincrement=True)
    name = Column(String(128),  nullable=False)
