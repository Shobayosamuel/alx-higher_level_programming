#!/usr/bin/python3
"""
    Write a script that lists all states with a name starting with N
    (upper N) from the database hbtn_0e_0_usa:
"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    conn = db.cursor()
    conn.execute("SELECT * FROM `states` ORDER BY `id`")
    [print(state) for state in conn.fetchall() if state[1][0] == "N"]
