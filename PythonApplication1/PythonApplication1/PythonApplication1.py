from tkinter import * # Import tkinter
from tkinter import ttk
import tkinter as tk    

class LoanCalculator:
    def __init__(self):
        self.window = Tk() # Create a self.window
        self.window.title("Car Loan Calculator") # Set title
        self.window.geometry('500x250')
        self.window.resizable(False,False)
        # Make some labels in grid form.
        Label(self.window, text = "Collection Data (DD,MM,YYYY").grid(row = 1, 
            column = 1, sticky = W)
        Label(self.window, text = "Return Data (DD,MM,YYYY)").grid(row = 2, 
            column = 1, sticky = W)
        Label(self.window, text = "test3").grid(row = 3, 
            column = 1, sticky = W)
        Label(self.window, text = "test4").grid(row = 4, 
            column = 1, sticky = W)
        Label(self.window, text = "test5").grid(row = 5, 
            column = 1, sticky = W)
        Label(self.window,text="test6").grid(row=6,
            column=1,sticky= W)
        
        #Make some TextBox to allow user to type in stuff.
        self.annualInterestRateVar = StringVar()
        Entry(self.window, textvariable = self.annualInterestRateVar, 
            justify = RIGHT).grid(row = 1, column = 2)
        self.numberOfYearsVar = StringVar()
        Entry(self.window, textvariable = self.numberOfYearsVar, 
            justify = RIGHT).grid(row = 2, column = 2)
        self.loanAmountVar = StringVar()
        Entry(self.window, textvariable = self.loanAmountVar, 
            justify = RIGHT).grid(row = 3, column = 2)
        
        #Some Labels and OptionBox.
        self.monthlyPaymentVar = StringVar()
        lblMonthlyPayment = Label(self.window, textvariable = 
            self.monthlyPaymentVar).grid(row = 4, column = 2, 
                sticky = E)
        self.totalPaymentVar = StringVar()
        lblTotalPayment = Label(self.window, textvariable = 
            self.totalPaymentVar).grid(row = 5, 
                column = 2, sticky = E)
        showcarselection = Label(self.window,textvariable = "Test").grid(row=6,column=2,sticky = E)
        
        self.carloanlist=["National Car","Foreign car"]
        self.carloan = StringVar()
        self.carloan.set(self.carloanlist[0])
        global national
        national=int(1)
        # Quote from Jonathan Goh,The Cat ==> "This is error one: self.carloan.trace("w",self.updatesecondoptionbox(national))"
        self.carloan.trace("w",lambda *args: self.updatesecondoptionbox(national)) # Jonathan Goh ==> "This is correct."
        self.carloanomenu=OptionMenu(self.window,self.carloan,*self.carloanlist)
        self.carloanomenu.grid(row=6,column=2)
        self.carloanb = StringVar()
        a=self.carloan.get()
        self.carloanlistb=["Proton Saga"]
        self.carlonmenub=OptionMenu(self.window,self.carloanb,*self.carloanlistb).grid(row=7,column=2)
        #Of Course, Some Buttons :) ...
        btComputePayment = Button(self.window, text = "Compute Payment", 
            command = self.maininput).grid(
                row = 8, column = 2, sticky = E)
        killswitch=Button(self.window,text="Quit",command=self.killswitch).grid(row=8,column=3,sticky=E)
        
        self.window.mainloop() # Create an event loop
    def maininput(self):
        #To Combine Two Function as One.
        self.getcarselection()
        self.computePayment()
    def getcarselection(self):
        #To read the data from the first OptionMenu and reply.
        a=self.carloan.get()
        if a.upper() == ("FOREIGN CAR"):
            print("Fuck you")
        else:
            print("Thanks for choosing a ",a,"Brand")
    def updatesecondoptionbox(self,national):
        #To Change data after knows the value selected from the first OptionMenu.
        b = self.carloan.get()
        national=1
        self.carloanb = StringVar()
        if b.upper()=="NATIONAL CAR":
            self.carloanlistb=["Proton Saga"]
            self.carlonmenub=OptionMenu(self.window,self.carloanb,*self.carloanlistb).grid(row=7,column=2)
            national=1
            return int(national)
        else:
            self.carloanlistb=["Honda Civic","Toyota Vios"]
            self.carlonmenub=OptionMenu(self.window,self.carloanb,*self.carloanlistb).grid(row=7,column=2)
            national=0
            return int(national)
    def pop(self):
        #Extra Stuff.
        print("Hi")
    def killswitch(self):
        #As the function said :) ...
        sys.exit()
        
    def computePayment(self):
        #Test algorithms.
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
        #Spam Detectors.
        a=int(loanAmount)
        b=int(monthlyInterestRate)
        c=int(numberOfYears)
        if (a<= 10 or c<=1):
            popup=tk.Tk()
            popup.wm_title("Insufficent Amount")
            popup.geometry("500x200")
            label = ttk.Label(popup,text="Seriously")
            label.pack(pady=10,anchor=CENTER)
            B1 = ttk.Button(popup,text="OK",command = popup.destroy)
            B1.pack()
            popup.mainloop()
        else:
            monthlyPayment = loanAmount * monthlyInterestRate / (1
            - 1 / (1 + monthlyInterestRate) ** (numberOfYears * 12))
            return monthlyPayment;

    


LoanCalculator()# Create GUI