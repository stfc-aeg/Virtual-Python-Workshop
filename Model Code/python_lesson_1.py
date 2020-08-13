# """Model code for lesson one of the Python workshop.
# This will follow the structure of the workshop,
# each lesson separated by a line of hashtags.
# """

######################################################

# Exercise 1 -- Variables

a = 15 + 5
b = 20 - a
c = 15 / 5
d = 10 + c
total = a + b + c + d
print(total)  # Should be 36

print(a)  # Proving that variables are remembered by Python

c = 35 / 5  # Increase c by 4
print(total)  # Should now be 40

########################################################

# Variables are cool, but I want to write a program!

welcome = "Hello, world!"  # Assign a string to the variable 'welcome'
print(welcome)  # Print it out!

########################################################

# User Input

name = input("Please enter your name: ")
print("Hello, " + name + "!")  # "Hello [name]!

########################################################

# Exercise 2 -- Customise your program

name = input("Hi! What's your name? ")
fav_colour = input("What's your favourite colour? ")
print("That's awesome " + name + "! My favourite colour is " + fav_colour + " too!")

########################################################

# Import Random

print("Two demonstration random values:")  # For when the program is run

import random  # In your own program, it's best practise to put imports at the top

value = random.randint(1,6)
print(value)

value = random.randint(10, 20)  # Reassigning 'value' to be between 10 and 20
print(value)

########################################################

# Exercise 3 -- Roll the dice

first_sides = int(input("How many sides do you want on the first die? "))
roll_1 = random.randint(1, first_sides)

second_sides = int(input("How many sides do you want on the second die? "))
roll_2 = random.randint(1, second_sides)

third_sides = int(input("How many sides do you want on the third die? "))
roll_3 = random.randint(1, third_sides)

roll_total = roll_1 + roll_2 + roll_3
print("Your rolls were: " + str(roll_1) + "\n" + str(roll_2) + "\n" + str(roll_3))
# \n puts the following text on another line
print("And your total is... " + str(roll_total))

########################################################

# Exercise 4 -- True or false?

a = 5
b = 10
print(a > b)  # False
print(a < b)  # True
print(a + b == b + a)  # True
print(a - b == b - a)  # False
print(a * b == b * a)  # True
print(a / b != b / a)  # True

# Alternatively, print all of them in one statement!
print(a>b, a<b, a+b == b+a, a-b == b-a, a*b == b*a, a/b != b/a)

########################################################

# While

x = 0
while x < 5:
    print(x)
    x = x + 1
# To make the limit higher, increase x < __:
# To make x jump differently, change x = __. x += 2, x *= x, etc.

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

print("Let's play a game! 'Guess the number'.")
print("You have to guess the number, it'll be between 1 and 20.")
guessesAllowed = int(input("How many guesses are you allowed? "))
# No. of allowed guesses. int() is to make sure the number is not a string.
guessesTaken = 0  # To begin with, no guesses are taken.

theNumber = random.randint(1, 20)  # The number to guess, between 1 and 20.

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

import math  # We'll use this for the square root

print("Let's find a prime number! WARNING: large numbers may take a long time to check.")
number = int(input("Enter the number to see if it's prime: "))

if number > 1:  # 1 is not a prime

    x = 2  # We won't use a for loop in this code.
    while x <= math.sqrt(number):
        if number % x == 0:  # 'modulo' (%) checks how many times a number divides into another number
                          # if modulo is zero, that number is a factor of the other. e.g.: 4 % 2 = 0

            print('\n', number, "is not a prime number.")
            print(x, "is a factor of", number, ".", x, "times", str(int(number)//int(x)), "is", number)
            break
        x += 1
    else:  # Make sure this else is indented to the same level as the 'while x <=' line!
           # What happens if it's indented to match the if statement following that line?
        print(str(number),  "is a prime number!")

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
    failed = 0              # If you haven't guessed a letter, this will increment by 1.
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
        guesses += guess  # A string with all of our guesses

        while x < len(word):
            if word[x] in guesses:  # word[x] is a letter in word. ex: word='string', word[0] = 's'
                word_display_list.append(word[x])  
            else:
                word_display_list.append("_")
                failed += 1
            x += 1  # Increment x for our while loop
        print(word_display_list)

        # Here's an alternative which uses for loops instead, covered in lesson 2.
        # This will look neater than the while loop!
        # Remove and add the # from each loop to see the difference.

        # for char in word:        # for each character in our word
        #     if char in guesses:  # if it's in our string of guesses
        #         word_display += char     # add that letter to the incomplete word
        #     else:
        #         word_display += "_"       # otherwise add a blank space
        #         failed += 1
        # print(word_display)

        if failed == 0:  # No wrong guesses
            print("You win!")
            break

        turns_remaining -= 1  # Lose one turn
        print("You have " + str(turns_remaining) + " turns remaining.")

        if turns_remaining == 0:  # If we run out of turns
            print("You lose! The word was " + word)









