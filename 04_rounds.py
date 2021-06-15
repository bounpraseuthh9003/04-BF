# There will be 10 questions, users should be able to quit anytime using 'xxx' and then display results.
# Users can also play infinite mode where they can press 'xxx' to quit anytime

# Version 1 - Makes sure the questions chosen by user is valid and is not too low or too high


# Functions


def get_rounds():

    error = "Please enter an integer between 1-10"

    valid = False

    while not valid:
        try:
            #   ask the question
            print()
            response = int(input("How many questions would you like between 1-10? "))

            if 1 < response <= 10:
                print("You have asked for {} questions ".format(response))
            # if response is 1, say "1 question" instead of "questions"
            elif response == 1:
                print("You have asked for 1 question")
            # return response if user chooses more than 0 questions
            elif response > 0:
                return response

            # output an error
            else:
                print()
                print(error)

        except ValueError:
            print()
            print(error)

# Main Routine
for item in range(0,5):  # run 8 times so I can test all possible options, loops for easier testing
    rounds = get_rounds(int("How many questions would you like between 1-10? "))