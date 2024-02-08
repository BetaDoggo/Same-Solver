import random

aMoves = []
bMoves = []
cMoves = []
dMoves = []
eMoves = []
fMoves = []
gMoves = []
hMoves = []

def convert(move): #converts the leters into human readable format
    if (move == "a"):
        Hmove = "Top-Left"
    if (move == "b"):
        Hmove = "Top-Middle"
    if (move == "c"):
        Hmove = "Top-Right"
    if (move == "d"):
        Hmove = "Middle-Left"
    if (move == "e"):
        Hmove = "Middle"
    if (move == "f"):
        Hmove = "Middle-Right"
    if (move == "g"):
        Hmove = "Bottom-Left"
    if (move == "h"):
        Hmove = "Bottom-Middle"
    if (move == "i"):
        Hmove = "Bottom-Right"
    return(Hmove)
    

def flip(num):
    if (num == "0"):
        num = "1"
    else:
        num = "0"
    return(num)

def step(Lboard, move):
    if (move == "a"):
        Lboard[0] = flip(Lboard[0])
        Lboard[1] = flip(Lboard[1])
        Lboard[3] = flip(Lboard[3])
    elif (move == "b"):
        Lboard[0] = flip(Lboard[0])
        Lboard[1] = flip(Lboard[1])
        Lboard[2] = flip(Lboard[2])
        Lboard[4] = flip(Lboard[4])
    elif (move == "c"):
        Lboard[1] = flip(Lboard[1])
        Lboard[2] = flip(Lboard[2])
        Lboard[5] = flip(Lboard[5])
    elif (move == "d"):
        Lboard[0] = flip(Lboard[0])
        Lboard[3] = flip(Lboard[3])
        Lboard[6] = flip(Lboard[6])
        Lboard[4] = flip(Lboard[4])
    elif (move == "e"):
        Lboard[1] = flip(Lboard[1])
        Lboard[3] = flip(Lboard[3])
        Lboard[4] = flip(Lboard[4])
        Lboard[5] = flip(Lboard[5])
        Lboard[7] = flip(Lboard[7])
    elif (move == "f"):
        Lboard[2] = flip(Lboard[2])
        Lboard[4] = flip(Lboard[4])
        Lboard[5] = flip(Lboard[5])
        Lboard[8] = flip(Lboard[8])
    elif (move == "g"):
        Lboard[3] = flip(Lboard[3])
        Lboard[6] = flip(Lboard[6])
        Lboard[7] = flip(Lboard[7])
    elif (move == "h"):
        Lboard[4] = flip(Lboard[4])
        Lboard[6] = flip(Lboard[6])
        Lboard[7] = flip(Lboard[7])
        Lboard[8] = flip(Lboard[8])
    elif (move == "i"):
        Lboard[5] = flip(Lboard[5])
        Lboard[7] = flip(Lboard[7])
        Lboard[8] = flip(Lboard[8])
    else:
        print("failed")
    return(Lboard)

def brute(): #brute force method
    target = 5
    steps = target + 1
    board = Startboard
    Listboard = list(board)
    moves = ["a","b","c","d","e","f","g","h","i"]
    sequence = ""
    attempts = 0
    while (steps > target):
        attempts = attempts + 1
        steps = 0
        sequence = ""
        board = Startboard
        Listboard = list(board)
        while (board != "000000000" and board != "111111111"):
            move = moves[random.randint(0,8)]
            Listboard = step(Listboard,move)
            board = "".join(Listboard)
            sequence = sequence + " | " + convert(move)
            steps = steps + 1
    print("Attempts: " + str(attempts))
    print("Steps: " + str(steps))
    print("Sequence: " + str(sequence))

def method1():    
    board = "000000000"
    Listboard = list(board)
    moves = ["a","b","c","d","e","f","g","h","i"]
    oneStep = []

    for move in moves:
        print(move)
        newboard = step(Listboard,move)
        if (move == "a"):
            aMoves.append(newboard)
        if (move == "b"):
            bMoves.append(newboard)
        if (move == "c"):
            cMoves.append(newboard)
        if (move == "d"):
            dMoves.append(newboard)
        if (move == "e"):
            eMoves.append(newboard)
        if (move == "f"):
            fMoves.append(newboard)
        if (move == "g"):
            gMoves.append(newboard)
        if (move == "h"):
            hMoves.append(newboard)
        if (move == "i"):
            iMoves.append(newboard)  
    print(oneStep)

#method1() # not working yet
print("Enter the value of each tile from left to right. ex: 100110111")
while True:
    Startboard = input("Enter the starting board: ")
    if (len(Startboard) != 9):
        print("Your board is the wrong size, it should be 9 digits. ex: 100110111")
    else:    
        brute()