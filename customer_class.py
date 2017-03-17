from super_simple_db import SqliteBase

class Customer():
    '''
    this class maps customers on company database. Relevant information as
    delivery address, and telephone are the main ones
    '''

    def __init__(self, parms):
        self.values = ['super_simple_db', 'customer', parms]
        self.name = parms[0]
        self.lastName = parms[1]
        self.phone = parms[2]
        self.address = parms[3]
        #self.clubPts = parms[4]

    def setCustDb(self):#This methos asents information for first time
        dbInter = SqliteBase(self.values)
        dbInter.fillTable()

    def updateCutInfo(self, tel = None, address = None, clubPts = None):
        #updatin customer contact info is a relevant method fo functionality
        dbCustomer = open('clientesDB.myd', 'w+')
        if tel:
            self.tel = tel
        if address:
            self.address = address
        if clubPts:
            self.clubPts = clubPts
        dbCustomer.close()
