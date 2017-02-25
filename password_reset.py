import tkinter as tk

class resetPassword(RegisterClass):
    '''
    This class models the password reset procedure.updates user password on
    company´s user database
    '''
    def __init__(self):
        pass
        #    self.name = ''
        #    self.lastName = ''
        #    self.phone = ''
        #    self.address = ''

    def checkUser(self):#two entry fields with labels. And some buttons are displayed
        checkTab = tk.Tk()
        checkTab.geometry("250x250+120+120")
        checkTab.title('Select new password')
        Pswd1  = tk.Entry(checkTab)
        Pswd1Label = tk.Label(checkTab, text = 'Write new passord').grid(row=0)
        Pswd3 = tk.Label(checkTab, text = 'for real').grid(row=0, column = 2)
        Pswd2  = tk.Entry(checkTab,)
        Pswd2Label = tk.Label(checkTab, text = 'Repeat password').grid(row=1)
        okButton  = tk.Button(checkTab)#add 'comman
        okButtonLabel = tk.Label(checkTab, text = 'Enter').grid(row=2)
        #forgotButton  = tk.Button(checkTab)#add 'command
        #forgotButtonLabel = tk.Label(checkTab, text = 'Forgot access').grid(row=3)

        Pswd1.grid(row = 0, column = 1)
        Pswd2.grid(row = 1, column = 1)
        okButton.grid(row = 2, column = 1)
        #forgotButton.grid(row = 3, column = 1)

        # Code to add widgets will go here...
        checkTab.mainloop()

    def resetACcount(self):
        #Define procedure for password reset. email or phon validation.
        pass
