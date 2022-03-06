try:
    value = int(input("Enter a natural number - "))
    print("The reciprocal of", value " is ", 1/value)
    
except ValueError:
    print("I do not know what to do.")
except ZeroDivisionError:
    print("Division by zero")
except:
    print("Somethung strange has happened here....")

temperature = float(input("Enter current temperature :"))
if temperature > 0:
    print("Above zero")
elif temperature < 0:
    prin("Below zero")
else:
    print("Zero")

while True:
    try:
        number = int(input("Enter an integer"))
        print(number / 2)
        break
    except:
        print("Warning: the value entered is not a valid number.")
