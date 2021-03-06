"""Model code for lesson two of the Pyhton workshop.
This will follow the structure of the workshop,
each lesson separated by a line of hashtags.
I won't include the recap section!
"""
import random  # Remember, this must be done in each unique Python file you want to use random.

######################################################

# Exercise 1 -- Mathematical function function

# For my maths function function, I'm going to make an average of the guesses.
# The mean: add them all together, divide by how many there are.

def guessMathsFunction(guess, guessTotal):
    guessTotal += guess
    print(guessTotal)
    return guessTotal

def guessQuality(guess, theNumber):
    distance = guess - theNumber
    # We say 'hot' is within 2, and warm is within 4.
    # We will need the boolean operator AND
    if distance >= -2 and distance <= 2:  # greater than -2, but less than 2
        print("You're getting hot!")
    elif distance >= -4 and distance <= 4:
        print("You're getting warm!")
    else:
        print("You're totally cold.")
    # You could also write this using abs(), which returns an absolute value.
    # e.g.: if abs(distance) <= 2:
    # But this is good practise using boolean operators


print("""This guess the number game uses functions! \n
You have to guess the number, it'll be between 1 and 20. \n
Our function will tell you if your guess is hot, warm, or cold. \n
How many guesses would you like?""")
# Multi-line strings are allowed using """. This saves us typing 'print' a lot.
guessesAllowed = int(input())  # Permitted guesses input as an integer
guessesTaken = 0               # No guesses taken yet
guessTotal = 0                 # No guesses taken yet

theNumber = random.randint(1, 20)  # Setting theNumber

while guessesTaken < guessesAllowed:
    guess = int(input("What's your guess? \n"))
    guessTotal = guessMathsFunction(guess, guessTotal)  # A running total of guesses
    guessesTaken += 1
    
    if guess > theNumber:
        print("Too high!")
        guessQuality(guess, theNumber)
    elif guess < theNumber:
        print("Too low!")
        guessQuality(guess, theNumber)
    else:
        print("That's right! Well done!")
        print("Your average guess was " + str(guessTotal / guessesTaken))
        break


    if guessesTaken == guessesAllowed:
        print("Game over! The number was " + str(theNumber))
        print("Your average guess was " + str(guessTotal / guessesTaken))


######################################################

# Exercise 2 -- The list commands

fruityList = ['Strawberry', 'Orange', 'Lemon', 'Lime', 'Blackcurrant']
fruityString = 'Generic Fruit Sweets'

fruityList.reverse()
print(fruityList)  # These two must be separated, as .reverse() does not
# return a value by itself, it updates the existing list.
# print(fruityList.reverse()) will return None

print(fruityString.upper())
print(fruityString.lower())
print(fruityString.split(" "))


######################################################

# Exercise 3 -- For a while

x = 0
while x < 10:  # While x is less than 10, print x and add 1 to it.
    print(x)
    x += 1

for i in range(10):  # print i, for every integer in range from 0 to 9.
    print(i)

# Or for printing colours

colours = ['Red', 'Yellow', 'Orange', 'Green', 'Blue', 'Indigo', 'Violet']
x = 0

while x < len(colours): # len() provides the length of the object you give it
    # we need len() to make sure we don't count past the end of our list
    # because that would throw an error!
    print(colours[x])
    x += 1

for i in range(len(colours)):
    print(colours[i])


######################################################

# Exercise 4 -- Cave Systems and Fire Lizards

# We have six games! Most will only need one function, but a couple are a little bigger than that.
# I won't build all of them here, we've done some of the others already: hangman, guess the number.
# In the case of noughts and crosses or anagrams, there's a number of ways to make them.
# I've deliberately not built anagrams. There are too many ways to make it into a game!
# But here's a hint: you could use str.sorted() to check both lists have the same letters...

import sys  # this will be used in noughts and crosses to end the game immediately

def cinders():  # Game over!
    print("Unfortunately, you've failed the dragon's game and been eaten! Better luck next time!")

