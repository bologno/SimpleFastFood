class Supplier(Object):
    '''
    This class models a supplier characteristics of relevance to company
    '''

    def __init__(self, pName, supTel, supId):
        self.pName = pName
        self.supTel = supTel
        self.supId = supId

    def actualizarStock(self, prodId, prodStock):#
        stockDb = open('stockDb.txt', 'w+')
        stockDb.write(prodId, prodStock)
        stockDb.close()
