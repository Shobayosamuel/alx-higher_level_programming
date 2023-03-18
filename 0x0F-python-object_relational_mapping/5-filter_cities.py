#!/usr/bin/python3
"""
    Write a script that takes in the name of a
    state as an argument and lists all cities
    of that state, using the database hbtn_0e_4_usa
"""

import MySQLdb
import sys

if __name__ == "__main__":
    mysql_user = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(host="localhost", user=mysql_user,
                         passwd=mysql_password, db=db_name)

    query = """
    SELECT cities.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    WHERE states.name LIKE BINARY %(state_name)s
    ORDER BY cities.id ASC;
    """
    cursor.execute(query, {'state_name': sys.argv[4]})

    rows = cursor.fetchall()
    if rows is not None:
        print(", ".join([row[0] for row in rows]))
    cursor.close()
    db.close()
