"""Creates a functional, playable tic-tac-toe board!
   Type python3 tictactoe.py to try it out for yourself :)
"""

#initiates games and calls other functions when necessary
def play_game():
    board = ["_|_|_", "_|_|_", " | | "]

    #intro
    print("\nLet's play Tic-Tac-Toe!")
    
    #directions
    print("\nDirections: To designate which box you want to fill, \nuse rows and columns. For instance, 1 3 would mean \nrow 1, column 3 and would represent filling the top right.")
    input("\nPress any key to start.")
    rounds = 0
    curr_player, next_player = "X", "O"

    #main loop, 30 is arbitrary. Just there because they probably won't mess up and try the same number again 20 times.
    while rounds < 30:
        print_board(board)
        move = input("\nPlayer " + curr_player + ", it's your turn.\nPick a row and column (e.g.: 1 3)\n")
        if len(move) != 3:
            move = input("You must type your answer in the form of: row<space>column. e.g. 1 3 or 2 2 or 1 1. \nTry again: ")
        row_num, column_num = int(move[0]), int(move[2])

        new_row, i = "", 0
        row = board[row_num - 1]

        if column_num == 1:
            if row[0] == "O" or row[0] == "X":
                new_row = row
            else:
                new_row = curr_player + row[1:] 
        if column_num == 2:
            if row[2] == "O" or row[2] == "X":
                new_row = row
            else:
                new_row = row[:2] + curr_player + row[3:]
        if column_num == 3:
            if row[4] == "O" or row[4] == "X":
                new_row = row
            else:
                new_row = row[:4] + curr_player

        if new_row == row:
            print("\n***That box is already filled. Please pick another.***")
        
        else:
            board[row_num - 1] = new_row
            curr_player, next_player = next_player, curr_player
            if game_over(board):
                rounds = 30
       
        rounds += 1

    play_again()
        

#displays current board
def print_board(board):
    print("\n")
    for row in board:
        print(row)

def play_again():
    if input("\nWould you like to play again? y/n ") == "y":
        play_game()

#logic for deciding if a game is over
def game_over(board):
    full, row1, row2, row3 = 0, board[0], board[1], board[2]

    #bottom right to top left diagonal win
    if row1[4] == row2[2] == row3[0] and row1[4] != " " and row1[4] != "_":
        print_board(board)
        print("\nCongratulations, Player " + row1[4] + "! You win.\n")
        return True

    #top left to bottom right diagonal win
    if row1[0] == row2[2] == row3[4] and row1[0] != " " and row1[0] != "_":
        print_board(board)
        print("\nCongratulations, Player " + row1[0] + "! You win.\n")
        return True
    
    for row in board:
        if "_" not in row and " " not in row:
            full += 1
        #horizontal win
        if row[0] == row[2] == row[4] and row[0] != " " and row[0] != "_":
            print_board(board)
            print("\nCongratulations, Player " + row[0] + "! You win.\n")
            return True

    #vertical win
    for i in range(len(row1)):
        if row1[i] == row2[i] == row3[i] and row1[i] != " " and row1[i] != "_" and row[i] != "|":
            print_board(board)
            print("\nCongratulations, Player " + row[i] + "! You win.\n")
            return True

    #tie
    if full == 3:
        print_board(board)
        print("\nLooks like we have a tie. Better luck next time.")
        return True

    return False

play_game()



