"""entities.py
Defines the Investor and Broker classes"""


# List of all Investors for broker to access
INVESTORS = list()

#class Portfolio(symbol, date):
#    """Portfolio class for stocks"""
#    symbol = symbol
#    date = date
    

class Investor:
    """Investor class for anyone wishing to invest with initial cash injection"""
    
    def __init__(self, name, cash):
        """Makes an Investor object with name, cash"""
        self.name = name
        self.cash = cash
        self.risk_money = 0.5 * cash
        self.credit_line = 100000
        self.portfolios = []
        INVESTORS.append(self)

    def add_stock(self, symbol, quantity):
        """Adds stock of given symbol and quantity to the portfolio"""
        stock_price_unit = "10"   # TODO write SQL statement
        stock_price_total = "1000"   # TODO write SQL statement
        # TODO deduct stock quantity from market
        self.portfolios.append((symbol, quantity, stock_price_unit))

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
        return "<Investor: %s>" % self.name


class Broker:
    """Broker class for faciliator of finances"""
    
    def __init__(self, cash=1000000):
        """Makes a Broker object with set cash"""
        self.cash = cash
        # self.investors = []



if __name__ == "__main__":
    investor1 = Investor("JohnDoe", 100575)
    investor1.add_stock("AAA", 50)
    investor1.add_stock("BHV", 1000)
    investor1.add_stock("BEX", 200)
    investor1.add_stock("AJW", 5000)
    investor1.add_stock("ZZZ", 30)
    investor2 = Investor("JaneDoe", 200175)
    investor2.add_stock("UNI", 250)
    investor2.add_stock("EZY", 100)
    print "Added %s" % investor1
    print "Added %s" % investor2
    print "PRINTING LIST OF INVESTORS:"
    print INVESTORS

