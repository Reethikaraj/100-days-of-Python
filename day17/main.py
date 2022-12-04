from data import question_data
from question_model import Question
from random import randint

x = randint(0, len(question_data)-1)
questions = []
score = 0
for i in range(len(question_data) - 1):
    question = Question(question_data[x]["text"], question_data[x]["answer"])
    answer = (input(f'Q.{i+1}: {question.text} True/False '))
    if answer.lower() == question_data[x]["answer"].lower():
        print("You got it Right!")
        print(f'The correct answer was: {question_data[x]["answer"]}')
        score += 1
        print(f"Your current score is {score}/ {i+1}\n")
    else:
        print("Wrong answer!")
        print(f'The correct answer was: {question_data[x]["answer"]}')
        print(f"Your current score is {score}/ {i + 1}\n")
print("Game over!")



