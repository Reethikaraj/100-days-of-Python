############### Blackjack Project #####################
############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import random
import replit
from art import logo

play_game = input('Do you want to play a game of BLACK JACK? y or n? \n ')

  
def play(): 
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  user_cards = []
  dealer_cards = []
  
  def select_user_cards():
    for i in range (0,2):
      user_cards.append(cards[random.randint(0,len(cards)-1)])
    return user_cards
  
  def select_dealer_cards():
    for i in range (0,2):
      dealer_cards.append(cards[random.randint(0,len(cards)-1)])
    return dealer_cards
    
  if play_game == 'y':
    print(logo)
    select_user_cards()
    select_dealer_cards()
    print(f'Your cards:  {user_cards}')
    print(f"Computer's first card: {dealer_cards[0]}")
    another_card = input('Type y to get another card, n to pass. ')
    if another_card == 'y':
      card_3 = cards[random.randint(0,len(cards)-1)]
      if card_3 == 11:
        final_user_score = 0
        for card in user_cards:
          final_user_score += card
        if final_user_score+ card_3 <= 21:
          user_cards.append(card_3)
        else:
           user_cards.append(1)
      user_cards.append(card_3)
      print(f'Your cards:  {user_cards}')
    print(f"Computer's cards: {dealer_cards}")  
    final_user_score = 0
    final_computer_score = 0
    for card in user_cards:
      final_user_score += card
    for card in dealer_cards:
      final_computer_score += card
    if final_user_score > final_computer_score and final_user_score <= 21:
      print("You win!!")
    elif final_user_score == final_computer_score:
      print("It's a Draw!")
    elif final_user_score < final_computer_score or final_user_score > 21:
      print("Computer wins!!")
    another_game = input("Would you like to play another game? y or n ")
    if another_game == 'y':
      play_game == 'y'
      replit.clear()
      play()
play()

  


