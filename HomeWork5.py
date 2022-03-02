# #HomeWork5.1
# #factorial function
# def fact(n):
#     sum = 1
#     if n < 0:
#         return None
#     elif n <= 1:
#         return 1
#     else:
#         for i in range(2, n+1):
#             sum *= i
#     return sum
# #Output of the factorial sum
# for i in range(-1,9):
#     print(fact(i))

# #HomeWork5.2
# # #Fibonacci function
# def fib(val):
#     f = [0,1,1]
#     if val < 1:
#         return None
#     elif val < 3:
#         return 1
#     else: 
#         for i in range(3, val):
#             f.append(f[i-2]+f[i-1])
#         ln = len(f)
#         return (f[ln-1] + f[ln-2])

# for i in range(-1,25):
#     print(fib(i))

#HomeWork5.3
import random
board = [i for i in range(1,10)]
print(board)
pcRes = 0
userRes = 0
def userMove():
    while True:
        userVal = int(input("Your move:"))
        if board.count(userVal) == 0:
            print("The cell is occupied")
        else:
            for i in range(0,9):
                    if board[i] == userVal:
                        board[i] = "O"
                        return
def pcMove():
    while True:
        pcVal = random.randrange(1,9)
        if board.count(pcVal) != 0:
            for i in range(0,9):
                if board[i] == pcVal:
                    board[i] = "X"
                    return
def checkResult():
    global pcRes
    global userRes
    #Horizontal check
    if (board[0] == board[1] == board[2] == "X") or (board[3] == board[4] == board[5] == "X") or (board[6] == board[7] == board[8] == "X"):
        pcRes += 1
    elif (board[0] == board[1] == board[2] == "O") or (board[3] == board[4] == board[5] == "O") or (board[6] == board[7] == board[8] == "O"):
        userRes += 1
    #Vertical check
    if (board[0] == board[3] == board[6] == "X") or (board[1] == board[4] == board[7] == "X") or (board[2] == board[5] == board[8] == "X"):
        pcRes += 1
    elif (board[0] == board[3] == board[6] == "O") or (board[1] == board[4] == board[7] == "O") or (board[2] == board[5] == board[8] == "O"):
        userRes += 1
    #Diagonal result
    if (board[2] == board[4] == board[6] == "X") or (board[0] == board[4] == board[8] == "X") :
        pcRes += 1
    elif (board[2] == board[4] == board[6] == "O") or (board[0] == board[4] == board[8] == "O"):
        userRes += 1
def dyspleyBoard():
    print("+-------" * 3,"+", sep="")
    for row in range(3):
        print("|       "*3, "|", sep="")
        for col in range(3):
            print("|   "+ str(board))
#The first move
board[4] = "X"
celling = len(board)
while celling > 1:
    userMove()
    print(board)
    pcMove()
    print(board)
    checkResult()
    celling -= 2
print(board)
print("Result PC = ",pcRes,"User = ",userRes, sep="|")
if userRes > pcRes:
    print("User Win")
elif pcRes > userRes:
    print("PC Win")
else:
    print("The result is a draw")
