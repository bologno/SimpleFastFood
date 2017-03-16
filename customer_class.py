class Customer():
    '''
    this class maps customers on company database. Relevant information as
    delivery address, and telephone are the main ones
    '''

    def __init__(self, parms):
        self.name = parms[0]
        self.tel = parms[1]
        self.cutomerId = parms[2]
        self.address = parms[3]
        #self.clubPts = parms[4]

    def setCustDb(self):#This methos asents information for first time
        dbCustomer = open('dbCustomer.myd', 'w+')
        dbCustomer.write(self.name +'-'+self.id+'-'+self.address)
        dbCustomer.close()

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
