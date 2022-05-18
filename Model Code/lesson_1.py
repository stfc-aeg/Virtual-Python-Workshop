# Model code for lesson one of the Python workshop.
# I'll follow the structure of the workshop!
# So I'll separate each lesson by

######################################################

# Exercise 1 -- Variables

a = 15 + 5  # 20
b = 20 - a  #  0
c = 15 / 5  #  3
d = 10 + c  # 13
total = a + b + c + d
print(total)  # Should be 36

print(a)  # Proving that variables are remembered by Python

c = 35 / 5  # Increase c by 4
total = a + b + c + d  # Redefine total
# Note that, even though d = 10 + c, we already defined d = 13 using c = 3.
# Variables, once assigned, retain that value until changed. This is not algebra!

print(total)  # Should now be 40

# Or, alternatively...
total = 40
print('Total is now', total)

########################################################

# Variables are cool, but I want to write a program!

welcome = "Hello, world!"  # Assign a string to the variable 'welcome'
print(welcome)  # Print it out!

########################################################

# Exercise 2 -- Customise your program

name = input("Hi! What's your name? ")
fav_colour = input("What's your favourite colour? ")
print("That's awesome " + name + "! My favourite colour is " + fav_colour + " too!")

########################################################

# Import Random

print("Two demonstration random values:")  # For when the program is run

import random  # In your own programs, it's best practise to put all imports at the top

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
# \n is a line break, it puts the following text on another line
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