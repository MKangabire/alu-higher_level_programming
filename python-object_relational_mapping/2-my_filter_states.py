#!/usr/bin/python3
"""
a script that takes in an argument and displays all values in the states tabl
"""

import MySQLdb
import sys

def search_states(username, password, db_name, state_name):
    """
    search states
    """
    try:
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=mysql_username,
            passwd=mysql_password,
            db=db_name
        )
        cursor = db.cursor()

        query = ("SELECT * FROM states "
                 "WHERE name = '{}' "
                 "ORDER BY states.id").format(state_name)
        cursor.execute(query)

        if not rows:
            print("No matching states found.")
        else:
            for row in rows:
                print(row[0], "'{}'".format(row[1]))

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

        mysql_username = sys.argv[1]
        mysql_password = sys.argv[2]
        db_name = sys.argv[3]
        state_name = sys.argv[4]

        search_states(mysql_username, mysql_password, db_name, state_name)
