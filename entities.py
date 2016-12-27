"""entities.py
Defines the Investor and Broker classes"""


class Portfolio(symbol, date):
    """Portfolio class for stocks"""
    symbol = symbol
    date = date

    

class Investor(name, cash):
    """Investor class for anyone wishing to invest with initial cash injection"""
    cash = cash
    risk_money = 0.5 * cash
    portfolios = []

    def add_stock(symbol, quantity):
        """Adds stock of given symbol and quantity to the portfolio"""
        stock_price_total = "1000"   # TODO write SQL statement
        # TODO deduct stock quantity from market
        portfolios.append(tuple(symbol, quantity, stock_price_total))

class Broker(name, portfolio):
    """Broker class for faciliator of finances"""
