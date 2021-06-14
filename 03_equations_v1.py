# BF Component 2 - Computer generates random questions based on chosen generator

import random

# values


# functions


# main routine
choice = input("Which one would you like to play with?\n"
               "A - Addition\n"
               "S - Subtraction\n"
               "M - Multiplication\n"
               "D - Division\n"
               "= ")

# associate user choice with correct sign
if choice == "a":
    choice = "+"
    sign = "+"
elif choice == "s":
    choice = "-"
    sign = "-"
elif choice == "m":
    choice = "*"
    sign = "×"
elif choice == "d":
    choice = "/"
    sign = "÷"
else:
    print("Please choose a letter ( A , S , M , D")

# Questions for each maths operation and round
num_1 = random.randint(1, 20)
num_2 = random.randint(1, 20)

# generating the question
print("What is... ")
question = "{} {} {}  ".format(num_1, choice, num_2)
print(question)

# Answers
result = int(input("Answer: "))
answer = eval(question)

# Incorrect or correct

if result == answer:
    feedback = "CORRECT"
    print(feedback)
else:
    feedback = "INCORRECT"
    print(feedback)
    print("The correct answer was {}".format(answer))