# With these imports, you need this file to be in a directory where the import path exists.
# Copy this next to the python lessons to use it there, or copy words.py over to this file
# Imports work much more neatly with Python packages, but that's out of scope for the workshop!
from extras.words import guess_words, all_words
import random

# With the guess, you need to check each letter of the guess against the random word character by character
# If the letter is at that place, it is correct and should be displayed with a 'positive indicator' (normally this is green)
# If the letter is in the word but not at that place, it is a 'partial indicator' (normally yellow)
# If the letter is not in the word at all, it is a 'negative indicator' (normally grey)

# The challenge comes from that yellow and green letters may overlap: you can't have more yellow/green of a thing than there are of that thing in the word
# So you need to count the letters as they come and compare this to the total of the characters in that word.
# In the context of the workshop - this is a good use case for dictionaries. Count up the letters and store them, then compare as you go through the guess.

random_word = random.choice(guess_words)

attempts = 6
history = []

def check_guess(guess, random_word):
    """Check the quality of a guess by evaluating each of its letters against the individual counts
    of letters in the original word
    :param guess: string: the guess
    :param random_word: string: the random word to check against
    """
    # It's a little easier to start with the assumption that all the entries are wrong and replace
    indicators = ["-"] * 5
    # We need to count the letters in the word so we know how many greens/yellows to assign
    letter_counts = {}
    for char in random_word:
        letter_counts[char] = letter_counts.get(char, 0) + 1

    # First, check for correct letters
    for i in range(5):
        if guess[i] == random_word[i]:
            indicators[i] = "+"
            letter_counts[guess[i]] -= 1

    # With that done, check for partial letters
    # Look over each letter, if it's not green, check if it can be yellow
    for i in range(5):
        if indicators[i] == "-":
            # If you have at least one of that letter 'left' in the word after your other guesses
            # Then it's yellow, otherwise leave the indicator as-is
            if letter_counts.get(guess[i], 0) > 0:
                indicators[i] = "~"
                letter_counts[guess[i]] -= 1

    return indicators

while (attempts > 0):
    guess = input("").lower()
    # Guess must be 5 characters long and be a valid word
    # You could check it for invalid characters but since we have a list of words...
    if guess not in all_words:
        print("Invalid guess! Please enter a valid 5 letter word.")
    else:
        indicators = check_guess(guess, random_word)
        history.append((guess, indicators))
        print("")
        for past_guess, past_indicators in history:
            print(f"{past_guess} {''.join(past_indicators)}")
        if guess == random_word:
            print("Congratulations! You've guessed the word!")
            break
        attempts -= 1
else:
    print(f"Bad luck! The word was {random_word}")
