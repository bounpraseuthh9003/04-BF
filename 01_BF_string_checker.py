# string checker, checks user input is valid


# Checks user input (either full word or first letter of word)
def string_checker(question, to_check):

    valid = False
    while not valid:
        # ask user question and change response to lowercase
        response = input(question).lower()

        if response == "xxx":
            return response

        # check response is in list OR that it's the first letter of an item in the list
        for item in to_check:
            if response == item:
                return response
            elif response == item[0]:
                return item

        # if item not in list, print error
        print("sorry that is not a valid response")


# *** Main Routine starts here ***

yes_no = ["yes", "no"]
math_list = ["addition", "subtraction", "multiplication", "division"]

mood = string_checker("Are you happy? ", yes_no)
print(mood)
print()

choose = string_checker("Choose: ", math_list)
print(choose)
