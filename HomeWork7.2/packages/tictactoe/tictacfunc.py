import random
def userMove(board):
    while True:
        userVal = int(input("Your move: "))
        if board.count(userVal) == 0:
            print("The cell is occupied")
        else:
            for i in range(9):
                    if board[i] == userVal:
                        board[i] = "O"
                        return
def pcMove(board):
    while True:
        pcVal = random.randrange(1,10)
        print("PC move: ",pcVal)
        if board.count(pcVal) != 0:
            for i in range(9):
                if board[i] == pcVal:
                    board[i] = "X"
                    return
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