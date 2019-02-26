import random

class TicTacToe:
    def __init__(self):
        self.player = player

    def drawBoard(self, board):

        print('   |   |')
        print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
        print('   |   |')

    def inputPlayerLetter(self):
        # Lets the player type which letter they want to be.
        # Returns a list with the player's letter as the first item, and the computer's letter as the second.
        letter = ''
        while not (letter == 'X' or letter == 'O'):
            print('Do you want to be X or O?')
            letter = input().upper()

        # the first element in the tuple is the player's letter, the second is the computer's letter.
        if letter == 'X':
            return ['X', 'O']
        else:
            return ['O', 'X']

    def whoGoesFirst(self):
        # Randomly choose the player who goes first.
        if random.randint(0, 1) == 0:
            return 'Player 1'
        else:
            return 'Player 2'

    def playAgain(self):
        # This function returns True if the player wants to play again, otherwise it returns False.
        print('Do you want to play again? (yes or no)')
        return input().lower().startswith('y')

    def makeMove(self, board, letter, move):
        board[move] = letter

    def isWinner(self, board, letter):
        # Given a board and a player's letter, this function returns True if that player has won.
        # We use bo = board and le = letter so we don't have to type as much.
        return ((board[7] == letter and board[8] == letter and board[9] == letter) or # across the top
        (board[4] == letter and board[5] == letter and board[6] == letter) or # across the middle
        (board[1] == letter and board[2] == letter and board[3] == letter) or # across the bottom
        (board[7] == letter and board[4] == letter and board[1] == letter) or # down the left side
        (board[8] == letter and board[5] == letter and board[2] == letter) or # down the middle
        (board[9] == letter and board[6] == letter and board[3] == letter) or # down the right side
        (board[7] == letter and board[5] == letter and board[3] == letter) or # diagonal
        (board[9] == letter and board[5] == letter and board[1] == letter)) # diagonal

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
        # Let the player type in his move.
        move = ' '
        while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
            print('What is your next move? (1-9)')
            move = input()
        return int(move)

    def isBoardFull(self, board):
        # Return True if every space on the board has been taken. Otherwise return False.
        for i in range(1, 10):
            if isSpaceFree(board, i):
                return False
        return True


p1 = TicTacToe(player1)
p2 = TicTacToe(player2)
print('Welcome to Tic Tac Toe!')

while True:
    # Reset the board
    theBoard = [' '] * 10
    p1Letter, p2Letter = p1.inputPlayerLetter()
    turn = p1.whoGoesFirst()
    print('The ' + turn + ' will go first.')
    gameIsPlaying = True

    while gameIsPlaying:
        if turn == 'player1':
            # Player's turn.
            p1.drawBoard(theBoard)
            move = p1.getPlayerMove(theBoard)
            p1.makeMove(theBoard, p1Letter, move)

            if p1.isWinner(theBoard, p1Letter):
                p1.drawBoard(theBoard)
                print('Hooray! You have won the game!')
                gameIsPlaying = False
            else:
                if p1.isBoardFull(theBoard):
                    p1.drawBoard(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'computer'

        else:
            # Computer's turn.
            move = p2.getPlayerMove(theBoard)
            makeMove(theBoard, p2Letter, move)

            if p2.isWinner(theBoard, p2Letter):
                p2.drawBoard(theBoard)
                print('The computer has beaten you! You lose.')
                gameIsPlaying = False
            else:
                if p2.isBoardFull(theBoard):
                    p2.drawBoard(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'player'

    if not playAgain():
        break
