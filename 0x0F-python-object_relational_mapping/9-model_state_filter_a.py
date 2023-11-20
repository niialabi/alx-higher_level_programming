#!/usr/bin/python3
"""
script that prints the first State object from the database hbtn_0e_6_usa
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
    output = (session.query(State)
              .filter(State.name.like('%a%'))
              .order_by(State.id.asc())
              .all())
    for out in output:
        print(f"{out.id}: {out.name}")
    session.close()
