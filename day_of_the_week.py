# Program to fetch day of the week for a given date

def isLeapYear(year): 
    if(year%400 == 0):
        return True
    if(year%100 == 0):
        return False 
    if(year%4 == 0):
        return True 
    return False

def calculateDay(date, month, year):
    century_digits = year // 100
    year_digits = year % 100
    value = year_digits + year_digits//4

    if(century_digits == 18):
        value += 2
    elif(century_digits == 20):
        value += 6
    
    if(month == 1 and not isLeapYear(year)):
        value += 1
    elif(month == 2):
        if(isLeapYear(year)):
            value += 3
        else:
            value += 4
    elif(month == 3 or month == 11):
        value += 4
    elif(month == 5):
        value += 2
    elif(month == 6):
        value += 5
    elif(month == 8):
        value += 3
    elif(month == 10):
        value += 1
    elif(month == 9 or month == 12):
        value += 6
    
    value = (value + date) % 7

    if(value == 1):
        print("SUNDAY")
    elif(value == 2):
        print("MONDAY")
    elif(value == 3):
        print("TUESDAY")
    elif(value == 4):
        print("WEDNESDAY")
    elif(value == 5):
        print("THURSDAY")
    elif(value == 6):
        print("FRIDAY")
    elif(value == 0):
        print("SATURDAY")


if __name__ == '__main__':
    #Sample date
    date, month, year = 20,10,2021

    calculateDay(date, month, year)
