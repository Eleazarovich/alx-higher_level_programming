#!/usr/bin/python3
"""this script lists all cities from the database hbtn_0e_4_usa"""
import MySQLdb
from sys import argv


def main():
    """entry to the main program"""
    with MySQLdb.connect(
            host="localhost",
            user=argv[1],
            passwd=argv[2],
            port=3306,
            db=argv[3]
            ) as db:
        with db.cursor() as cur:
            cur.execute("SELECT cities.id, cities.name, states.name FROM\
                    cities JOIN states ON cities.state_id = states.id\
                    ORDER BY cities.id ASC")
            rows = cur.fetchall()
            for row in rows:
                print(row)


if __name__ == "__main__":
    """this code won't run when this file is imported"""
    main()
