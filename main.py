from entities import Portfolio, Investor, Broker
from margin import give_stocks_margin
from short import give_stocks_short
from queries import check_price, get_all_stocks
from decimal import Decimal
import logging
import MySQLdb
import MySQLdb.cursors
import random
import settings


# Setup logging configurations
logging.basicConfig(level=logging.DEBUG,
                    format=' %(levelname)s - hello - %(asctime)s - %(module)s:%(lineno)d - %(message)s')
logging.disable(logging.DEBUG)

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
#all_stocks = list()
#query_symbols = "SELECT DISTINCT TRADING_SYMBOL FROM STOCK_HISTORY"
#cur.execute(query_symbols)
#stocks = cur.fetchall()

#for row in stocks:
    #stock_symbol = row["TRADING_SYMBOL"]
    #all_stocks.append((stock_symbol)) #, volume))
all_stocks = get_all_stocks()


# Create short investors
short1 = Investor("Short1", 250000)
short2 = Investor("Short2", 250000)

# Create margin investors
margin1 = Investor("Margin1", 250000)
margin2 = Investor("Margin2", 250000)

# Add all investors to the list
all_investors.extend((short1, short2, margin1, margin2))

# Create a broker
broker = Broker("Gordon Gekko", 1000000)
broker_portfolio = Portfolio()

# Select 4 stocks at random
stocks = random.sample(all_stocks, 4)
# logging.info("Stocks to add are %s" % (stocks)
query= 'SELECT SUM(OPEN_PRICE) FROM STOCK_HISTORY WHERE TRADING_SYMBOL IN ("%s","%s","%s","%s") AND TRADE_DATE="2005-3-1"' % (stocks[0], stocks[1], stocks[2], stocks[3])
cur.execute(query)
result = cur.fetchone()
sum_price = int(result["SUM(OPEN_PRICE)"])
qty = int(round(broker.stock_money / sum_price, 0))
# logging.info("Volume to add for each stock is %s" % qty

# Find stock info and add to portfolio
for stock in stocks:
    # logging.info("stock to add is %s" % stock
    #query_price = 'SELECT OPEN_PRICE FROM STOCK_HISTORY WHERE TRADING_SYMBOL="%s" AND TRADE_DATE="2005-3-1"' % stock
    #cur.execute(query_price)
    #result_price = cur.fetchone()
    #price = result_price["OPEN_PRICE"]
    price = check_price(symbol=stock, year=2005, month=3, day=1)
    # logging.info("Price of stock is $%s" % price
    broker_portfolio.add_stock(stock, qty, price)
logging.info("Broker's portfolio is %s" % broker_portfolio)

# Adding broker_portfolio to broker
broker.add_portfolio(broker_portfolio)

logging.info("PRINTING broker: %s" % broker)


# Start a counter
for count in range(0, 21+1):
    if count % broker.term == 0:
        logging.debug("Count mod term is 0.")
    else:
        logging.debug("Count = %s" % count)

logging.info(broker.portfolios)
give_stocks_short(short2, broker)

logging.info(broker.portfolios)
give_stocks_margin(margin1, broker)

logging.info(broker.portfolios)
give_stocks_margin(margin2, broker)

logging.info(broker.portfolios)
give_stocks_short(short1, broker)

logging.info(broker.portfolios)

db.close()
