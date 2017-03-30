#!/usr/bin/python

import tkinter
from store_user_mainmenu import StoreLoginClass

class StoreLogin():

    '''
    This class models the Register/Log in menu of the store.
    '''

    def __init__(self):
        pass

    def setUserForm(self):
        top = tkinter.Tk()
        top.title('Nice to have you working at Pollos Hnos')
        registerBtn = tkinter.Button(top, text='Register',
                                     command=lambda: self.callLogin(top))
        #logInBtn = tkinter.Button(top, text='Login',
        #                          command=lambda: self.callLogin(top))

        registerBtn.pack()
        # Code to add widgets will go here...
        top.mainloop()

    def callLogin(self, mainForm):
        logInForm = StoreLoginClass().showLogin(mainForm)
        logInForm.grab_set()

'''    def callLogin(self, mainForm):
        loginForm = LogInClass().checkUser(mainForm)
        loginForm.grab_set()

    def callMenu(self, mainForm):
        menuForm = CustomerMenu().showMenu(mainForm)
        menuForm.grab_set()

    def callPromo(self, mainForm):
        promoForm = Promotion().showPromo(mainForm)
        promoForm.grab_set()


    def callSup(self, mainForm):
        suppForm = Support().showHelp(mainForm)
        suppForm.grab_set()'''


if __name__ == '__main__':
    helloScreen = StoreLogin()
    helloScreen.setUserForm()
