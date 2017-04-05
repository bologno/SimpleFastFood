import tkinter
class Stock():

    '''
    This class represents products stuck. Includes triggers
    for low levels besides products numbers.
    '''

    def __init__(self):
        pass

    def checkStock(self, mainForm):
        stockForm = tkinter.Toplevel(mainForm)
        stockForm.after(1, lambda: stockForm.focus_force())
        stockForm.title('Store stock')
        searchEntry = tkinter.Entry(stockForm)
        searchLabel = tkinter.Label(stockForm, text='Enter prod ID')
        searchBtn = tkinter.Button(stockForm, text='Search',
                                command=lambda: self.searchStock(searchEntry))
        backBtn = tkinter.Button(stockForm, text='Back',
                                command=stockForm.destroy)
        searchEntry.pack()
        searchLabel.pack()
        searchBtn.pack()
        backBtn.pack()
        return (stockForm)

    def searchStock(self, searchEntry):
        #This method should search prod id and display prod stock
        pass
