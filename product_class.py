class Product(Object):
    '''
    This class models a particular raw product used on company's menu
    '''

    def __init__(self, olderId = 0, nameProd, stockProd, descr,\
     retailPrice):#Method starts all class variables
        self.prodId = olderId + 1
        self.nameProd = nameProd
        self.stockProd = stockProd
        self.descr = descr
        self.retailPrice = retailPrice

    def actualziarSock(self, soldSize = None, boughtSize = None):
        if ingreso:#Method updates stock on sales and supplier drops.
            self.stock += boughtSize
        if egreso:
            self.stock -= soldSize
