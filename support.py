import tkinter as tk

class Support():

    '''
    this class was thought as a form for customer support and
    customer feedback. Eventually should offer a chat service
    as well as email, phone and social network links.
    '''

    def __init__(self):
        pass

    def showHelp(self):
        checkTab = tk.Tk()
        checkTab.geometry("250x250+120+120")
        checkTab.title('Contact')
        questionLabel = tk.Label(checkTab, text='Enter your question').grid(
                                row=0, column=0)
        question  = tk.Entry(checkTab).grid(row=0, column=1)
        emailLabel = tk.Label(checkTab, text='Enter your email').grid(row=1,
                                    column=0)
        email  = tk.Entry(checkTab).grid(row=1, column=1)

        okButton  = tk.Button(checkTab, text='Send question').grid(row=2,
                                    column=0)
        canButton = tk.Button(checkTab, text='Back to main menu').grid(row=2,
                                    column=1)
        checkTab.mainloop()
