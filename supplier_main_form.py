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

    def mainSupForm(self, mainForm):
        suppForm = tkinter.Toplevel(mainForm)
        suppForm.after(3, lambda: suppForm.focus_force())
        suppForm.title('Suppliers menu')
        registerBtn = tkinter.Button(suppForm, text='Add/Edit',
                                    command=lambda: self.addEditForm(suppForm))
        specialBtn = tkinter.Button(suppForm, text='Special req',
                                    command=lambda: self.makeSpecial(suppForm))#add 'command =' parameter
        backBtn = tkinter.Button(suppForm, text='Back', command=suppForm.destroy)#add 'command =' parameter
        registerBtn.pack()
        specialBtn.pack()
        backBtn.pack()
        return (suppForm)

    def addEditForm(self, mainTab):
        suppAdd = tkinter.Toplevel(mainTab)
        suppAdd.grab_set()
        suppAdd.after(3, lambda: suppAdd.focus_force())
        suppAdd.title('Add Supplier')
        nameEntry = tkinter.Entry(suppAdd)
        nameLabel = tkinter.Label(suppAdd, text='Enter supplier name')
        saveBttn = tkinter.Button(suppAdd, text='Save')
        nameEntry.pack()
        nameLabel.pack()
        saveBttn.pack()
        return(suppAdd)

    def makeSpecial(self, mainTab):
        suppAdd = tkinter.Toplevel(mainTab)
        suppAdd.grab_set()
        suppAdd.after(3, lambda: suppAdd.focus_force())
        suppAdd.title('Add special order products')
        p1Entry = tkinter.Entry(suppAdd)
        p1Label = tkinter.Label(suppAdd, text='Enter prod ID')
        p1Qnty = tkinter.Entry(suppAdd)
        p1QntyLabel = tkinter.Label(suppAdd, text='Enter prod amount')
        saveBttn = tkinter.Button(suppAdd, text='Save')
        p1Entry.pack()
        p1Label.pack()
        p1Qnty.pack()
        p1QntyLabel.pack()
        saveBttn.pack()
        return(suppAdd)

if __name__ == '__main__':
    helloScreen = SupplierForm()
    helloScreen.mainSupForm()
