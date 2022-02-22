#Homework 3.1
#Write numbers
numOne, numTwo, numThree, numFour = 12, -4, 22, 9 
numberCell = numOne
#Choose the larger number
if numberCell <= numTwo:
    numberCell = numTwo
else:
    if numberCell <= numThree:
        numberCell = numThree
if numberCell <= numFour:
     numberCell = numFour
print("the largest numbers = ",numberCell)

#Homework 3.2
#Write numbers
numOne, numTwo, numThree, numFour,numFive, numSix = 129, -90, 2, 9, 22, 613 
numMax,numMin = numOne,0
#Choose the larger number
if numMax <= numTwo:
    numMax = numTwo
else:
    if numMax <= numThree:
        numMax = numThree
if numMax <= numFour:
     numMax = numFour
else:
    if numMax <= numFive:
        numMax = numFive
if numMax <= numSix:
    numMax = numSix

if numOne > numTwo:
    numMin = numTwo
else:
    numMin = numOne
if numMin > numThree:
    numMin = numThree
if numMin > numFour:
     numMin = numFour
if numMin > numFive:
    numMin = numFive
if numMin > numSix:
    numMin = numSix
print("the largest numbers = ",numMax,"the small numbers = ",numMin)
#Using functions min and max
print ("the largest numbers = ", max(numOne, numTwo, numThree, numFour,numFive, numSix),end=" ")
print ("the small numbers = ", min(numOne, numTwo, numThree, numFour,numFive, numSix))

#Homework 3.3
stringTru = "Spathiphyllum"
stringFalse = "spathiphyllum"
stringCell = input("Enter name ")
if stringCell == stringTru:
    print("Yes - Spathiphyllum is the best plant ever!")
elif stringCell == stringFalse:
    print( "No, I want a big Spathiphyllum!")
else:
    print("Spathiphyllum! Not "+ stringCell +"!")

#Homework 3.4
userWallet = float(input("Enter your profit - "))
userCash = userWallet - userWallet*0.15
print("Your income is tax-free", round(userCash,2),"Your tax-free",round(userWallet*0.15,2))


#Homework 3.5
#Read year
nowYear = int(input("Enter year "))
if (nowYear < 1800) or (nowYear > 2020):
    print("Invalid year")
else:
    if nowYear % 4 != 0:
        print("Common year")
    else: 
        if nowYear % 100 != 0:
            print("Leap year")
        else:
            if nowYear % 400 != 0:
                print("Common year")
            else:
                print("Leap year")

#Homework 3.6
num = int(input("Enter number "))
numFocus = 4
while num != numFocus:
    print("Ha ha! You're stuck in my loop!")
    num = int(input("Enter number "))
print("Well done, muggle! You are free now.", numFocus)

#Homework 3.7
import time

for i in range(5):
    if i == 0:
        print("one Mississippi")
    elif i == 1:
        print("two Mississippi")
    elif i == 2:
        print("three Mississippi")
    elif i == 3:
        print("four Mississippi")
    elif i == 4:
        print("five Mississippi")
    time.sleep(1)
print("Ready or not, here I come!")

#Homework 3.8

nameWild = "chupacabra"
nameUser = ""
while True:
    if nameWild!=nameUser:
        nameUser = input()
    else:
        break
        print("You've successfully left the loop.")

#Homework 3.9
strUser = input("Enter word - ")
strUser.upper()
for strI in strUser:
    if strI == "A":
        continue
    elif strI == "E":
        continue
    elif strI == "I":
        continue
    elif strI == "O":
        continue
    elif strI == "U":
        continue
    else:
        print(strI)

#Homework 3.10
strUser = input("Enter word - ")
word_without_vowels = ""
for strI in strUser:
    if strI == "A":
        continue
    elif strI == "E":
        continue
    elif strI == "I":
        continue
    elif strI == "O":
        continue
    elif strI == "U":
        continue
    else:
        word_without_vowels += strI.upper()
print(word_without_vowels)

#Homework 3.11

c0 = int(input("Enter number"))
if c0 < 0:
    print("Invalid numver")
else:
    while c0 != 1:
        if c0 % 2 == 0:
            c0 /= 2
        elif c0 % 2 != 0:
            c0 = 3 * c0 + 1
        print(c0)


#Homework 3.12
firstData = 0.0
secondData = 0.0
step = 0
typeOperation = input("Enter type of operation ")
while typeOperation !="exit":
    if typeOperation == "**":
        firstData = float(input("Enter number"))
        step = int(input("Enter degree"))
        print(firstData**step)
    elif typeOperation == "+":
        firstData = float(input("Enter one number"))
        secondData = float(input("Enter two number"))
        print(firstData+secondData)
    elif typeOperation == "-":
        firstData = float(input("Enter one number"))
        secondData = float(input("Enter two number"))
        print(firstData-secondData)
    elif typeOperation == "/":
        firstData = float(input("Enter one number"))
        secondData = float(input("Enter two number"))
        print(round((firstData/secondData),2))
    elif typeOperation == "*":
        firstData = float(input("Enter one number"))
        secondData = float(input("Enter two number"))
        print(round((firstData*secondData),2))
    elif typeOperation == "%":
        firstData = float(input("Enter one number"))
        secondData = float(input("Enter two number"))
        print(firstData%secondData)
    elif typeOperation == "//":
        firstData = float(input("Enter one number"))
        secondData = float(input("Enter two number"))
        print(firstData//secondData)