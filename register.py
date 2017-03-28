import tkinter
from customer_class import Customer


class RegisterClass():
    '''
    This class models the Register for new customers. Takes customer
    information and validates customer via email or cellphone
    '''
    def __init__(self):
        pass
    #    self.name = ''
    #    self.lastName = ''
    #    self.phone = ''
    #    self.address = ''

    def getProfile(self, entryList):
        # this method saves Wnrey values from customer to a local variable,
        # After, is called a method for saving new customer information on DB
        #custParms = [str(entryList[0]), str(entryList[1]), int(entryList[2]), str(entryList[3])]
        custParms = []

        for i in entryList:
            custParms.append(i.get())

        custLogic = Customer(**custParms)
        custLogic.setCustDb()

        profTab = tkinter.Tk()
        profTab.title('Customer Info shuld be saved on DB')
        nameLabel = tkinter.Label(profTab, text='Name '+str(custLogic.name))
        nameLabel.pack()
        profTab.mainloop
#        custLogic.setCusDb

    def askInfo(self, mainForm):
        registerTab = tkinter.Toplevel(mainForm)
        registerTab.after(1, lambda: registerTab.focus_force())
        registerTab.title('Please provide your information')
        nameEntry = tkinter.Entry(registerTab)  # add 'command
        nameLabel = tkinter.Label(registerTab, text='Name')
        lastNameEntry = tkinter.Entry(registerTab,)  # add '
        lastNameLabel = tkinter.Label(registerTab, text='Last name')
        phoneEntry = tkinter.Entry(registerTab)  # add 'comman
        phoneLabel = tkinter.Label(registerTab, text='Phone')
        addressEntry = tkinter.Entry(registerTab)
        addressLabel = tkinter.Label(registerTab, text='Address ')
        userEntry = tkinter.Entry(registerTab)
        userLabel = tkinter.Label(registerTab, text='P ')
        passwordEntry = tkinter.Entry(registerTab)
        passwordLabel = tkinter.Label(registerTab, text='Address ')
        entryList = [nameEntry, lastNameEntry, phoneEntry, addressEntry]
        # lambda function here allows to blend as parameter
        # the function called on the button with his own
        # arguemnt. Otherwise doesnt work on tkinter.
        registerBtn = tkinter.Button(registerTab, text='Save ',
                                     command=lambda: self.getProfile(entryList))
        #self.name  = tkinter.Entry(registerTab, text = 'Name')#add 'command

        nameEntry.pack()
        nameLabel.pack()
        lastNameEntry.pack()
        lastNameLabel.pack()
        phoneEntry.pack()
        phoneLabel.pack()
        addressEntry.pack()
        addressLabel.pack()
        registerBtn.pack()

        return registerTab

        # Code to add widgets will go here...
        # registerTab.mainloop()

'''
if __name__ == '__main__':
    registerCustomer = Register()
    registerCustomer.askInfo()
'''
