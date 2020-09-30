# Hangman GUI
# Version 2.0
# Created by Han
# Finished on 4/5/2020
# Note: Need comments and reorganising code before uploading to GitHub
# Update: Reorganzing and notes completed on 30/9/2020

import random
import tkinter as tk
from tkinter import messagebox

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


def hint_config():
    hint['text'] = "Hints:"
    hint1['text'] = "The word chosen has " + str(len(chosen_word)) + " characters."
    hint2['text'] = "The first letter or the word is " + chosen_word[0] + "."


# function to mask the secret word wth asterisks
def word_masker():

    global chosen_word
    global masked_word

    word_generator()
    hint_config()
    enable()
    root.counter = 15
    result['text'] = ""
    masked_word = ""
    for i in range(len(chosen_word)):
        masked_word += "*"
    wordlabel['text'] = masked_word
    count['text'] = 'Counts: ' + str(root.counter)


# main function to run the Hangman Game 
def main_game(guess):

    global chosen_word
    global masked_word
    # make the masked word into a list so they will be interchangable for verification later
    masked_word_list = [masked_word[i] for i in range(len(chosen_word))]

    if guess in root.usedwords:
        root.counter -= 1
        result['text'] = "You have used the word already"
    elif guess not in chosen_word:
        root.counter -= 1
        result['text'] = "You are wrong!"
        addusedwords(guess)
    elif guess in chosen_word:
        result['text'] = "You are correct!"
        addusedwords(guess)
        for i in range(len(masked_word_list)):
            if chosen_word[i] == guess:
                masked_word_list[i] = guess
        masked_word = ''.join(masked_word_list)
        wordlabel['text'] = masked_word

    count['text'] = 'Counts: ' + str(root.counter)
    output()


# function to show the output of the game in a messagebox 
def output():
    if masked_word == chosen_word:
        disable()
        result['text'] = ""
        messagebox.showinfo("Result", "You've guess the correct word!\nThe secret word is " + chosen_word +"." +"\nPress start to play again!")
    elif root.counter == 0:
        disable()
        result['text'] = ""
        messagebox.showinfo("Result", "You lose!\nThe secret word is " + chosen_word +"." + '\nPress start to play again!')


# function to disable the buttons before the game starts
def disable():
    false = True
    if false == True:
        button1['state'] = tk.DISABLED
        button2['state'] = tk.DISABLED
        button3['state'] = tk.DISABLED
        button4['state'] = tk.DISABLED
        button5['state'] = tk.DISABLED
        button6['state'] = tk.DISABLED
        button7['state'] = tk.DISABLED
        button8['state'] = tk.DISABLED
        button9['state'] = tk.DISABLED
        button10['state'] = tk.DISABLED
        button11['state'] = tk.DISABLED
        button12['state'] = tk.DISABLED
        button13['state'] = tk.DISABLED
        button14['state'] = tk.DISABLED
        button15['state'] = tk.DISABLED
        button16['state'] = tk.DISABLED
        button17['state'] = tk.DISABLED
        button18['state'] = tk.DISABLED
        button19['state'] = tk.DISABLED
        button20['state'] = tk.DISABLED
        button21['state'] = tk.DISABLED
        button22['state'] = tk.DISABLED
        button23['state'] = tk.DISABLED
        button24['state'] = tk.DISABLED
        button25['state'] = tk.DISABLED
        button26['state'] = tk.DISABLED


# function to enable the buttons after the game starts
def enable():
    false = False
    if false == False:
        button1['state'] = tk.NORMAL
        button2['state'] = tk.NORMAL
        button3['state'] = tk.NORMAL
        button4['state'] = tk.NORMAL
        button5['state'] = tk.NORMAL
        button6['state'] = tk.NORMAL
        button7['state'] = tk.NORMAL
        button8['state'] = tk.NORMAL
        button9['state'] = tk.NORMAL
        button10['state'] = tk.NORMAL
        button11['state'] = tk.NORMAL
        button12['state'] = tk.NORMAL
        button13['state'] = tk.NORMAL
        button14['state'] = tk.NORMAL
        button15['state'] = tk.NORMAL
        button16['state'] = tk.NORMAL
        button17['state'] = tk.NORMAL
        button18['state'] = tk.NORMAL
        button19['state'] = tk.NORMAL
        button20['state'] = tk.NORMAL
        button21['state'] = tk.NORMAL
        button22['state'] = tk.NORMAL
        button23['state'] = tk.NORMAL
        button24['state'] = tk.NORMAL
        button25['state'] = tk.NORMAL
        button26['state'] = tk.NORMAL

# Graphical code starts
root = tk.Tk()
root.title("Hangman Game Version 2.0 GUI")

root.counter = 15
root.usedwords = []

# function that runs within root to count the guess 
def addusedwords(guess):
    root.usedwords.append(guess)

