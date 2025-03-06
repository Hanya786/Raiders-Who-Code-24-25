# while loop problems answers

# problem #1
def count_to_num():

  count = 0
  # input here is optional. You can just make it any number if you'd like.
  num = int(input("Please give me a number!: "))
  while count < num:
    print(count)
    # count += 1 is the same as count = count + 1
    count += 1

# problem #2
def fill_cup():
  
  max_volume = 100
  current_volume = 0

  while current_volume < max_volume:
    current_volume += 1
    if (max_volume - current_volume) % (max_volume * 0.25) == 0:
      print(current_volume)

# problem #3
def guessing_game():

  print("Welcome to my guessing game! Try guessing a number and we'll see if it was right!")
  correct_num = 5
  player_guess = 0

  while player_guess != correct_num:
    player_guess = int(input("Enter your guess here!: "))
    if player_guess == correct_num:
      break
    print("Sorry, that wasn't right. Try again.")

# problem #3 BONUS

import random

def guessing_game_update():

  # it asks the player to play again if they win.
  playing = True
  print("Welcome to my guessing game! Try guessing a number and we'll see if it was right!")

  while playing:

    # the number is chosen randomly
    correct_num = random.randint(1,20)
    player_guess = 0
    player_chances = 5

    # only a certain number of chances
    while player_chances > 0:
      player_guess = int(input("Enter your guess here!: "))
      if player_guess == correct_num:
        break
      elif abs(correct_num - player_guess) <= 2: # player is close
        print("You're close.")
      elif abs(correct_num - player_guess) >= 10: # player is far
        print("Yikes, you're really far.")
      print("Sorry, that wasn't right.")
      player_chances -= 1

    if player_chances > 0:
      print("Congrats! You did it.")
    else:
      print("Aw. You ran out of tries.")

    # play again?
    responses = ["Y", "N"]
    player_response = ""
    while player_response not in responses:
      player_response = input("Wanna play again? (Y/N): ")
      if player_response == "N":
        print("Okay. Later!")
        playing = False
      elif player_response == "Y":
        print("Okay! Let's play again!")
      else:
        print("Sorry, I don't understand.")
