import MySQLdb
import MySQLdb.cursors
import config

db = MySQLdb.connect(host=HOST,
                     user=USER,
                     passwd=PASSWD,
                     db=DB,
                     cursorclass=MySQLdb.cursors.DictCursor)

cur = db.cursor()
cur.execute("SELECT VERSION()")

rows = cur.fetchall()

for row in rows:
    print row["VERSION()"]
