# There will be 10 questions, users should be able to quit anytime using 'xxx' and then display results.
# Users can also play infinite mode where they can press 'xxx' to quit anytime

# Version 2 - continuous mode is added


# Functions

def get_rounds():

  error = "Please enter an integer or press <enter>"

  valid = False

  while not valid:
    print()
    response = input("How many rounds? \nPress <enter> for continuous mode: \n")

    if response == "":
      return("continuous")

    try:
      response = int(response)

      if response > 0:
        return response
      else:
        print(error)

    except ValueError:
      print(error)

num_rounds = get_rounds()
print(num_rounds)
