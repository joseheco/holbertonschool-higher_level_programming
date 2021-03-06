#!/usr/bin/python3
""" script that takes in an argument and displays all values in
the state table of hbtn_0e_0_usa"""
import MySQLdb
import sys

if __name__ == '__main__':
    # Database connect
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE BINARY name = '{}'".format(
        sys.argv[4]))
    list_states = cur.fetchall()
    for state in list_states:
        print("{}".format(state))
    db.close()
