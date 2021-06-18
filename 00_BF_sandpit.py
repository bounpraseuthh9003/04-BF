
# Number Checker - round mechanics


def check_rounds():
    while True:
        response = input("How many questions would you like?: ")

        round_error = "Please enter an integer more than 0 OR press <Enter> for infinite mode."
        if response != "":
            try:
                response = int(response)

                if response < 1:
                    print(round_error)
                    continue

            except ValueError:
                print(round_error)
                continue

        return response


# Main routine goes here...

rounds_played = 0
end_game = "no"
choose_instruction = "Please choose rock (r), paper (p) or scissors (s)"

rounds = check_rounds()

while end_game == "no":

    # Rounds Heading
    print()
    if rounds == "":
        heading = "Continuous Mode: Round {}".format(rounds_played + 1)
        print(heading)
        choose = input("{} or 'xxx' to end: ".format(choose_instruction))
        if choose == "xxx":
            break
    else:
        heading = "Round {} of {}".format(rounds_played + 1, rounds)
        print(heading)
        choose = input(choose_instruction)
        if rounds_played == rounds - 1:
            end_game = "yes"

    print("You chose {}".format(choose))

    rounds_played += 1

print("Thank you for playing")

