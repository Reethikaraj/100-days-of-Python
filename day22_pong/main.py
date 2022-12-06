from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

my_screen = Screen()
my_screen.setup(width=800, height=600)
my_screen.bgcolor('black')
my_screen.title("Welcome to PONG!!")
# To remove the paddle movement from center to that position
my_screen.tracer(0)

paddle_R = Paddle((350, 0))
paddle_L = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

my_screen.listen()
my_screen.onkey(paddle_R.go_up, 'Up')
my_screen.onkey(paddle_R.go_down, 'Down')
my_screen.onkey(paddle_L.go_up, 'w')
my_screen.onkey(paddle_L.go_down, 's')

game_is_on = True
while game_is_on:
    # To remove the paddle movement from center to that position
    time.sleep(0.1)
    my_screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
#     To detect collision with right paddle
    if ball.distance(paddle_R) < 50 and ball.xcor() > 320 or ball.distance(paddle_L)<50 and ball.xcor() < -320:
        ball.bounce_x()

        # Detect R paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

        # Detect L paddle misses:
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

my_screen.exitonclick()
