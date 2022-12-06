import turtle
from turtle import Turtle, Screen
from random import choice, randint
import colorgram

turtle.colormode(255)
my_turtle = Turtle()
my_turtle.shape("turtle")
direction = [0, 90, 180, 270]


def rgb_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return r, g, b


def extract_colors():
    """Extracting colors from an image, storing them as an array of tuples.  rgb_colors=[(),(),.....]"""
    colors = colorgram.extract('dot_painting.jpg', 100)
    rgb_colors = []
    for color in colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        rgb = (r, g, b)
        rgb_colors.append(rgb)
    return rgb_colors


def draw_square(x):
    for i in range(4):
        print({turtle.position()})
        my_turtle.forward(x)
        my_turtle.right(90)


# draw_square(100)
# turtle.goto(10, 10)

def draw_dashed_line(x):
    for i in range(x):
        if i % 2 == 0:
            my_turtle.pendown()
            my_turtle.forward(10)
        else:
            my_turtle.penup()
            my_turtle.forward(10)


# draw_dashed_line(200)

def draw_closed_figures():
    for i in range(3, 15):
        angle = 360 / i
        my_turtle.pencolor(rgb_color())
        for n in range(i):
            my_turtle.forward(100)
            my_turtle.right(angle)


# draw_closed_figures()


def random_walk(x):
    my_turtle.pensize(10)
    for i in range(x):
        my_turtle.pencolor(rgb_color())
        my_turtle.forward(30)
        my_turtle.setheading(choice(direction))


# random_walk(60)

def draw_spirograph(x):
    my_turtle.speed('fastest')
    for i in range(36):
        my_turtle.pencolor(choice(extract_colors()))
        my_turtle.circle(x)
        my_turtle.right(10)


# draw_spirograph(50)


def draw_dots():
    my_turtle.speed('fastest')
    for i in range(10):
        my_turtle.pencolor(choice(extract_colors()))
        my_turtle.dot(20)
        my_turtle.penup()
        my_turtle.forward(50)


def draw_dots_multiple_lines():
    for i in range(10):
        draw_dots()
        my_turtle.left(90)
        my_turtle.forward(50)
        my_turtle.left(90)
        my_turtle.forward(500)
        my_turtle.right(180)


draw_dots_multiple_lines()
screen = Screen()
screen.exitonclick()
