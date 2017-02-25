import tkinter as tk

class CustomerMenu():
    '''
    This class models the password reset procedure.updates user password on
    company´s user database
    '''
    def __init__(self):
        self.localDollar = 15.8
        #    self.lastName = ''
        #    self.phone = ''
        #    self.address = ''

    def checkUser(self):#two entry fields with labels. And some buttons are displayed
        checkTab = tk.Tk()
        checkTab.geometry("250x250+120+120")
        checkTab.title('Select new password')
        prdct1  = tk.Entry(checkTab).grid(row = 0, column = 1)
        prdct1Descrip = tk.Label(checkTab, text = 'Hamburguesa').grid(row=0\
        , column = 0)
        prdct1Price = tk.Label(checkTab, text = 2.5 * self.localDollar )\
        .grid(row=0, column = 2)

        prdct2  = tk.Entry(checkTab)
        prdct2Descrip = tk.Label(checkTab, text = 'Muzzarella').grid(row=1\
        , column = 0)
        prdct2Price = tk.Label(checkTab, text = 4 * self.localDollar )\
        .grid(row=1, column = 2)
        okButton  = tk.Button(checkTab)#add 'comman
        okButtonLabel = tk.Label(checkTab, text = 'Enter Order').grid(row=2)
        #prdct1.grid(row = 0, column = 1)
        prdct2.grid(row = 1, column = 1)
        okButton.grid(row = 2, column = 1)

        checkTab.mainloop()

    def resetACcount(self):
        #Define procedure for password reset. email or phon validation.
        pass
