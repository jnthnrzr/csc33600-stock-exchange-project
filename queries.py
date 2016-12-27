import MySQLdb
import MySQLdb.cursors
import settings

db = MySQLdb.connect(host=settings.HOST,
                     user=settings.USER,
                     passwd=settings.PASSWD,
                     db=settings.DB,
                     cursorclass=MySQLdb.cursors.DictCursor)

cur = db.cursor()
cur.execute("SELECT VERSION()")

rows = cur.fetchall()

for row in rows:
    print row["VERSION()"]
