#HomeWork7.2
from sys import path
path.append("D:\\Proects\\my_py_hw\\HomeWork7.2")
pcRes = 0
userRes = 0
from packages.tictactoe.tictacfunc import *
def checkResult(board):
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
board = [i for i in range(1,10)]
#The first move
board[4] = "X"
celling = len(board)
displayBoard(board)
while celling >= 2:
    userMove(board)
    displayBoard(board)
    pcMove(board)
    displayBoard(board)
    celling -= 2
checkResult(board)
print("Result PC = ",pcRes,"User = ",userRes,"|", sep="|")
if userRes > pcRes:
    print("User Win")
elif userRes < pcRes:
    print("PC Win")
else:
    print("The result is a draw")