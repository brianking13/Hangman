#script plays a game of hangman

from os import system, name
from time import sleep
import re

def clear():
    if name == "nt":
        _ = system('cls')


def guessing_time(word, the_word):
    global run, turns, guesses
    guesses = []
    run = True
    while run == True:
        print("")
        guess = input("Guess a letter: ")
        guess = guess.lower()
        guesses.append(guess)
        clear()
        if guess.isalpha() == True and len(guess) == 1:
            are_they_right(word, guess, the_word)
        else:
            print("That's not letter. If you need help, try looking up the word \"letter\" in a dictionary.")
            print("")
            print("You have " + str(turns) + " turns left...")
            print("")
            print("You have already guessed " + str(guesses))


def set_up(word):
    global call, turns
    turns = 5
    print("")
    call = input("What is your name? ")
    print("")
    print("Okay " + str(call) + ", here are the rules:")
    print("You have five wrong guesses and you have to guess all the letters in the word. If you don't guess them... well let's just say you should lock your door tonight.")
    word = word.lower()
    print("")
    the_word = ["_  "] * len(word)
    print(" ".join(the_word))
    print("")
    guessing_time(word, the_word)


def are_they_right(word, guess, the_word):
    global count
    count = 0
    for n in re.finditer(guess, word):
            the_word[n.start()] = guess
            count = count + 1
    if count == 0:
            wrong(word, the_word)
    elif word == "".join(the_word):
        are_equal(word, the_word)
    else:
        print("")
        print("   ".join(the_word))
        print("")
        print("You have " + str(turns) + " wrong guesses left...")
        print("")
        print("You have already guessed " + str(guesses))


def wrong(word,the_word):
    global run, turns
    turns = turns - 1
    if turns == 0:
        print("")
        print("You lost. You LOST " + str(call) + ". You are so dumb.")
        print("")
        print("The word was actually " + str(word))
        run = False
    else:
        print("")
        print("Sorry, that letter is not in the word.")
        print("")
        print("".join(the_word))
        print("")
        print("You have " + str(turns) + " wrong guesses left...")
        print("")
        print("You have already guessed " + str(guesses))


def are_equal(word, the_word):
    global run, call, turns, count
    global run
    print("")
    print("Yup, " + str(word) + " was the word!")
    print("")
    print("You have won " + str(call) + "! Great job.")
    run = False
    sleep(10)
    return




def game(word):
        set_up(word)




game("Test")    # word player is attempting to correctly guess
