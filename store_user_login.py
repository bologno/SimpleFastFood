import tkinter
from store_user_main_menu import UserMenu
from store_user_pswd_fgt import RestorePass

class StoreLogin():

    '''
    This class models the Login menu for the store user.
    '''

    def __init__(self):
        pass

    def loginForm(self, topForm):
        storeLoginTab = tkinter.Toplevel(topForm)
        storeLoginTab.after(1, lambda: storeLoginTab.focus_force())
        storeLoginTab.title('User Main Menu')
        userEntry = tkinter.Entry(storeLoginTab)
        userLbl = tkinter.Label(storeLoginTab, text='Enter user')
        psswdEntry = tkinter.Entry(storeLoginTab)
        psswdLbl = tkinter.Label(storeLoginTab, text='Enter password')
        enterBtn = tkinter.Button(storeLoginTab, text='Enter',
                                    command=lambda: self.storeLogin(storeLoginTab))#add 'command =' parameter
        fgtBtn = tkinter.Button(storeLoginTab, text='Forgot user',
                                    command=lambda: self.resetPsw(storeLoginTab))#add 'command =' parameter
        userEntry.pack()
        userLbl.pack()
        psswdEntry.pack()
        psswdLbl.pack()
        enterBtn.pack()
        fgtBtn.pack()
        return (storeLoginTab)

    def storeLogin(self, mainForm):
        suppForm = UserMenu().getStoreUser(mainForm)
        suppForm.grab_set()

    def resetPsw(self, mainForm):
        suppForm = RestorePass().pswdForm(mainForm)
        suppForm.grab_set()
