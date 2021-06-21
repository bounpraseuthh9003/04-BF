# BF Component 4 - Computer generates random questions based on chosen generator
import random


# functions

def string_checker(question, to_check):
    valid = False
    while not valid:

        response = input(question).lower()

        for item in to_check:
            if response == item:
                return response
            elif response == item[0]:
                return item

        print("Please choose a valid letter ( A - Addition, S - Subtraction, M - Multiplication, D - Division)")
        print()


# *** Main Routine starts here ***

# lists
yes_no = ["yes", "no"]
math_list = ["a", "s", "m", "d"]

# ask user what they want to play with
choice = string_checker("Which one would you like to play with?\n"
                        "A - Addition\n"
                        "S - Subtraction\n"
                        "M - Multiplication\n"
                        "D - Division\n"
                        "= ", math_list).lower()

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
    choice = "//"
    sign = "÷"
else:
    print("Please choose a valid letter ( A - Addition, S - Subtraction, M - Multiplication, D - Division)")
    print()

# loop for testing purposes
for item in range(0, 5):  # testing -  loops for easier testing

    # Questions for each maths operation and round
    if choice == "+" or choice == "-":
        num_1 = random.randint(1, 20)
        num_2 = random.randint(1, 20)

    elif choice == "*":
        num_1 = random.randint(1, 12)
        num_2 = random.randint(1, 12)

    else:  # how to get / to same as multiplication?
        num_1 = random.randint(1, 144)
        num_2 = random.randint(1, 144)

    # generating the question
    print()
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