"""margin.py

Functions for margin investors
"""
# from decimal import Decimal
import random
from entities import Portfolio


def give_stocks_margin(investor, broker):
        # stock_value_cap = min(investor.credit_line,investor.risk_money
        #print broker.cash,investor.cash
        # detrmine loan amount for investor
        # give investor loan money & update brokers cash
        loan = min(investor.credit_line, (0.5 * investor.risk_money))
        investor.cash = investor.cash + loan
        broker.cash = broker.cash - loan

        r_stk_name, r_stk_quant, r_stk_price = random.choice(broker.portfolios[0].portfolios)
        # r_stk_name = rand_stock[0]
        # r_stk_quant = rand_stock[1]
        # r_stk_price = rand_stock[2]

        #  print broker.cash,investor.cash , " pre buy "
        # print rand_stock, " pre buy "
        print r_stk_name, r_stk_quant, r_stk_price, " pre buy "

        qty_tobuy = int( (investor.cash / float(r_stk_price)) )
        print qty_tobuy,"quantity to buy of ", r_stk_name

        print "buying"

        if (qty_tobuy >= r_stk_quant):
                first_purchase = r_stk_quant * float(r_stk_price)
                investor.cash = investor.cash - first_purchase
                print "buying all of", r_stk_name
        else:
            investor.cash = investor.cash - (qty_tobuy * r_stk_price)

        print "AFTER BUY"

        # print r_stk_name, r_stk_quant,r_stk_price
        # print loan
        # print broker.cash,investor.cash
        p = Portfolio()
        p.add_stock(r_stk_name, r_stk_quant, r_stk_price)
        investor.add_portfolio(p)
        print "stock %s, %s, %s has been added" % (r_stk_name, r_stk_quant, r_stk_price)
        print "PRINTING investor: %s" % investor
