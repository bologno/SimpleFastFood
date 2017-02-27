
import tkinter as tk
from menu_customer import CustomerMenu

class Stock():
    '''
    This class models products stock availability numbers.
    '''
    def __init__(self):
        #self.localDollar = 15.8
        #    self.lastName = ''
        #    self.phone = ''
        #    self.address = ''
        pass

    def viewStock(self, ):#Labels for the order are shown in kitchen
        root = tk.Tk()
        #top_bg = tk.PhotoImage()
        root.geometry("1280x900+3+3")
        cv=tk.Canvas(root,width=1280,height=100, bg= 'green', border=2)
        cv.pack(side="top",fill="both",expand="yes")
        #cv.create_image(0,0,image=top_bg,anchor='nw')
        Btn1 = tk.Label(cv,text="Zero Coke")
        Btn1.grid(row=0,column=0,padx=5,pady=5)
        Btn2 = tk.Label(cv,text="10")
        Btn2.grid(row=0,column=1,padx=5,pady=5)

        mcv=tk.Canvas(root,width=1280,height=700,bg="blue",border=1)
        mcv.pack(side="top",fill="both",expand="yes")
        Btn1 = tk.Label(mcv,text="Hot dog buns")
        Btn1.grid(row=0,column=0,padx=5,pady=5)
        Btn2 = tk.Label(mcv,text="22")
        Btn2.grid(row=0,column=1,padx=5,pady=5)

        bcv=tk.Canvas(root,width=1280,height=100,bg="yellow")
        bcv.pack(side="top",fill="both",expand="yes")
        root.mainloop()

    def orderDisplay(self):
        #Define procedure for password reset. email or phon validation.
pass
