import mysql.connector
import sys

if __name__ == "__main__":
    try:
        db = mysql.connector.connect(
            host="localhost",
            user=sys.argv[1],
            passwd=sys.argv[2],
            database=sys.argv[3],
            port=3306
        )
        cur = db.cursor()
        cur.execute("""SELECT cities.id, cities.name, states.name FROM
                    cities INNER JOIN states ON states.id=cities.state_id""")
        rows = cur.fetchall()
        for row in rows:
            print(row)
        cur.close()
        db.close()
    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))

