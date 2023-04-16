#!/usr/bin/python3
"""
this script takes in arguments and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument
this script is safe from MySQL injections!
"""
import MySQLdb
from sys import argv


def main():
    with MySQLdb.connect(
            host="localhost",
            user=argv[1],
            passwd=argv[2],
            port=3306,
            db=argv[3]
            ) as db:
        with db.cursor() as cur:
            cur.execute(f"SELECT * FROM states WHERE name = %s\
                    ORDER BY states.id ASC", (argv[4],))
            rows = cur.fetchall()
            for row in rows:
                print(row)


if __name__ == "__main__":
    """this code won't be run when this code is imported"""
    main()
