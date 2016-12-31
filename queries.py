"""Helper functions to lookup the sql database"""
import MySQLdb
import MySQLdb.cursors
import settings


db = MySQLdb.connect(host=settings.HOST,
                     user=settings.USER,
                     passwd=settings.PASSWD,
                     db=settings.DB,
                     cursorclass=MySQLdb.cursors.DictCursor)
cursor = db.cursor()

def check_version():
    """Check sql version (dummy test function to check active connection)"""
    sql = 'SELECT VERSION'
    # cursor = db.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    for row in rows:
        print row["VERSION()"]

def check_price(symbol, year, month, day):
    """Check open price for stock with symbol on year-month-day"""
    sql = 'SELECT OPEN_PRICE FROM STOCK_HISTORY WHERE TRADING_SYMBOL="%s" AND TRADE_DATE="%s-%s-%s"' % (symbol, year, month, day)
    cursor.execute(sql)
    result = cursor.fetchone()
    price = result["OPEN_PRICE"]
    # print "Price for %s on %s-%s-%s is $%s." % (symbol, year,  month, day, price)
    return price

def get_all_stocks():
    """Return a list of all distinct stock symbols into a list and return it"""
    stocklist = list()
    sql = 'SELECT DISTINCT TRADING_SYMBOL FROM STOCK_HISTORY'
    cursor.execute(sql)
    rows = cursor.fetchall()
    
    for row in rows:
        stock_symbol = row["TRADING_SYMBOL"]
        stocklist.append(stock_symbol)
    return stocklist

if __name__ == '__main__':
    check_price(symbol='BML', year=2005, month=3, day=1)
