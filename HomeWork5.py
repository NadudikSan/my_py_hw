#HomeWork4.1
firstData = 0.0
secondData = 0.0
def plus( first=0, second=0):
    print("additional = ", first+second)

def minus(first=0, second=0):
    print("difference = ", first-second)

def div(first=0, second=1):
    print("division = ", round((first / second), 2))
    
def multip(first=0, second=1):
    print("multiplication = ", round((first * second), 2))

def pow(first=1,step=1):
    print("exponentiation = ", first ** step)

def remain(first=1, second=1):
    print("remainder = ", firstData % secondData)

def fract(first=1, second=1):
    print("", firstData // secondData)

typeOperation = ""
while typeOperation !="exit":
    typeOperation = input("Enter type of operation ")
    if typeOperation == "**":
        firstData = float(input("Enter number - "))
        step = int(input("Enter degree"))
        pow(firstData,step)
    elif typeOperation == "+":
        firstData = float(input("Enter number - "))
        secondData = float(input("Enter two number - "))
        plus(firstData,secondData)
    elif typeOperation == "-":
        firstData = float(input("Enter number - "))
        secondData = float(input("Enter two number - "))
        minus(firstData,secondData)
    elif typeOperation == "/":
        firstData = float(input("Enter number - "))
        secondData = float(input("Enter two number - "))
        div(firstData,secondData)
    elif typeOperation == "*":
        firstData = float(input("Enter number - "))
        secondData = float(input("Enter two number - "))
        multip(firstData,secondData)
    elif typeOperation == "%":
        firstData = float(input("Enter number - "))
        secondData = float(input("Enter two number - "))
        remain(firstData,secondData)
    elif typeOperation == "//":
        firstData = float(input("Enter number - "))
        secondData = float(input("Enter two number"))
        fract(firstData,secondData)

#HomeWork4.2
#function body
def year_leap(nowYear):
    if (nowYear < 1800) or (nowYear > 2020):
        print("Invalid year")
    else:
        if nowYear % 4 != 0:
            return False
        else: 
            if nowYear % 100 != 0:
                return True
            else:
                if nowYear % 400 != 0:
                    return False
                else:
                    return True

#checking on the list
test_data = [1996, 2000, 2016, 1987]
test_results = [False, True, True, False]
for i in range (len(test_data)):
    yr = test_data[i]
    print(yr, "->", end="")
    result = year_leap(yr)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")

#HomeWork4.3
#function body
def year_leap(nowYear):
    if (nowYear < 1800) or (nowYear > 2020):
        print("Invalid year")
    else:
        if nowYear % 4 != 0:
            return False
        else: 
            if nowYear % 100 != 0:
                return True
            else:
                if nowYear % 400 != 0:
                    return False
                else:
                    return True
def in_monts(mon, year):
    monts = [31,28,31,30,31,30,31,31,30,31,30,31]
    leapMonts = [31,29,31,30,31,30,31,31,30,31,30,31]
    if mon > 0 and mon < 13:
        if year_leap(year) == True:
            return leapMonts[mon-1]
        elif year_leap(year) == False:
            return monts[mon-1]

#checking on the list
test_years = [1990, 2000, 2016, 1987]
test_monts = [2, 2, 1, 11]
test_results = [28,29,31,30]
for i in range (len(test_years)):
    yr = test_years[i]
    mo = test_monts[i]
    print(yr, mo, "->", end="")
    result = in_monts(mo, yr)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")

#HomeWork4.4
def year_leap(nowYear):
    if (nowYear < 1800) or (nowYear > 2020):
        print("Invalid year")
    else:
        if nowYear % 4 != 0:
            return False
        else: 
            if nowYear % 100 != 0:
                return True
            else:
                if nowYear % 400 != 0:
                    return False
                else:
                    return True

def day_year (year, mon, day):
    monts = [31,28,31,30,31,30,31,31,30,31,30,31]
    leapMonts = [31,29,31,30,31,30,31,31,30,31,30,31]
    sum = 0
    if mon > 0 and mon < 13:
        if year_leap(year) == True:
            for i in range(mon-1):
                sum += leapMonts[i]
            return sum + day
        elif year_leap(year) == False:
            for i in range(mon-1):
                sum += monts[i]
            return sum + day
print(day_year(2000, 12, 31))
print(day_year(2007, 11, 12))
print(day_year(2013, 5, 6))

#HomeWork4.5
finding prime numbers
def funcPrime(num):
    for i in range(2, (num//2)+1):
        if num % i == 0:
            return False
    return True

for i in range(1, 20):
    if funcPrime(i + 1) == True:
        print(i+1, end=" ")

#HomeWork4.6
def galon_litr(mile):
    km = 1.609344 * mile
    litre = 3.7854
    return round(((100*litre) / km), 2)

def litr_galone(litr):
    galone = litr / 3.7854
    mile = 100 / 1.609344
    return round(mile / galone,2)
print(galon_litr(60.3))
print(galon_litr(31.4))
print(litr_galone(3.9))
print(litr_galone(7.5))
