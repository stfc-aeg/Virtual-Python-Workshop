# I'm going to build the six-games version of the text adventure.
# Since we've already built some of these games (hangman, guess the number) in other lessons I'll only build the new ones here.
# There are a few ways you could do anagrams and noughts or crosses. Maybe you can improve on mine?

import sys  # this will be used in noughts and crosses to end the game immediately
import random

def gameWon(scores):
    print("You win! A point to you. Keep it up!")
    scores['player'] += 1
    return scores

def gameLost(scores):
    print("You lose! One point to the dragon. Better luck next time!")
    scores['dragon'] += 1
    return scores

def backwards_names(scores):
    names = ['Sophy', 'Tom', 'Gregg', 'Jacob', 'Lauren', 'Mika', 'Annabelle', 'Constantine', 'Lorelai', 'Hannah']
    print("""The dragon speaks...

    \"So, adventurer, you've chosen the cave of esrever!
    A simple challenge. I will give you three names, you must spell them all backwards EXACTLY to earn your point.
    Let the challenge, begin!\"\n""")

    for i in range(3):  # three times
        if i == 2:  # a twist on the third time!
            chosen_name = input("And what is YOUR name, adventurer?")
        else:
            chosen_name = names[random.randint(0, len(names)) - 1]
            # lists count from zero, so our length will be 1 too high
            names.remove(chosen_name)

        reverse_name = ""
        for char in chosen_name:  # every letter
            reverse_name = char + reverse_name
            # each char has the letters before it placed after it
            # e.g.: Mika.    1: M    2:  i + M     3: k + iM     4: a + kiM = akiM
        print("Spell this backwards: " + chosen_name)
        response = input("")

        if response == reverse_name:  # EXACT match, including caps!
            print("The dragon speaks... \"Well done...")
            if i < 2:
                print("...but it's not over yet!\"")
            else:
                print("...another game?\"")
                scores = gameWon(scores)
                return scores

        else:
            scores = gameLost(scores)
            return scores


def rpsls(scores):  # rockPaperScissorsLizardSpock is a little long for a function name!
    options = {'rock':0, 'spock':1, 'paper':2, 'lizard':3, 'scissors':4}
    player_rps_score, dragon_rps_score = 0, 0
    print("""The dragon speaks...

    \"Welcome to the cave of Bryla! We will play rock, paper, scissors, lizard, spock!
    I hope you remember the rules? I think there was a flowchart outside...
    Beat me in a best of three and you will earn your point.\"    
    """)

    # This game is best handled by matching each option to a number and comparing values.
    # Each option beats and loses to two other options. So if we order our options right,
    # we can use modulo to really compact the code. Well done if you thought of this one too!
    # Rock, Spock, paper, lizard, scissors = 0,1,2,3,4. Pick one, skip two, it beats the next two.
    # The difference between the numbers (dragon-you) % 5 being 1,2 means you lose, 3,4, you win.
    # Examples: you pick Spock, computer picks paper. (2-1)%5 = 1, so you lose.
    # You pick scissors, computer picks lizard. (3-4)%5 = 3, so you win.

    while (player_rps_score < 2 and dragon_rps_score < 2):  # if either reach 2, game end
        player_choice = input("Choose wisely... (rock,paper,scissors,lizard,spock) ")
        player_number = options[player_choice]  # Get value from the dictionary!

        dragon_choice = random.choice(list(options))  # random.choice cannot use dict
        dragon_number = options[dragon_choice]

        difference = (dragon_number - player_number) % 5
        if (difference == 1 or difference == 2):
            print("The dragon beats " + player_choice + " with " + dragon_choice)
            dragon_rps_score += 1
        elif (difference == 3 or difference == 4):
            print("You beat the dragon's " + dragon_choice + " with " + player_choice)
            player_rps_score += 1
        else:
            print("It's a tie!")

    if player_rps_score > dragon_rps_score:
        print("The dragon speaks... \"Hmph. How? Another round?\"")
        scores = gameWon(scores)
        return scores
    else:
        scores = gameLost(scores)
        return scores

