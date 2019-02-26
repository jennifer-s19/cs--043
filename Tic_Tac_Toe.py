# Tic Tac Toe

import random

class TicTacToe:
    def drawBoard(self,board):
        print('    |   |')
        print('  '  + board[7] + ' | ' + board[8] + ' | ' + board[9])
        print('    |   |  ')
        print('-------------')
        print('    |   |')
        print('  ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
        print('    |   | ')
        print('-------------')
        print('    |   |')
        print('  ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
        print('    |   |  ')


    def inputPlayerLetter(self):
        letter = ''
        while not (letter == 'X' or letter == 'O'):
            print('Do you want to be X or O?')
            letter = input().upper()
        if letter == 'X':
            return ['X', 'O']
        else:
            return ['O', 'X']

    def whoGoesFirst(self):
        if random.randint(0, 1) == 0:
            return 'Player 1'
        else:
            return 'Player 2'

    def playAgain(self):
        print('Do you want to play again? (yes or no)')
        return input().lower().startswith('y')

    def makeMove(self, board, letter, move):
        board[move] = letter

    def isWinner(self, bo, le):
        return ((bo[7] == le and bo[8] == le and bo[9] == le) or # across the top
        (bo[4] == le and bo[5] == le and bo[6] == le) or # across the middle
        (bo[1] == le and bo[2] == le and bo[3] == le) or # across the bottom
        (bo[7] == le and bo[4] == le and bo[1] == le) or # down the left side
        (bo[8] == le and bo[5] == le and bo[2] == le) or # down the middle
        (bo[9] == le and bo[6] == le and bo[3] == le) or # down the right side
        (bo[7] == le and bo[5] == le and bo[3] == le) or # diagonal
        (bo[9] == le and bo[5] == le and bo[1] == le)) # diagonal

    def getBoardCopy(self, board):
        # Make a duplicate of the board list and return it the duplicate.
        dupeBoard = []
        for i in board:
            dupeBoard.append(i)
        return dupeBoard

    def isSpaceFree(self, board, move):
        # Return true if the passed move is free on the passed board.
        return board[move] == ' '

    def getPlayerMove(self, board):
        # Let the player type in their move.
        move = ' '
        while move not in '1 2 3 4 5 6 7 8 9'.split() or not play.isSpaceFree(board, int(move)):
            print('What is your next move?\n (7, 8, 9 \n 4, 5, 6, \n 1, 2, 3)')
                                           
            move = input()
        return int(move)

    def isBoardFull(self, board):
        for i in range(1, 10):
            if play.isSpaceFree(board, i):
                return False
        return True

    def rules(self):
        answer = ''
        print('Do you want to read the rules? (yes or no)')
        answer = input().lower()
        if answer == 'yes':
            print('Tic Tac Toe is a two-player game where each player\'s move is portrayed by either X or O and players take alternating turns.\n Your objective is to get three in a row, column, or diagonal with either three X\'s or O\'s before your oponent. \nTo make your move you will have to select a number that corresponds to a spot on the nine square grid. \nThere will be a smaller version of the grid to help you understand which number corresponds to which space.')
        else:
            print('Good luck!')



        
            
    


print('WELCOME TO TIC TAC TOE!')
print()


play = TicTacToe()

while True:
    # Reset the board
    theBoard = [' '] * 10
    play.rules()
    print()
    player1Letter, player2Letter = play.inputPlayerLetter()
    turn = play.whoGoesFirst()
    print(turn + ' will go first.')
    gameIsPlaying = True

    while gameIsPlaying == True:
        if turn == 'Player 1':
            play.drawBoard(theBoard)
            print("TURN: PLAYER 1")
            move = play.getPlayerMove(theBoard)
            print()
            play.makeMove(theBoard, player1Letter, move)
            if play.isWinner(theBoard, player1Letter):
                play.drawBoard(theBoard)
                print('Hooray! Player 1 you have won the game!')
                gameIsPlaying = False
            else:
                if play.isBoardFull(theBoard):
                    play.drawBoard(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'Player 2'

        else:
            play.drawBoard(theBoard)
            print("TURN: PLAYER 2")
            move2 = play.getPlayerMove(theBoard)
            play.makeMove(theBoard, player2Letter, move2)
            if play.isWinner(theBoard, player2Letter):
                play.drawBoard(theBoard)
                print('Hooray! Player 2 you have won the game!')
                gameIsPlaying = False
            else:
                if play.isBoardFull(theBoard):
                    play.drawBoard(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'Player 1'
    if not play.playAgain():
        break
