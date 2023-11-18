#!/usr/bin/python3
"""script that lists all states from the database hbtn_0e_0_usa:"""
import MySQLdb
from sys import argv

if __name__=="__main__":
    db = argv[3]
    db = MySQLdb.connect(host="localhost", user=argv[1], passwd=argv[2], db=db, port=3306)
    cur = db.cursor()

    cur.execute("SELECT * FROM states")
    result = cur.fetchall()
    for row in result:
        print(row)
    cur.close()
    db.close()