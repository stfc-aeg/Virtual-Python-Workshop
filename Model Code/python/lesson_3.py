# Lesson 3! Everything leading up to the final exercise.

import random  # Remember, this must be done in each unique Python file you want to use random.

######################################################

# Exercise 9 -- Mathematical function function

# For my maths function function, I'm going to make an average of the guesses.
# The mean: add them all together, divide by how many there are.

def guessMathsFunction(guess, guessTotal):
    guessTotal += guess
    print("The sum of your guesses was:", guessTotal)
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
    # But this is good practise for using boolean operators


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

# Exercise 10 -- The list commands

fruityList = ['Apple', 'Tangerine', 'Raspberry Pie', 'Orange', 'Apricot']
fruityString = 'Totally Unrelated Fruits'

fruityList.reverse()
fruityList.remove('Tangerine')
# Methods that update a list don't return a value directly, so printing them
# like `print(fruityList.remove('Apple'))`
# will output 'None'
print(fruityList)

print(fruityString.upper())
print(fruityString.lower())
print(fruityString.split(" "))


######################################################

# Exercise 11 -- For a while

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

# Exercise 12 -- Lists and tuples and dictionaries, oh my!

# Normal

fruityProducts = ('Apple', 'Tangerine', 'Raspberry Pie', 'Orange', 'Apricot','Acorn','Blackberry')
fruityPrices = [2, 1, 5, 1, 2, 4, 2]
productInfo = {}

for i in range(len(fruityProducts)):
    productInfo[fruityProducts[i]] = fruityPrices[i]

print(productInfo)

# Extension

sortedByPrice = {}
uniquePrices = set(fruityPrices)  
# You could do this by iterating over the fruityPrices and removing prices you've seen before, but a set is faster!
# That might look like this:        (// = line break, -> = indent)
# uniquePrices = [] // for price in fruityPrices: // -> if price not in uniquePrices // -> -> uniquePrices.append(price)

for price in uniquePrices:  # for all our unique prices
    byPrice = []
    for i in range(len(fruityProducts)):  # Check all the prices
        if fruityPrices[i] == price:      # if it's our unique price
            byPrice.append(fruityProducts[i])  # add the product to a list

    sortedByPrice[price] = byPrice  # the list is our group of products

print(sortedByPrice)
# In short: get unique prices, compare all prices to each unique price, find products matching that price and group them
