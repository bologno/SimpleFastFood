#!/usr/bin/python

import tkinter
from register import RegisterClass
registerC = RegisterClass()
#import LogInMenu
#import Menu
#import Promotion
#import RepChat
#import FeedBack

class MainMenuClass():
    '''
    This class models the mainMenu of the store. Sets up the interfaces and shows
    buttons and information for cutomer register, Login, menu information, or just
    skip to promotion information
    '''

    def __init__(self):
        pass
    def setForm(self):
        top = tkinter.Tk()
        top.title('Welcome to Los Pollos Hnos')
        registerBtn = tkinter.Button(top, text = 'Register', \
        command = registerC.askInfo)
        logInBtn = tkinter.Button(top, text = 'Login')#add 'command =' parameter
        menuBtn = tkinter.Button(top, text = 'Menu')#add 'command =' parameter
        promotion = tkinter.Button(top, text = 'Promotions')#add 'command =' parameter
        repChat = tkinter.Button(top, text = 'repChat')#add 'command =' parameter
        feedBack = tkinter.Button(top, text = 'FeedBack/Suggestions')#add 'command =' parameter

        registerBtn.pack()
        logInBtn.pack()
        menuBtn.pack()
        promotion.pack()
        repChat.pack()
        feedBack.pack()
        # Code to add widgets will go here...
        top.mainloop()

if __name__ == '__main__':
    helloScreen = MainMenu()
    helloScreen.setForm()
