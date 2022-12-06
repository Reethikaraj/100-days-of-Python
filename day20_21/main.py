from turtle import Turtle
from turtle import Screen
import time
from random import randint

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


# *************************************************************************************************************************************
class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)


# *************************************************************************************************************************************
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("yellow")
        self.speed('fastest')
        random_x = randint(-200, 200)
        random_y = randint(-200, 200)
        self.goto(random_x, random_y)
        self.refresh()

    def refresh(self):
        random_x = randint(-200, 200)
        random_y = randint(-200, 200)
        self.goto(random_x, random_y)


# *************************************************************************************************************************************

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# *************************************************************************************************************************************
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.clear()
        self.penup()
        self.goto(0, 280)
        self.color('white')

# *************************************************************************************************************************************

score = 0
score_board = ScoreBoard()
game_over = Turtle()
game_over.hideturtle()
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    score_board.write(f"Score = {score}", align='center', font=("Arial", 10, "normal"))
    # Detecting food and eating it
    if snake.head.distance(food) < 15:
        score += 1
        score_board.clear()
        score_board.write(f"Score = {score}", align='center', font=("Arial", 10, "normal"))
        # Generating food in a different place
        food.refresh()
        # Increasing snake length
        snake.extend()
    # If snake collides with wall
    if snake.head.xcor() <= -300 or snake.head.xcor() >= 300 or snake.head.ycor() <= -300 or snake.head.ycor() >= 300:
        game_is_on = False
        game_over.color('white')
        game_over.write(f"Game Over!", align='center', font=("Arial", 20, "normal"))
    # If snake collides itself
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            game_over.color('white')
            game_over.write(f"Game Over!", align='center', font=("Arial", 20, "normal"))

screen.exitonclick()
