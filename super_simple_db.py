
import sqlite3
#settings = input('Enter Data Base and table to crete. ')
#parms = input('Enter parms list. ')
def dbDef():
    parms = []
    types = []
    index = {'N':'NULL', 'I':'INTEGER', 'R':'REAL', 'T':'TEXT', 'B':'BLOB'}
    base = input('Enter base name. ')
    table = input('Enter table name. ')
    parmNbr = int(input('Enter number of parms for table. '))
    for i in range(parmNbr):
        parms.append(input('Enter parm name. '))
        types.append(index[input('Type initial (INT, REAL, TEXT, BLOB)')])
    definition = [base, table, parms, types]
    return(definition)
#settings = dbDef()

class SqliteBase():

    # This method init should online take Databes and table nmaes.
    # Parms and types should be provided only on buidlTable method.
    # Values should be provided when fillTable method is called.
    def __init__(self, settings):
        #self.conn = sqlite.connect()
        self.base = settings[0]
        self.table = settings[1]
        #self.parms = settings[2]
        #self.types = settings[3]
        self.values = settings[2]
        pass
    #DB to hold
    def getTable(self):
        return(self.table, self.parms, self.types)

    def buildDb(self):
        dBase = sqlite3.connect(self.base+'.db')
        dBase.commit()
        dBase.close()
        print('DB built')

    def parmTypeFormat(self, parms, types):
        if not len(parms) == len(types):
            #Error detection shuold be improvved to avoid missmatch lenght
            print('parms and types are missmatched. ')

        else:
            prevStructure = []
            for i in range(len(parms)):
                prevStructure.append(parms[i] +' '+ types[i])
            return(', '.join(prevStructure))

    def buildTable(self):
        formatedParms = self.parmTypeFormat(self.parms, self.types)
        conn = sqlite3.connect(self.base+'.db')
        c = conn.cursor()


        # Create table
        c.execute('CREATE TABLE '+self.table+' ('+formatedParms+')')
        conn.commit()
        conn.close()


    def fillTable(self):
        #for i in range(len(self.parms)):
        #    self.values.append(input('Enter vl '+str(i)+' for '+str(self.table)))
        conn = sqlite3.connect(self.base +'.db')
        c = conn.cursor()
        #Number of values needs to match parms/valeus amount.
        #SEcurity need to be improoved.
        values = ", ".join(self.values)
        sql = 'INSERT INTO '+self.table+" VALUES (?, ?, ?, ?)"
        c.execute(sql, values)
        # Save (commit) the changes
        conn.commit()
        conn.close()

        # We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.)
