import tkinter
from supplier_main_form import SupplierForm

class StoreLogin():

    '''
    This class models the Login menu for the store user.
    '''

    def __init__(self):
        pass

    def loginForm(self, topForm):
        storeLoginTab = tkinter.Toplevel(topForm)
        storeLoginTab.after(2, lambda: storeLoginTab.focus_force())
        storeLoginTab.title('User Main Menu')
        userEntry = tkinter.Entry(storeLoginTab)
        userLbl = tkinter.Label(storeLoginTab, text='Enter user')
        psswdEntry = tkinter.Entry(storeLoginTab)
        psswdLbl = tkinter.Label(storeLoginTab, text='Enter password')
        enterBtn = tkinter.Button(storeLoginTab, text='Enter',
                                    command=lambda: self.customerList)#add 'command =' parameter
        fgtBtn = tkinter.Button(storeLoginTab, text='Forgot user',
                                    command=lambda: self.supplierList(storeLoginTab))#add 'command =' parameter
        userEntry.pack()
        userLbl.pack()
        psswdEntry.pack()
        psswdLbl.pack()
        enterBtn.pack()
        fgtBtn.pack()
        return (storeLoginTab)

    def storeLogin(self, mainForm):
        suppForm = SupplierForm().mainSupForm(mainForm)
        suppForm.grab_set()
