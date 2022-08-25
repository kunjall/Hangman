import time
import random

name = input("what is your name")
print("hello " + name + " let's play hangman")
print(" ")

time.sleep(1)
print("Start guessing...")
time.sleep(0.5)
words = ['Kunjal' , 'Ananya', 'Aditi', 'Aryan', 'Joel', 'Angad', 'Adrija', 'Shubhangi', 'Kanishk']
word = random.choice(words).lower()

guesses = ''
turns = 10
while turns > 0:
    failed = 0
    for char in word:
        if char in guesses:
            print(char,)
        else:
            print("_")
            failed += 1
    if failed == 0:
        print("you won")

        break

    guess = input("guess a character: ")

    guesses += guess
    if guess not in word:
        turns -= 1
        print("wrong")
        print("you have", turns, "more guesses")
        if turns == 0:
            print("you lose")
            print("the word is", word)
