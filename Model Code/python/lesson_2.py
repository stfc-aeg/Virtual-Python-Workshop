# Here's the model code for lesson 2! Same structure as lesson 1.

import random

# While

x = 0
while x < 5:
    print(x)
    x += 1
# To make the limit higher, increase x < __:
# To make x jump differently, change x += __. x += 2, x *= x, etc.

########################################################

# If

x = int(input("Choose a value! x = "))  # Make sure x is an integer
                                        # If it's a string, it can't == 5
if x == 5:
    print("x == 5")
elif x == 4:
    print("x == 4")
else:
    print("x is not 4 or 5")

########################################################

# Exercise 5 -- Guess the number

import random

print("Let's play a game! 'Guess the number'.")
print("You have to guess the number!")
difficulty = input("What difficulty do you want (pick one: easy,med,hard)? ")

if difficulty == 'easy':
    print("You have four guesses, the number is between 1 and 20.")
    guessesAllowed = 4
    upperLimit = 20
elif difficulty == 'hard':
    print("You have three guesses, the number is between 1 and 30.")
    guessesAllowed = 3
    upperLimit = 30
else:
    if difficulty != 'med':
        print("Defaulting to medium difficulty.")
    print("You have four guesses, the number is between 1 and 30.")
    guessesAllowed = 4
    upperLimit = 30


# No. of allowed guesses. int() is to make sure the number is not a string.
guessesTaken = 0  # To begin with, no guesses are taken.

theNumber = random.randint(1, upperLimit)  # The number to guess.

# Make a while loop for our guess count, it must be less or equal than guessesAllowed.
while guessesTaken < guessesAllowed:
    guess = int(input("What's your guess? \n"))

    if guess > theNumber:    # If guess is more than theNumber
        print("Too high!")
    elif guess < theNumber:  # If guess is less than theNumber
        print("Too low!")
    else:                    # If guess == theNumber
        print("That's right! Well done!")
        break                # Breaks the loop
                             # no matter how many guesses remain

    guessesTaken += 1  # Increase number of guesses taken by one each time

    if guessesTaken == guessesAllowed:  # guess limit exceeded
        print("You're out of guesses! The number was " + str(theNumber))


########################################################

# Functions

def greeting(name):
    print("Welcome " + name)

greeting("Sophy")
greeting("Angus")
greeting("Callum")

# Another example

def double(number):
    number *= 2  # Double our number
    return number  # Give back the new doubled number

doubled = double(2)
print(doubled)

########################################################

# Exercise 6 -- Functions and Guess Quality in 'Guess the Number'

# To do this, I'm going to hit two birds with one stone
# and use a function /for/ guess quality

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

theNumber = random.randint(1, 20)  # Setting theNumber

while guessesTaken < guessesAllowed:
    guess = int(input("What's your guess? \n"))

    if guess > theNumber:
        print("Too high!")
        guessQuality(guess, theNumber)
    elif guess < theNumber:
        print("Too low!")
        guessQuality(guess, theNumber)
    else:
        print("That's right! Well done!")
        break

    guessesTaken += 1

    if guessesTaken == guessesAllowed:
        print("Game over! The number was " + str(theNumber))


########################################################

# Exercise 7 -- Prime Numbers

# A number is prime if it does not have any factors aside from 1 and itself. For example, 3.
# This means that one is not a prime number! 1 is its only factor, prime numbers have two factors.
# So, primes can be found by checking if every number from 2 to number-1 is a factor of number.
# You can save time by just checking up to the square root of the prime.
#    --> A composite number must have a factor less than its square root.

# 437632794689 is a good prime
import math  # We'll use this for square root and rounding.

print("Let's find a prime number! WARNING: large numbers may take a long time to check.")
number = int(input("Enter a number to see if it's prime: "))

if number > 1:  # 1 is not a prime number! It has only one factor, itself.
    rangeLimit = math.ceil(math.sqrt(number))  # Math.ceil rounds up.

    while x <= rangeLimit:
        if number % x == 0:  # 'modulo' (%) checks how many times a number divides into another number
                          # if modulo is zero, that number is a factor of the other. e.g.: 4 % 2 = 0
            print("\n" + str(number) + " is not a prime number.")

            numStr = str(number)
            iterStr = str(x)
            pairedFactor = str(number//x)

            print(iterStr + " is a factor of " + numStr + ".")
            print(iterStr + " x " + pairedFactor + " = " + numStr)
            # An extension would be to get all factors of the number!
            break
        x += 1
    else:  # Make sure this else is indented to the same level as the 'loop' line!
           # What happens if it's indented to match the if statement following that line?
        print(str(number) + " is a prime number!")

else:
    print("1 is not a prime number.")


########################################################

# Exercise 8 -- Hangman
# I'll use underscore notation for my variables this time.

print("Hello! Let's play a game of hangman!")
print("Your guess can either be the entire word, or just one character.")

word = "enigma"  # There are ways to generate a random word, but we don't need that here.

guesses = ""  # We can add to strings, so we'll do that here.
              # You could also use something like a list.

turns_remaining = 10  # You need at least as many turns as unique letters in your word!

# We'll count our turns downwards
while turns_remaining > 0:  # while we have turns left

    word_display = ''       # An empty string we will use to display our incomplete word
    missing = 0             # If you haven't guessed a letter, this will increment by 1.
                            # you win when it's zero (when you've guessed every right letter)

    guess = input("Enter your guess here: ")

    if guess == word:  # You can guess the entire word if you like! But only the entire word.
        print("You win!")
        break

    elif len(guess) > 1:  # To make sure you only guess one character
        print("Your guess must be only one character.")

    elif guess in guesses:  # To prevent duplicate guesses
        print("You already guessed this letter! So far, you have guessed: " + guesses)
    
    else:  # If the guess isn't the whole word, previously guessed, and is one character, the program continues.
        guesses += guess  # Add guess to the string of guesses

        x = 0
        while x < len(word):
            if word[x] in guesses:  # word[x] is a letter in word. ex: word='string', word[0] = 's'
                word_display += word[x]  # Fill with correct letter
            else:
                word_display += "_"  # Blank, wrong letters
                missing += 1
            x += 1  # Increment x for our while loop
        print(word_display)

        # In specific_exercises, you can find a version using a for loop, which is a little neater.
        # But those are only covered in lesson 3 so I won't use them here.

        if missing == 0:  # No missing letters
            print("You win!")
            break

        turns_remaining -= 1  # Lose one turn
        print("You have " + str(turns_remaining) + " turns remaining.")

        if turns_remaining == 0:  # If we run out of turns
            print("You lose! The word was " + word)
