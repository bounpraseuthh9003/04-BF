
game_summary = []

correct = 0
incorrect = 0

for item in range(0, 5):
  result = input("choose result: ")

  outcome = "Round {}: {}".format(item, result)

  if result == "correct":
    correct += 1
  elif result == "incorrect":
    incorrect += 1

  game_summary.append(outcome)

games_played = correct + incorrect

# **** Calculate Game Stats ******
percent_win = correct / games_played * 100
percent_lose = incorrect / games_played * 100

print()
print("***** Game Summary *******")
for game in game_summary:
  print(game)

print()

# displays game stats with % values to the nearest whole number
print("******* Game Statistics ********")
print("Correct: {}, ({:.0f}%)\nIncorrect: {}, ({:.0f}%)".format(correct, percent_win, incorrect, percent_lose))
