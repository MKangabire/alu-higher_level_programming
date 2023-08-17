import MySQLdb
import sys

def search_states(username, password, db_name, state_name):
    try:
        # Connect to the MySQL server
        db = MySQLdb.connect(host='localhost',
                port=3306,
                user=username,
                passwd=password,
                db=db_name)

        cursor = db.cursor()


