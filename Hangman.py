# Hangman Game
# Version 1.0
# Created by Han
# Finished on: 11/4/2020

#import random module
import random

# function for game introduction
def intro():
    print("Welcome to the Hangman Game!")
    print("In this game, the computer will generate a random word for you to guess.")
    print("You will six attempts, if you failed to guess the letter.")
    print("")

# Function to generate random word from library
def word_generator():
    #make library variable into a global variable
    global library
    global chosen_word
    library = ["apple", "orange", "pear", "samsung", "google"]
    chosen_word = random.choice(library)

# function to hide the word into asterisks
def word_masker():
    # make masked_word variable into a global variable
    global masked_word
    # main process
    masked_word = ""
    for i in range(len(chosen_word)):
        masked_word += "*"
    print("The secret word is " + masked_word + ".")

# function to check user input
def hangman_execution():
    count = 6
    global chosen_word
    global masked_word
    while masked_word != chosen_word and count != 0:
        #make the masked word into a list so they will be switchable for verification
        masked_word_list = [masked_word[i] for i in range(len(chosen_word))]

        guess = input("Please guess the letter!\n>>>")

        if guess not in chosen_word:
            count -= 1
            if count != 0:
                print("You have " + str(count) + " attempts left.")
                print("Wrong guess! Please try again!")
            else:
                print("")

        elif guess in chosen_word:
            print("You've guess correctly!")
            print("")
            for i in range(len(masked_word_list)):
                if chosen_word[i] == guess:
                    masked_word_list[i] = guess
            masked_word = ''.join(masked_word_list)

# function to show win or lose
def output():
    if masked_word == chosen_word:
        print("The secret word is " + chosen_word +".")
        print("Congratulations! You've guessed the word correctly!")
    else:
        print('You lost.')

intro()
word_generator()
word_masker()
hangman_execution()
output()

