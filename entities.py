"""entities.py
Defines the Investor and Broker classes"""


class Investor(name, cash):
    """Investor class for anyone wishing to invest with initial cash injection"""
    cash = cash
    risk_money = 0.5 * cash
    portfolio = []

    def add_stock(symbol, quantity):
        """Adds stock of given symbol and quantity to the portfolio"""
        stock_price_total = "SQL"   # TODO write sql statement
        

class Broker(name, portfolio):
    """Broker class for faciliator of finances"""
