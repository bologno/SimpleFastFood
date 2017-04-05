import tkinter
from product_class import Product


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
        addPdctBtn = tkinter.Button(stockForm, text='Add Product',
                                command=lambda: self.addPdct(stockForm))
        backBtn = tkinter.Button(stockForm, text='Back',
                                command=stockForm.destroy)
        searchEntry.pack()
        searchLabel.pack()
        searchBtn.pack()
        addPdctBtn.pack()
        backBtn.pack()
        return (stockForm)

    def searchStock(self, searchEntry):
        #This method should search prod id and display prod stock
        pass

    def addPdct(self, stockForm):
        addStockForm = tkinter.Toplevel(stockForm)
        addStockForm.grab_set()
        addStockForm.after(1, lambda: stockForm.focus_force())
        addStockForm.title('ADd Stock')
        idEntry = tkinter.Entry(addStockForm)
        idLabel = tkinter.Label(addStockForm, text='New Product ID')
        nameEntry = tkinter.Entry(addStockForm)
        nameLabel = tkinter.Label(addStockForm, text='New Prodcut Name')
        brandEntry = tkinter.Entry(addStockForm)
        brandLabel = tkinter.Label(addStockForm, text='New Product Brand')
        qtyEntry = tkinter.Entry(addStockForm)
        qtyLabel = tkinter.Label(addStockForm, text='Quantity')
        minEntry = tkinter.Entry(addStockForm)
        minLabel = tkinter.Label(addStockForm, text='Set Min threshold')
        pdctParms = [idEntry, nameEntry, brandEntry, qtyEntry, minEntry]

        addPdctBtn = tkinter.Button(addStockForm, text='Add Product',
                                command=lambda: self.savePdct(pdctParms))
        backBtn = tkinter.Button(addStockForm, text='Back',
                                command=addStockForm.destroy)
        idEntry.pack()
        idLabel.pack()
        nameEntry.pack()
        nameLabel.pack()
        brandEntry.pack()
        brandLabel.pack()
        qtyEntry.pack()
        qtyLabel.pack()
        minEntry.pack()
        minLabel.pack()
        addPdctBtn.pack()
        backBtn.pack()
        return (stockForm)
    def savePdct(self, pdctParms):
        readyParms =[]
        for i in pdctParms:
            readyParms.append(i.get())
        newProd = Product(readyParms)
        newProd.setProductDb()
