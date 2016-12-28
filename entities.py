"""entities.py
Defines the Investor and Broker classes"""


# List of all Investors for broker to access
INVESTORS = list()

class Portfolio:
    """Portfolio class for stocks"""

    def __init__(self):
        """Make a portfolio to keep track of stocks"""
        self.portfolios = list()
        self.value = 0.00

    def __repr__(self):
        """Shows details about the portfolio"""
        return str(self.portfolios) + ", valued at " + str(self.value)


    def add_stock(self, symbol, quantity):
        """Adds stock of given symbol and quantity to the portfolio"""
        stock_price_unit = 10   # TODO write SQL statement
        stock_price_total = 1000   # TODO write SQL statement
        # TODO deduct stock quantity from market
        self.portfolios.append((symbol, quantity, stock_price_unit))
        self.value += stock_price_total

    def remove_stock(self, symbol):
        """Removes stocks of given symbol and quantity from the portfolio"""
        for p_symbol, p_quantity, p_unit_price in self.portfolios:
            if p_symbol == symbol:
                print "Found %s" % p_symbol, p_quantity, p_unit_price
                # TODO delete total value of stock from portfolio
                p_total_price = p_quantity * p_unit_price
                self.value -= p_total_price
                self.portfolios.remove((p_symbol,
                                        p_quantity,
                                        p_unit_price))


class Investor:
    """Investor class for anyone wishing to invest with initial cash injection"""
    
    def __init__(self, name, cash):
        """Makes an Investor object for stock exchange
        Fields: name, cash, risk_money, credit_line, portfolios
        Methods: add_portfolio(portfolio)
        """
        self.name = name
        self.cash = cash
        self.risk_money = 0.5 * cash
        self.credit_line = 100000
        self.portfolios = []
        # Add to global list of INVESTORS
        INVESTORS.append(self)

    def __repr__(self):
        """Shows details about the Investor"""
        info = "\n%s Cash : $%.2f RiskMoney : $%.2f\n" % (self.name,
                                                          self.cash,
                                                          self.risk_money)
        info += "PRINTING Portfolios: ..."
        for symbol, quantity, unit_price in self.portfolios:
            info += "\n%s units of %s @ $%s each" % (quantity, symbol, unit_price)
        return info

    def __str__(self):
        """String representation"""
        return "<Investor: %s | Portfolio: %s >" % (self.name, self.portfolios)

    def add_portfolio(self, portfolio):
        """Adds portfolio to investor's financial records"""
        self.portfolios.append(portfolio)


class Broker:
    """Broker class for faciliator of finances"""
    
    def __init__(self, cash=1000000):
        """Makes a Broker object with set cash"""
        self.cash = cash
        # self.investors = []



if __name__ == "__main__":
    print "Creating investor1"
    investor1 = Investor("JohnDoe", 200000)

    print "Creating portfolio1... "
    p1 = Portfolio()
    p1.add_stock("BMD", 50)
    p1.add_stock("AZA", 10)
    p1.add_stock("ATI", 50)
    p1.add_stock("AYZ", 40)
    
    print "Adding portfolio1 to investor1... "
    investor1.add_portfolio(p1)

    print "Displaying investor1 info: "
    print investor1
    
    print "Removing stock BMD from portfolio..."
    p1.remove_stock("BMD")

    print "investor1 info after removing stock"
    print investor1
    # print "PRINTING LIST OF INVESTORS:"
    # print INVESTORS

