inputYear = input("Please enter a year: ")
try:
    year = int(inputYear)
except ValueError:
    print('\nThat is not a valid integer')
if(year%100==0 and year%400!=0):
    print(str(year) +" is not a leap year")
elif(year%4==0): 
    print(str(year) +" is a leap year")
else:
    print(str(year) +" is not a leap year")