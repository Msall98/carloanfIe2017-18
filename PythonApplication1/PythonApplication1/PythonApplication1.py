from tkinter import * # Import tkinter
from tkinter import ttk
import tkinter as tk    

class LoanCalculator:
    def __init__(self):
        self.window = Tk() # Create a self.window
        self.window.title("Car Loan Calculator") # Set title
        self.window.geometry('500x400')

        
        Label(self.window, text = "Test1").grid(row = 1, 
            column = 1, sticky = W)
        Label(self.window, text = "test2").grid(row = 2, 
            column = 1, sticky = W)
        Label(self.window, text = "test3").grid(row = 3, 
            column = 1, sticky = W)
        Label(self.window, text = "test4").grid(row = 4, 
            column = 1, sticky = W)
        Label(self.window, text = "test5").grid(row = 5, 
            column = 1, sticky = W)
        Label(self.window,text="test6").grid(row=6,
            column=1,sticky= W)
        
        self.annualInterestRateVar = StringVar()
        Entry(self.window, textvariable = self.annualInterestRateVar, 
            justify = RIGHT).grid(row = 1, column = 2)
        self.numberOfYearsVar = StringVar()
        Entry(self.window, textvariable = self.numberOfYearsVar, 
            justify = RIGHT).grid(row = 2, column = 2)
        self.loanAmountVar = StringVar()
        Entry(self.window, textvariable = self.loanAmountVar, 
            justify = RIGHT).grid(row = 3, column = 2)
        
        self.monthlyPaymentVar = StringVar()
        lblMonthlyPayment = Label(self.window, textvariable = 
            self.monthlyPaymentVar).grid(row = 4, column = 2, 
                sticky = E)
        self.totalPaymentVar = StringVar()
        lblTotalPayment = Label(self.window, textvariable = 
            self.totalPaymentVar).grid(row = 5, 
                column = 2, sticky = E)
        showcarselection = Label(self.window,textvariable = "Test").grid(row=6,column=2,sticky = E)
        
        self.carloanlist=["National Car","Test"]
        self.carloan = StringVar()
        self.carloan.set(self.carloanlist[0])
        global national
        national=int(1)
        # Quote from Jonathan Goh,The Cat ==> "This is error one: self.carloan.trace("w",self.updatesecondoptionbox(national))"
        self.carloan.trace("w",lambda *args: self.updatesecondoptionbox(national)) # Jonathan Goh ==> "This is correct."
        self.carloanomenu=OptionMenu(self.window,self.carloan,*self.carloanlist)
        self.carloanomenu.grid(row=7,column=2)
        self.carloanb = StringVar()
        a=self.carloan.get()
        if self.carloan=="National Car":
            self.carloanlistb=["Proton Saga"]
            self.carlonmenub=OptionMenu(self.window,self.carloanb,*self.carloanlistb).grid(row=8,column=2)
        else:
            self.carloanlistb=["Honda Civic"]
            self.carlonmenub=OptionMenu(self.window,self.carloanb,*self.carloanlistb).grid(row=8,column=2)


        btComputePayment = Button(self.window, text = "Compute Payment", 
            command = self.maininput).grid(
                row = 9, column = 2, sticky = E)
        killswitch=Button(self.window,text="Quit",command=self.killswitch).grid(row=9,column=3,sticky=E)
        
        self.window.mainloop() # Create an event loop
    def maininput(self):
        self.getcarselection()
        self.computePayment()
    def getcarselection(self):
        a=self.carloan.get()
        if a.upper() == ("TEST"):
            print("Fuck you")
        else:
            print("Thanks for choosing a ",a,"Brand")
    def updatesecondoptionbox(self,national):
        b = self.carloan.get()
        national=0
        self.carloanb = StringVar()
        if b.upper()=="NATIONAL CAR":
            self.carloanlistb=["Proton Saga"]
            self.carlonmenub=OptionMenu(self.window,self.carloanb,*self.carloanlistb).grid(row=8,column=2)
            national=1
            return national
        else:
            self.carloanlistb=["Honda Civic"]
            self.carlonmenub=OptionMenu(self.window,self.carloanb,*self.carloanlistb).grid(row=8,column=2)
            national="0"
            return int(national)
    def pop(self):
        print("Hi")
    def killswitch(self):
        sys.exit()
        
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

    


LoanCalculator()# Create GUI