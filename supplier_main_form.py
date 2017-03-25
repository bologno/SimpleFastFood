import tkinter
class SupplierForm():

    '''
    This class models the mainMenu of the store. Sets up the
    interfaces and shows buttons and information for cutomer
    register, Login, menu information, or just skip to
    promotion information
    '''

    def __init__(self):
        pass

    def mainSupForm(self):
        top = tkinter.Tk()
        top.title('Suppliers menu')
        registerBtn = tkinter.Button(top, text='Add/Edit',
                                    command=self.addEditForm)
        specialBtn = tkinter.Button(top, text='Special req',
                                    command=self.makeSpecial)#add 'command =' parameter
        backBtn = tkinter.Button(top, text='Back', command=top.destroy)#add 'command =' parameter
        registerBtn.pack()
        specialBtn.pack()
        backBtn.pack()
        top.mainloop()

    def addEditForm(self,):
        top = tkinter.Tk()
        top.title('Add/Edit supplier and prodcuts')

    def makeSpecial(self,):
        top = tkinter.Tk()
        top.title('Add/Edit supplier and prodcuts')
