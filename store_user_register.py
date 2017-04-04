import tkinter
from store_user_login import StoreLogin
from tkinter import messagebox


class StoreRegClass():
    '''
    This class models the Register and LOgin for store system users.
    '''
    def __init__(self):
        pass
    #    self.name = ''
    #    self.lastName = ''
    #    self.phone = ''
    #    self.address = ''



    def showRegister(self, mainForm):
        loginTab = tkinter.Toplevel(mainForm)
        loginTab.after(1, lambda: loginTab.focus_force())
        loginTab.title('Provide user info')
        userEntry = tkinter.Entry(loginTab)  # add 'command
        userLabel = tkinter.Label(loginTab, text='Enter user')
        pswdEntry = tkinter.Entry(loginTab)  # add '
        pswdLabel = tkinter.Label(loginTab, text='Enter password')
        pswd2Entry = tkinter.Entry(loginTab)  # add 'comman
        pswd2Label = tkinter.Label(loginTab, text='Repeat password')
        emailEntry = tkinter.Entry(loginTab)
        emailLabel = tkinter.Label(loginTab, text='Enter email ')

        registerBtn = tkinter.Button(loginTab, text='Save ',
                                     command=lambda: self.getProfile(loginTab, mainForm))
        #aself.name  = tkinter.Entry(registerTab, text = 'Name')#add 'command

            #        custLogic.setCusDb
        userEntry.pack()
        userLabel.pack()
        pswdEntry.pack()
        pswdLabel.pack()
        pswd2Entry.pack()
        pswd2Label.pack()
        emailEntry.pack()
        emailLabel.pack()
        registerBtn.pack()

        return (loginTab)


    def getProfile(self, loginTab, mainForm):
        # This method should validate for security and then.
        # add store user name and password.
        # into store user Database. And then open login menu.
        messagebox.showinfo('Registered', 'Check email')
        loginTab.destroy()

        mainMenuForm = StoreLogin().loginForm(mainForm)
        mainMenuForm.grab_set()
