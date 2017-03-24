#!/usr/bin/python

import tkinter
from register import RegisterClass
from promotions import Promotion
from log_in import LogInClass
from menu_customer import CustomerMenu
from support import Support



registerC = RegisterClass()
newProm = Promotion()
newLog = LogInClass()
orderMenu = CustomerMenu()
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
                                    command=registerC.askInfo)
        logInBtn = tkinter.Button(top, text='Login', command=newLog.checkUser)#add 'command =' parameter
        menuBtn = tkinter.Button(top, text='Menu', command=orderMenu.checkUser)#add 'command =' parameter
        promotion = tkinter.Button(top, text='Promotions', command=newProm.showPromo)#add 'command =' parameter
        repChat = tkinter.Button(top, text='Support/Feedback', command=support.showHelp)#add 'command =' parameter

        registerBtn.pack()
        logInBtn.pack()
        menuBtn.pack()
        promotion.pack()
        repChat.pack()
        # Code to add widgets will go here...
        top.mainloop()

if __name__ == '__main__':
    helloScreen = MainMenu()
    helloScreen.setForm()
