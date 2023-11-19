#!/usr/bin/python3

import MySQLdb
from sys import argv

# connecting to DB
db = MySQLdb.connect(
    host="localhost",
    user=argv[1],
    passwd=argv[2],
    db=argv[3],
    port=3306
    )

# create curson object
cur = db.cursor()
cur.execute("SELECT cities.id, cities.name, \
    states.name FROM cities JOIN \
        states ON states.id = cities.state_id \
            ORDER BY cities.id ASC")
res = cur.fetchall()
for cit in res:
    print(cit)
cur.close()
db.close()
