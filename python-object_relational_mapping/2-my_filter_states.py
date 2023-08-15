import MySQLdb
import sys

if __name__ == "__main__":
    # Get the command line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]

    # Connect to the MySQL server
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
    cursor.execute(query, (name_argument,))

    if not rows:
        print("No matching states found.")
    else:
        for row in rows:
            print(row)

    cursor.close()
    db.close()
