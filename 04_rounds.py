# Component 2 - Rounds mechanics v1

# Function used to check input is valid


def check_rounds():
    while True:
        print()
        response = input("How many questions would you like?\n"
                         "Press <Enter> for continuous mode:\n")

        round_error = "Please enter an integer that is more than 0 OR press <Enter> for continuous mode "

        # if user response is <Enter> continue with continous mode
        if response == "":
            print("continuous")

        # if user response is not <Enter> continue with chosen number of questions
        if response != "":
            try:
                response = int(response)

                # if response less than 1, print error
                if response < 1:
                    print(round_error)
                    continue

                # if response is higher than 2 say they have asked for that amount of questions with the plural(s)
                elif response >= 2:
                    print("You have asked for {} questions ".format(response))

                # if response is 1, say "1 question" instead of "questions"
                elif response == 1:
                    print("You have asked for 1 question")

            except ValueError:
                print(round_error)
                continue

        return response


# Main routine goes here

# Ask users for # of rounds then loop, <enter> for infinite mode
rounds = check_rounds()
