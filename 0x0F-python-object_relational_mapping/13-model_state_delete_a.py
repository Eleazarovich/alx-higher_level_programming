#!/usr/bin/python3
"""
this script changes the name of a State object from the database hbtn_0e_6_usa
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
        state = session.query(State).filter(State.name.contains('a'))
        for i in state:
            session.delete(i)
        session.commit()


if __name__ == "__main__":
    """this code won't run if this file is imported"""
    main()
