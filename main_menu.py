#!/usr/bin/python

import tkinter
from register import RegisterClass
from log_in import LogInClass
from menu_customer import CustomerMenu
from promotions import Promotion
from support import Support



#import LogInMenu
#import Menu
#import Promotion
#import RepChat
#import FeedBack


class MainMenuClass():

    '''
    This class models the mainMenu of the store. Sets up the
    interfaces and shows buttons and information for cutomer
    register, Login, menu information, or just skip to
    promotion information
    '''

    def __init__(self):
        pass

    def setForm(self):
        top = tkinter.Tk()
        top.title('Welcome to Los Pollos Hnos')
        registerBtn = tkinter.Button(top, text='Register',
                                     command=lambda: self.callRegister(top))
        logInBtn = tkinter.Button(top, text='Login',
                                  command=lambda: self.callLogin(top))
        menuBtn = tkinter.Button(top, text='Menu',
                                 command=lambda: self.callMenu(top))
        promotion = tkinter.Button(top, text='Promotions',
                                   command=lambda: self.callPromo(top))
        repChat = tkinter.Button(top, text='Support/Feedback',
                                 command=lambda: self.callSup(top))

        registerBtn.pack()
        logInBtn.pack()
        menuBtn.pack()
        promotion.pack()
        repChat.pack()
        # Code to add widgets will go here...
        top.mainloop()

    def callRegister(self, mainForm):
        # mainForm.iconify()
        regForm = RegisterClass().askInfo(mainForm)
        regForm.grab_set()

    def callLogin(self, mainForm):
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
        suppForm.grab_set()



if __name__ == '__main__':
    helloScreen = MainMenuClass()
    helloScreen.setForm()
