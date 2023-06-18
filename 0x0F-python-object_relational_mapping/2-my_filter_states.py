#!/usr/bin/python3
""" lists all states from the database """
import MySQLdb
import sys

if __name__ == "__main__":

    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3], name=sys.argv[4], port=3306)
    cur = db.cursor()
    name = input()
    cur.execute("""SELECT * FROM states WHERE name LIKE '{:s}'
                ORDER BY id ASC""".format(name))
    rows = cur.fetchall()
    for r in rows:
        print(r)
    cur.close()
    db.close()
