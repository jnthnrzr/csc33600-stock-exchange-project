from entities import Portfolio, Investor, Broker
from margin import buy_on_margin
from short import short_seller
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
# logging.disable(logging.INFO)

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
#short2 = Investor("Short2", 250000)

# Create margin investors
margin1 = Investor("Margin1", 250000)
#margin2 = Investor("Margin2", 250000)

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
for count in [0, 6, 7]:
    
    if count % broker.term == 6:
        logging.info("It is Saturday")
        logging.info("Margin1: ")
        logging.info(margin1)
        # margin seller has to sell everything
        broker.get_stock(margin1)
        #broker.get_stock(margin2)
        broker.get_stock(short1)
        #broker.get_stock(short2)
        # logging.info("Broker after Saturday:")
        # logging.info(broker)

        logging.warning("margin1 cash: $%s" % margin1.cash)

    elif count % broker.term == 0:
        logging.info("Sunday: It is time to meet the broker")
        # logging.info(broker)
        margin1.get_stock(broker)
        #margin2.get_stock(broker)
        short1.get_stock(broker)
        #short2.get_stock(broker)

        logging.info("Margin1: ")
        logging.info(margin1)
        logging.info("Short1: ")
        logging.info(short1)
        logging.warning("broker cash: $%s" % broker.cash)
    else:
        logging.info("Weekdays, Count = %s" % count)
        day = 1 + count
        if day in [5, 6, 12, 13, 19, 20, 26, 27, ]:
            logging.info("STock market closed. ZZZZZZZZZZZZZZ")
            continue

        logging.info("Margin1: ")
        logging.info(margin1)
        logging.info("Short1: ")
        logging.info(short1)
        # Short
        ## Find stock name
        # logging.info("What is this: %s" % short1.portfolios[0])
        short_stock = short1.portfolios[0].portfolios[0][0]
        ## Check the new price of the short stock
        new_price = check_price(short_stock, 2005, 3, day)
        # logging.info("check_price gives $%s" % new_price)
        # logging.info(broker.portfolios)
        p2 = Portfolio()
        p2.add_stock(short_stock, qty, new_price)
        short1.add_portfolio(p2)
        short_seller(short1, broker)


        # Margin
        margin1.get_stock(broker)
        p3 = Portfolio()

        # Find stock to buy on margin
        logging.warning("margin1 details: %s" % margin1.portfolios[0])
        margin_stock = margin1.portfolios[0].portfolios[0][0]
        # Check the new price of the margin stock
        margin_price = check_price(margin1.portfolios[0].portfolios[0][0], 2005, 3, day)
        p3.add_stock(margin_price, qty, margin_price)
        margin1.add_portfolio(p3)
        buy_on_margin(margin1, broker)

        
 
db.close()
