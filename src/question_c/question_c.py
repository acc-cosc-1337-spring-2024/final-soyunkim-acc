class Stock:
    __symbol = 0
    __company_name = 0
    
    def __init__(self, symbol, company_name):
        self.__symbol = symbol
        self.__company_name = company_name

    def get_symbols(self):
        return self.__symbol

    def get_company_name(self):
        return self.__company_name    