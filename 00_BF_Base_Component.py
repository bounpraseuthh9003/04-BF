# Base Component


# Functions goes here...
def choice_checker(question, options):
    valid = False
    while not valid:

        # Ask users for their choice (what component they would like to play with)
        response = input(question).lower()

        if response == "a":
            response = "addition"
        elif response == "s":
            response = "subtraction"
        elif response == "m":
            response = "multiplication"
        elif response == "d":
            response = "division"

        if response in options:
            return response
        else:   # if not in list, says to choose a valid letter
            print("Please choose a valid letter ( A - Addition, S - Subtraction, M - Multiplication, D - Division)")
            print()


# Checks input is valid
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


# Main routine goes here

rounds_played = 0
math_list = ["addition", "subtraction", "multiplication", "division"]
choose_instructions = "equation\n(any integer - testing)"


# print out choice for comparison purposes
user_choice = choice_checker("Which one would you like to play with?\n"
                             "A - Addition\n"
                             "S - Subtraction\n"
                             "M - Multiplication\n"
                             "D - Division\n"
                             "= ", math_list)

# Ask users for # of rounds then loop, <enter> for infinite mode
rounds = check_rounds()

end_game = "no"
while end_game == "no":

    # Start of Game Play loop

    # Rounds Heading
    print()
    if rounds == "":
        heading = "Continuous Mode: Round {}".format(rounds_played + 1)
    else:
        heading = "Round {} of {}".format(rounds_played + 1, rounds)

    print(heading)
    choose = input("{} or 'xxx' to end: ".format(choose_instructions))

    # End game if exit code is typed
    if choose == "xxx":
        break

    # rest of loop / game
    rounds_played += 1

    # end game if requested # of rounds has been played
    if rounds_played == rounds:
        break

print()
print("You played {} rounds. Thank you for playing".format(rounds_played))
