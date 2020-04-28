#---global variables---
board = ["_","_","_",
        "_","_","_",
        "_","_","_"]

game_still_going = True
winner = None
current_player = 'x'

def display_board():
  print(board[0]+ " | " + board[1]+ " | " + board[2])
  print(board[3]+ " | " + board[4]+ " | " + board[5])
  print(board[6]+ " | " + board[7]+ " | " + board[8])

def play_game():

  display_board()
  while game_still_going:

   handle_turn(current_player)

   check_if_game_over()
  #flip to the other player
   flip_player()
  if winner == 'x' or winner == 'o':
    print(winner + "won.")
  elif winner == None:
    print("Tie.")

def handle_turn(current_player):
    position= input("Spot your area from 1-9:")
    position = int(position)-1
    board[position] = "X"
    display_board()

def check_if_game_over():
    check_for_winner()
    check_if_tie()

def check_for_winner():
     global winner
     row_winner = check_rows()
     columns_winner = check_columns()
     diagonal_winner = check_diagonals()
     if row_winner:
       winner = row_winner
     elif columns_winner:
       winner= columns_winner
     elif diagonal_winner:
       winner = diagonal_winner
     return

def check_rows():
   global game_still_going
   row1 = board[0] == board[1] == board[2] != "-"
   row2 = board[3] == board[4] == board[5] != "-"
   row3 = board[6] == board[7] == board[8] != "-"
   if row1 or row2 or row3:
     game_still_going = False

   if row1:

     return board[0]
   elif row2:
     return board[3]
   elif row3:
     return board[6]
     return

def check_columns():
        global game_still_going
        columns1 = board[0] == board[3] == board[6] != "-"
        columns2 = board[1] == board[4] == board[7] != "-"
        columns3 = board[2] == board[5] == board[8] != "-"
        if columns1 or columns2 or columns3:
                game_still_going = False

        if columns1:

                return board[0]
        elif columns2:
                return board[1]
        elif columns3:
                return board[2]
        return

def check_diagonals():
        global game_still_going
        diagonal1 = board[0] == board[4] == board[8] != "-"
        diagonal2 = board[6] == board[4] == board[2] != "-"

        if diagonal1 or diagonal2 :
                game_still_going = False

        if diagonal1:

                return board[0]
        elif diagonal2:
                return board[6]

        return

def check_if_tie():
        return
def flip_player():
        return
play_game()







