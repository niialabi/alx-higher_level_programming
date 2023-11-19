#!/usr/bin/python3
"""script that lists all cities from the database hbtn_0e_4_usa"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    # connecting to DB
    db = MySQLdb.connect(
        host="localhost",
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
        port=3306
        )
    user_input = argv[4]

    # create curson object
    cur = db.cursor()
    query = "SELECT name FROM cities WHERE state_id = \
        (SELECT id FROM states WHERE name = %s) ORDER BY cities.id ASC"
    cur.execute(query, (user_input, ))
    res = cur.fetchall()
    output_tup = ()
    for row in res:
        output_tup += row
    print(*output_tup, sep=", ")
    """
    i = 0
    for cit in res:
        for ci in cit:
            i += 1
            if i == len(res):
                print(ci)
            else:
                print(ci, end=", ")
    """
    cur.close()
    db.close()
