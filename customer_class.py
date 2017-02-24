class Customer(Object):
    '''
    this class maps customers on company database. Relevant information as
    delivery address, and telephone are the main ones
    '''

    def __init__(self, name, tel, cutomerId, address, clubPts):
        self.name = name
        self.tel = tel
        self.cutomerId = cutomerId
        self.address = address
        self.clubPts = clubPts

    def setCustomer(self):#This methos asents information for first time
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
