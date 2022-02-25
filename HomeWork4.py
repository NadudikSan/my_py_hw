# #Home work 3.1

hat_list = [1,2,3,4,5] #This is an existing list of numbers hidden in the hat
hat_list[int(len(hat_list)/2)] = int(input("Enter a value - 23"))
del hat_list[-1]
print("length of the existing list - ")
print(hat_list)

#Home work 3.2

#create an empty list 
beatles = []
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
#add of the band to the list
for i in range(2):
    beatles.append(input("Add "))
del beatles[-1]
del beatles[-1]
beatles.insert(0,"Ringo Starr")
print(beatles)

#Home work 3.3
valueList = []
marker = True
flagSort = int(input("Choose type of sort 1 - increased,-1 - reversed : "))
nVal = int(input("How many numbers do u want:")) 
if nVal > 0:
    for i in range(nVal):
        valueList.append(int(input(str(i+1)+" value - ")))
while marker:
    marker = False
    for val in range(len(valueList) - 1):
        if flagSort == 1:
            if valueList[val] > valueList[val+1]:
                valueList[val], valueList[val+1] = valueList[val+1], valueList[val]
                marker = True
        elif flagSort == -1:
            if valueList[val] < valueList[val+1]:
                valueList[val], valueList[val+1] = valueList[val+1], valueList[val]
                marker = True
print(valueList)
#Reverse list
valueList.reverse()
print(valueList)


#Home work 3.4

myList = [3,4,1,22,7,3,7,1]
newList = []
for val in myList:
    if val not in newList:
        newList.append(val)
print(newList.sort())

#Home work 3.5
strok = input("Put string of numbers by space ")
listStr = strok.split()
valStr = [int(val) for val in listStr]
print(listStr)
print(valStr)
print(sum(valStr))

#Home work 3.6
s = input("Put string of numbers by space ")
listNew = []
listStart = s.split()
listS = [int(val) for val in listStart]
tNum = 0
sizeList = len(listS)
for i in range(sizeList-1):
    tNum = 0
    for j in range(i+1,sizeList):
        if listS[i] == listS[j]:
            tNum += 1
    if tNum > 0:
        listNew.append(listS[i])
print(listNew.sort())

#Home work 3.7
strok = input("Put string of numbers by space ")
listStr = strok.split()
#Converting elements from a string to integers
valStr = [int(val) for val in listStr]
averageList = sum(valStr)/ len(valStr)
print("Average value = ", averageList)
print("Sum of elements = ", sum(valStr))

# #Home work 3.8
#The user enters the size of the list
valueOne = int(input("Enter the beginning of the intervals - "))
valueTwo = int(input("Enter the beginning of the intervals - "))
listUser = [i for i in range(valueOne,valueTwo + 1) if i % 3 == 0]
valueSr = sum(listUser)/len(listUser)
print("Elements ", listUser, "Average value - ", valueSr)