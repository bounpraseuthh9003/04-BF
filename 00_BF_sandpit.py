import random

played_before = ""
game_history = ""


# Statement Generator, has top and bottom decoration for headings
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


# Checking round number, must be more than 0
def check_rounds():
    while True:
        response = input("How many rounds: ")
        round_error = "Please type either <enter> or an integer that is more than 0 "

        # If Infinite Play Mode not chosen, check response
        # Make sure it is an integer that is more than 0
        if response != "":
            try:
                response = int(response)

                # If response is too low, go back to
                # start of the loop
                if response < 1:
                    print(round_error)
                    continue

            # If response not an integer, go back to
            # start of the loop
            except ValueError:
                print(round_error)
                continue

        return response


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

# Main routine goes here

# Statement for starting game
statement_generator("Welcome to the Rock Paper Scissors Game", "*")
print()

# Instructions
instructions = "**** How To Play ****\n" \
               "\n" \
               "- Choose the amount of rounds you want to play \n" \
               "or press <enter> for infinite mode\n" \
               "\n" \
               "For each round, choose from rock / paper / scissors (or xxx to quit)\n" \
               "You can type r / p / s / x if you do not want to type the entire word.\n" \
               "\n" \
               "The rules are...\n" \
               "- Rock beats scissors\n" \
               "- Scissors beats paper\n" \
               "- Paper beats rock\n" \
               "\n" \
               "*** Have Fun Playing ***"

# Lists of valid responses
yes_no_list = ["yes", "no"]
rps_list = ["rock", "paper", "scissors", "xxx"]
test_results = ["won", "won", "loss", "loss", "tie"]
summary = []

played_before = choice_checker("Have you played this game before? ", yes_no_list, "Please enter yes / no")

if played_before == "no":
    print(instructions)
else:
    print("Let's play!")


# Ask users for # of rounds then loop...
rounds_played = 0

# lost / draw
rounds_lost = 0
rounds_draw = 0

# Ask users for # of rounds then loop, <enter> for infinite mode
rounds = check_rounds()

end_game = "no"
while end_game == "no":

    # Start of Game Play loop

    # Rounds Heading
    print()
    if rounds == "":
        heading = "======= Infinite Play Mode: Round {} =======".format(rounds_played + 1)
    else:
        heading = "======= Round {} of {} =======".format(rounds_played + 1, rounds)

    print(heading)
    choose_instructions = "Please choose rock (r), paper (p) or scissors (s) or 'xxx' to exit: "
    choose_error = "Please choose from rock / paper / scissors (or xxx to quit)"

    # Ask user for choice and check if it is valid
    user_choice = choice_checker(choose_instructions, rps_list, choose_error)

    # Get computer choice
    comp_choice = random.choice(rps_list[:-1])

    # Compare Choices
    if comp_choice == user_choice:
        result = "tie"
        rounds_draw += 1
        prize_decoration = "T"
    elif user_choice == "rock" and comp_choice == "scissors":
        result = "won"
        prize_decoration = "🏆"
    elif user_choice == "paper" and comp_choice == "rock":
        result = "won"
        prize_decoration = "🏆"
    elif user_choice == "scissors" and comp_choice == "paper":
        result = "won"
        prize_decoration = "🏆"

    # if user chooses 'xxx' and has played one round, exit game
    elif user_choice == "xxx" and rounds_played > 0:
        break

    # if user tries to exit without playing, outputs error
    elif user_choice == "xxx":
        print("You need to play at least one round")
        continue
    else:
        result = "lost"
        rounds_lost += 1
        prize_decoration = "❌"

    if result == "tie":
        feedback = "It's a tie"
        prize_decoration = "😣"
    else:
        feedback = "{} vs {} - you {}".format(user_choice, comp_choice, result)
        summary.append("Round {}: {}".format(rounds_played, feedback))

    statement_generator(feedback, prize_decoration, "yes")

    # rest of loop / game
    rounds_played += 1

    # end game if requested # of rounds has been played
    if rounds_played == rounds:
        break

# If rounds more than 10 rounds, Ask user if they want to see their game history
want_history = choice_checker("Do you want to see your game history? ", yes_no_list, "Please enter yes / no")

if want_history == "yes":
    statement_generator("Game History", "*", "yes")

    for item in summary:
        print(item)

# Show game statistics

# Quick Calculations (stats) - GAME STATISTICS
rounds_won = rounds_played - rounds_lost - rounds_draw

# Quick Calculations (percent) - GAME STATISTICS
percent_win = rounds_won / rounds_played * 100
percent_lose = rounds_lost / rounds_played * 100
percent_tie = rounds_draw / rounds_played * 100

# End of Game statements
print()
print('****** End Game Summary ******')
print("Won: {} \t|\t Lost: {} \t|\t Draw: {}".format(rounds_won, rounds_lost, rounds_draw))
print()

# Game statistics statements
print("******** Game Statistics ********")
print("Won: {}, ({:.0f}%)\nLost: {}, ({:.0f}%)\nDraw: {}, ({:.0f}%)".format(rounds_won, percent_win, rounds_lost,
                                                                         percent_lose, rounds_draw, percent_tie))
print()
print("Thanks for playing")
