# Task 1
# The greatest number
# Write a Python program to get the largest number from a list of random numbers with the length of 10
# Constraints: use only while loop and random module to generate numbers

import random
from random import randint
a = []
for _ in range(10):
    b = 0
    c = set()
    while len(c) < 10:
        c.add(randint(1, 100))
        b += 1
    a.append(b)
print(a)
print(max(a))

a = [random.randrange(1, 50, 1) for i in range(10)]
print("Випадкові числа : " + str(a))
print(max(a))

# Task 2
# Exclusive common numbers.
# Generate 2 lists with the length of 10 with random integers from 1 to 10, and make a third list containing the common integers between the 2 initial lists without any duplicates.
# Constraints: use only while loop and random module to generate numbers


i = 5

a_list = []
b_list = []
r = set(a_list)
y = set(b_list)

while i != 0:

    j = randint(0, 10)
    k = randint(0, 10)

    a_list.append(j)
    b_list.append(k)

    i -= 1
unique_number1 = list(set(a_list))
unique_number2 = list(set(b_list))

print(a_list + b_list)
print(unique_number1 + unique_number2)


# Task 3
# Extracting numbers.
# Make a list that contains all integers from 1 to 100, then find all integers from the list that are divisible by 7 but not a multiple of 5, and store them in a separate list. Finally, print the list.
# Constraint: use only while loop for iteration/
