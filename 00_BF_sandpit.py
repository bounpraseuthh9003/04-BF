# BF Component 1 - Getting input from user (what component they would like to play with)

result = ""


# Functions goes here...
def choice_checker(question):

    valid = False
    while not valid:

        # Ask users for choice
        response = input(question)

        if response == "1":
            result == "+"
            continue
        elif response == "2":
            result == "-"
            continue
        elif response == "3":
            result == "x"
            continue
        elif response == "4":
            result == "÷"
            continue
        else:
            print("Please choose a number between 1-4")

        return response

# Main routine goes here

# Ask user their choice of ( + , - , x , / ) - check if this is valid


# print out choice for comparison purposes
user_choice = choice_checker("Choose 1 for ' + '\n"
                             "Choose 2 for ' - '\n"
                             "Choose 3 for ' x '\n"
                             "Choose 4 for ' ÷ '\n"
                             "\n"
                             "= ")

print("You chose {}".format(result))