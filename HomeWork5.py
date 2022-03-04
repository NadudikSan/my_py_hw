#HomeWork5.1
#factorial function
def fact(n):
    sum = 1
    if n < 0:
        return None
    elif n <= 1:
        return 1
    else:
        for i in range(2, n+1):
            sum *= i
    return sum
#Output of the factorial sum
for i in range(-1,9):
    print(fact(i))

#HomeWork5.2
# #Fibonacci function
def fib(val):
    f = [0,1,1]
    if val < 1:
        return None
    elif val < 3:
        return 1
    else: 
        for i in range(3, val):
            f.append(f[i-2]+f[i-1])
        ln = len(f)
        return (f[ln-1] + f[ln-2])

for i in range(-1,25):
    print(fib(i))

#HomeWork5.3
import random
board = [i for i in range(1,10)]
pcRes = 0
userRes = 0
def userMove():
    while True:
        userVal = int(input("Your move: "))
        if board.count(userVal) == 0:
            print("The cell is occupied")
        else:
            for i in range(9):
                    if board[i] == userVal:
                        board[i] = "O"
                        return
def pcMove():
    while True:
        pcVal = random.randrange(1,10)
        print("PC move: ",pcVal)
        if board.count(pcVal) != 0:
            for i in range(9):
                if board[i] == pcVal:
                    board[i] = "X"
                    return
def checkResult():
    global pcRes
    global userRes
    #Horizontal check
    for i in range(0,9,3):
        if board[i] == board[i+1] == board[i+2] == "X":
            pcRes += 1
        elif board[i] == board[i+1] == board[i+2] == "O":
            userRes += 1
    #Vertical check
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] == "X":
            pcRes += 1
        elif board[i] == board[i+3] == board[i+6] == "O":
            userRes += 1
    #Diagonal result
    if (board[2] == board[4] == board[6] == "X"):
        pcRes += 1
    elif (board[0] == board[4] == board[8] == "X"):
        pcRes += 1
    if (board[2] == board[4] == board[6] == "O"):
        userRes += 1
    elif (board[0] == board[4] == board[8] == "O"):
        userRes += 1
def displayBoard(board):
    print("+-------" * 3,"+", sep="")
    c=0
    for row in range(3):
        print("|       "*3, "|", sep="")
        for col in range(3):
            print("|   "+ str(board[c]) + "   ", end="")
            c += 1
        print("|")
        print("|       " * 3, "|", sep="")
        print("+-------" * 3, "+", sep="")
        
#The first move
board[4] = "X"
celling = len(board)
displayBoard(board)
while celling >= 2:
    userMove()
    displayBoard(board)
    pcMove()
    displayBoard(board)
    celling -= 2
checkResult()
print("Result PC = ",pcRes,"User = ",userRes,"|", sep="|")
if userRes > pcRes:
    print("User Win")
elif userRes < pcRes:
    print("PC Win")
else:
    print("The result is a draw")

#HomeWork5.4
import time
messageUser = input("Enter message:")
with open('note.txt','w') as file:
    while messageUser != "end":
        named_tuple = time.localtime() # receive struct_time
        time_string = time.strftime("%m/%d/%Y, %H:%M:%S", named_tuple)
        file.write(time_string +" "+ messageUser+"\n" )
        messageUser = input("Enter message:")
