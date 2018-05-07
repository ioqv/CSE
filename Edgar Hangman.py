"""
A general guide for Hangman
1.Make a word bank - 10 items
2.Pick a random item from the list
3.Hide the word (use *)4.Reveal letters already guessed
5.Create the win condition
"""
import string
import random

guesses_left = 10

list_word = ["School", "House", "Computer", "Dog", "Cat", "Eat", "Hospital", "supreme", "pencil","truck", "Soccer"]
random_word = random.choice(list_word)
letters_guessed = []
ranged_word = len(random_word)
print(random_word)
guess = ""
correct = list(random_word)

guess = ""
while guess != "quit":
    output = []
    for letter in random_word:
        if letter in letters_guessed:
            output.append(letter)
        else:
            output.append("*")
    print(" ".join(list(output)))

    guess = input("Guess a letter: ")
    letters_guessed.append(guess)
    print(letters_guessed)

    if guess not in random_word:
        guesses_left -= 1
        print(guesses_left)
    if output == correct:
        print ("You win")
        exit(0)
    if guesses_left == 0:
        print("you loose")
    Guesses = input("Guesses a letter:")
    print("These are your letter %s" % letters_guessed)

    lower = Guesses.lower()
    letters_guessed.append(lower)