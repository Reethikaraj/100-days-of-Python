from turtle import Turtle, Screen
from random import randint

myScreen = Screen()
myScreen.setup(width=500, height=400)
raceOn = False
user_bet = myScreen.textinput(title="Make your bet", prompt="Guess which color turtle wins the race? VIBGYOR: ")
colors = ["violet", "indigo", "blue", "green", "yellow", "orange", "red"]
all_turtles = []

if user_bet:
    raceOn = True


def create_turtles():
    y_axis = 170
    for i in range(7):
        myTurtle = Turtle(shape="turtle")
        myTurtle.color(colors[i])
        myTurtle.penup()
        myTurtle.goto(x=-230, y=y_axis)
        y_axis -= 50
        all_turtles.append(myTurtle)


create_turtles()

while raceOn:

    for t in all_turtles:
        if t.xcor() > 230:
            raceOn = False
            winning_color = t.pencolor()
            if winning_color == user_bet:
                print("Congratulations! You win!")
            else:
                print(f"{winning_color} turtle won the race. You lose the bet.")
        distance = randint(0, 10)
        t.forward(distance)


myScreen.exitonclick()
