from tkinter import * # Import tkinter
from tkinter import ttk
from datetime import date
import tkinter as tk    
import sys 


model = 1
class LoanCalculator:
    def __init__(self):
        self.window = Tk() # Create a self.window
        self.window.title("Car Loan Calculator") # Set title
        self.window.geometry('500x250')
        self.window.resizable(False,False)
        # Make some labels in grid form.
        Label(self.window, text = "Collection Data (DD)").grid(row = 1, 
            column = 1, sticky = W)
        Label(self.window, text = "Collection Data (MM)").grid(row = 2, 
            column = 1, sticky = W)
        Label(self.window, text = "Collection Data (YYYY)").grid(row = 3, 
            column = 1, sticky = W)
        Label(self.window, text = "Return Data (DD)").grid(row = 4, 
            column = 1, sticky = W)
        Label(self.window, text = "Return Data (MM)").grid(row = 5, 
            column = 1, sticky = W)
        Label(self.window,text="Return Data (YYYY)").grid(row=6,
            column=1,sticky= W)
        
        #Make some TextBox to allow user to type in stuff.
        self.d1 = StringVar()
        Entry(self.window, textvariable = self.d1, 
            justify = LEFT).grid(row = 1, column = 2)
        self.m1 = StringVar()
        Entry(self.window, textvariable = self.m1, 
            justify = LEFT).grid(row = 2, column = 2)
        self.y1 = StringVar()
        Entry(self.window, textvariable = self.y1, 
            justify = LEFT).grid(row = 3, column = 2)
        self.d2 = StringVar()
        Entry(self.window, textvariable = self.d2, 
            justify = LEFT).grid(row = 4, column = 2)
        self.m2 = StringVar()
        Entry(self.window, textvariable = self.m2, 
            justify = LEFT).grid(row = 5, column = 2)
        self.y2 = StringVar()
        Entry(self.window, textvariable = self.y2, 
            justify = LEFT).grid(row = 6, column = 2)
        
        #OptionBox.
        showcarselection = Label(self.window,textvariable = "Test").grid(row=6,column=2,sticky = E)
        self.carloanlist=["National Car (RM 100 Deposit)","Foreign car (RM 300 Deposit)"]
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
        self.carloanlistb=[" "]
        self.carlonmenub=OptionMenu(self.window,self.carloanb,*self.carloanlistb).grid(row=8,column=2)
        #Of Course, Some Buttons :) ...
        btComputePayment = Button(self.window, text = "Compute Payment", 
            command = self.maininput).grid(
                row = 9, column = 2)
        
        self.window.mainloop() # Create an event loop
    def maininput(self):
        #To Combine Two Function as One.
        selection=self.carloanb.get()
        d1=self.d1.get()
        m1=self.m1.get()
        y1=self.y1.get()
        d2=self.d2.get()
        m2=self.m2.get()
        y2=self.y2.get()
        if d1.isnumeric()==True and m1.isnumeric()==True and y1.isnumeric()==True and d2.isnumeric()==True and m2.isnumeric()==True and y2.isnumeric()==True:
            if selection == "Proton Saga (1.3cc) (RM135/day)":
                carname='Proton Saga (1.3cc)'
                rate1=135
                deposit=100
                model=1
                algorithm(d1,m1,y1,d2,m2,y2,rate1,model,carname,deposit)
            elif selection == "Toyota Vios (1.5cc) (180/day)":
                carname='Toyota Vios (1.5cc)'
                rate1=180
                deposit=300
                model=2
                algorithm(d1,m1,y1,d2,m2,y2,rate1,model,carname,deposit)
            elif selection == "Honda Civic (2.0cc) (300/day)":
                carname='Honda Civic (2.0cc)'
                rate1=300
                deposit=300
                model=3
                algorithm(d1,m1,y1,d2,m2,y2,rate1,model,carname,deposit)
            elif selection == "Hyundai Starex (2.5cc) (500/day)":
                carname='Hyundai Starex (2.5cc)'
                rate1=500
                deposit=300
                model=4
                algorithm(d1,m1,y1,d2,m2,y2,rate1,model,carname,deposit)
        else:
            popup=tk.Tk()
            popup.wm_title("Error:")
            popup.geometry("500x200")
            label = ttk.Label(popup,text="Error : Only numbers allowed in dates")
            label.pack(pady=10,anchor=CENTER)
            B1 = ttk.Button(popup,text="OK",command = popup.destroy)
            B1.pack()
            popup.mainloop()
            print('Invalid time period, maximum number of days of rental should be 30 days')
        

    def updatesecondoptionbox(self,national):
        #To Change data after knows the value selected from the first OptionMenu.
        b = self.carloan.get()
        national=1
        self.carloanb = StringVar()
        if b.upper()=="NATIONAL CAR (RM 100 DEPOSIT)":
            self.carloanlistb=["Proton Saga (1.3cc) (RM135/day)"]
            self.carlonmenub=OptionMenu(self.window,self.carloanb,*self.carloanlistb).grid(row=8,column=2)
            national=1
            return int(national)
        else:
            self.carloanlistb=["Toyota Vios (1.5cc) (180/day)","Honda Civic (2.0cc) (300/day)","Hyundai Starex (2.5cc) (500/day)"]
            self.carlonmenub=OptionMenu(self.window,self.carloanb,*self.carloanlistb).grid(row=8,column=2)
            national=0
            return int(national)
    def pop(self):
        #Extra Stuff.
        print("Hi")        

    





