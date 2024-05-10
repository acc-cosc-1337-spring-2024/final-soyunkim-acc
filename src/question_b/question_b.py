class Stock:
    __symbol = 0
    __company_name = 0
    
    def __init__(self, symbol, company_name):
        self.__symbol = symbol
        self.__company_name = company_name

    def return_symbols(self):
        return self.__symbol

    def return_company_name(self):
        return self.__company_name
    
def stock_purchase_history():
    aapl = Stock('AAPL', 'Apple Inc')
    cat = Stock('CAT', 'Caterpillar')
    ek = Stock('EK', 'Eastman Kodak')
    goog = Stock('Goog', 'Google')
    msft = Stock('MSFT', 'Microsoft')

    stocks = {'AAPL' : aapl, 'CAT' : cat, 'EK' : ek, 'GOOG' : goog, 'MSFT' : msft}
    print('Stock purchase history:\n')
    print('Symbol\t', 'Company Name\n')

    for key, value in stocks.items():
        print (key, value.return_company_name(), sep="\t")