# function to reset the counter after the game ends 
def resetcounter():
    count['text'] = 'Counts: ' + str(root.counter)


canvas = tk.Canvas(root, height=800, width=800)
canvas.pack()

frame = tk.Frame(root, bg='#D1F2EB')
frame.place(relheight=1, relwidth=1)

title = tk.Label(root, text='Hangman Game',font='Helvectica 50', relief='flat', bg='#D1F2EB', fg='#0E6251')
title.place(x=150, y=50)

subtitle = tk.Label(root, text='Guess the correct word!',font='Helvectica 15', relief='flat', bg='#D1F2EB', fg='#138D75')
subtitle.place(x=285, y=135)

wordframe =tk.Frame(root,height=90, width=750, bg="#D1F2EB")
wordframe.place(relx=0.035, rely=0.235)

wordlabel = tk.Label(wordframe, anchor='n', font='Helvectica 40', relief='flat', bg="#E8F8F5", fg='#17A589')
wordlabel.place(relheight=1, relwidth=1, rely=0.15)

hintframe = tk.Frame(root, height=130, width=750, bg ='#E8F8F5')
hintframe.place(relx=0.035, rely=0.365)

hint = tk.Label(hintframe, font='Helvectica 25', bg='#E8F8F5', fg='#148F77')
hint.place(relx=0.01, rely=0.01)

hint1 = tk.Label(hintframe, font='Helvectica 25', bg ='#E8F8F5', fg='#148F77')
hint1.place(relx=0.01, rely=0.31)

hint2 = tk.Label(hintframe, font='Helvectica 25', bg ='#E8F8F5', fg='#148F77')
hint2.place(relx=0.01, rely=0.62)

countframe = tk.Frame(root, height=50, width=750, bg ='#E8F8F5')
countframe.place(relx=0.035, rely=0.545)

count = tk.Label(countframe, font='Helvectica 25', bg ='#E8F8F5', fg='#148F77')
count.place(relx=0.01, rely=0.1)

resultframe = tk.Frame(root, height=50, width=750, bg ='#E8F8F5')
resultframe.place(relx=0.035, rely=0.605)

result = tk.Label(resultframe, font='Helvectica 25', bg ='#E8F8F5', fg='#148F77')
result.place(relx=0.01, rely=0.1)

letterframe = tk.Frame(root, height=150, width=750, bg ='#D1F2EB')
letterframe.place(relx=0.035, rely=0.685)

button1 = tk.Button(letterframe, text='A', font='Helvectica 20', relief='flat', bg='#45B39D',fg='white', command=lambda: main_game("A"), state=tk.DISABLED)
button1.place(relx =0.005, rely=0.05,height=60, width=55)

button2 = tk.Button(letterframe, text='B',font='Helvectica 20', relief='flat', bg='#45B39D',fg='white', command=lambda: main_game("B"), state=tk.DISABLED)
button2.place(relx =0.081, rely=0.05,height=60, width=55)

button3 = tk.Button(letterframe, text='C',font='Helvectica 20', relief='flat', bg='#45B39D',fg='white', command=lambda: main_game("C"), state=tk.DISABLED)
button3.place(relx =0.157, rely=0.05,height=60, width=55)

button4 = tk.Button(letterframe, text='D',font='Helvectica 20', relief='flat', bg='#45B39D',fg='white', command=lambda: main_game("D"), state=tk.DISABLED)
button4.place(relx =0.233, rely=0.05,height=60, width=55)

button5 = tk.Button(letterframe, text='E',font='Helvectica 20', relief='flat', bg='#45B39D', fg='white',command=lambda: main_game("E"), state=tk.DISABLED)
button5.place(relx =0.309, rely=0.05,height=60, width=55)

button6 = tk.Button(letterframe, text='F',font='Helvectica 20', relief='flat', bg='#45B39D', fg='white',command=lambda: main_game("F"), state=tk.DISABLED)
button6.place(relx =0.385, rely=0.05,height=60, width=55)

button7 = tk.Button(letterframe, text='G',font='Helvectica 20', relief='flat', bg='#45B39D', fg='white',command=lambda: main_game("G"), state=tk.DISABLED)
button7.place(relx =0.461, rely=0.05,height=60, width=55)

button8 = tk.Button(letterframe, text='H',font='Helvectica 20', relief='flat', bg='#45B39D', fg='white',command=lambda: main_game("H"), state=tk.DISABLED)
button8.place(relx =0.537, rely=0.05,height=60, width=55)

button9 = tk.Button(letterframe, text='I',font='Helvectica 20', relief='flat', bg='#45B39D', fg='white',command=lambda: main_game("I"), state=tk.DISABLED)
button9.place(relx =0.613, rely=0.05,height=60, width=55)

