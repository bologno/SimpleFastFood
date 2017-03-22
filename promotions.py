import tkinter

class Promotion():
    '''
    This class represents a form for showing available promotions and
    other customer useful information.
    Takes a list as parameter, the list has three elements for each
    product. Which represents product/bundle, price and picture.
    '''
    def __init__(self):

        self.promo = [['pizza', 3,5], ['hamburguer', 2]]
    #    self.name = ''
    #    self.lastName = ''
    #    self.phone = ''
    #    self.address = ''
    def showPromo(self):
        checkTab = tkinter.Tk()
        #checkTab.geometry("250x250+120+120")
        checkTab.title('Promotions')
        col = 0
        for i in range(len(self.promo)):
            prdName = tkinter.Label(checkTab, text=self.promo[i][0])
            prdPrice = tkinter.Label(checkTab, text=self.promo[i][1])
            orderEntry = tkinter.Entry(checkTab)
            prdName.grid(row=i, column=col)
            prdPrice.grid(row=i, column=col+1)
            orderEntry.grid(row = i, column = col+2)

            #prdPic = tkinter.Label(checkTab, text=self.promo[i]).grid(row=i)
            #Define tkinter element for showing a picture of the product
        orderButton = tkinter.Button(checkTab, text = 'Go order')
        mainMenu = tkinter.Button(checkTab, text = 'Back to main menu')
        orderButton.grid(row=len(self.promo)+1, column= 0)
        mainMenu.grid(row=len(self.promo)+1, column= 1)
        checkTab.mainloop()
