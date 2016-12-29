from entities import Portfolio, Investor, Broker
import MySQLdb
import MySQLdb.cursors
import settings
import random

all_investors = list()
all_stock = list()

db = MySQLdb.connect(host=settings.HOST,
                     user=settings.USER,
                     passwd=settings.PASSWD,
                     db=settings.DB,
                     cursorclass=MySQLdb.cursors.DictCursor)
cur = db.cursor()

# Create short investors
short1 = Investor("Shorty", 250000)
short2 = Investor("Morty", 250000)

# Create margin investors
margin1 = Investor("Corky", 250000)
margin2 = Investor("Dorky", 250000)

# Add all investors to the list
all_investors.extend((short1, short2, margin1, margin2))

# Create a broker
broker = Broker("Gordon Gekko", 1000000)

query = "SELECT DISTINCT TRADING_SYMBOL FROM STOCK_HISTORY"
cur.execute(query)
stocks = cur.fetchall()

for row in stocks:
    # print row["TRADING_SYMBOL"]
    all_stock.append(row["TRADING_SYMBOL"])

print all_stock
# print all_investors
