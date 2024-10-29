#!/usr/bin/python3

'''my SQLldb'''

import MySQLdb
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    matchname = sys.argv[4].split(";")[0].strip("'")

    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database,
        charset="utf8"
    )
    cur = conn.cursor()
    cur.execute(f"SELECT c.name \
        FROM cities AS c \
        JOIN states AS st \
            ON c.state_id = st.id \
        WHERE st.name = '{matchname}' \
        ORDER BY c.id")
    query_rows = cur.fetchall()

    index = 0
    for row in query_rows:
        if index > 0:
            print(", ", end="")
        print(row[0], end="")
        index += 1
    print()

    cur.close()
    conn.close()