def jumble(scores):  # 'anagrams'
    # You could make this by making up the anagrams yourself, picking them from a list
    # and checking if they got the answer right. A dictionary to store those pairs would work well.
    # But I want to jumble the words myself, randomly!
    # Technically this is a word jumble instead of an anagrams... oh well ;)

    print("""The dragon speaks...
    
    \"Ah, the cave of Paragon An Myths. 
    Can you identify these scrambled Python terms? You've learned about all of them...
    Get at least two of three correct, and I'll give you the point.\"
    """)
    words = ['integers', 'concatenation', 'function', 'while', 'boolean', 'conditional', 'module', 'variable', 'input', 'jupyter', 'python', 'notebook']
    score = 0

    for i in range(3):
        word = random.choice(words)  # Pick a word for me!
        words.remove(word)  # No repeats
        correct = word
        jumbled = ""

        while word:
            position = random.randrange(len(word))  # Pick a number up to the number of chars in word (zero indexing)
            jumbled += word[position]  # Add the character at that position to our jumble
            word = word[:position] + word[(position + 1): ]  # Word = word[up to position] + word[past position]. 
            # Cut the char out! Two slices on either end. We can't use replace() because that replaces ALL of that character.
            # Once all characters have been taken, word is '', or null, or False, and the loop ends!

        print("The jumble is: " + jumbled)
        guess = input("What was the original word? ")
        guess = guess.lower()  # all lowercase
        if guess == correct:
            print("Well done!")
            score += 1
        else:
            print("That is... not correct.")
    
    if score < 2:
        print("The dragon speaks... \"Surely I must have enough overall points by now...\"")
        scores = gameLost(scores)
        return scores
    else:
        print("The dragon speaks... \"You win... this time.\"")
        scores = gameWon(scores)
        return scores


# The final game I'll make in this model code is noughts and crosses. This one's a big one!
# We've got to identify wins, make and display the board, get moves... that's a lot.
# I'm going to use a coordinates system for this.
# This will also require a few extra functions...
# For proper organisation you would do this as a Python class, but that's a little beyond the scope of this course!

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

                return [playing,active_player]

    # Is the board full?
    spaces = [column for row in game_board for column in row]  # for sublist in board, for item in sublist

    if "." not in spaces:  # i.e.: no spaces
        print("It's a tie! The board is full!")
        playing = False
        active_player = None
        return [playing,active_player]

    return [playing,active_player]

def noughts_and_crosses(scores):

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

        continuation = check_win(active_player, you, dragon, game_board, playing)  # Did player win?
        playing = continuation[0]
        active_player = continuation[1]  # What's a better way to handle ties specifically?

        # Swap turns only if the game is not over.
        if playing != False:
            if active_player == you:
                active_player = dragon
            else:
                active_player = you
    
    print("The game is over! Here is the final board.")
    display_board(game_board)

    if active_player == you:
        scores = gameWon(scores)
        return scores
    elif active_player == dragon:
        scores = gameLost(scores)
        return scores
    elif active_player == None:
        print("No points awarded this time.")
        return scores


def main(scores):
    while (scores['player'] < 2 and scores['dragon'] < 2):
        print("player:", scores['player'], " | dragon: ", scores['dragon'])
        # pick game here
        print("""The dragon speaks...
        
        \"Please, choose a game, from one to six.
        (and I won't tell you which is which)!\"
        """)
        game_choice = int(input("Pick a number from 1 to 6: "))

        if game_choice == 1:
            backwards_names(scores)
        elif game_choice == 2:
            rpsls(scores)
        elif game_choice == 3:
            jumble(scores)
        elif game_choice == 4:
            noughts_and_crosses(scores)
        elif game_choice == 5 or game_choice == 6:
            print("Those games can be found elsewhere.")
            # The code exists in other exercises!
            # It just needs to be put into a function.

    if scores['player'] == 2:
        print("""The dragon speaks...
        \"What? How?!
        Well, I am a dragon of my word.\"
        
Congratulations! You have beaten the dragon at their games and are free to go!
        """)
    elif scores['dragon'] == 2:
        print("""The dragon speaks...
        
        \"I'd say better luck next time, but, well... you tried!\"
        
You have become the dragon's dinner! No hard feelings!""")

# Initialise variables and intro dialogue.
print("""You find yourself in a cave, face to face with a very large and rather hungry dragon!

But dragons are a fair sort, so you will have the opportunity to save yourself, 
if you can beat the dragon at their games.
Good luck!
""")

scores = {'player': 0, 'dragon':0}  # One variable to track all the scores makes it easier to pass around.
# Another reason this might be easier in a class... so we don't have to pass this around all the time!
# There's some advanced reading for you to get to some time ;)
main(scores)
