import sqlite3

class dbSqlite():

    def __init__(self):
        #self.conn = sqlite.connect()
        self.dBase = None
        pass

    def buildDb(self, dBase):
        self.dBase = sqlite3.connect(dBase+'.db')
        self.dBase.commit()
        self.dBase.close()


    def buildTable(self, dBase, table, parms, types):
        conn = sqlite3.connect(dBase +'.db')
        c = conn.cursor()

        # Create table
        c.execute('CREATE TABLE '+table+' ('+parms[0]+' '+types[0]+','+ \
        parms[1]+' '+types[1]+','+parms[2]+' '+types[2]+')')
        conn.commit()
        conn.close()

    def fillTable(self, dBase, table, values):
        # Insert a row of data
        conn = sqlite3.connect(dBase +'.db')
        c = conn.cursor()
        c.execute('INSERT INTO'+table+"VALUES ('"+", '".join(values)+"')")
        # Save (commit) the changes
        conn.commit()
        conn.close()

        # We can also close the connection if we are done with it.
        # Just be sure any changes have been committed or they will be lost.)
