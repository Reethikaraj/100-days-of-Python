from turtle import Turtle, Screen

cursor = Turtle()


def move_forward():
    cursor.forward(20)


def clockwise():
    cursor.left(15)
    cursor.forward(20)


def anti_clockwise():
    cursor.right(15)
    cursor.forward(20)


def go_back():
    cursor.back(20)


def clear():
    cursor.speed('fastest')
    cursor.clear()
    cursor.penup()
    cursor.setposition(0, 0)
    cursor.pendown()


screen = Screen()
screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="a", fun=anti_clockwise)
screen.onkey(key="d", fun=clockwise)
screen.onkey(key="s", fun=go_back)
screen.onkey(key="c", fun=clear)
screen.exitonclick()
