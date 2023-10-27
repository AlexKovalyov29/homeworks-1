"""The Guessing Game.
Write a program that generates a random number between 1 and 10 and lets the user guess what number was generated.
The result should be sent back to the user via a print statement."""

import random


player =int(input("Let`s try to guess the number:"))
target_number = random.randint(1,10)
if player == target_number:
    print("ok")
else:
    print('wrong',target_number)


