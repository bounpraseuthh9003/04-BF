# RPS Component 5 - Score mechanics

import random

# Functions go here


# Function used to check input is valid
def check_rounds():
    while True:
        print()
        response = input("How many questions would you like?\n"
                         "Press <Enter> for continuous mode:\n")

        round_error = "Please enter an integer that is more than 0 OR press <Enter> for continuous mode "

        # if user response is not <Enter> continue with chosen number of questions
        if response != "":
            try:
                response = int(response)

                # if response less than 1, print error
                if response < 1:
                    print(round_error)
                    continue

            except ValueError:
                print(round_error)
                continue

        return response


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


# Checks that the user has valid answers for each question
def int_check(question, low=None, high=None, exit_code=None):

    valid = False
    while not valid:
        response = input(question).lower()

        if exit_code == "xxx" and response == "xxx":
            return response
        elif exit_code == "" and response == "":
            return response

        situation = ""

        if low is not None and high is not None:
            situation = "both"
        elif low is not None and high is None:
            situation = "low only "

        try:
            response = int(response)

            # are specified
            if situation == "both":
                if response < low or response > high:
                    print("Please enter a number between {} and {}".format(
                        low, high))
                    continue

            # checks input is not too low
            elif situation == "low only ":
                if response < low:
                    print(
                        "Plese enter a number that is more than (or equal to) {}"
                        .format(low))
                    continue

            return response

        # Checks input is integer
        except ValueError:
            print("Please enter an integer")
            continue

# *** Main Routine starts here ***

# lists
math_list = ["addition", "subtraction", "multiplication", "division", "+", "-", "x", "*", "/"]
result = ""
feedback = ""
end_game = "no"

# rounds (total , lost , won)
rounds_played = 0
rounds_lost = 0
rounds_won = 0

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

# Play Game
rounds = check_rounds()

while end_game == "no":

    # Start of Game Play loop

    # Rounds Heading
    print()
    if rounds == "":
        heading = "Continuous Mode: Round {}".format(rounds_played + 1)
    else:
        heading = "Round {} of {}".format(rounds_played + 1, rounds)

        # end game if # of rounds has been played
        if rounds_played == rounds - 1:
            end_game = "yes"

    print(heading)

    # rest of loop / game
    rounds_played += 1  # This must be AFTER the break otherwise the rounds won calculation will be incorrect.

    # Questions for each maths operation and round
    num_1 = random.randint(1, 12)
    num_2 = random.randint(1, 12)

    # if operation is ' - ' ensure second # is less than first number
    if choice != "-":
        num_2 = random.randint(1, 12)
    else:
        num_2 = random.randint(1, num_1)

    # generating the question
    print("What is... ")
    question = "{} {} {} ".format(num_1, choice, num_2)
    answer = eval(question)

    # generating division question
    if choice == "//":
        question = "{} ÷ {} ".format(num_1 * num_2, num_2)
        answer = num_1

    # print question and answer
    print(question)
    result = int_check("Answer: ", exit_code="xxx")

    # Break when users enter 'xxx'
    if result == "xxx":
        keep_going = "no"
        break

    # Incorrect or correct
    if result == answer:
        feedback = "CORRECT"
        print(feedback)
        rounds_won += 1
    else:
        feedback = "INCORRECT"
        print(feedback)
        print("The correct answer was {}".format(answer))
        rounds_lost += 1


# End of Game Statements
print()
print('***** End Game Summary *****')
print("Correct: {} \t|\t Incorrect: {}".format(rounds_won, rounds_lost))
print("Thanks for playing")
