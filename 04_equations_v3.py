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
math_list = ["addition", "subtraction", "multiplication", "division", "+", "-", "x", "*", "/"]

# ask user what they want to play with
choice = string_checker("Which one would you like to play with?\n"
                        "A - Addition\n"
                        "S - Subtraction\n"
                        "M - Multiplication\n"
                        "D - Division\n"
                        "= ", math_list)

# associate user choice with correct sign
if choice == "addition" or choice == "+":
    choice = "+"
elif choice == "subtraction" or choice == "-":
    choice = "-"
elif choice == "multiplication" or choice == "x" or choice == "*":
    choice = "*"
elif choice == "division" or choice == "/":
    choice = "//"

# loop for testing purposes
for item in range(0, 5):  # testing -  loops for easier testing

    # Questions for each maths operation and round
    num_1 = random.randint(1, 12)
    num_2 = random.randint(1, 12)

    # if operation is ' - ' ensure second # is less than first number
    if choice != "-":
        num_2 = random.randint(1, 12)
    else:
        num_2 = random.randint(1, num_1)

    # generating the question
    print()
    print("What is... ")
    question = "{} {} {} ".format(num_1, choice, num_2)
    answer = eval(question)

    # generating division question
    if choice == "//":
        question = "{} ?? {} ".format(num_1 * num_2, num_2)
        answer = num_1

    # print question and answer
    print(question)
    result = int(input("Answer: "))

    # Incorrect or correct
    if result == answer:
        feedback = "CORRECT"
        print(feedback)
    else:
        feedback = "INCORRECT"
        print(feedback)
        print("The correct answer was {}".format(answer))