button10 = tk.Button(letterframe, text='J',font='Helvectica 20', relief='flat', bg='#45B39D', fg='white',command=lambda: main_game("J"), state=tk.DISABLED)
button10.place(relx =0.689, rely=0.05,height=60, width=55)

button11 = tk.Button(letterframe, text='K',font='Helvectica 20', relief='flat', bg='#45B39D', fg='white',command=lambda: main_game("K"), state=tk.DISABLED)
button11.place(relx =0.765, rely=0.05,height=60, width=55)

button12 = tk.Button(letterframe, text='L',font='Helvectica 20', relief='flat', bg='#45B39D', fg='white',command=lambda: main_game("L"), state=tk.DISABLED)
button12.place(relx =0.841, rely=0.05,height=60, width=55)

button13 = tk.Button(letterframe, text='M',font='Helvectica 20', relief='flat', bg='#45B39D', fg='white',command=lambda: main_game("M"), state=tk.DISABLED)
button13.place(relx =0.917, rely=0.05,height=60, width=55)

button14 = tk.Button(letterframe, text='N',font='Helvectica 20', relief='flat', bg='#45B39D', fg='white',command=lambda: main_game("N"), state=tk.DISABLED)
button14.place(relx =0.005, rely=0.52,height=60, width=55)

button15 = tk.Button(letterframe, text='O',font='Helvectica 20', relief='flat', bg='#45B39D', fg='white',command=lambda: main_game("O"), state=tk.DISABLED)
button15.place(relx =0.081, rely=0.52,height=60, width=55)

button16 = tk.Button(letterframe, text='P',font='Helvectica 20', relief='flat', bg='#45B39D', fg='white',command=lambda: main_game("P"), state=tk.DISABLED)
button16.place(relx =0.157, rely=0.52,height=60, width=55)

button17 = tk.Button(letterframe, text='Q',font='Helvectica 20', relief='flat', bg='#45B39D', fg='white',command=lambda: main_game("Q"), state=tk.DISABLED)
button17.place(relx =0.233, rely=0.52,height=60, width=55)

button18 = tk.Button(letterframe, text='R',font='Helvectica 20', relief='flat', bg='#45B39D', fg='white',command=lambda: main_game("R"), state=tk.DISABLED)
button18.place(relx =0.309, rely=0.52,height=60, width=55)

button19 = tk.Button(letterframe, text='S',font='Helvectica 20', relief='flat', bg='#45B39D', fg='white',command=lambda: main_game("S"), state=tk.DISABLED)
button19.place(relx =0.385, rely=0.52,height=60, width=55)

button20 = tk.Button(letterframe, text='T',font='Helvectica 20', relief='flat', bg='#45B39D', fg='white',command=lambda: main_game("T"), state=tk.DISABLED)
button20.place(relx =0.461, rely=0.52,height=60, width=55)

button21 = tk.Button(letterframe, text='U',font='Helvectica 20', relief='flat', bg='#45B39D', fg='white',command=lambda: main_game("U"), state=tk.DISABLED)
button21.place(relx =0.537, rely=0.52,height=60, width=55)

button22 = tk.Button(letterframe, text='V',font='Helvectica 20', relief='flat', bg='#45B39D', fg='white',command=lambda: main_game("V"), state=tk.DISABLED)
button22.place(relx =0.613, rely=0.52,height=60, width=55)

button23 = tk.Button(letterframe, text='W',font='Helvectica 20', relief='flat', bg='#45B39D', fg='white',command=lambda: main_game("W"), state=tk.DISABLED)
button23.place(relx =0.689, rely=0.52,height=60, width=55)

button24 = tk.Button(letterframe, text='X',font='Helvectica 20', relief='flat', bg='#45B39D', fg='white',command=lambda: main_game("X"), state=tk.DISABLED)
button24.place(relx =0.765, rely=0.52,height=60, width=55)

button25 = tk.Button(letterframe, text='Y',font='Helvectica 20', relief='flat', bg='#45B39D', fg='white',command=lambda: main_game("Y"), state=tk.DISABLED)
button25.place(relx =0.841, rely=0.52,height=60, width=55)

button26 = tk.Button(letterframe, text='Z',font='Helvectica 20', relief='flat', bg='#45B39D', fg='white',command=lambda: main_game("Z"), state=tk.DISABLED)
button26.place(relx =0.917, rely=0.52,height=60, width=55)

start_button = tk.Button(root, text='Start', font='Helvectica 20', bg='#82E0AA', relief='flat', fg='white',command=lambda: word_masker())
start_button.place(relx=0.435, rely=0.895)

name_label = tk.Label(root, bg='#D1F2EB', fg = '#7D87A6', text ='Version 2.0, created by Han, 4/5/2020', font = 'Helvectica 9')
name_label.place(relx = 0.725, rely = 0.972)

root.mainloop()
# Graphical Code ends