#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print('Welcome to tip calculator')
bill=input('What was the total bill? $')
tip_percentage=input('What percentage would you like to give for the tip? 10, 12, 15 ')
people=input('How many people are splitting the bill? ')
total_tip = float(tip_percentage)*float(bill)/100
total_bill = float(bill)+ total_tip
share_per_person= total_bill/int(people)
print('Each person should pay ', round(share_per_person, 2))
