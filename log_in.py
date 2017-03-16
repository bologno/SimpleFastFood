'''
comment
'''
import tkinter

class LogInClass():
    '''
    This class models the Log in procedur. Matches user and pasword against
    companies user database
    '''
    def __init__(self):
        pass
    #    self.name = ''
    #    self.lastName = ''
    #    self.phone = ''
    #    self.address = ''
    def checkUser(self):
        checkTab = tkinter.Tk()
        checkTab.geometry("250x250+120+120")
        checkTab.title('Enter credentials')
        userCheck  = tkinter.Entry(checkTab)
        userCheckLabel = tkinter.Label(checkTab, text = 'User Name').grid(row=0)
        passwordCheck  = tkinter.Entry(checkTab,)
        passwordCheckLabel = tkinter.Label(checkTab, text = 'Password').grid(row=1)
        EnterButton  = tkinter.Button(checkTab)#add 'comman
        EnterButtonLabel = tkinter.Label(checkTab, text = 'Enter').grid(row=2)
        forgotButton  = tkinter.Button(checkTab)#add 'command
        forgotButtonLabel = tkinter.Label(checkTab, text = 'Forgot access').grid(row=3)

        userCheck.grid(row = 0, column = 1)
        passwordCheck.grid(row = 1, column = 1)
        EnterButton.grid(row = 2, column = 1)
        forgotButton.grid(row = 3, column = 1)

        # Code to add widgets will go here...
        checkTab.mainloop()
