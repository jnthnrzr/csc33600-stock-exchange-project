#!/usr/bin/env python
"""entities.py

Defines the Portfolio, Investor, and Broker classes
"""
import logging


logging.basicConfig(level=logging.DEBUG,
                    format=' %(asctime)s - %(levelname)s - %(message)s')
# List of all Investors for broker to access
INVESTORS = list()

class Portfolio:
    """Portfolio class for stocks

    Fields: portfolios, value
    Methods: add_stock(symbol, quantity), remove_stock(symbol)
    """

    def __init__(self):
        """Make a portfolio to keep track of stocks"""
        self.portfolios = list()
        self.value = 0.00

    def add_stock(self, symbol, quantity):
        """Add stock of given symbol and quantity to the portfolio"""
        stock_price_unit = 10   # TODO write SQL statement
        stock_price_total = 1000   # TODO write SQL statement
        # TODO deduct stock quantity from market
        self.portfolios.append((symbol, quantity, stock_price_unit))
        self.value += stock_price_total

    def remove_stock(self, symbol):
        """Remove stocks of given symbol and quantity from the portfolio"""
        for p_symbol, p_quantity, p_unit_price in self.portfolios:
            if p_symbol == symbol:
                print "Found %s" % p_symbol, p_quantity, p_unit_price
                # TODO delete total value of stock from portfolio
                p_total_price = p_quantity * p_unit_price
                self.value -= p_total_price
                self.portfolios.remove((p_symbol,
                                        p_quantity,
                                        p_unit_price))

    def __repr__(self):
        """Show details about the portfolio"""
        return str(self.portfolios) + ", valued at " + str(self.value)


class Investor:
    """Investor class for anyone wishing to invest with some cash

    Fields: name, cash, risk_money, credit_line, portfolios
    Methods: add_portfolio(portfolio)
    """

    def __init__(self, name, cash):
        """Make an Investor object for stock exchange"""
        self.name = name
        self.cash = cash
        self.risk_money = 0.5 * cash
        self.credit_line = 100000
        self.portfolios = []
        # Add to global list of INVESTORS
        INVESTORS.append(self)

    def add_portfolio(self, portfolio):
        """Add portfolio to investor's financial records"""
        self.portfolios.append(portfolio)

    def __repr__(self):
        """Show details about the Investor"""
        name = "Investor: %s" % self.name
        cash = "Cash: %s" % self.cash
        risk_money = "Risk Money: %s" % self.risk_money
        portfolio = "Portfolio: %s" % self.portfolio
        info = name + cash + risk_money + portfolio
        return info

    def __str__(self):
        """Show string representation of the Investor"""
        return "<Investor: %s | Portfolio: %s >" % (self.name, self.portfolios)


class Broker:
    """Broker class for faciliator of finances"""

    def __init__(self, name, cash=1000000):
        """Make a Broker object

        Fields: name, cash, term, stock_money, margin_money, fee, portfolio,
        maintenance_threshold
        Methods:
        """
        self.name = name
        self.cash = cash
        self.term = 7
        self.stock_money = 0.40 * cash
        self.margin_money = 0.40 * cash
        self.fee = 30
        self.portfolios = list()
        self.maintenance_threshold = 0.25


    def add_portfolio(self, portfolio):
        """Add portfolio to broker's financial records"""
        self.portfolios.append(portfolio)

    def __repr__(self):
        """Show details about the broker"""
        name = "Broker: %s" % self.name
        cash = "Cash: %s" % self.cash
        portfolio = "Portfolio: %s" % self.portfolio
        return name + cash + portfolio

    def __str__(self):
        """Show string representation of the Broker"""
        return "<Broker: %s | Portfolio: %s >" % (self.name, self.portfolios)

if __name__ == "__main__":
    print "Creating portfolio1... "
    p1 = Portfolio()
    p1.add_stock("BMD", 50)
    p1.add_stock("AZA", 10)
    p1.add_stock("ATI", 50)
    p1.add_stock("AYZ", 40)

    print "Creating broker1"
    broker1 = Broker("GordonGekko")

    print "Creating investor1"
    investor1 = Investor("JohnDoe", 200000)

    print "Adding portfolio1 to broker1... "
    broker1.add_portfolio(p1)

    print "Adding portfolio1 to investor1... "
    investor1.add_portfolio(p1)

    print "Displaying broker1 info: "
    print broker1

    print "Displaying investor1 info: "
    print investor1

    print "Removing stock BMD from portfolio..."
    p1.remove_stock("BMD")

    print "broker1 info after removing stock "
    print broker1

    print "investor1 info after removing stock"
    print investor1
