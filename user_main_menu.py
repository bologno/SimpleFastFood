import tkinter


class UserMenu():

    '''
    This class models the mainMenu of the store app user.
    provides functionality to manually check register and kitchen
    hitorical movement. Also for customer and supplier information
    updates.
    '''

    def __init__(self):
        pass

    def mainForm(self, topForm):
        mainMenuTab = tkinter.Toplevel(topForm)
        mainMenuTab.after(2, lambda: mainMenuTab.focus_force())
        mainMenuTab.title('User Main Menu')
        registerBtn = tkinter.Button(mainMenuTab, text='Cash Reg',
                                    command=lambda: self.cashResgister)
        customerBtn = tkinter.Button(mainMenuTab, text='Customers',
                                    command=lambda: self.customerList)#add 'command =' parameter
        supplierBtn = tkinter.Button(mainMenuTab, text='Supplier',
                                    command=lambda: elf.supplierList)#add 'command =' parameter
        stockBtn = tkinter.Button(mainMenuTab, text='Stock', command=lambda: self.checkStock)#add 'command =' parameter
        registerBtn.pack()
        customerBtn.pack()
        supplierBtn.pack()
        stockBtn.pack()
        return (mainMenuTab)

'''    def cashResgister(self,):
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
'''


if __name__ == '__main__':
    helloScreen = User()
    helloScreen.mainForm()
