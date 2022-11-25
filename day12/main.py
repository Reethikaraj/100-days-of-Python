import random
import replit
from art import logo



def guess_number():
  print(logo)
  print("\nWelcome to the Number Guessing Game!\nI'm thinking a number between 1 and 100.")
  game_level = input("Choose the game level. Type easy or hard: ")
  computer_number = random.randint(1,100)
  print(computer_number)
  
  if game_level == 'easy':
    num_of_attempts = 10
  if game_level == 'hard':
    num_of_attempts = 5
  
  win = False
  while num_of_attempts > 0 and win==False:
    number = int(input('Make a guess: '))
    if number > computer_number:
      print('Too high.')
      print(f'{num_of_attempts-1} attempts left.')
    elif number < computer_number:
      print('Too low.')
      print(f'Y{num_of_attempts-1} attempts left.')
    elif number == computer_number:
      print("You win !!")
      win = True
    num_of_attempts -= 1

  if num_of_attempts < 1:
    print("Game over. Better luck next time!")

guess_number()
play_again = input("Would you like to play again? y or n: ")
while play_again == 'y':
  replit.clear()
  guess_number()
  
  
    
    
  
  
