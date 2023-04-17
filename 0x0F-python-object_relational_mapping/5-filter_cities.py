#!/usr/bin/python3
"""
this script akes in the name of a state as an argument and lists all cities
of that state, using the database hbtn_0e_4_usa
"""
import MySQLdb
from sys import argv


def main():
    """main entry of the program"""
    with MySQLdb.connect(
            host="localhost",
            user=argv[1],
            passwd=argv[2],
            port=3306,
            db=argv[3]
            ) as db:
        with db.cursor() as cur:
            cur.execute(f"SELECT cities.name FROM cities JOIN states ON\
            cities.state_id = states.id WHERE states.name = %s\
            ORDER BY cities.id", (argv[4],))
            rows = cur.fetchall()
            print(", ".join(city[0] for city in rows))


if __name__ == "__main__":
    """this code won't run when this file is imported"""
    main()
