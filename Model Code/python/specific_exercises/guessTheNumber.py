# Lesson 2, Exercises 5/6
# Lesson 3, exercise 9
import random

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

print("Let's play a game! 'Guess the number'.")
print("You have to guess the number, it'll be between 1 and 20.")
print("And we have some functions to do some other cool stuff for you!")
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
