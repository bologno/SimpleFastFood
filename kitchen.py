#!/usr/bin/python
import tkinter as tk
#from menu_customer import CustomerMenu

'''
This class models the kiotchen display for ongoing orders
Details products to be made with standard time running
sort orders in FIFO + order type(small order may come up earlier).
One canvass represents one order.
'''
class Kitchen():

    def __init__(self):
        #self.localDollar = 15.8
        #    self.lastName = ''
        #    self.phone = ''
        #    self.address = ''
        pass

    def ordersDisplay(self, order = None):#Labels for the order are shown in kitchen
        checkTab = tk.Tk()
        checkTab.geometry("250x250+120+120")
        checkTab.title('On going orders')
        order = tk.Canvas(checkTab, width=200, height=100)
        orderP1 = tk.Label(checkTab, text = 'Hambur').grid(row=0, column = 0)
        orderP2 = tk.Label(checkTab, text = "M Fries" ).grid(row=1, column = 0)
        oneMinButton = tk.Button(checkTab, text = "+ time")
        okButton  = tk.Button(checkTab, text = "Done" )
        okButton.grid(row = 2, column = 1, command = None)#call to getOrder method
        oneMinButton.grid(row = 2, column = 0, command = None)#call to getOrder method
        checkTab.mainloop()

    def orderDisplay(self):
        #Define procedure for password reset. email or phon validation.
        pass
