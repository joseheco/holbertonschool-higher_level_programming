#!/usr/bin/python3
""" a script that takes in arguments and displays all values
in the states table of hbtn_0e_0_usa."""
import MySQLdb
import sys

if __name__ == '__main__':
    # Database connection
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name = %s", (sys.argv[4],))
    list_states = cur.fetchall()
    for state in list_states:
        print("{}".format(state))
    db.close()
