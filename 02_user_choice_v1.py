# BF Component 1 - Getting input from user (what component they would like to play with)


# Functions goes here...
def choice_checker(question):

    valid = False
    while not valid:

        # Ask users for their choice (what component they would like to play with)
        response = input(question)

        if response == "1":
            response = "+"
            return response
        elif response == "2":
            response = "-"
            return response
        elif response == "3":
            response = "x"
            return response
        elif response == "4":
            response = "÷"
            return response
        else:
            print("Please choose a number between 1-4")
            print()

# Main routine goes here

# Ask user their choice of ( + , - , x , / ) - check if this is valid

# print out choice for comparison purposes
for item in range(0, 5):    # run 5 times so I can test all possible options
    user_choice = choice_checker("Choose 1 for ' + '\n"
                                 "Choose 2 for ' - '\n"
                                 "Choose 3 for ' x '\n"
                                 "Choose 4 for ' ÷ '\n"
                                 "\n"
                                 "= ")
    print("You chose {}".format(user_choice))
