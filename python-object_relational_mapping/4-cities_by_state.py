#!/usr/bin/python3
"""
 a script that lists all cities from the database hbtn_0e_4_usa
"""

import MySQLdb
import sys


def cities_name(username, password, db_name):
    try:
        db = MySQLdb.connect(
                host='localhost',
                port=3306,
                user=username,
                password=password,
                db=db_name
                )

        cursor = db.cursor()

        query = "SELECT * FROM cities ORDER BY cities.id"

        cursor.execute(query)

        results = cursor.fetchall()

        for row in results:
            print(row)

        db.close()
        cursor.close()

    except MySQLdb.Error as e:
        print("Error:", e)
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python script.py <mysql_username> <mysql_password> <db_name> <state_name>")
        sys.exit(1)
    
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]

    search_states(mysql_username, mysql_password, db_name, state_name)
