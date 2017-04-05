import tkinter

class CashReg():

    '''
    This class represents customers list.
    '''

    def __init__(self):
        pass

    def getCashReg(self, mainForm):
        cashRegForm = tkinter.Toplevel(mainForm)
        cashRegForm.after(1, lambda: cashRegForm.focus_force())
        cashRegForm.title('Cash Register')
        searchEntry = tkinter.Entry(cashRegForm)
        prodEntry = tkinter.Entry(cashRegForm)
        prodLabel = tkinter.Label(cashRegForm, text='Enter Product Name or Id')
        updtBtn = tkinter.Button(cashRegForm, text='Update Order',
                                command=lambda: self.updateOrder(searchEntry))
        addBtn = tkinter.Button(cashRegForm, text='Add Product',
                                command=lambda: self.addProduct(searchEntry))
        pmntLabel = tkinter.Label(cashRegForm, text='Payment Method')
        paperBtn = tkinter.Button(cashRegForm, text='Paper/coins',
                                command=lambda: self.moneyPayment(searchEntry))
        cardBtn = tkinter.Button(cashRegForm, text='Credit/Debit',
                                command=lambda: self.cardPayment(searchEntry))
        backBtn = tkinter.Button(cashRegForm, text='Back',
                                command=cashRegForm.destroy)
        prodEntry.pack()
        prodLabel.pack()
        updtBtn.pack()
        addBtn.pack()
        pmntLabel.pack()
        paperBtn.pack()
        cardBtn.pack()
        backBtn.pack()
        return (cashRegForm)

    def updateOrder(self, searchEntry):
        #This method adds product to manual order.
        pass

    def addProduct(self, searchEntry):
        #This method adds product to manual order.
        pass

    def moneyPayment(self, searchEntry):
        #This method should records money payment for the order.
        pass

    def cardPayment(self, searchEntry):
        #This method should records card payment for the order.
        pass
