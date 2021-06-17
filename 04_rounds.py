# There will be 10 questions, users should be able to quit anytime using 'xxx' and then display results.
# Users can also play infinite mode where they can press 'xxx' to quit anytime

# Version 1 - Makes sure the questions chosen by user is valid and is not too low or too high + continuous


# Functions
def get_rounds():

    error = "Please enter an integer more than 0 OR press <Enter> for infinite mode."

    valid = False
    while not valid:
        try: # fix  try
            # ask the question
            print()
            response = int(input("How many questions would you like? \n"
                                 "You can press <Enter> for infinite mode \n"
                                 "= "))

            if response == "":
                return ("continuous")

            # if response is higher than 2 say they have asked for that amount of questions with the plural(s)
            if response >= 2:
                print("You have asked for {} questions ".format(response))

            # if response is 1, say "1 question" instead of "questions"
            elif response == 1:
                print("You have asked for 1 question")

            else:
                print()
                print(error)

        except ValueError:
            print(error)

num_rounds = get_rounds()
print(num_rounds)