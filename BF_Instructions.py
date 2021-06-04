# Base component () -


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

# Statement for starting game
statement_generator("Welcome to the Basic Facts Game", "*")
print()

# Instructions for new users
instructions = "**** How To Play ****\n" \
               "\n" \
               "For each game you will be asked to...\n" \
               "- Enter a 'low' and 'high' number. The computer will randomly\n" \
               "generate a 'secret' number between your two chosen numbers.\n" \
               "It will use these numbers for all the rounds in a given game.\n" \
               "- The computer will calculate how many guesses you are allowed\n" \
               "- enter the number of rounds you want to play\n" \
               "- guess the secret number\n" \
               "\n" \
               "Good Luck!"

# List of valid responses
yes_no_list = ["yes", "no"]
scores = []

played_before = choice_checker("Have you played this game before? ", yes_no_list, "Please enter yes / no")
if played_before == "no":
    print(instructions)
else:
    print("Let's play!")

print()
to_play = input("Press <Enter> to play... ").lower()
print()