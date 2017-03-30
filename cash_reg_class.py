class CashRegister():
    '''
    This class maps regiter movements ons sales, as price (input) and separated
    (output). Upadtes info on records for daily and hitoric movements.
    '''

    def __init__(self, olderId, salePrice):
        self.olderId = olderId
        self.salePrice = salePrice

    def cobroDigital(self,):#For figital payments, this method should call
        #online modules for online charging. This is an ongoing feature
        salesDb = open('salesDb.txt', 'w+')
        salesDb.write(self.salePrice)
        salesDb.close()

    def cobroEfectivo(self, grossIncome):#This method tracks payment and spare
        salesDb = open('salesDb.txt', 'w+')
        salesDb.write(self.salePrice) #sale price recording.
        salesDb.write(grossIncome-self.salePrice)#Spare recording..
        salesDb.close()
