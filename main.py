from entities import Portfolio, Investor, Broker
import MySQLdb
import MySQLdb.cursors
import settings
import random

# Make a connection to database
db = MySQLdb.connect(host=settings.HOST,
                     user=settings.USER,
                     passwd=settings.PASSWD,
                     db=settings.DB,
                     cursorclass=MySQLdb.cursors.DictCursor)
cur = db.cursor()

# Create an empty list of all investors
all_investors = list()

# Create a list of all stocks
all_stocks = list()
query_symbols = "SELECT DISTINCT TRADING_SYMBOL FROM STOCK_HISTORY"
cur.execute(query_symbols)
stocks = cur.fetchall()

for row in stocks:
    stock_symbol = row["TRADING_SYMBOL"]
    #query_volume = "SELECT VOLUME FROM STOCK_HISTORY WHERE TRADING_SYMBOL='%s' AND TRADE_DATE='2005-02-08'" % stock_symbol
    #cur.execute(query_volume)
    #result_volume = cur.fetchone()
    #volume = int(result_volume["VOLUME"])
    all_stocks.append((stock_symbol)) #, volume))

# print all_stocks

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

#for number in range(0,4):
    #random_stock = random.choice(all_stocks)
    #print "random_stock is %s" % random_stock
    # query_price_vol = 'SELECT OPEN_PRICE, VOLUME FROM STOCK_HISTORY WHERE TRADING_SYMBOL="%s" AND TRADE_DATE = "2005-02-08"' % random_stock
    #cur.execute(query_price_vol)
    #result_price_vol = cur.fetchone()
    #print "price is $%s" % result_price_vol["OPEN_PRICE"]
    #print "qty is %s" % result_price_vol["VOLUME"]
s = random.sample(all_stocks, 4)
print "Stocks to add are %s" % (s)
# placeholder= '?' # For SQLite. See DBAPI paramstyle.
# placeholders= ', '.join(placeholder for unused in s)
query= 'SELECT SUM(OPEN_PRICE) FROM STOCK_HISTORY WHERE TRADING_SYMBOL IN ("%s","%s","%s","%s") AND TRADE_DATE="2005-02-08"' % (s[0], s[1], s[2], s[3])
cur.execute(query)
result = cur.fetchone()
sum_price = int(result["SUM(OPEN_PRICE)"])
qty = round(broker.stock_money / sum_price)
print "Volume to add for each stock is %s" % qty



db.close()