def write_name_backwards():
    names = ['John', 'Amy', 'Mika', 'Thomas', 'Greg', 'Annabelle', 'Alistair', 'Constantine', 'Lorelai', 'Hannah']
    print("""The dragon speaks...
    
    \"So, adventurer, you've chosen the cave of esrever!
    This is a simple challenge. I will give you some names, you must spell them backwards exactly, or I'll turn you to ash!\"
    Let's begin!\n""")

    for i in range(3):  # we want to do this twice
        if i == 2:  # third time is for user input
            chosen_name = input("And what is YOUR name, adventurer? ") 
        else:  # first and second time 
            chosen_name = names[random.randint(0, len(names)) - 1]  # A random name from the list
                                                                    # -1 because lists count from 0!

        reverse_name = ""  # empty string
        for char in chosen_name:  # for each character
            reverse_name = char + reverse_name # reverse = one character + reverse
        print("Spell this name backwards: " + chosen_name)
        response = input("")

        if response == reverse_name:  # it must match EXACTLY, this includes the capital letter!
            print("Congratulations!")
            if i < 2:
                print("You're not done with this challenge yet!")
            else:
                print("You're free to go. Well done, adventurer.")
        else:
            cinders()
            break  

def rpsls():
    options = {'rock':0, 'spock':1, 'paper':2, 'lizard':3, 'scissors':4}
    player_score = 0
    dragon_score = 0  # We'll do a best of three
    print("""So, adventurer, you've chosen the cave of Bryla!
    We will play rock, paper, scissors, lizard, spock!
    Best me, best of three, and you may pass.\n""")

    # This game is best handled by matching each string/option to a number and comparing
    # these values. Each option beats two other options, and loses to two others
    # So we can use modulo with number comparisons to make this very compact, to avoid a lot of 'if/elif'.
    # rock, spock, paper, lizard, scissors = 0, 1, 2, 3, 4. Pick one, skip two, it beats the two after those.
    # This means that the difference between the numbers % 5 being 1, 2 means you lose, and 3, 4 means you win.
    # e.g.: you pick spock, computer picks paper. (2-1)%5 = 1, meaning you lose.
    # e.g.: you pick scissors, computer picks rock. (0-4)%5 = 1, meaning you lose. 

    while (player_score < 2 and dragon_score < 2):  # ends when either player reaches 2
        player_choice = input("What will you go for (rock, paper, scissors, lizard, spock)? ")
        player_number = options[player_choice]

        dragon_choice = random.choice(list(options))  # To use this random.choice, we need to give it a list or tuple, not dictionary
            # See an example at https://pynative.com/python-random-choice/, which is where I found this information
        dragon_number = options[dragon_choice]

        difference = (dragon_number - player_number) % 5
        if (difference == 1 or difference == 2):
            print("The dragon wins with", dragon_choice)
            dragon_score += 1
        elif (difference == 3 or difference == 4):
            print("You win! The dragon chose", dragon_choice)
            player_score += 1
        else:
            print("It's a tie!")
    
    if player_score > dragon_score:
        print("Congratulations. You win... this time.")
    elif player_score < dragon_score:
        cinders()

# Noughts and crosses below here!
def NaC_win(player):
    if player == 'x':
        print("Congratulations adventurer... You win... this time.")
    else:
        cinders()


def NaC_check(board, player, win):  # We will need to pass the variable 'board' as an argument if we want to check it!
                               # I've given 'player' across too. This is either 'x' or 'o'.
    # This is to check if anyone has won the game noughts and crosses!
    # You win horizontally, vertically or diagonally. This makes eight win conditions.
    for i in range(0, 6, 3):  # Start at 0, stop at 6, step in 3. positions 1, 4, 7
        if board[i] == player and board[i+1] == player and board[i+2] == player:
            print(player, "wins!")
            win = 1
            return win, player

    # Downwards. i = 0, 1, 2. 
    for i in range(3):
        if board[i] == player and board[i+3] == player and board[i+6] == player:
            print(player, "wins!")
            win = 1
            return win, player

    # Diagonal
    if board[0] == player and board[4] == player and board[8] == player:
        print(player, "wins!")
        win = 1

    elif board[2] == player and board[4] == player and board[6] == player:
        print(player, "wins!")
        win = 1
    return win, player

