from super_simple_db import SqliteBase

class Supplier():

    '''
    this class maps suppliers on company database.
    Relevant information as Name, phone, products
    and/or address is stored
    '''

    def __init__(self, parms):
        self.values = ['super_simple_db', 'supplier', parms]
        self.name = parms[0]
        self.phone = parms[2]
        self.address = parms[3]
        self.products = parms[4]
        #self.clubPts = parms[4]

    def setCustDb(self):#This methos asents information for first time
        dbInter = SqliteBase(self.values)
        dbInter.fillTable()

    def updateCutInfo(self, name=None, phone=None, address=None, products=None):
        #updatin customer contact info is a relevant method fo functionality
        dbCustomer = open('clientesDB.myd', 'w+')
        if name:
            self.name = name
        if phone:
            self.phone = phone
        if address:
            self.address = address
        if products:
            self.products = address
        dbCustomer.close()
