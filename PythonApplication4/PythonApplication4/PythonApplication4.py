from tkinter import * # Import tkinter
from tkinter import ttk
import tkinter as tk    
import sys 



class LoanCalculator:
    def __init__(self):
        self.window = Tk() # Create a self.window
        self.window.title("Car Loan Calculator") # Set title
        self.window.geometry('500x250')
        self.window.resizable(False,False)
        # Make some labels in grid form.
        Label(self.window, text = "Vehicle Cost      (In RM) :").grid(row = 1, 
            column = 1, sticky = W)
        Label(self.window, text = "Down Payment (In RM) :").grid(row = 2, 
            column = 1, sticky = W)
        Label(self.window, text = "Loan Period (In Years):").grid(row = 3, 
            column = 1, sticky = W)
        Label(self.window, text = "Interest rate (in %):").grid(row = 4,
            column = 1, sticky = W)                                                          

        #Make some TextBox to allow user to type in stuff.
        self.price = StringVar()
        Entry(self.window, textvariable = self.price, 
            justify = LEFT).grid(row = 1, column = 2)

        self.dp = StringVar()
        Entry(self.window, textvariable = self.dp, 
            justify = LEFT).grid(row = 2, column = 2)

        self.carloantimelist=["1","2","3","4","5","6","7","8","9","10"]
        self.carloan = StringVar()
        self.carloan.set(self.carloantimelist[0])
        self.carloanomenu=OptionMenu(self.window,self.carloan,*self.carloantimelist)
        self.carloanomenu.grid(row=3,column=2)

        self.interest = StringVar()
        Entry(self.window, textvariable = self.interest, 
            justify = LEFT).grid(row = 4, column = 2)
        #Of Course, Some Buttons :) ...
        btComputePayment = Button(self.window, text = "Compute Payment", 
            command = self.maininput).grid(
                row = 9, column = 2)

    def maininput(self):
        #To Combine Two Function as One.
        price1=self.price.get()
        price=price1.replace(',','')
        down_payment1=self.dp.get()
        down_payment=down_payment1.replace(',','')
        time=int(self.carloan.get())
        interest_rate=self.interest.get()
        if price.replace('.','',1).isdigit()==True and interest_rate.replace('.','',1).isdigit()==True and down_payment.replace('.','',1).isdigit()==True:
            algorithm(price,down_payment,time,interest_rate)           


        elif price=='' or down_payment=='' or interest_rate=='':
            popup=tk.Tk()
            popup.wm_title("Error")
            popup.geometry("550x200")
            popup.resizable(False,False)
            label = ttk.Label(popup,text="Missing Information")
            label.config(font=("Arial",12))
            label.pack(pady=10,anchor=CENTER)
            B1 = ttk.Button(popup,text="OK",command = popup.destroy)
            B1.pack()
            popup.mainloop()

        else:
                popup=tk.Tk()
                popup.wm_title("Invaild Information")
                popup.geometry("550x200")
                popup.resizable(False,False)
                label = ttk.Label(popup,text="Invalid information entered")
                label.config(font=("Arial",12))
                label.pack(pady=10,anchor=CENTER)
                B1 = ttk.Button(popup,text="OK",command = popup.destroy)
                B1.pack()
                popup.mainloop()            

def algorithm(price,down_payment,time,interest_rate):
    if float(price)>=float(down_payment):
        loanamount=float(price)-float(down_payment)
        Total_interest=(float(interest_rate)/100)*time*loanamount
        Monthly_interest=Total_interest/(time*12)
        Monthly_installment=(loanamount+Total_interest)/(time*12)

        popup=tk.Tk()
        popup.wm_title("Thank you")
        popup.geometry("500x200")
        popup.resizable(False,False)
        label_1 = ttk.Label(popup,text=('Your monthly Installment for loaning RM '+str(price)+'\nwith a down payment of RM '+str(down_payment)+' for '+str(time)+' year(s) is:\n RM '+"{0:.2f}".format(Monthly_installment)))
        label_1.pack(pady=10,anchor=CENTER)
        B1 = ttk.Button(popup,text="OK",command = popup.destroy)
        B1.pack()
        popup.mainloop()
    else:
        popup=tk.Tk()
        popup.wm_title("Error")
        popup.geometry("550x200")
        popup.resizable(False,False)
        label = ttk.Label(popup,text=('Down Payment should not be more than the loan amount'))
        label.pack(pady=10,anchor=CENTER)
        B1 = ttk.Button(popup,text="OK",command = popup.destroy)
        B1.pack()
        popup.mainloop()

LoanCalculator()# Create GUI