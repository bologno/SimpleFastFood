#!/usr/bin/python

import tkinter
from register import RegisterClass
from log_in import LogInClass
from menu_customer import CustomerMenu
from promotions import Promotion
from support import Support



# registerC =
newLog = LogInClass()
orderMenu = CustomerMenu()
newProm = Promotion()
support = Support()

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
        mainForm.iconify()
        regForm = newLog.checkUser(mainForm)

    def callMenu(self, mainForm):
        mainForm.iconify()
        regForm = orderMenu.showMenu(mainForm)

    def callPromo(self, mainForm):
        mainForm.iconify()
        regForm = newProm.showPromo(mainForm)

    def callSup(self, mainForm):
        mainForm.iconify()
        regForm = support.showHelp(mainForm)
        mainForm.deiconify()


if __name__ == '__main__':
    helloScreen = MainMenuClass()
    helloScreen.setForm()
