import random

first = 0
playerO = 'O'
playerX = 'X'

class TicTacToe:
   def __init__(self, board, move, letter):
       self.board = board
       self.move = move
       self.letter = letter

   def drawBoard(self):
       print('   |   |')
       print(' ' + self.board[7] + ' | ' + self.board[8] + ' | ' + self.board[9])
       print('   |   |')
       print('-----------')
       print('   |   |')
       print(' ' + self.board[4] + ' | ' + self.board[5] + ' | ' + self.board[6])
       print('   |   |')
       print('-----------')
       print('   |   |')
       print(' ' + self.board[1] + ' | ' + self.board[2] + ' | ' + self.board[3])
       print('   |   |')

   def makeMove(self):
       self.board[self.move] = self.letter

   def playAgain(self):
       # This function returns True if the player wants to play again, otherwise it returns False.
       print('Do you want to play again? (yes or no)')
       return input().lower().startswith('y')


   def isWinner(self):
       # Given a board and a player's letter, this function returns True if that player has won.
       # We use bo instead of board and le instead of letter so we don't have to type as much.
       return ((self.board[7] == self.letter and self.board[8] == self.letter and self.board[9] == self.letter) or  # across the top
               (self.board[4] == self.letter and self.board[5] == self.letter and self.board[6] == self.letter) or  # across the middle
               (self.board[1] == self.letter and self.board[2] == self.letter and self.board[3] == self.letter) or  # across the bottom
               (self.board[7] == self.letter and self.board[4] == self.letter and self.board[1] == self.letter) or  # down the left side
               (self.board[8] == self.letter and self.board[5] == self.letter and self.board[2] == self.letter) or  # down the middle
               (self.board[9] == self.letter and self.board[6] == self.letter and self.board[3] == self.letter) or  # down the right side
               (self.board[7] == self.letter and self.board[5] == self.letter and self.board[3] == self.letter) or  # diagonal
               (self.board[9] == self.letter and self.board[5] == self.letter and self.board[1] == self.letter))  # diagonal

   def getPlayerXMove(self):
       # Let the player type in his move.
       x_move = ' '
       if first == 0:
           while x_move not in '1 2 3 4 5 6 7 8 9'.split() or not self.board[int(x_move)] == ' ':
               print('What is Player X\'s first move? (1-9)')
               x_move = input()
       else:
           while x_move not in '1 2 3 4 5 6 7 8 9'.split() or not self.board[int(x_move)] == ' ':
               print('What is Player X\'s next move? (1-9)')
               x_move = input()
       return int(x_move)


   def getPlayerOMove(self):
       # Let the player type in his move.
       o_move = ' '
       if first==1:
           while o_move not in '1 2 3 4 5 6 7 8 9'.split() or not self.board[int(o_move)] == ' ':
               print('What is Player O\'s first move? (1-9)')
               o_move = input()
       else:
           while o_move not in '1 2 3 4 5 6 7 8 9'.split() or not self.board[int(o_move)] == ' ':
               print('What is Player O\'s next move? (1-9)')
               o_move = input()
       return int(o_move)


   def isBoardFull(self):
       # Return True if every space on the board has been taken. Otherwise return False.
       for i in range(1, 10):
           if self.board[i] == ' ':
               return False
       return True


print('Welcome to Tic Tac Toe!')
if random.randint(0, 1) == 0:
    print('Player X goes first')
    first = 0
else:
    print('Player O goes first')
    first = 1

while True:
   theBoard = [' '] * 10
   play = TicTacToe(theBoard, first, playerX)
   gameIsPlaying = True
   while gameIsPlaying:
       if first % 2 == 0:
           play.drawBoard()
           move = play.getPlayerXMove()
           play = TicTacToe(theBoard, move, playerX)
           play.makeMove()
           if play.isWinner():
               play.drawBoard()
               print('Player X has won the game!')
               gameIsPlaying = False
               if random.randint(0, 1) == 0:
                    first = 0
               else:
                    first = 1
           else:
               if play.isBoardFull():
                   play.drawBoard()
                   print('The game is a tie!')
                   if random.randint(0, 1) == 0:
                        first = 0
                   else:
                        first = 1
                   break
               else:
                   first = first + 1

       else:
           play.drawBoard()
           play = TicTacToe(theBoard, first, playerO)
           move = play.getPlayerOMove()
           play = TicTacToe(theBoard, move, playerO)
           play.makeMove()
           if play.isWinner():
               play.drawBoard()
               print('Player O has won the game!')
               gameIsPlaying = False
           else:
               if play.isBoardFull():
                   play.drawBoard()
                   print('The game is a tie!')
                   break
               else:
                   first = first + 1

   if not play.playAgain():
       print('Thanks for playing!')
       break
