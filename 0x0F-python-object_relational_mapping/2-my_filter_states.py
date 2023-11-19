#!/usr/bin/python3
"""script that lists all states from the database hbtn_0e_0_usa:"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
        port=3306
        )
    # create object instance
    cur = db.cursor()

    # execute query
    cur.execute("SELECT * FROM states WHERE name = '{0}' ORDER BY id".format(
        argv[4]))
    result = cur.fetchall()
    for row in result:
        print(row)
    cur.close()
    db.close()
