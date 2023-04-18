#!/usr/bin/python3
"""
this script lists all State objects that contain the letter a
from the database hbtn_0e_6_usa
"""
from model_state import Base, State
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def main():
    """entry to the main program"""
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    with Session() as session:
        state_a = session.query(State).order_by(State.id).\
                filter(State.name.contains('a'))
        for state in state_a:
            print(f"{state.id}: {state.name}")


if __name__ == "__main__":
    """this code won't run if this file is imported"""
    main()
