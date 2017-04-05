import tkinter

class CustomerList():

    '''
    This class represents customers list.
    '''

    def __init__(self):
        pass

    def showCustomers(self, mainForm):
        stockForm = tkinter.Toplevel(mainForm)
        stockForm.after(1, lambda: stockForm.focus_force())
        stockForm.title('Customer Ínfo Edition')
        searchEntry = tkinter.Entry(stockForm)
        searchLabel = tkinter.Label(stockForm, text='Enter Customer ID')
        searchBtn = tkinter.Button(stockForm, text='Search',
                                command=lambda: self.searchCust(searchEntry))
        backBtn = tkinter.Button(stockForm, text='Back',
                                command=stockForm.destroy)
        searchEntry.pack()
        searchLabel.pack()
        searchBtn.pack()
        backBtn.pack()
        return (stockForm)

    def searchCust(self, searchEntry):
        #This method should search customer id and display his user info.
        pass
