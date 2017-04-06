#  File: Day.py

#  Description: prompt the user to enter a date so the program outputs the day of the week of that date

#  Student Name: Arturo Reyes Munoz

#  Student UT EID: ar48836

#  Course Name: CS 303E

#  Unique Number: 50865

#  Date Created: 02/05

#  Date Last Modified:02/06



def main():
    #promt the user to enter the date
    year = eval(input( "Enter year:"))
    while ((year<1000) or (year>2100)):
        year = eval(input( "Enter year:"))
        
    month = eval( input( "Enter month:"))
    while ((month<1) or (month>12)):
        month = eval( input( "Enter month:"))
        
    day = eval( input( "Enter day:"))
    while ((day<0) or (day>31)):
        day = eval( input( "Enter day:"))
    num_days = 0
    #create variable for leap years
    is_leap = ((year%4==0) and (not(year%100==0)))

    #establish the number of days in the selected month             
    if ((month==1) or (month==3) or (month==5) or (month==7) or (month==8) or (month==10) or (month==12)):
        num_days=31
    elif ((month==4) or (month==6) or (month==9) or (month==11)):
            num_days=30
    elif (month==2):
                num_days=28
    #follow algorith given the assignment description              
    a = 0
    # January and February shoould give the variable values of a=11 and a=12 respectively
    if ((month==1) or (month==2)):
        a = month+10
    elif (month>2):
    
        a=month-2

    b = day

    #take into acount January and February pertain to the last months of the previous year to the one chosen
    c = 0
    if ((a==11) or (a==12)):
        c=((year%1000)%100)-1
    elif (a<11):
            c=(year%1000)%100
            
    d = 0
    if (((a==11) or (a==12)) and (year%100==0)):
        d=(year//100)-1
    else:
        d=year//100

    w = (13*a-1)//5
    x=c//4
    y=d//4
    z=w+x+y+b+c-2*d
    r=z%7
    r=(r+7)%7 #to take the negative values of r
    # assign a string with the weekday for each value of r
    if (r==0):
        week_day = "Sunday"
    elif (r==1):
        week_day = "Monday"
    elif (r==2):
        week_day = "Tuesday"
    elif (r==3):
        week_day = "Wednesday"
    elif (r==4):
        week_day = "Thursday"
    elif (r==5):
        week_day = "Friday"
    elif (r==6):
        week_day = "Saturday"

    print (" The day is " + week_day + ".")

               
    

    


main()

    
