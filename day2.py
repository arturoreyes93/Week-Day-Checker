def main():

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
    is_leap = ((year%4==0) and (not(year%100==0))

               
    if ( (month==1) or (month==3) or (month==5) or (month==7) or (month==8) or (month==10) or (month==12) ) :
               num_days=31
               elif ((month==4) or (month==6) or (month==9) or (month==11)):
               num_days=30
               elif (month==2):
               num_days=28
               
    a = month
    if (month==1):
               a = 13
               elif (month==2):
               a = 14
               else
               a= month-2
    b = day
    c = (year%1000)%100
    d = year//1000

    w = (13*a-1)//5
    x=c//4
    y=d//4
    z=w+x+y+b+c-2*d
    r=z%7
    r=(r+7)%7 #to take the negative values of r

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

    print (" The day is" + week_day + ".")

               
    

    


main()

    
