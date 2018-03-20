from datetime import date
def algorithm(d1,m1,y1,d2,m2,y2,rate1,model,carname):
    d1 = date(y1, m1, d1)
    d2 = date(y2, m2, d2)
    time = d2 - d1
    rate=int(rate1)
    grandtotal=deposit+rate*int(time.days+1)


    if int(time.days+1)<=30 and int(time.days+1)>=1:
        print('You wish to rent the',carname,'for',str(time.days+1),'day(s)\n')
        print('The grand total would of renting the',carname,'would be RM'+str(grandtotal)+'\n')
        choice=input('To see Grand Total breakdown, press {Y}, or press any other button to escape\n')
        if choice.isalpha()==True:
            if choice.upper()=='Y':
                print('Deposit        :   ',deposit,'\n')
                print('Rental Price   :   ',rate,'x',time.days+1,'\n')
                print('*************************\n')
                print('Grand Total    :   ',grandtotal,'\n')
                print('Thank You for using ...')
            else :
                print('Thank You for using ...')
        else :
            print('Thank You for using ...')

    else:
        print('Invalid time period')
        






print('Please Enter the relevant dates:\n')
print('Please Enter the collection date:\n')
d1=int(input('Enter day   :  '))
m1=int(input('Enter month :  '))
y1=int(input('Enter year  :  '))
print('Please Enter the return date:\n')
d2=int(input('Enter day   :  '))
m2=int(input('Enter month :  '))
y2=int(input('Enter year  :  '))
print('\n')
model=int(input('Enter car model:'))
print('\n')

if model==1:
    carname='Proton Saga (cc)'
    rate1=1
    deposit=100
    algorithm(d1,m1,y1,d2,m2,y2,rate1,model,carname)

    
elif model==2:
    carname='Honda Civic (cc)'
    rate1=2
    deposit=300
    algorithm(d1,m1,y1,d2,m2,y2,rate1,model,carname)
    

elif model==3:
    carname='Honda Accord (cc)'
    rate1=3
    deposit=300
    algorithm(d1,m1,y1,d2,m2,y2,rate1,model,carname)
    

elif model==4:
    carname='Nissan X-trail (cc)'
    rate1=4
    deposit=300
    algorithm(d1,m1,y1,d2,m2,y2,rate1,model,carname)

else :
    print('Invalid car model')
    



