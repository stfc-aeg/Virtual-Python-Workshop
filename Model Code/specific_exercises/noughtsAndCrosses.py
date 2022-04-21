# The final game I'll make in this model code is noughts and crosses. This one's a big one!
# We've got to identify wins, make and display the board... that's a lot already.
# I'm going to use a coordinates system!

# This will also require a few extra functions...
# For proper organisation you would do this as a Python class, but that's a little beyond the scope of this course!
import random

def gameWon():
    print("You win! Congratulations!")

def gameLost():
    print("You lose! The dragon has turned you into a elevenses.")


def get_move(active_player, you, dragon, game_board):
    # Get the player's/dragon's move
    row = -1
    column = -1  # some default values so we can see if something has gone wrong

    if active_player == you:
        player_input = input("Please choose a column and a row (e.g.: 2 1)")
        # Validating this input a little out of scope for this course. So you'd better enter it right!
        r, c = player_input.split(" ")
        r = int(r)
        c = int(c)

        if r >= 0 and r < 3:
            row = int(r)
        if c >= 0 and c < 3:
            column = int(c)

        return row, column

    elif active_player == dragon:
        # Want to pick random numbers, but let's make it only pick from legal ones.
        # Don't want to wait forever if it keeps picking bad ones! This bit's optional.
        legal_moves = []
        i = 0
        for row in game_board:
            j = 0  # Reset column each row
            for space in row:
                if space == ".":
                    legal_moves.append([i, j])  # row, column
                j += 1
            i += 1
        dragon_move = random.choice(legal_moves)
        row = dragon_move[0]
        column = dragon_move[1]
        print("The dragon chooses ", row, column)

        return row, column

def move_check(row, column, game_board):
    # Is this a legal move?
    if row == -1 or column == -1:
        return False
    
    if game_board[row][column] == ".":
        return True
    
    print(row, column, "is not a valid move. Please try again.")
    return False

def display_board(game_board):
    # show the board
    for row in game_board:
        row_string = ""
        for space in row:  # list of lists!
            row_string = row_string + " " + space + " " # with formatting: "{} {} ".format(row_string, space)
        print(row_string)

def check_win(active_player, you, dragon, game_board, playing):
    # What are all the ways you can win?
    win_combos = [  # row, column
        # Horizontal
        [(0,0), (0,1), (0,2)],
        [(1,0), (1,1), (1,2)],
        [(2,0), (2,1), (2,2)],
        # Vertical next
        [(0,0), (1,0), (2,0)],
        [(0,1), (1,1), (2,1)],
        [(0,2), (1,2), (2,2)],
        # and diagonals!
        [(0,0), (1,1), (2,2)],
        [(0,2), (1,1), (2,0)]
    ]

    for combination in win_combos:
        letters = [game_board[row][column] for row,column in combination]

        # Are all the letters the same and not empty?
        if "." not in letters:
            if len(set(letters)) == 1:  # sets can only have unique values. 
                # len = 1 means 1 player on all those spaces
                print("Well done, " + active_player + ", you've won!")

                playing = False # Game's done!

                return playing

def noughts_and_crosses():

    print("""The dragon speaks...
    
    \"Welcome to the truest test of skill! The cave of Harary.
    You understand the rules of noughts and crosses? We take turns. Make three-in-a-row.
    Count columns and rows from the top-left.
    You play X.\"
    """)
    you = "X"
    dragon = "O"
    playing = True

    # Game board! A list of lists. A . will represent empty spaces so we can see it.
    game_board = [ 
                    [".", ".", "."],
                    [".", ".", "."],
                    [".", ".", "."]
                ]
    active_player = ""

    # A random first player
    firstPlayer = random.randint(1,2)
    
    if firstPlayer == 1:
        player = you
        print("You (X) will start the game!")
    else:
        player = dragon
        print("The dragon (O) will start the game!")

    active_player = player

    while playing != False:

        display_board(game_board)

        row, column = get_move(active_player, you, dragon, game_board)

        if move_check(row, column, game_board):
            game_board[row][column] = active_player

        playing = check_win(active_player, you, dragon, game_board, playing)  # Did player win?

        # Swap turns only if the game is not over.
        if playing != False:
            if active_player == you:
                active_player = dragon
            else:
                active_player = you
    
    print("The game is over! Here is the final board.")
    display_board(game_board)

    if active_player == you:
        gameWon()
    else:
        gameLost() 

noughts_and_crosses()