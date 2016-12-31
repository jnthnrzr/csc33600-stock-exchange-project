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


def short_seller(investor, broker):

    old_portfolio = investor.portfolios[0]
    new_portfolio = investor.portfolios[1]
    # logging.info("new_portfolio: %s" % new_portfolio)
    # logging.info(new_portfolio.portfolios[0][2])
    stock_price = Decimal(str(old_portfolio.portfolios[0][2]))
    cur_stk_price = Decimal(str(new_portfolio.portfolios[0][2]))
    stock_quant = old_portfolio.portfolios[0][1]
    stock_symbol = old_portfolio.portfolios[0][0]

    # logging.info(old_portfolio.value)
    # looking for decres in stock price 
        
    # If true we buy back the stock at a lose
    max_loss = (0.5*((investor.cash)+float(old_portfolio.value)) - (investor.risk_money))
    logging.info("short seller: %s" % investor)


    if stock_price == cur_stk_price:
        logging.info("stock_price %s is equal to cur_stk_price %s" % (stock_price, cur_stk_price))
        return "stock_price is equal to cur_stk_price"

    elif (stock_price-cur_stk_price > 0):
        investor.portfolios[0].remove_stock(stock_symbol, stock_quant)
        investor.cash += float(old_portfolio.value)
        # buy new portfolio
        investor.portfolios[0].add_stock(stock_symbol, stock_quant, cur_stk_price)
        investor.cash -= float(new_portfolio.value)
        #investor.portfolios[0].remove_stock(stock_symbol)
        #investor.cash = investor.cash + stock_total_value
        #investor.portfolios[0].add_stock(stock_symbol,stock_quant,cur_stk_price)
        #investor.cash = investor.cash - (cur_stk_price*stock_quant)
        logging.info("stock bought back at a profit %s ... %s " % (stock_price, cur_stk_price))
    elif ((stock_quant * cur_stk_price) >= max_loss):
        # sale old portfolio, get cash
        investor.portfolios[0].remove_stock(stock_symbol, stock_quant)
        investor.cash += float(old_portfolio.value)
        # buy new portfolio
        investor.portfolios[0].add_stock(stock_symbol, stock_quant, cur_stk_price)
        investor.cash -= float(new_portfolio.value)
        logging.info("bought back at a lose %s .. %s" % (stock_price, cur_stk_price))

    else:
        logging.info("short selling didn't buy back stocks")
       
    
    #print "\n","trade.py",stock_symbol,invest_portf.portfolios, stock_total_value
    #print "\n","current price of ",stock_symbol,cur_stk_price
    

