year = int(input("Please enter a year: "))
if(year%100==0 and year%400!=0):
    print(str(year) +" is not a leap year")
elif(year%4==0): 
    print(str(year) +" is a leap year")
else:
    print(str(year) +" is not a leap year")