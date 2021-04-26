# Exercise 8 -- Hangman
# To break this down a little bit:

# We want to check every letter of our word and compare it to all of our guesses
# If we have guessed that letter, we display it, otherwise we display a blank/_/etc.
# Repeat every time a guess is made, and add some conditions to the guesses.

print("Hello! Let's play a game of hangman!")
print("Your guess can either be the entire word, or just one character.")

word = "mystery"  # There are ways to generate a random word, but we don't need that here.

guesses = ""  # We can add to strings, so we'll do that here.
              # You could also use something like a list to store guesses.

turns_remaining = 10  # You need at least as many turns as unique letters!

# We'll count our turns down
while turns_remaining > 0:  # while we have turns left

    word_display = ''       # An empty string we will use to display our incomplete word
    missing = 0              # If you haven't guessed a letter, this will increment by 1.
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
        guesses += guess  # Add guess to the string of guesses.

        for char in word:        # for each character in our word
            if char in guesses:  # if it's in our string of guesses
                word_display += char     # add that letter to the incomplete word
            else:
                word_display += "_"       # otherwise add a blank space
                missing += 1
    

        print(word_display)

        if missing == 0:  # No missing letters
            print("You win!")
            break

        turns_remaining -= 1  # Lose one turn
        print("You have " + str(turns_remaining) + " turns remaining.")

        if turns_remaining == 0:  # If we run out of turns
            print("You lose! The word was " + word)
