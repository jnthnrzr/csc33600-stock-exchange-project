from entities import Portfolio, Investor, Broker
from margin import give_stocks_margin
from decimal import Decimal
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
    all_stocks.append((stock_symbol)) #, volume))

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
broker_portfolio = Portfolio()

# Select 4 stocks at random
stocks = random.sample(all_stocks, 4)
# print "Stocks to add are %s" % (stocks)
query= 'SELECT SUM(OPEN_PRICE) FROM STOCK_HISTORY WHERE TRADING_SYMBOL IN ("%s","%s","%s","%s") AND TRADE_DATE="2005-02-08"' % (stocks[0], stocks[1], stocks[2], stocks[3])
cur.execute(query)
result = cur.fetchone()
sum_price = int(result["SUM(OPEN_PRICE)"])
qty = int(round(broker.stock_money / sum_price, 0))
# print "Volume to add for each stock is %s" % qty

# Find stock info and add to portfolio
for stock in stocks:
    # print "stock to add is %s" % stock
    query_price = 'SELECT OPEN_PRICE FROM STOCK_HISTORY WHERE TRADING_SYMBOL="%s" AND TRADE_DATE="2005-02-08"' % stock
    cur.execute(query_price)
    result_price = cur.fetchone()
    price = result_price["OPEN_PRICE"]
    # print "Price of stock is $%s" % price
    broker_portfolio.add_stock(stock, qty, price)


print "Broker's portfolio is %s" % broker_portfolio

# Adding broker_portfolio to broker
broker.add_portfolio(broker_portfolio)

print "PRINTING broker: %s" % broker


# Start a counter
for count in range(0, 21+1):
    if count % broker.term == 0:
        print "Count mod term is 0."
    else:
        print "Count = %s" % count

# rndm = random.choice(broker.portfolios[0].portfolios)
# print type(broker.portfolios)
# print "Randomly chose %s from broker_portfolio" % str(rndm)


give_stocks_margin(short1, broker)



db.close()
