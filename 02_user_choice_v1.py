# BF Component 1 - Getting input from user (what component they would like to play with)
# Version 1 - Checks users entered valid numbers. The functions then returned the word.


# Functions goes here...
def choice_checker(question):
    valid = False
    while not valid:

        # Ask users for their choice (what component they would like to play with)
        response = input(question)

        if response == "1":
            return response

        elif response == "2":
            return response

        elif response == "3":
            return response

        elif response == "4":
            return response

        else:   # if not in list, says to choose a valid number
            print("Please enter a number between 1-4 ")
            print()

# Main routine goes here

# Ask user their choice of r / p / s - check if this is valid

# print out choice for comparison purposes
for item in range(0, 8):  # run 8 times so I can test all possible options, loops for easier testing
    print()
    user_choice = choice_checker("Which one would you like to play with?\n"
                                 "1 - Addition\n"
                                 "2 - Subtraction\n"
                                 "3 - Multiplication\n"
                                 "4 - Division\n"
                                 "= ")
