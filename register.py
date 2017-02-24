import tkinter

class RegisterClass():
    '''
    This class models the Register for new customers. Takes customer information
    and validates customer via email or cellphone
    '''
    def __init__(self):
        pass
    #    self.name = ''
    #    self.lastName = ''
    #    self.phone = ''
    #    self.address = ''
    def askInfo(self):
        registerTab = tkinter.Tk()
        registerTab.title('Please provide your information')
        nameEntry  = tkinter.Entry(registerTab)#add 'command
        nameLabel = tkinter.Label(registerTab, text = 'Name')
        lastNameEntry  = tkinter.Entry(registerTab,)#add '
        lastNameLabel = tkinter.Label(registerTab, text = 'Last name')
        phoneEntry  = tkinter.Entry(registerTab)#add 'comman
        phoneLabel = tkinter.Label(registerTab, text = 'Phone')
        addressEntry  = tkinter.Entry(registerTab)
        addressLabel = tkinter.Label(registerTab, text = 'Address ')
        #self.name  = tkinter.Entry(registerTab, text = 'Name')#add 'command

        nameLabel.pack( side = tkinter.LEFT)
        nameEntry.pack( side = tkinter.RIGHT)
        lastNameLabel.pack()
        lastNameEntry.pack()
        phoneLabel.pack()
        phoneEntry.pack()
        addressLabel.pack()
        addressEntry.pack()

        # Code to add widgets will go here...
        registerTab.mainloop()

'''
if __name__ == '__main__':
    registerCustomer = Register()
    registerCustomer.askInfo()
'''
