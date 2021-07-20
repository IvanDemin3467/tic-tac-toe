from random import randrange

def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|   " + board[0][0] + "   |   " + board[0][1] + "   |   " + board[0][2] + "   |")
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|   " + board[1][0] + "   |   " + board[1][1] + "   |   " + board[1][2] + "   |")
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|   " + board[2][0] + "   |   " + board[2][1] + "   |   " + board[2][2] + "   |")
    print("|       |       |       |")
    print("+-------+-------+-------+")


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
    move = int(input("Enter your move: ")) - 1
    list_of_free_fields = make_list_of_free_fields(board)
    move_row = move // 3
    move_col = move % 3
    move_tup = (move_row, move_col)
    if move_tup in list_of_free_fields:
        board[move_row][move_col] = "O"
    else:
        print("Already taken")
        enter_move(board)


def draw_move(board):
    # The function draws the computer's move and updates the board.
    list_of_free_fields = make_list_of_free_fields(board)
    move = randrange(len(list_of_free_fields))
    move_row = list_of_free_fields[move][0]
    move_col = list_of_free_fields[move][1]
    board[move_row][move_col] = "X"
    print("My move: ", move_row * 3 + move_col + 1)


def victory_for(board, sign):
    # The function analyzes the board status in order to check if 
    # the player using 'O's or 'X's has won the game
    for i in range(3): #checks rows and cols
        if (board[i][0] == sign and board[i][1] == sign and board[i][2] == sign) or \
           (board[0][i] == sign and board[1][i] == sign and board[2][i] == sign):
            return True
    if (board[0][0] == sign and board[1][1] == sign and board[2][2] == sign) or \
       (board[0][2] == sign and board[1][1] == sign and board[2][0] == sign):
        return True
    return False


board = [[str(i+j) for j in range(3)] for i in range(1,9,3)]
board[1][1] = "X"
display_board(board)

while True:
    enter_move(board)
    display_board(board)
    if victory_for(board, "O"):
        print("You won!")
        break
    draw_move(board)
    display_board(board)
    if victory_for(board, "X"):
        print("Computer won!")
        break
    if len(make_list_of_free_fields(board)) == 0:
        print("Tie!")
        break
