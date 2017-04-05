from super_simple_db import SqliteBase

class User():
    '''
    this class maps users on company database. Relevant information as
    name, id, user name, password and telephone are stored on data base.
    '''

    def __init__(self, parms):
        self.values = ['super_simple_db', 'user', parms]
        self.name = parms[0]
        self.lastName = parms[1]
        self.user = parms[2]
        self.password = parms[3]
        self.email = parms[4]

    def setUserDb(self):#This method sends information for first time
        dbInter = SqliteBase(self.values)
        dbInter.fillTable()

    def updateCutInfo(self, tel = None, address = None, clubPts = None):
        #updatin useromer contact info is a relevant method fo functionality
        dbUser = open('user.myd', 'w+')
        if tel:
            self.tel = tel
        if address:
            self.address = address
        if clubPts:
            self.clubPts = clubPts
        dbUser.close()
