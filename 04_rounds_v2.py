# There will be 10 questions, users should be able to quit anytime using 'xxx' and then display results.
# Users can also play infinite mode where they can press 'xxx' to quit anytime

# Version 2 - continuous mode is added


# Functions


def get_rounds():

    error = "Please enter an integer between 1-10"

    valid = False

    while not valid:
        try:
            #   ask the question
            print()
            response = int(input("How many questions would you like between 1-10? \n"
                                 "You can press <Enter> for continuous mode: \n"))
            if response == "":
                return ("continuous")

            if 1 < response <= 10:
                print("You have asked for {} questions ".format(response))
            # if response is 1, say "1 question" instead of "questions"
            elif response == 1:
                print("You have asked for 1 question")

            # output an error
            else:
                print()
                print(error)

        except ValueError:
            print()
            print(error)
