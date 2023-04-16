#!/usr/bin/python3
"""
this script lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa
"""
import MySQLdb
from sys import argv


def main():
    """main entry of the program"""
    db = MySQLdb.connect(
            host="localhost",
            user=argv[1],
            passwd=argv[2],
            port=3306,
            db=argv[3]
            )

    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%'\
            ORDER BY states.id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()


if __name__ == "__main__":
    """this code won't run if this file is imported"""
    main()
