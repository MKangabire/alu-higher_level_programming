#!/usr/bin/python3
"""
a script that takes in an argument and displays all values in the states tabl
"""

import MySQLdb
import sys

    def search_states(username, password, db_name, state_name):
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
                     "ORDER BY states.id").format(states_name)
            cursor.execute(query)

            if not rows:
                print("No matching states found.")
            else:
                for row in rows:
                    print(row)

            cursor.close()
            db.close()
