#!/usr/bin/python3
"""
this script takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument
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
    query = """
    SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY states.id ASC
    """
    query = query.format(argv[4])
    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()


if __name__ == "__main__":
    """this code won't be run if this file is imported"""
    main()
