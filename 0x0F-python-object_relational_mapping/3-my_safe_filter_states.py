#!/usr/bin/python3
"""script that lists all states from the database hbtn_0e_0_usa:"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    # Connecting to db
    db = MySQLdb.connect(
        host="localhost",
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
        port=3306
        )
    # Create Cursur object
    cur = db.cursor()

    # Mitigating SQL injection with parameterized statements
    query = "SELECT * FROM states WHERE name = %s ORDER BY id"

    # take note: input must be tuple
    user_input = (argv[4], )
    cur.execute(query, user_input)
    result = cur.fetchall()
    for row in result:
        print(row)
    cur.close()
    db.close()
