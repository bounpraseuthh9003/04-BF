# BF Base Component


# Functions goes here...
def choice_checker(question, options):
    valid = False
    while not valid:

        # Ask users for their choice (what component they would like to play with)
        response = input(question)
        response = response.lower()

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

# Main routine goes here

# Set up lists
math_list = ["addition", "subtraction", "multiplication", "division"]

# Ask user their choice of ( + , - , x , / ) - check if this is valid

# print out choice for comparison purposes
user_choice = choice_checker("Which one would you like to play with?\n"
                             "A - Addition\n"
                             "S - Subtraction\n"
                             "M - Multiplication\n"
                             "D - Division\n"
                             "= ", math_list)