def noughts_and_crosses():
    # Just one version of a noughts and crosses game.
    # You could improve on this a lot using a coordinate system, to avoid all of those if/elif statements!
    # Maybe a neater way to print the board, without all of those [], "" and , everywhere?
    # Give it a go, using this as inspiration!
    win = 0
    turn = 0
    board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]  # 9 spaces, 3x3 board
    go = 0

    print("""Here are the board numberings:
    [1, 2, 3]
    [4, 5, 6]
    [7, 8, 9]
    """)

    while win == 0:
        go = 0
        while go != 1:  # repeating turn if go is not set to 1
            move = int(input("Which position would you like to put an x? "))
            if board[move-1] == " ":
                board[move-1] = "x"
                turn += 1
                go = 1
                player = 'x'
            else:
                print("That space has been taken")

        print('{} \n{} \n{} \n'.format(board[0:3], board[3:6], board[6:]))
        # You can use .format with the {} to print multiple variables more easily
        # In this case, the board split into threes. 0-2, 3-5, 6-8.
        win, player = NaC_check(board, player, win)  # if someone wins, we get back 1 and who won
        if win == 1:  # If we do not have the check, the loop will finish and set player to 'o', stopping you from ever winning!
            break
        if turn == 9:
            break
        # Computer's turn. It will pick a random number. 
        # No print statement on if the move is taken, this is to stop the prompt filling up!
        go = 0
        while go != 1:
            move = random.randint(0, 9)
            if board[move-1] == " ":
                board[move-1] = "o"
                turn += 1
                go = 1
                player = 'o'
            else:
                go = 0  # Not necessary but emphasises that the turn is not over if a valid space is not picked.

        print('{} \n {} \n {}'.format(board[0:3], board[3:6], board[6:]))
        win, player = NaC_check(board, player, win)

    if win == 1 and player == 'x':
        print("Congratulations. You win... this time.")
    elif win == 1 and player == 'o':
        cinders()
    else:
        print("It's a draw!")

def anagrams():
    # You could make this game by typing the anagrams and if-checking a correct answer
    # Or using .sorted() to check if the same letters are in both (to avoid lots of if statements)
    # I'm going to jumble the words myself!
    print("Can you solve my Python-themed anagrams? \nYou learned about all of these things earlier...")
    words = ['integers', 'concatenation', 'function', 'while', 'boolean', 'conditional', 'module', 'variable', 'input', 'jupyter', 'python', 'notebook']
    score = 0

    for i in range(3):  # Repeat three times to win!
        word = random.choice(words)  #  Using the random module to pick a word for us!
        words.remove(word)  # We don't want repeat words!
        correct = word
        jumbled = ""

        while word:
            position = random.randrange(len(word))  # Pick a number that is max the no. of characters in word
            jumbled += word[position]  # Go to the [position]th character in the word.
            word = word[:position] + word[(position + 1): ]  # Remove the character we just added to jumble
                # We do this by slicing the string on either side of position
    
        print("The anagram is: ", jumbled)
        guess = input("What was the original word? ")
        guess = guess.lower()  # All lowercase!
        if guess == correct:
            print("Well done...")
            score += 1
        else:
            print("That's not right, sorry.")

    if score < 2:
        print("Oh dear, adventurer, you didn't get enough correct.")
        cinders()
    else:
        print("You win... this time.")




import random
print("""Greetings, adventurer...
Choose the challenge of your demise!
Pick a number between one and six, and see if you can beat me at my games.""")
game_choice = int(input())

# If selections followed by functions is more than fine for text adventure games!
if game_choice == 1:
    write_name_backwards()
elif game_choice == 2:
    rpsls()
elif game_choice == 3:
    noughts_and_crosses()
elif game_choice == 4:
    anagrams()
elif game_choice == 5 or game_choice == 6:
    print("Hangman/guess the number have been done elsewhere! You can bring your own code over C: ")
else:
    print("I said between one and six... the only games we will play here are MINE!")
# What do you do to let the adventurer pick where they want to go?











