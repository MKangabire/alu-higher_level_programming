#!/usr/bin/python3
"""
a script that takes in arguments and displays all values in the states table
"""

import MySQLdb
import sys


def search_states(username, password, db_name, state_name):
    try:
        
        db = MySQLdb.connect(
                host='localhost',
                port=3306,
                user=username,
                passwd=password,
                db=db_name)

        cursor = db.cursor()

        query = "SELECT * FROM states WHERE name = %s ORDER BY id"
        cursor.execute(query, (state_name,))

        results = cursor.fetchall()

        for row in results:
            print(row)

        cursor.close()
        db.close()
        
    except MySQLdb.Error as e:
        print("Error:", e)
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python script.py <mysql_username> <mysql_password>"
              "<db_name> <state_name>")
        sys.exit(1)


