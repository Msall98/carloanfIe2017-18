from tkinter import * # Import tkinter
from tkinter import ttk
import tkinter as tk    
class LoanCalculator:
    def __init__(self):
        window = Tk() # Create a window
        window.title("Car Loan Calculator") # Set title
        window.geometry('500x200')

        
        Label(window, text = "Test1").grid(row = 1, 
            column = 1, sticky = W)
        Label(window, text = "test2").grid(row = 2, 
            column = 1, sticky = W)
        Label(window, text = "test3").grid(row = 3, 
            column = 1, sticky = W)
        Label(window, text = "test4").grid(row = 4, 
            column = 1, sticky = W)
        Label(window, text = "test5").grid(row = 5, 
            column = 1, sticky = W)
        Label(window,text="test6").grid(row=6,
            column=1,sticky= W)
        
        self.annualInterestRateVar = StringVar()
        Entry(window, textvariable = self.annualInterestRateVar, 
            justify = RIGHT).grid(row = 1, column = 2)
        self.numberOfYearsVar = StringVar()
        Entry(window, textvariable = self.numberOfYearsVar, 
            justify = RIGHT).grid(row = 2, column = 2)
        self.loanAmountVar = StringVar()
        Entry(window, textvariable = self.loanAmountVar, 
            justify = RIGHT).grid(row = 3, column = 2)
        
        self.monthlyPaymentVar = StringVar()
        lblMonthlyPayment = Label(window, textvariable = 
            self.monthlyPaymentVar).grid(row = 4, column = 2, 
                sticky = E)
        self.totalPaymentVar = StringVar()
        lblTotalPayment = Label(window, textvariable = 
            self.totalPaymentVar).grid(row = 5, 
                column = 2, sticky = E)
        self.carloanlist=["One","Two"]
        self.carloan = StringVar()
        self.carloan.set(self.carloanlist[0])
        self.carloanomenu=OptionMenu(window,self.carloan,*self.carloanlist)
        self.carloanomenu.grid(row=6,column=2)
        btComputePayment = Button(window, text = "Compute Payment", 
            command = self.computePayment).grid(
                row = 7, column = 2, sticky = E)
        killswitch=Button(window,text="Quit",).grid(row=7,column=3,sticky=E)
        
        window.mainloop() # Create an event loop
    def pop(self):
        print("Hi")
        
    def computePayment(self):
        monthlyPayment = self.getMonthlyPayment(
            float(self.loanAmountVar.get()), 
            float(self.annualInterestRateVar.get()) / 1200, 
            int(self.numberOfYearsVar.get()))
        self.monthlyPaymentVar.set(format(monthlyPayment, '10.2f'))
        totalPayment = float(self.monthlyPaymentVar.get()) * 12 \
            * int(self.numberOfYearsVar.get())
        self.totalPaymentVar.set(format(totalPayment, '10.2f'))
        print(self.carloanlist)
        
        
    def getMonthlyPayment(self,
            loanAmount, monthlyInterestRate, numberOfYears):
        a=int(loanAmount)
        b=int(monthlyInterestRate)
        c=int(numberOfYears)
        if (a<= 10 or c<=1):
            popup=tk.Tk()
            popup.wm_title("Insufficent Amount")
            popup.geometry("500x200")
            label = ttk.Label(popup,text="Seriously")
            label.pack(pady=10,anchor=CENTER)
            B1 = ttk.Button(popup,text="okay",command = popup.destroy)
            B1.pack()
            popup.mainloop()
        else:
            monthlyPayment = loanAmount * monthlyInterestRate / (1
            - 1 / (1 + monthlyInterestRate) ** (numberOfYears * 12))
            return monthlyPayment;

    


LoanCalculator()  # Create GUI 