from random import randrange

def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console. It's appearance should be:
    # +-------+-------+-------+
    # |       |       |       |
    # |   1   |   2   |   3   |
    # |       |       |       |
    # +-------+-------+-------+
    # |       |       |       |
    # |   4   |   5   |   6   |
    # |       |       |       |
    # +-------+-------+-------+
    # |       |       |       |
    # |   7   |   8   |   9   |
    # |       |       |       |
    # +-------+-------+-------+
    for i in range(3):
        print(("+"+"-"*7)*3+"+")
        print(("|"+" "*7)*3+"|")
        for j in range(3):
            print("|   " + board[i][j] + "   ", end="")
        print("|")
        print(("|"+" "*7)*3+"|")
    print(("+"+"-"*7)*3+"+")



def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    list_of_free_fields = []
    for i in range(3):
        for j in range(3):
            if not(board[i][j] == "X" or board[i][j] == "O"):
                list_of_free_fields.append((i, j))
    return list_of_free_fields


def enter_move(board):
    # The function accepts the board current status, asks the user about their move, 
    # checks the input and updates the board according to the user's decision.
    # Uses recursion to restart on invalid input.
    # Questionable solution as the user might try to overflow memory.
    # Recursion is only used for demonstration
    try:                                   # User makes a move
        move = int(input("Enter your move: ")) - 1 
    except ValueError:                     # If user inputs not integer -> try again
        print("Only integers in range (1 .. 9) accepted. Try again.")
        enter_move(board)                  # Recursion to start over
        return
    if move not in range(9):               # If incorrect input -> try again
        print("Out of range. Use integers in range (1 .. 9). Try again.")
        enter_move(board)                  # Recursion to start over
        return
    # Converting user's move to coordinates:
    move_row = move // 3
    move_col = move % 3
    move_tup = (move_row, move_col)
    # Checking if the field is empty
    list_of_free_fields = make_list_of_free_fields(board)
    if move_tup in list_of_free_fields:    # Yes, the field is empty
        board[move_row][move_col] = "O"    # Occupy that field
    else:                                  # No, the field is occupied
        print("Already taken. Try again.") 
        enter_move(board)                  # Recursion to start over
        return


def draw_move(board):
    # The function draws the computer's move and updates the board.
    list_of_free_fields = make_list_of_free_fields(board) 
    move = randrange(len(list_of_free_fields)) # Computer plays randomly
    # Getting coords of chosen field
    move_row = list_of_free_fields[move][0]
    move_col = list_of_free_fields[move][1]
    # Occupy that field
    board[move_row][move_col] = "X"
    print("My move: ", move_row * 3 + move_col + 1)


def victory_for(board, sign):
    # The function analyzes the board status in order to check if 
    # the player using 'O's or 'X's has won the game

    # Checks rows and cols
    for i in range(3): 
        if (board[i][0] == sign and board[i][1] == sign and board[i][2] == sign) or \
           (board[0][i] == sign and board[1][i] == sign and board[2][i] == sign):
            return True
    # Checks diagonals
    if (board[0][0] == sign and board[1][1] == sign and board[2][2] == sign) or \
       (board[0][2] == sign and board[1][1] == sign and board[2][0] == sign):
        return True
    # No lines found -> no winner
    return False


#####################################################################################

# Init the board
board = [[str(i+j) for j in range(3)] for i in range(1,9,3)]
board[1][1] = "X"
display_board(board)
# Starting game in infinite loop
while True:
    # User's turn
    enter_move(board)
    display_board(board)
    # Checks if user won
    if victory_for(board, "O"):                   
        print("You won!")
        break
    # Computer's turn
    draw_move(board)
    display_board(board)
    # Checks if computer won
    if victory_for(board, "X"):                   
        print("Computer won!")
        break
    # Checks if board is full -> no winner
    if len(make_list_of_free_fields(board)) == 0: 
        print("Tie!")
        break
