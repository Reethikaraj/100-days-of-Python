rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

computer_choice = random.randint(0,2)
my_choice = int(input('What do you want to choose? Type 0 for rock, 1 for paper or 2 for scissors. \n'))
if my_choice == 0:
  print(rock)
elif my_choice == 1:
  print(paper)
elif my_choice == 2:
  print(scissors)


print('Computer chose: \n')
if computer_choice == 0:
  print(rock)
elif computer_choice == 1:
  print(paper)
elif computer_choice == 2:
  print(scissors)

# rock wins against scissors
# scissors wins against paper
# paper wins against rock


if my_choice == 0:
  if computer_choice == 0:
    print('Draw!')
  elif computer_choice == 1:
    print('Computer wins!')
  elif computer_choice == 2:
    print('You win!!')
elif my_choice == 1:
  if computer_choice == 0:
    print('You win!!')
  elif computer_choice == 1:
    print('Draw!')
  elif computer_choice == 2:
    print('Computer wins!')
elif my_choice == 2:
  if computer_choice == 0:
    print('Computer wins!')
  elif computer_choice == 1:
    print('You win!!')
  elif computer_choice == 2:
    print('Draw!')


