#!/usr/bin/python3
"""script lists all State objects contain
the letter a from the database hbtn_0e_6_usa"""
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import sys

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(State).filter(State.name.contains('a')):
        print("{:d}: {:s}".format(state.id, state.name))
