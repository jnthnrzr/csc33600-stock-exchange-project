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
# logging.disable(logging.CRITICAL)

def buy_on_margin(investor, broker):
    """Buying on margin 6(b)"""
    logging.info("BUYING on Margin...")
    loan = min(investor.credit_line, 0.5 * investor.risk_money)
    # logging.info("Cash $%s, Loan $%s, Risk_money $%s" % (investor.cash, loan, investor.risk_money))
    old_portfolio = investor.portfolios[0]
    new_portfolio = investor.portfolios[1]

    logging.info("OLD %s vs NEW %s" % (old_portfolio.value, new_portfolio.value))

    if new_portfolio.value > old_portfolio.value:
        logging.info("Sell stock and repay the broker.")
        investor.cash += float(new_portfolio.value)
        sym = old_portfolio.portfolios[0][0]
        qty = old_portfolio.portfolios[0][1]
        broker.get_stock(investor)
        investor.portfolios[0].remove_stock(sym, qty)
        del investor.portfolios[0]
        logging.info("CALL the get_stock function here.")
    else:
        # Price has gone down
        qty = old_portfolio.portfolios[0][1]
        # Calculate the Equity
        equity = float(new_portfolio.value) - investor.get_loan_amount()
        maintenance_margin = equity / float(new_portfolio.value)
        logging.info("ELSE statement caught")
        # 
        if maintenance_margin > broker.maintenance_threshold:
            # Calculate the percent decrease in price of stock
            percent_decrease = float(abs(new_portfolio.portfolios[0][2] - old_portfolio.portfolios[0][2]) / old_portfolio.portfolios[0][2])
            some_number = investor.investment_seed - ( qty * float(old_portfolio.value) * percent_decrease)
            margin_call = abs(( (0.25 - maintenance_margin)/(maintenance_margin) ) * equity)
            logging.info("margin call is $%s" % margin_call)
            if some_number == 0:
                logging.info("The investor MUST sell in order to repay the broker.")
                logging.info("SELL THE STOCKS TO THE MARKET")
                logging.info("add cash by the newprice * qty")
                investor.cash += float(new_portfolio.value)
                sym = old_portfolio.portfolios[0][0]
                qty = old_portfolio.portfolios[0][1]
                investor.portfolios[0].remove_stock(sym, qty)
                #del investor.portfolios[0]

            elif some_number - margin_call > 0:
                logging.info("Pay the margin call")
                logging.info("Decrease investor.cash and increase broker.cash by margin_call amount.")
                investor.cash -= margin_call
                broker.cash += margin_call

            else:
                # some_number is LESS THAN zero
                logging.info("Margin call cannot be afforded and the stock should be sold at a loss.")
                logging.info("Don't buy anymore stocks.")
                investor.cash += float(new_portfolio.value)
                sym = old_portfolio.portfolios[0][0]
                qty = old_portfolio.portfolios[0][1]
                investor.portfolios[0].remove_stock(sym, qty)
                #del investor.portfolios[0]

        else:
            logging.info("Maintenance margin is LESS THAN maintenance_threshold")

    logging.info("Margin done")
    logging.info(investor)
    logging.info("Cash $%s, Loan $%s, Risk_money $%s" % (investor.cash, loan, investor.risk_money))
    logging.info(broker)

