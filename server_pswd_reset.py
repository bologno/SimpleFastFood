class StoreUserAccount():

    '''
    This class models the store user account. Saves data on Database and
    handles information updates on those accounts.
    '''

    def __init__(self):
        pass

    def pswdForm(self, topForm):
        emailEntry.pack()
        emailLbl.pack()
        enterBtn.pack()
        psswdLbl.pack()
        enterBtn.pack()
        fgtBtn.pack()
        return (storeLoginTab)

    def emailVerifier(self, email):
        

    def resetChecker(self, mainForm):
        suppForm = SupplierForm().mainSupForm(mainForm)
        suppForm.grab_set()
