#HomeWork7.1
#Connecting modules
from platform import machine, python_version, processor
with open('info.txt','w') as file:
    while True:
        str = input("Enter a command, please \n")
        if str == "version":
            file.write("Python version ", python_version(),"\n")
            print("Python version ", python_version())#python version
        elif str == "bit":
            file.write("Capacity of the machine", machine(),"\n")
            print("Capacity of the machine", machine())#bit depth
        elif str == "processor":
            file.write("Processor", processor(),"\n")
            print("Processor", processor())#model processor
        elif str == "Linux":
            print("Wow you makin'a hacker!")
        elif str == "exit":
                break # exit
        else:
            print("Invalid command")

#HomeWork7.2
