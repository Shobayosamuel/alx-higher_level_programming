#!/usr/bin/python3
import MySQLdb
import sys
if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], port=3306, host="localhost",
                         passwd=sys.argv[2], db=sys.argv[3])
    conn = db.cursor()
    conn.execute("SELECT * FROM `states` WHERE `name` like '{:s}'\
    ORDER BY `id` ASC".format(sys.argv[4]))
    [print(state) for state in conn.fetchall() if state[1] == sys.argv[4]]
    conn.close()
    db.close()
