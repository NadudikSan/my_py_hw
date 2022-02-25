#Homework 2.0
print("Homework 2.0")
print("Hello, Python!")
print("Hello, Alexandr\n")

#Homework 2.1
print("Homework 2.1")
print("Programming", "Essentials", "in",sep="***",end="...")
print("Python\n")

#Homework 2.2
print("\nHomework 2.2")
print("     *\n", "   * *\n", "  *   *\n", " *     *\n", "***   ***\n", "  *   *\n", "  *   *\n",  "  *****")
print("     *", "   * *", "  *   *", " *     *", "***   ***", "  *   *", "  *   *",  "  *****", sep="\n ")

#Homework 2.2*
print("    *", "     *", sep="       ")
print("   * *", "   * *", sep="       ")
print("  *   *", "  *   *", sep="      ")
print(" *     *", " *     *", sep="     ")
print("***   ***", "***   ***", sep="    ")
print("  *   *", "  *   *", sep="      ")
print("  *   *", "  *   *", sep="      ")
print("  *****", "  *****", sep="      ")

#Homework 2.2**
print("    *\n   * *\n  *   *\n *     *")
print(3 * "*", 3 * "*", sep="   ")
print("  *   *\n  *   *\n  *****")

#Homework 2.3
print("\nHomework 2.3")
print("\"I'm\"", "\"\"learning\"\"", "\"\"Python\"\"", sep="\n")

#Homework 2.4
print("\nHomework 2.4")
john, mary, adam = 3, 45, 12
print(john, mary, adam, sep=", ")
print("john = ", john, ", mary = ", mary, ", adam = ", adam,)
total_apples = john + mary + adam
print("Total: ", total_apples)

#Homework 2.5
print("\nHomework 2.5")
d = 1.61
km = 12.25
ml = 7.38
print(ml, "miles is ", round(ml*d,2))
print(km, "kilometers is ", round(km/d,2))

#Homework 2.6
print("\nHomework 2.6")
x = 0
y = (3 * x ** 3 - 2  *x ** 2 + 3 * x - 1)
print(" x = 0\n y = ", float(y))
x = 1
y = (3 * x ** 3 - 2  *x ** 2 + 3 * x - 1)
print(" x = 1 \n y = ", float(y))
x = -1
y = (3 * x ** 3 - 2  * x ** 2 + 3 * x - 1)
print(" x = -1 \n y = ", float(y))
x = int(input("Enter x \ n"))
y = (3 * x ** 3 - 2  *x ** 2 + 3 * x - 1)
print(" x = ", x, "\n y = ", float(y))

#Homework 2.7
print("\nHomework 2.7")
#this program computes the number of seconds in a given number of hours
# this program has been written two days ago
a = 3 # number of hours
seconds = 3600 # number of seconds in 1 hour
print("Hours: ", a) #printing the number of hours
print("Seconds in Hours: ", a * seconds) # printing the number of seconds in a given number of hours
#here we should also print "Goodbye", but a programmer didn't have time to write any code
#this is the end of the program that computes thenumber of seconds in 3 hour

#Homework 2.8
print("\nHomework 2.8")
firstData = int(input("Enter first number - "))
typeOperation = input("Enter type of operation ")
secondData = int(input("Enter second number - "))
if typeOperation == "+":
    print("Result = ", firstData + secondData)
elif typeOperation == "-":
    print("Result = ", firstData - secondData)
elif typeOperation == "/":
    print("Result = ", firstData / secondData)
elif typeOperation == "*":
    print("Result = ", firstData * secondData)
elif typeOperation == "**":
    print("Result = ", firstData ** secondData)
elif typeOperation == "//":
    print("Result = ", firstData // secondData)
elif typeOperation == "%":
    print("Result = ", firstData % secondData)
#Homework 2.9
print("\nHomework 2.9")
x = 6
y = 1 / (x + (1 / (x + (1 / (x + 1 / x)))))
print(y)

#Homework 2.10
print("\nHomework 2.10")
print("Hello World")

#Homework 2.11
print("\nHomework 2.11")
oneRet = 11111
twoRet = 1111111
totalRet = oneRet + twoRet
print("Total", totalRet)

#Homework 2.12
print("\nHomework 2.12")
denominator = 4 + 2 *(-2)
if denominator != 0:
    print("Value = ",42 / denominator)

#Homework 2.13
print("\nHomework 2.13")
print("= ", 2014 ** 14)

#Homework 2.14
print("\nHomework 2.14")
days = 30
hours = 24 * days  
seconds = 3600 # number of seconds in 1 hour
print("Hours: ", hours) #printing the number of hours
print("Seconds in month: ", hours * seconds)

#Homework 2.15
print("\nHomework 2.15")
print("= ", float(2014 ** 14))