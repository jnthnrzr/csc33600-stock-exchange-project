"""entities.py
Defines the Investor and Broker classes"""


#class Portfolio(symbol, date):
#    """Portfolio class for stocks"""
#    symbol = symbol
#    date = date
    

class Investor():
    """Investor class for anyone wishing to invest with initial cash injection"""
    def __init__(self, name, cash, portfolios=[]):
        self.name = name
        self.cash = cash
        self.risk_money = 0.5 * cash
        self.portfolios = []

    def add_stock(self, symbol, quantity):
        """Adds stock of given symbol and quantity to the portfolio"""
        stock_price_unit = "10"   # TODO write SQL statement
        stock_price_total = "1000"   # TODO write SQL statement
        # TODO deduct stock quantity from market
        self.portfolios.append((symbol, quantity, stock_price_unit))

    def details(self):
        """Prints out details about the Investor"""
        print "PRINTING Investor Details ..." 
        print "NAME: " + self.name
        print "CASH: ", self.cash
        print "RISK MONEY: ", self.risk_money
        print "PORTFOLIO CONTAINS: ..."
        for symbol, quantity, unit_price in self.portfolios:
            print("%s units of %s @ $%s each" % (quantity, symbol, unit_price))

#class Broker(name, portfolio):
#    """Broker class for faciliator of finances"""
#    pass


if __name__ == "__main__":
    investor1 = Investor("JohnDoe", 100575)
    investor1.add_stock("AAA", 50)
    investor1.add_stock("BHV", 1000)
    investor1.add_stock("BEX", 200)
    investor1.add_stock("AJW", 5000)
    investor1.add_stock("ZZZ", 30)
    investor1.details()

