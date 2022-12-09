import turtle
from turtle import Turtle
import pandas as pd

data = pd.read_csv("50_states.csv")

screen = turtle.Screen()
screen.title("US States Game")
screen.addshape("blank_states_img.gif")
turtle.shape("blank_states_img.gif")


class WriteSomething(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.pencolor()
        self.goto(x, y)
        self.pendown()


score_board = WriteSomething(0, 280)
answer_board = WriteSomething(200, 300)
score = 0


def get_mouse_click_color(x, y):
    i = 0
    answer = screen.textinput(title="Guess the state's name", prompt="What is the state's name?").capitalize()
    for state in data.state:
        i += 1
        if answer == state:
            new_x = data.x[i - 1]
            new_y = data.y[i - 1]
            name = turtle.Turtle()
            name.hideturtle()
            name.penup()
            name.goto(new_x, new_y)
            name.write(state)
            global score
            score += 1

            score_board.clear()
            score_board.write(f"Score: {score}", font=("Courier", 25, "normal"))
        else:
            pass


turtle.onscreenclick(get_mouse_click_color)
turtle.mainloop()
