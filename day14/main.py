from game_data import data
from art import logo
from art import vs
from random import randint
from replit import clear

def play():
  print(logo)
  people = []
  for i in range (2):
    person = data[randint(0,len(data)-1)]
    people.append(person)
  print(f'Compare A: {people[0]["name"]}, {people[0]["description"]} from {people[0]["country"]}.')
  print(vs)
  print(f'Against B: {people[1]["name"]}, {people[1]["description"]} from {people[1]["country"]}.')
  answer = 0
  person_with_more_followers = ''
  for i in range (2):
    # print(f'{people[i]}')
    if people[i]['follower_count'] >= answer:
      answer = people[i]['follower_count']
      person_with_more_followers = people[i]['name']
  # print(f'{person_with_more_followers}, {answer}')
  guess = input("Who has more followers on Instagram? Type A or B ").lower()
  if guess == 'a':
    if people[0]['name'] == person_with_more_followers:
      print("Congratulations!! You win!")
    else:
      print(f"Sorry! Better luck next time! {person_with_more_followers} has more followers. ")
  elif guess == 'b':
    if people[1]['name'] == person_with_more_followers:
      print("Congratulations!! You win!")
    else:
      print(f"Sorry! Better luck next time! {person_with_more_followers} has more followers. ")
  elif guess != 'a' and guess != 'b':
    print("You entered an invalid input. You lose! Play again. ")
    play()
    
play()

play_again = input("Want to play again? y or n ").lower()

def play_again_or_not(play_again):
  if play_again == 'y':
    clear()
    play()
  elif play_again == 'n':
    print("It was nice playing with you!")
    print("Bye! Take care! See you!!!")
  elif play_again != 'y' and play_again != 'n':
    print("Please enter a valid input.")
    play_again_again = input("Want to play again? y or n ")
    play_again_or_not(play_again_again)

play_again_or_not(play_again)
    
