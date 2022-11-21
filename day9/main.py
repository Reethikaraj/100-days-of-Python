from replit import clear
#HINT: You can call clear() to clear the output in the console.

print('Welcome to the secret auction program!! \n')
auctions = []

def add_auction():
  new_auction = {}
  new_auction['name'] = input("What is your name? ")
  new_auction['bid'] = int(input("What is your bid? "))
  auctions.append(new_auction)

  
add_auction()
next = input('Are there any other bidders? Yes or No ')
while next.lower() == 'yes':
  clear()
  add_auction()
  next = input('Are there any other bidders? Yes or No ')
# print(auctions)
clear()
max = 0
for i in range (0, len(auctions)):
  if auctions[i]['bid'] > max:
    max = auctions[i]['bid']
    name = auctions[i]['name']

print(f'{name} wins auction with {max} as the highest bid.\n Congratulations {name}!!')
