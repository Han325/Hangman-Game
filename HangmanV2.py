# Hangman Game
# Version 2.0
# Created by Han
# Finished on: 10/4/2020

# import random module:
import random


# function to introduce the game and get input from user
def intro_and_user_input():
    print("Welcome to the Hangman Game!")
    print("In this game, the computer will generate a random word from the Sowpods text file for you to guess.")
    print("There are three difficulty levels:\nEasy, Moderate, Hard\n")
    print("Easy - 15 attempts and two hints\nModerate - 9 attempts and one hint\nHard - 6 attempts and no hints\n")


# function to determine difficulty level
def difficulty_config():
    global count
    difficulty = input("Please enter your difficultly level(easy\moderate\hard):\n>>>")

    if difficulty == "easy":
        count = 15
        print("Hint 1:")
        print("The word chosen has " + str(len(chosen_word)) + " characters.")
        print("Hint 2:")
        print("The first letter or the word is " + chosen_word[0] + ".")
    elif difficulty == "moderate":
        count = 9
        print("Hint 1:")
        print("The word chosen has " + str(len(chosen_word)) + " characters.")
    elif difficulty == "hard":
        count = 6
    else:
        print("Invalid input!")
        difficulty_config()


# generates words from sowpods.txt
def word_generator():
    global chosen_word
    with open("sowpods.txt") as f:
        contents_of_file = f.read()
    lines = contents_of_file.splitlines()
    line_number = random.randrange(0, len(lines))
    chosen_word = lines[line_number]
    if len(chosen_word) <6:
        word_generator()


#function to mask the secret word with asterisks:
def word_masker():
    global chosen_word
    # make masked_word variable into a global variable
    global masked_word
    # main process
    masked_word = ""
    for i in range(len(chosen_word)):
        masked_word += "*"


# main function to run the Hangman Game
def main_game():

    global chosen_word
    global masked_word
    global count

    while masked_word != chosen_word and count != 0:
        # make the masked word into a list so they will be switchable for verification
        masked_word_list = [masked_word[i] for i in range(len(chosen_word))]
        print("Word: " + masked_word)
        guess = input("Please guess the letter!\n>>>")
        guess = guess.upper()
        if guess not in chosen_word:
            count -= 1
            if count != 0:
                print("You have " + str(count) + " attempts left.")
                print("Wrong guess! Please try again!")
            else:
                print("")

        elif guess in masked_word_list:
            print("You've already used that letter. Try again with a different letter.")

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
        print("The secret word is " + chosen_word +".")


# function to restart game:
def restart_game():
    choice = input("You have completed the game. Do you wish to play it again? (Yes/No)\n>>>")
    if choice == "Yes":
        word_generator()
        word_masker()
        intro_and_user_input()
        difficulty_config()
        main_game()
        output()
        restart_game()

    elif choice == "No":
        print("Alright then, bye bye!")

    else:
        print("Invalid input.")
        restart_game()


word_generator()
word_masker()
intro_and_user_input ()
difficulty_config()
main_game()
output()
restart_game()