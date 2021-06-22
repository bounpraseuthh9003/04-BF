# BF Component 4 - Computer generates random questions based on chosen generator
import random


# Checks user input (either full word or first letter of word)
def string_checker(question, to_check):

    valid = False
    while not valid:
        # ask user question and change response to lowercase
        response = input(question).lower()

        if response == "xxx":
            return response

        # check response is in list OR that it's the first letter of an item in the list
        for item in to_check:
            if response == item:
                return response
            elif response == item[0]:
                return item

        # if item not in list, print error
        print("sorry that is not a valid response")

# *** Main Routine starts here ***

# lists
math_list = ["a", "s", "m", "d"]

# ask user what they want to play with
choice = string_checker("Which one would you like to play with?\n"
                        "A - Addition\n"
                        "S - Subtraction\n"
                        "M - Multiplication\n"
                        "D - Division\n"
                        "= ", math_list)

# associate user choice with correct sign
if choice == "a":
    choice = "+"
elif choice == "s":
    choice = "-"
elif choice == "m":
    choice = "*"
elif choice == "d":
    choice = "//"

# loop for testing purposes
for item in range(0, 5):  # testing -  loops for easier testing

    # Questions for each maths operation and round
    if choice == "+" or choice == "-":
        num_1 = random.randint(1, 20)
        num_2 = random.randint(1, 20)

    elif choice == "-":
        num_1 = random.choice(1, 20)
        num_2 = random.randint(1, num_1)

    elif choice == "*":
        num_1 = random.randint(1, 12)
        num_2 = random.randint(1, 12)

    else:  # how to get / to same as multiplication?
        num_1 = random.randint(5, 60)
        num_2 = random.randint(5, 60)

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
