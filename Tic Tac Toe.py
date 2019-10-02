#Tic Tac Toe - Basic 3x3 Board. Players will play in turns.

#Random Module to make Computer randomly choose the position to place.
from random import *

def row_check(board, player):
    ''' Checks if all the postions are filled with the player symbol same row-wise. '''
    for i in range(3):
        if (board[i][0] == player) and (board[i][1] == player) and (board[i][2] == player):
            return 1
    return 0


def col_check(board, player):
    ''' Checks if all the postions are filled with the player symbol same column-wise. '''
    for j in range(3):
        if (board[0][j] == player) and (board[1][j] == player) and (board[2][j] == player):
            return 1
    return 0


def diagonal_check(board, player):
    ''' Checks if all the postions are filled with the player symbol same diagonally. '''
    if ((board[0][0] == player) and (board[1][1] == player) and (board[2][2] == player)) or ((board[0][2] == player) and (board[1][1] == player) and (board[2][0] == player)):
        return 1
    return 0


def print_board(board):
    ''' Prints the Tic-Tac-Toe Board.'''
    for i in range(3):
        for j in range(3):
            print(board[i][j], end= "   ")
        print(end="\n\n")
    

def winner_check(board, player):
    ''' Checks if there are all same symbols ['X' or 'O'] across diagonals, columns and rows.'''
    if 1 in (row_check(board, player), col_check(board, player), diagonal_check(board, player)):
        return True
    return False



def tic_tac_toe_comp_player(board):
    '''Main Logic of the Game in Computer vs Player Mode. '''
    turns = 9

    #Visited array to mark as visited
    visited = [x for x in range(turns)]

    #Computer's Symbol
    comp = 'X'
    #Player's Symbol
    player = 'O'

    #Dictionary that stores the Integers[0-8] and maps them to the locations of the matrix [Tic Tac Toe Board].
    d = {0 :[0,0], 1: [0,1], 2: [0,2], 3: [1,0], 4: [1,1], 5: [1,2], 6: [2,0], 7: [2,1], 8: [2,2]}

    #A 3x3 tic-tac-toe game will take atmost 9 moves to know if it was a Tie or not.
    chances = 0

    while True:
        print('------------------------------ Computer\'s Turn --------------------------------')
        ch = visited[randrange(0,len(visited))] if len(visited) > 1 else visited[0]
        print('Computer\'s Choice: {}'.format(ch))
        
        #Setting the position given by the Computer with its symbol
        board[d[ch][0]][d[ch][1]] = comp
        visited.remove(ch)
        print('\n')

        #To print board after every move
        print_board(board)
        chances += 1

        #Check if there is a possibility of winning the game
        if winner_check(board, comp):
            print('Computer Won the Game.')
            return '=========================== Game Over! ============================'

        #Break out of the loop when number crosses 9 {That's when we know if there is a Tie}
        if chances >= 9:
            break
        
    
        print('****************************** Player\'s Turn *********************************')
        print(visited)
        ch1 = int(input('Choose a position from the above available list: '))

        #Setting the position given by the user with his symbol
        board[d[ch1][0]][d[ch1][1]] = player
        visited.remove(ch1)
        print('\n')

        #To print board after every move
        print_board(board)
        chances += 1

        #Check if there is a possibility of winning the game
        if winner_check(board, player):
            print('Second Player Won the Game.')
            return '=========================== Game Over! ============================'
            
        #Break out of the loop when the number of turns crosses 9
        if chances >= 9:
            break
        
    return '+++++++++++++++ Game Draw!!! +++++++++++++++++'




def tic_tac_toe_2_players(board):
    ''' Main Logic of Tic-Tac-Toe Game goes here. Player vs Player Mode. '''
    turns = 9

    #Visited array to mark as visited
    visited = [x for x in range(turns)]

    #First Player's Symbol
    fp = 'X'
    #Second Player's Symbol
    sp = 'O'

    #Dictionary that stores the Integers[0-8] and maps them to the locations of the matrix [Tic Tac Toe Board].
    d = {0 :[0,0], 1: [0,1], 2: [0,2], 3: [1,0], 4: [1,1], 5: [1,2], 6: [2,0], 7: [2,1], 8: [2,2]}

    #A 3x3 tic-tac-toe game will take atmost 9 moves to know if it was a Tie or not.
    chances = 0

    while True:
        print('------------------------------ First Player Turn --------------------------------')
        print(visited)
        ch = int(input('Choose a position from the above available list: ')) if len(visited) > 1 else visited[0]

        #Setting the position given by the user with his symbol
        board[d[ch][0]][d[ch][1]] = fp
        visited.remove(ch)
        print('\n')

        #To print board after every move
        print_board(board)
        chances += 1

        #Check if there is a possibility of winning the game
        if winner_check(board, fp):
            print('First Player Won the Game.')
            return '=========================== Game Over! ============================'

        #Break out of the loop when number crosses 9 {That's when we know if there is a Tie}
        if chances >= 9:
            break
        
    
        print('****************************** Second Player Turn *********************************')
        print(visited)
        ch1 = int(input('Choose a position from the above available list: ')) if len(visited) > 1 else visited[0]

        #Setting the position given by the user with his symbol
        board[d[ch1][0]][d[ch1][1]] = sp
        visited.remove(ch1)
        print('\n')

        #To print board after every move
        print_board(board)
        chances += 1

        #Check if there is a possibility of winning the game
        if winner_check(board, sp):
            print('Second Player Won the Game.')
            return '=========================== Game Over! ============================'
            
        #Break out of the loop when the number of turns crosses 9
        if chances >= 9:
            break
        
    return '++++++++++++++ Game Draw!!! +++++++++++++++++' 
        
        
    

''' Driver Code for Tic-Tac-Toe Game. '''
board = [['_' for i in range(3)] for j in range(3)]
while True:
    option = input('Choose a Game Mode: \n1. Computer vs Player\t\t2. Player vs Player \n')
    if option not in (1, 2, '1', '2'):
        print('Please Choose one of the Two Options.')
    else:
        break

if int(option) == 2:
    print(tic_tac_toe_2_players(board))
elif int(option) == 1:
    print(tic_tac_toe_comp_player(board))
    








'''
-- First player is 'X' and the other is 'O'.
-- User Should give a number [0-8] that denotes the cell number.
-- Maintain a visited array [0-8] and mark it as visited, for all the numbers that the players had chosen earlier
   such that already existing 'O' and 'X' are not altered.



1. Two Modes --> Computer vs Player and Player1 vs player2
2. For Computer, use random module and place either 'O' or 'X' at a random AVAILABLE position.
3. For Two Players, make turns and take their input.
4. Print the Board after every turn.


5. Extend the game to more than 3x3 board i.e, write code for tic-tac-toe on a NxN board.
'''