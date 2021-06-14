# RPS Component 4 - Set up round mechanics (allow user to choose number of rounds / continuous mode)


def check_rounds():
    while True:
        response = input("How many questions would you like? ")

        round_error = "Please type either <Enter> or an integer that is more than 0"
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

print(" You have asked for {} questions ".format(response))


