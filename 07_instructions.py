# Base component 7 - Ask users if they have played before.
# If they say yes, program continues. If they say no, display instructions
# if they say something else, print error <please say yes or no>


#  Makes user choice lowercase and goes through the list and make sure it is a valid response
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

                    # Output error if item not in list
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

# Main Routine

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

# List of valid responses
yes_no_list = ["yes", "no"]

# Ask users if they have played played before. If users type an invalid response, tell them to enter yes / no
see_instructions = choice_checker("Do you want to see the instructions for the game? ", yes_no_list, "Please enter yes / no")

if see_instructions == "yes":   # if users have not played before display instructions
    print(instructions)
else:
    print("Let's play!")

print()
to_play = input("Press <Enter> to play... ").lower()
