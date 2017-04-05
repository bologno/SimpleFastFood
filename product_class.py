from super_simple_db import SqliteBase

class Product():
    '''
    this class maps products from store. Relevant information as
    name, brand, remaining quantity and minimum required(threshold).
    '''

    def __init__(self, parms):
        #self.values = ['super_simple_db', 'customer', parms]
        #self.values = ['super_simple_db', 'user', parms]
        self.values = ['super_simple_db', 'product', parms]
        self.id = parms[0]
        self.name = parms[1]
        self.brand = parms[2]
        self.qty = parms[3]
        self.threshold = parms[4]

    def setProductDb(self):#This method sends information for first time
        dbInter = SqliteBase(self.values)
        dbInter.fillTable()

    def updateCutInfo(self, name = None, brand = None, qty = None):
        #updatin useromer contact info is a relevant method fo functionality
        dbUser = open('product.myd', 'w+')
        if name:
            self.name = name
        if brand:
            self.brand = brand
        if qty:
            self.qty = qty
        dbUser.close()
