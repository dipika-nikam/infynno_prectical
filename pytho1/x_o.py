
board = ['#', '#', '#',
       '#', '#', '#',
       '#', '#', '#', ]
player_win = None
game_still_going = True
winner = None
global name2
name2 = input('Enter Player1 Name')
global name
name = input('Enter Player2 name')

def main():
    option = input("do you want to play[yes/no]:")
    while option == 'no':
        if option.lower() == 'no':
            print("Okay meet you soon")
        break

    while option.lower() == 'yes' and game_still_going:
            handle_turn()
            win()
    if winner == "X" or winner == "o":
        print(winner + ' '+ "is winner")
    elif winner == None:
         print("Tie")
    else:
        pass


def play(board):
    print(board[0], "|", board[1], "|", board[2])
    print(board[3], "|", board[4], "|", board[5])
    print(board[6], "|", board[7], "|", board[8])

# #Player inputs for player 1 or 2
def get_input1():
    userInput = input("{} first player".format(name2))
    if userInput < 0 or userInput > 8 or board[userInput] == "X" or board[userInput] == "o":
        print("Wrong input! You cannot move there! ")
    else:
        board[userInput] = "X"

    play(board)

def get_input2():

    userInput = int(input("{} second player".format(name)))
    if userInput < 0 or userInput > 8 or board[userInput] == "X" or board[userInput] == "o":
        print("Wrong input! You cannot move there! ")
    else:
        board[userInput] = "o"
    play(board)

def win():
    check_for_winner()
    check_for_tie()

def game_tai():
    return print("Game Tai")

#for input and check winner
def handle_turn():
    get_input1()
    get_input2()
    check_for_winner()

def check_for_winner():

    global winner
    row_winner = check_rows()
    column_winner = check_columns()
    diagonal_winner = check_diagonals()
    # Get the winner
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None


# Check the rows for a win
def check_rows():

    global game_still_going
    row_1 = board[0] == board[1] == board[2] != "#"
    row_2 = board[3] == board[4] == board[5] != "#"
    row_3 = board[6] == board[7] == board[8] != "#"
    # If any row does have a match, flag that there is a win
    if row_1 or row_2 or row_3:
        game_still_going = False

    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]

    else:
        return None


# Check the columns for a win
def check_columns():
    # Set global variables
    global game_still_going
    # Check if any of the columns have all the same value (and is not empty)
    column_1 = board[0] == board[3] == board[6] != "#"
    column_2 = board[1] == board[4] == board[7] != "#"
    column_3 = board[2] == board[5] == board[8] != "#"
    # If any row does have a match, flag that there is a win
    if column_1 or column_2 or column_3:
        game_still_going = False
    # Return the winner
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
        # Or return None if there was no winner
    else:
        return None


# Check the diagonals for a win
def check_diagonals():
    # Set global variables
    global game_still_going
    # Check if any of the columns have all the same value (and is not empty)
    diagonal_1 = board[0] == board[4] == board[8] != "#"
    diagonal_2 = board[2] == board[4] == board[6] != "#"
    # If any row does have a match, flag that there is a win
    if diagonal_1 or diagonal_2:
        game_still_going = False
    # Return the winner
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[2]
    # Or return None if there was no winner
    else:
        return None


# Check if there is a tie
def check_for_tie():
    global game_still_going
    if "#" not in board:
        game_still_going = False
        return True
    else:
        return False
main()

def print_scoreboard():
    print("\t~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("\t         SCOREBOARD       ")
    print("\t~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("\t x"+'                '+'\t O')
    print("\t~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    x = 0
    o = 0
    if winner == 'X':

        x += 1
    elif winner == 'O':
        o += 1
    else:
        print('')
    print("\t {}                \t {}".format(name, name2))
    print("\t {}                \t {}".format(x,o))

print_scoreboard()
