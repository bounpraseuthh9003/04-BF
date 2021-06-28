# Base Component - Basic Facts Version 3

import random   # import random for numbers

# Functions go here


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
                        "Please enter a number that is more than (or equal to) {}"
                        .format(low))
                    continue

            return response

        # Checks input is integer
        except ValueError:
            print("Please enter an integer")
            continue


# Checks user input, makes choice lowercase and goes through the list to make sure it is a valid response
def choice_checker(question, valid_list, error):

        valid = False
        while not valid:

            # Ask users for choice - make sure choice is lowercase
            response = input(question).lower()

            # Goes through list, if response is an item in the list
            # (or the first letter of an item), the full item name is returned

            for item in valid_list:
                if response == item[0] or response == item:
                    return item

            # if item not in list, print error
            print(error)


# Decorations to read easily and make it more appealing to users
def statement_generator(statement, decoration, is_heading=None):

    sides = decoration * 3

    statement = "{} {} {}".format(sides, statement, sides)
    top_bottom = decoration * len(statement)

    if is_heading is not None:
        print(statement)

    else:
        print(top_bottom)
        print(statement)
        print(top_bottom)

    return ""

# *** Main Routine starts here ***

# lists
math_list = ["addition", "subtraction", "multiplication", "division", "+", "-", "x", "*", "/"]
yes_no = ["yes", "no"]
game_summary = []

result = ""
feedback = ""
end_game = "no"

# rounds (total , lost , won)
rounds_played = 0
rounds_lost = 0
rounds_won = 0

# Statement for starting game
statement_generator("Welcome to the Basic Facts Game", "*")
print()

# Instructions for new users
instructions = "**** How To Play ****\n" \
               "\n" \
               "We first ask which math operation you would like to play with\n" \
               "\n" \
               "Your choices are:\n" \
               "A - Addition (+)\n" \
               "S - Subtraction (-)\n" \
               "M - Multiplication (x)\n" \
               "D - Division (/)\n" \
               "\n" \
               "Then we ask the amount of questions you would like. This game will gave you\n" \
               "a range of questions with the chosen operator you want to play with.\n " \
               "You can press 'xxx' to end the game if you change your mind.\n" \
               "\n" \
               "This game will give you feedback on whether your answer was correct / incorrect\n" \
               "Try your hardest and test your knowledge! Good luck"

# Ask users if they have played played before. If users type an invalid response, tell them to enter yes / no
see_instructions = choice_checker("Do you want to see the instructions for the game? ", yes_no, "Please enter yes / no")

if see_instructions == "yes":   # if users have not played before display instructions
    print(instructions)
else:
    print("Let's play!")

print()
to_play = input("Press <Enter> to play... ").lower()
print()

# ask user what they want to play with
choice = choice_checker("Which operator would you like to play with?\n"
                        "A - Addition (+)\n"
                        "S - Subtraction (-)\n"
                        "M - Multiplication (x)\n"
                        "D - Division (/)\n"
                        "= ", math_list, "Please enter a letter ( A / S / M / D)")

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
rounds = int_check("How many questions would you like?\n"
                   "Press <Enter> for continuous mode:\n", low=1, exit_code="")

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

    # Break when users enter 'xxx'
    if result == "xxx":
        keep_going = "no"
        break

    games_played = rounds_won + rounds_lost

    # summary of game (question + answer + feedback)
    round_result = "Question {} = ( {}= {} ): {}  ".format(rounds_played, question, result, feedback)
    game_summary.append(round_result)

    # End of Game Statements
    print()
    print('***** End Game Summary *****')
    print("Correct: {} \t|\t Incorrect: {}".format(rounds_won, rounds_lost))

    #  **** Calculate Game Stats ******
    percent_win = rounds_won / games_played * 100
    percent_lose = rounds_lost / games_played * 100

    print()
    print("***** Game Summary *******")
    for game in game_summary:
        print(game)

    print()

    # displays game stats with % values to the nearest whole number
    print("******* Game Statistics ********")
    print("Correct: {}, ({:.0f}%)\nIncorrect: {}, ({:.0f}%)".format(rounds_won, percent_win, rounds_lost, percent_lose))
