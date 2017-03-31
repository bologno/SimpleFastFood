import tkinter
from user_main_menu import UserMenu


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



    def showLogin(self, mainForm):
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
        forgotBttn = tkinter.Button(loginTab, text='Forget pswd ')
        # lambda function here allows to blend as parameter
        # the function called on the button with his own
        # arguemnt. Otherwise doesnt work on tkinter.
        registerBtn = tkinter.Button(loginTab, text='Save ',
                                     command=lambda: self.getProfile(loginTab))
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
        forgotBttn.pack()
        registerBtn.pack()

        return (loginTab)


    def getProfile(self, topLevel):
        #This method checks new user information and callSup
        #User main menu
        mainMenuForm = UserMenu().mainForm(topLevel)
        mainMenuForm.grab_set()
