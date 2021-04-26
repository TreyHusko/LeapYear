# series of if/else statements to determine if input year is leap year 
def isLeapYear(year):
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                print(str(year) + " is a leap year")
            else: 
                print (str(year) + " is not a leap year")
        else: 
            print (str(year) + " is a leap year")
    else: 
        print (str(year) + " is not a leap year")

# get a number from the user giving error if not int, repeat until valid integer received 
def getNumber(message):
    while True:
        try:
            userNum = int(input(message))
        except ValueError:
            print("Not a valid integer year! Try Again!")
            continue
        else:
            return userNum
            break
#Main 

numYear = getNumber("Enter a year to see if it's a leap year: ")
isLeapYear(numYear)

