#!/usr/bin/python3
"""
script that lists all State objects from the database hbtn_0e_6_usa
"""
from sys import argv
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine(f"mysql://{argv[1]}:\
        {argv[2]}@localhost:3306/{argv[3]}")
    Session = sessionmaker(bind=engine)
    session = Session()
    state_lui = State(name="Louisiana")
    session.add(state_lui)
    session.commit()
    print(state_lui.id)
    session.close()
