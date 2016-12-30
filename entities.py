#!/usr/bin/env python
"""entities.py

Defines the Portfolio, Investor, and Broker classes
"""
import logging


logging.basicConfig(level=logging.DEBUG,
                    # filename='entities.log',
                    # mode='w',
                    format=' %(asctime)s - %(levelname)s - %(message)s')
# logging.disable(logging.CRITICAL)

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
        self.value = 0

    def add_stock(self, symbol, quantity, unit_price):
        """Add stock of given symbol and quantity to the portfolio"""
        # TODO write SQL statement to grab unit_price
        stock_price_total = quantity * unit_price  # TODO write SQL statement
        # TODO deduct stock quantity from market ??
        self.portfolios.append((symbol, quantity, unit_price))
        self.value += stock_price_total

    def remove_stock(self, symbol, quantity):
        """Remove stocks of given symbol and quantity from the portfolio"""
        for p_symbol, p_quantity, p_unit_price in self.portfolios:
            if p_symbol == symbol:
                logging.debug("Found %s, %s, %s" %
                              (p_symbol, p_quantity, p_unit_price))
                # First delete completely
                self.portfolios.remove((p_symbol,
                                        p_quantity,
                                        p_unit_price))
                # Check if some quantity of stocks should remain
                if quantity < p_quantity:
                    # Keep remainder
                    self.portfolios.append((p_symbol,
                                            p_quantity-quantity,
                                            p_unit_price))
                # Reduce value of portfolio by value of stocks removed
                total_price = quantity * p_unit_price
                self.value -= total_price

    def __repr__(self):
        """Show details about the portfolio"""
        return "<Portfolio: %s | valued at %s>" % (self.portfolios, self.value)


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
        return "<Investor: %s | Portfolio: %s>" % (self.name, self.portfolios)


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
        return "<Broker: %s | Portfolio: %s>" % (self.name, self.portfolios)


if __name__ == "__main__":
    logging.info("Creating portfolio1... ")
    p1 = Portfolio()
    p1.add_stock("BMD", 50, 15)
    p1.add_stock("AZA", 10, 15)
    p1.add_stock("ATI", 50, 15)
    p1.add_stock("AYZ", 40, 15)

    logging.info("Creating broker1")
    broker1 = Broker("GordonGekko")

    logging.info("Creating investor1")
    investor1 = Investor("JohnDoe", 200000)

    logging.info("Adding portfolio1 to broker1")
    broker1.add_portfolio(p1)

    logging.info("Adding portfolio1 to investor1")
    investor1.add_portfolio(p1)

    logging.info("Displaying broker1 info AFTER ADDING portfolio")
    logging.info(broker1)

    logging.info("Displaying investor1 info AFTER ADDING portfolio")
    logging.info(investor1)

    logging.info("Removing stock 'BMD' from portfolio")
    p1.remove_stock("BMD")

    logging.info("Displaying broker1 info AFTER REMOVING stock")
    logging.info(broker1)

    logging.info("Displaying investor1 info AFTER REMOVING stock")
    logging.info(investor1)
