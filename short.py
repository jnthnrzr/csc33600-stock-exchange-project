"""short.py

Functions for short selling investors
"""
from decimal import Decimal
from entities import Portfolio
import logging
import random


# Set logging configuration
logging.basicConfig(level=logging.DEBUG,
                    format=' %(asctime)s - %(levelname)s - %(message)s')
# logging.disable(logging.CRITICAL)

def give_stocks_short(investor, broker):
    """Investor gets a random share from broker for short selling"""
    
    # Take a loan from broker to investor
    loan = min(investor.credit_line, investor.risk_money)
    investor.cash += loan
    broker.cash -= loan
    
    # Pay broker fees
    fee = broker.fee
    investor.cash -= fee
    broker.cash += fee

    # Pick a stock from broker at random and buy it
    sym, qty, price = random.choice(broker.portfolios[0].portfolios)

    logging.info("Picked stock %s, qty %s, price %s" % (sym, qty, price))
    qty_tobuy = int ( (investor.cash / Decimal(price)) )
    logging.info( "qty %s to buy of %s" % (qty_tobuy, sym) )

    logging.info("BUYING...")

    if (qty_tobuy >= qty):
        first_purchase = qty * Decimal(price)
        investor.cash -= first_purchase
        logging.info("Buying all of %s" % sym)
    else:
        investor.cash -= qty_tobuy * price

    logging.info("AFTER BUY")

    # Make portfolio p and add stock to it
    p = Portfolio()
    p.add_stock(sym, qty, price)
    investor.add_portfolio(p)
    logging.info("stock %s, %s, %s has been added" % (sym, qty, price))
    logging.info("Displaying investors: %s" % (investor))
    
