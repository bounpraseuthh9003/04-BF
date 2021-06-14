# BF Component 2 - Computer generates random questions based on chosen generator
# Version 1

from random import randint

# values
num_1 = ""
num_2 = ""

# functions
def addition():

    num_1 = randint(0,10)
    num_2 = randint(0,10)

    print(f"What is {num_1} + {num_2} ?")
    choice = (input("= "))

    if int(choice) == num_1 + num_2:
      print("correct, nice job! keep on playing")
    else:
      print(f"Incorrect... the answer is {num_1 + num_2}")

def subtraction():

    num_1 = randint(0,10)
    num_2 = randint(0,10)

    print(f"What is {num_1} - {num_2} ?")
    choice = (input("= "))

    if int(choice) == num_1 - num_2:
      print("correct, nice job! keep on playing")
    else:
      print(f"Incorrect... the answer is {num_1 - num_2}")

def multiplication():

    num_1 = randint(0,10)
    num_2 = randint(0,10)

    print(f"What is {num_1} x {num_2} ?")
    choice = (input("= "))

    if int(choice) == num_1 * num_2:
      print("correct, nice job! keep on playing")
    else:
      print(f"Incorrect... the answer is {num_1 * num_2}")

def division():

    num_1 = randint(0,10)
    num_2 = randint(0,10)

    print(f"What is {num_1} / {num_2} ?")
    choice = (input("= "))

    if int(choice) == num_1 / num_2:
      print("correct, nice job! keep on playing")
    else:
      print(f"Incorrect... the answer is {num_1 / num_2}")

# main routine
choice = input("Which one would you like to play with?\n"
"A - Addition\n"
"S - Subtraction\n"
"M - Multiplication\n"
"D - Division\n"
"= ")

if choice == "a":
  addition()
elif choice == "s":
  subtraction()
elif choice == "m":
  multiplication()
elif choice == "d":
  division()
else:
  print("Please choose a letter ( A , S , M , D")
