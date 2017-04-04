import tkinter
from tkinter import messagebox


class RestorePass():

    '''
    This class models the password restore form for store users.
    '''

    def __init__(self):
        pass

    def pswdForm(self, topForm):
        fgtPswdTab = tkinter.Toplevel(topForm)
        fgtPswdTab.after(1, lambda: fgtPswdTab.focus_force())
        fgtPswdTab.title('Forgot password')
        emailEntry = tkinter.Entry(fgtPswdTab)
        emailLbl = tkinter.Label(fgtPswdTab, text='Enter email')
        enterBtn = tkinter.Button(fgtPswdTab, text='Reset Password',
        command=lambda: self.popAndDestroy(fgtPswdTab))#add 'command =' parameter

        emailEntry.pack()
        emailLbl.pack()
        enterBtn.pack()
        return (fgtPswdTab)
    def popAndDestroy(self, fgtPswdTab):
        messagebox.showinfo('Reset on process', 'Check email')
        fgtPswdTab.destroy()
