import tkinter
from store_user_login import StoreLogin
from user_class import User
from tkinter import messagebox


class StoreRegClass():
    '''
    This class models the Register and LOgin for store system users.
    '''
    def __init__(self):
        pass
    #    self.name = ''
    #    self.lastName = ''
    #    self.phone = ''
    #    self.address = ''

    def getProfile(self, entryList):
        # this method saves Wnrey values from user to a local variable,
        # After, is called a method for saving new user information on DB
        #userParms = [str(entryList[0]), str(entryList[1]), int(entryList[2]), str(entryList[3])]
        userParms = []

        for i in entryList:
            userParms.append(i.get())

        userLogic = User(userParms)
        userLogic.setUserDb()

        profTab = tkinter.Tk()
        profTab.title('User Info shuld be saved on DB')
        nameLabel = tkinter.Label(profTab, text='Name '+str(userLogic.name))
        nameLabel.pack()
        profTab.mainloop


    def showRegister(self, mainForm):
        # This methos displays form, validates data security
        # and sends the data to be saved on DB.
        loginTab = tkinter.Toplevel(mainForm)
        loginTab.after(1, lambda: loginTab.focus_force())
        loginTab.title('Provide user info')
        nameEntry = tkinter.Entry(loginTab)  # add 'command
        nameLabel = tkinter.Label(loginTab, text='Enter Name')
        lastNEntry = tkinter.Entry(loginTab)  # add 'command
        lastNLabel = tkinter.Label(loginTab, text='Enter Last Name')
        userEntry = tkinter.Entry(loginTab)  # add 'command
        userLabel = tkinter.Label(loginTab, text='Enter user')
        pswdEntry = tkinter.Entry(loginTab)  # add '
        pswdLabel = tkinter.Label(loginTab, text='Enter password')
        pswd2Entry = tkinter.Entry(loginTab)  # add 'comman
        pswd2Label = tkinter.Label(loginTab, text='Repeat password')
        emailEntry = tkinter.Entry(loginTab)
        emailLabel = tkinter.Label(loginTab, text='Enter email ')
        listParms = [nameEntry, lastNEntry, userEntry, pswdEntry, emailEntry]

        registerBtn = tkinter.Button(loginTab, text='Save ',
                    command=lambda: self.getProfile(listParms))
        #aself.name  = tkinter.Entry(registerTab, text = 'Name')#add 'command

        nameEntry.pack()
        nameLabel.pack()
        lastNEntry.pack()
        lastNLabel.pack()
        userEntry.pack()
        userLabel.pack()
        pswdEntry.pack()
        pswdLabel.pack()
        pswd2Entry.pack()
        pswd2Label.pack()
        emailEntry.pack()
        emailLabel.pack()
        registerBtn.pack()

        return (loginTab)


    def setProfile(self, loginTab, mainForm):
        # This method should validate for security and then.
        # add store user name and password.
        # into store user Database. And then open login menu.
        messagebox.showinfo('Registered', 'Check email')
        loginTab.destroy()

        mainMenuForm = StoreLogin().loginForm(mainForm)
        mainMenuForm.grab_set()
