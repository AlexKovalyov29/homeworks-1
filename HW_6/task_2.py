"""Exclusive common numbers.
Generate 2 lists with the length of 10 with random integers from 1 to 10,
and make a third list containing the common integers between the 2 initial lists without any duplicates.
Constraints: use only while loop and random module to generate numbers"""

import random

list1 = []
i = 0
while i < 10:
    list1.append(random.randint(1, 10))
    i += 1

list2 = []
i = 0
while i < 10:
    list2.append(random.randint(1, 10))
    i += 1

list3 = list(set(list1) and set(list2))

print("1 list:", list1)
print("2 list:", list2)
print("3 list:", list3)
#не совсем понял суть задания, сделал как понял

