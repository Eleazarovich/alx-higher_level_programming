#!/usr/bin/python3
"""
this script prints the State object with the name passed
as argument from the database hbtn_0e_6_usa
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
        query = session.query(State).order_by(State.id).\
                filter(State.name == (argv[4],))
        try:
            print(query[0].id)
        except IndexError:
            print("Not found")


if __name__ == "__main__":
    """this code won't run if this file is imported"""
    main()
