from datetime import date
def algorithm(d1,m1,y1,d2,m2,y2,rate1,model,carname):
    dd1 = date(y1, m1, d1)
    dd2 = date(y2, m2, d2)
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
        print('Invalid time period, maximum number of days of rental should be 30 days')
        






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
    carname='Proton Saga (1.3cc)'
    rate1=135
    deposit=100
    algorithm(d1,m1,y1,d2,m2,y2,rate1,model,carname)

    
elif model==2:
    carname='Toyota Vios (1.5cc)'
    rate1=180
    deposit=300
    algorithm(d1,m1,y1,d2,m2,y2,rate1,model,carname)
    

elif model==3:
    carname='Honda Civic (2.0cc)'
    rate1=300
    deposit=300
    algorithm(d1,m1,y1,d2,m2,y2,rate1,model,carname)
    

elif model==4:
    carname='Hyundai Starex (2.5cc)'
    rate1=500
    deposit=300
    algorithm(d1,m1,y1,d2,m2,y2,rate1,model,carname)

else :
    print('Invalid car model')