def algorithm(d1,m1,y1,d2,m2,y2,rate1,model,carname,deposit):
    if ((int(y1)%4)==0 and int(m1)==2 and (int(d1)<1 or int(d1)>29)) or ((int(y2)%4)==0 and int(m2)==2 and (int(d2)<1 or int(d2)>29)) or ((int(y1)%4)!=0 and int(m1)==2 and (int(d1)<1 or int(d1)>28)) or ((int(y2)%4)!=0 and int(m2)==2 and (int(d2)<1 or int(d2)>28)) or int(y1)<2000 or int(y1)>2100 or int(y2)<2000 or int(y2)>2100 or (str(m1) in ('1','3','5','7','8','10','12') and (int(d1)<1 or int(d1)>31)) or (str(m1) in ('4','6','9','11') and (int(d1)<1 or int(d1)>30)) or (str(m2) in ('1','3','5','7','8','10','12') and (int(d2)<1 or int(d2)>31)) or (str(m2) in ('4','6','9','11') and (int(d2)<1 or int(d2)>30)):
        popup=tk.Tk()
        popup.wm_title("Invaild Data")
        popup.geometry("550x200")
        label = ttk.Label(popup,text="Invalid date(s)")
        label.pack(pady=10,anchor=CENTER)
        B1 = ttk.Button(popup,text="OK",command = popup.destroy)
        B1.pack()
        popup.mainloop()
        
    else:        
        dd1 = date(int(y1), int(m1), int(d1))
        dd2 = date(int(y2), int(m2), int(d2))
        time = dd2 - dd1
        rate=int(rate1)
        grandtotal=deposit+rate*int(time.days+1)

        if int(time.days+1)<=30 and int(time.days+1)>=1:
            history=open('rental_history.txt','a')

            history.write('Collection date:'+str(d1)+'.'+str(m1)+'.'+str(y1)+'\n')
            history.write('Return date    :'+str(d2)+'.'+str(m2)+'.'+str(y2)+'\n')
            history.write('Car model      :'+carname+'\n')
            history.write('Deposit        :   '+str(deposit)+'\n')
            history.write('Rental Price   :   '+str(rate)+'x'+str(time.days+1)+'\n')
            history.write('***************************************\n')
            history.write('Grand Total    :   '+str(grandtotal)+'\n')
            history.write('***************************************\n')
            history.close()
            popup=tk.Tk()
            popup.wm_title("Thank you")
            popup.geometry("500x200")
            label_1 = ttk.Label(popup,text=("You wish to rent the " + carname + " for " + str(time.days+1) + " day(s)\n"))
            label_1.pack(pady=10,anchor=CENTER)
            label_2 = ttk.Label(popup,text=("The grand total would of renting the " + carname + " would be RM " + str(grandtotal)+ "\n"))
            label_2.pack(pady=10,anchor=CENTER)
            B1 = ttk.Button(popup,text="OK",command = popup.destroy)
            B1.pack()
            popup.mainloop()

        else:
            popup=tk.Tk()
            popup.wm_title("Invaild Date")
            popup.geometry("500x200")
            label = ttk.Label(popup,text="Invalid time period, maximum number of days of rental should be 30 days")
            label.pack(pady=10,anchor=CENTER)
            B1 = ttk.Button(popup,text="OK",command = popup.destroy)
            B1.pack()
            popup.mainloop()
             


LoanCalculator()# Create GUI

