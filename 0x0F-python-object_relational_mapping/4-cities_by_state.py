#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    conn = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                           db=sys.argv[3])
    cursor = conn.cursor()
    cursor.execute("SELECT cities.id, cities.name, states.name\
                    FROM cities INNER JOIN states\
                    ON cities.state_id = states.id\
                    ORDER BY cities.id ASC")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    conn.close()
