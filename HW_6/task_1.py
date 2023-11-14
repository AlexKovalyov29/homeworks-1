"""The greatest number
Write a Python program to get the largest number from a list of random numbers with the length of 10
Constraints: use only while loop and random module to generate numbers"""
import random

list_number = [1,2,3,4,5,6,7,8,9,10]
#print(type(random.choice(list_number)))
while random.choice(list_number):
    if max(list_number) == 10:
        print(True)
        break
