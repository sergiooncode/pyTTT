import random
import time
import pdb

HUMAN_TOKEN = "X"
COMPUTER_TOKEN = "O"
INFINITY = 1000000

def init_board():
    board = []
    for i in range(9):
        board.append('-')
    return board 

def show_board(b):
    # Shows the board list row by row
    print "     __     __     __  "
    print " "
    for k in range(3):
        print "  |  ",
        for j in range(3):
            print b[j + 3*k] + "  |  ",
        print " "
        print "     __     __     __  "
        print " "
        
def show_board_coord():
    # Shows the board list row by row
    print "     __     __     __  "
    print " "
    for k in range(3):
        print "  |  ",
        for j in range(3):
            print str(j + 3*k + 1) + "  |  ",
        print " "
        print "     __     __     __   "
        print " "

def makeMove(brd, move, cp):
    b = []
    for l in range(9):
        b.append(brd[l])
    if cp == 1:
        b[move] = HUMAN_TOKEN
    else:
        b[move] = COMPUTER_TOKEN
    return b

def getMoves(brd):
    moves = []
    for k in range(9):
        if brd[k] == '-':
            moves.append(k)
    random.shuffle(moves)
    return moves 

def isGameover(board, cp):
    return evaluate(board, cp) != None

def evaluate(board, cp):
    winner = check_for_winner(board)
    if cp == 1: 
        cpl = HUMAN_TOKEN
        opl = COMPUTER_TOKEN
    if cp == 2: 
        cpl = COMPUTER_TOKEN
        opl = HUMAN_TOKEN 
    if winner == cpl:
        return INFINITY
    elif winner == opl:
        return -INFINITY
    elif check_if_filled(board):
        return 0

def negamax(board, currentPlayer, maxDepth, currentDepth):
    if is_gameover(board) or currentDepth == maxDepth:
        return evaluate(board, currentPlayer), None
    bestMove = None
    bestScore = -INFINITY
    if currentPlayer == 2:
        otherPlayer = 1
    else:
        otherPlayer = 2
    for move in getMoves(board):
        newBoard = makeMove(board, move, currentPlayer)
        recursedScore, currentMove = negamax(newBoard, otherPlayer, maxDepth, currentDepth + 1)
        currentScore = -recursedScore
        if currentScore > bestScore:
            bestScore = currentScore
            bestMove = move
    return bestScore, bestMove

def get_random_move(b):
    k = random.randint(0, 8) 
    while b[k] != '-':
        k = random.randint(0, 8)
    return k

def get_computer_move(b):
    maxDepth = 9
    cp = 2
    score, move = negamax(b, cp, maxDepth, 0)
    if move == None:
        move = get_random_move(b)
        print "Since move == None, the best move to make is:"
        print score, move+1
        return move
    print "Best move to make is:"
    print score, move+1
    return move

def get_human_move(b):
    m = int(raw_input())
    while b[m - 1] != '-':
        print "Human player, please enter a valid move:"
        m = int(raw_input())
    return m - 1

def check_rows(b):
    i = 0
    while i < 9:
        if b[i] != '-' and b[i] == b[i + 1] and b[i] == b[i + 2]: 
            return b[i]
        i = i + 3
    return -1

def check_columns(b):
    if b[0] != '-' and b[0] == b[3] and b[0] == b[6]: 
        return b[0]
    if b[1] != '-' and b[1] == b[4] and b[1] == b[7]: 
        return b[1]
    if b[2] != '-' and b[2] == b[5] and b[2] == b[8]: 
        return b[2]
    return -1

def check_diagonals(b):
    i = 0
    if b[i] != '-' and b[i] == b[i + 4] and b[i] == b[i + 8]: 
        return b[i]
    i = i + 6
    if b[i] != '-' and b[i] == b[i - 2] and b[i] == b[i - 4]: 
        return b[i]
    return -1    

def check_if_filled(b):
    c = True
    for t in b:
        if t == "-":
            c = False
    return c 

def change_turn(ct):
    # ct = 1 means was turn of human player, if 2 it was turn of computer player
    if ct == 1:
        return 2
    else:
        return 1

def check_for_winner(b):
    if check_rows(b) != -1:
        return check_rows(b) 
    if check_columns(b) != -1:
        return check_columns(b)
    if check_diagonals(b) != -1:
        return check_diagonals(b) 
    
def is_gameover(b):
    if check_rows(b) != -1 or check_columns(b) != -1 or check_diagonals(b) != -1:
        return True
    if check_if_filled(b):
        return True 
    return False

def set_square(value, b, m):
    b[m] = value
    return b

if __name__ == '__main__':
    turn = 0
    current_player = random.choice([1, 2])
    bd = init_board()
    print "Human player, please enter your moves using the numbers shown next:"
    show_board_coord()
    while not is_gameover(bd):
        if current_player == 1:
            print "Human player, please enter your next move:"
            mv = get_human_move(bd)
            bd = set_square(HUMAN_TOKEN, bd, mv)
            turn = turn + 1
            print "The turn number is: " + str(turn)
            show_board(bd)
            current_player = change_turn(current_player)
        else:
            print "Computer player is thinking its next move..."
            time.sleep(0.5)
            cm = get_computer_move(bd)
            bd = set_square(COMPUTER_TOKEN, bd, cm)
            turn = turn + 1
            print "The turn number is: " + str(turn)
            show_board(bd)
            current_player = change_turn(current_player)
             
    if check_if_filled(bd):
        result = 3
    else:
        result = change_turn(current_player)
       
    if result == 1:
        print "Game Over. The human player won."
    if result == 2:
        print "Game Over. The computer player won."
    if result == 3:
        print "Game Over. It was a tie."
    
    
    
    
