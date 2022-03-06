def mysplit(str):
    myList = []
    newStr = ""
    for i in str:
        if i.isspace() != True:
            newStr += i
        else:
            myList.append(newStr)
            newStr = ""
    myList.append(newStr)    
    return myList