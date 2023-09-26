#!/usr/bin/python3
''' lists all states with a name matching with specific name
 from the database hbtn_0e_0_usa
'''
import MySQLdb
import sys

<<<<<<< HEAD
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
                 "WHERE name = %s "
                 "ORDER BY states.id")
        cursor.execute(query, (state_name,))

        if not rows:
            print("No matching states found.")
        else:
            for row in rows:
                print("({}, '{}')".format(row[0], row[1]))

        cursor.close()
        db.close()

    except MySQLdb.Error as e:
        print("Error:", e)
        sys.exit(1)

=======
>>>>>>> 9bca717da99d5c666cf05a40fab020738d7bae44
if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, db=sys.argv[3],
                         user=sys.argv[1], passwd=sys.argv[2])
    c = db.cursor()
    c.execute(
        '''SELECT * FROM states WHERE states.name = '{:s}' ORDER\
        BY states.id ASC'''.format(sys.argv[4])
    )
    for row in c.fetchall():
        if row[1] == sys.argv[4]:
            print(row)
    c.close()
    db.close()
