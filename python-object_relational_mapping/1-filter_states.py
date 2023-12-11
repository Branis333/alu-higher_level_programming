#!/usr/bin/python3
<<<<<<< HEAD
"""
    Create a that lists all states with a name starting with N
"""


import sys
import MySQLdb

if __name__ == "__main__":
    conn = MySQLdb.connect(
       user=sys.argv[1],
       password=sys.argv[2],
       db=sys.argv[3],
       host="localhost",
       port=3306
    )

    cur = conn.cursor()

    cur.execute("SELECT * FROM states \
        WHERE name LIKE BINARY 'N%' \
        ORDER BY id ASC")

    states = cur.fetchall()

    for state in states:
        print(state)

    cur.close()
    conn.close()
=======
""" lists all states with a name starting with N
(upper N) from the
database hbtn_0e_0_usa
"""

import MySQLdb
import sys


def select_states_with_names():
    """ lists all states with a name starting with N
    (upper N) from the
    database hbtn_0e_0_usa
    """
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3]
                         )
    cursor = db.cursor()

    cursor.execute("SELECT * FROM states "
                   "WHERE name LIKE BINARY 'N%' "
                   "ORDER BY id")

    records = cursor.fetchall()
    for data in records:
        print(data)

    cursor.close()
    db.close()


if __name__ == "__main__":
    select_states_with_names()
>>>>>>> 2bbca3d47bdf7221149f28bea47d7356b032b0a6
