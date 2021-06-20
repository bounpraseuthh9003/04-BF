# Component 2 - Rounds mechanics v2


# Function used to check input is valid
def check_rounds():
    while True:
        print()
        response = input("How many questions would you like?\n"
                         "Press <Enter> for continuous mode:\n")

        round_error = "Please enter an integer that is more than 0 OR press <Enter> for continuous mode "  # get rid of "more > 0" ?

        # if user response is not <Enter> continue with chosen number of questions
        if response != "":
            try:
                response = int(response)

                # if response less than 1, print error
                if response < 1:
                    print(round_error)
                    continue

            except ValueError:
                print(round_error)
                continue

        return response


# Main routine goes here

rounds_played = 0
choose_instructions = "equation\n(any integer - testing)"

# Ask users for # of rounds then loop, <enter> for infinite mode
rounds = check_rounds()

end_game = "no"
while end_game == "no":

    # Start of Game Play loop

    # Rounds Heading
    print()
    if rounds == "":
        heading = "Continuous Mode: Round {}".format(rounds_played + 1)
    else:
        heading = "Round {} of {}".format(rounds_played + 1, rounds)

    print(heading)
    choose = input("{} or 'xxx' to end: ".format(choose_instructions))

    # End game if exit code is typed
    if choose == "xxx":
        break

    # rest of loop / game
    print("You chose {}".format(choose))

    rounds_played += 1

    # end game if requested # of rounds has been played
    if rounds_played == rounds:
        break

print()
print("You played {} rounds. Thank you for playing".format(rounds_played))