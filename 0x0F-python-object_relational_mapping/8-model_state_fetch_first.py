#!/usr/bin/python3
"""
this script prints the first State object from the database hbtn_0e_6_usa
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
        first_state = session.query(State).order_by(State.id).first()
        if first_state is None:
            print("Nothing")
        else:
            print(f"{first_state.id}: {first_state.name}")


if __name__ == "__main__":
    """this code won't run if this file is imported"""
    main()
