"""margin.py

Functions for margin investors
"""
# from decimal import Decimal
import logging
import random
from entities import Portfolio


# Set logging configuration
logging.basicConfig(level=logging.DEBUG,
                    format=' %(asctime)s - %(levelname)s - %(message)s')
#logging.disable(logging.CRITICAL)

def give_stocks_margin(investor, broker):

    logging.info("RUNNING give_stocks_margin()...")
    # Determine loan amount for investor
    loan = min(investor.credit_line, (0.5 * investor.risk_money))
    # Give investor loan money & update broker's cash
    investor.cash = investor.cash + loan
    broker.cash = broker.cash - loan

    # Randomly select a stock from broker
    sym, qty, price = random.choice(broker.portfolios[0].portfolios)
    # logging.info("Selected the stock (%s, %s, $%s) randomly from broker's portfolio" % (sym, qty, price))

    # Buy correct quantity
    qty_tobuy = int( (investor.cash / float(price)) )
    logging.info("%s stocks buy of symbol = %s will be bought" % (qty, sym) )

    logging.info("BUYING")

    if (qty_tobuy >= qty):
        first_purchase = qty * float(price)
        investor.cash = investor.cash - first_purchase
        logging.info("Buying all of %s" % sym)
    else:
        investor.cash = investor.cash - (qty_tobuy * price)

    logging.info("AFTER BUY")

    p = Portfolio()
    p.add_stock(sym, qty, price)
    investor.add_portfolio(p)
    logging.info("stock %s, %s, %s has been added" % (sym, qty, price))
    logging.info("PRINTING investor: %s" % investor)

    # Remove stock from broker's portfolio
    logging.info("Broker portfolio BEFORE removal: %s" % (broker.portfolios[0].portfolios))
    # logging.info("type: %s" % type(broker.portfolios[0]))
    broker.portfolios[0].remove_stock(sym, qty)

    logging.info("Broker portfolio AFTER removal: %s" % (broker.portfolios[0].portfolios))
