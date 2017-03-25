import tkinter
class User():

    '''
    This class models the mainMenu of the store app user.
    provides functionality to manually check register and kitchen
    hitorical movement. Also for customer and supplier information
    updates.
    '''

    def __init__(self):
        pass

    def mainForm(self):
        top = tkinter.Tk()
        top.title('User Main Menu')
        registerBtn = tkinter.Button(top, text='Register',
                                    command=self.cashResgister)
        customerBtn = tkinter.Button(top, text='Customers',
                                    command=self.customerList)#add 'command =' parameter
        supplierBtn = tkinter.Button(top, text='Supplier',
                                    command=self.supplierList)#add 'command =' parameter
        stockBtn = tkinter.Button(top, text='Stock', command=self.checkStock)#add 'command =' parameter
        registerBtn.pack()
        customerBtn.pack()
        supplierBtn.pack()
        stockBtn.pack()
        top.mainloop()

    def cashResgister(self,):
        top = tkinter.Tk()
        top.title('Cash Register')

    def customerList(self,):
        top = tkinter.Tk()
        top.title('Regesiterd Customers')

    def supplierList(self,):
        top = tkinter.Tk()
        top.title('Regesiterd Suppliers')

    def checkStock(self,):
        top = tkinter.Tk()
        top.title('Kitchen Stock')
