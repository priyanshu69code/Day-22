from turtle import Screen
from ball import Ball
from paddel import Padel
import time
from scoreboard import Scoreboard

SLEEP_TIME = 0.2
screen = Screen()
screen.bgcolor("Black")
screen.setup(height=600, width=800)
screen.tracer(0)

# Intiallizing the Ball
ball = Ball()
right_padel = Padel(350, 0)
left_padel = Padel(-350, 0)
scoreboard = Scoreboard()
# left_padel.goto(-380, 0)
screen.update()


screen.listen()
screen.onkey(right_padel.goto_up, "Up")
screen.onkey(right_padel.goto_down, "Down")
screen.onkey(left_padel.goto_up, "w")
screen.onkey(left_padel.goto_down, "s")


is_gameover = True
while is_gameover:
    ball.move()
    screen.update()
    time.sleep(SLEEP_TIME)

    # Detecting Collision with Up and Down Walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detecting Collision with Paddels and Bouncing the ball
    if ball.distance(right_padel) < 50 and ball.xcor() > 320 or ball.distance(left_padel) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        SLEEP_TIME /= 1.1

    # Detecting if Right Paddel missess the ball
    if ball.xcor() > 380:
        ball.reset_poss()
        scoreboard.l_point()
        SLEEP_TIME = 0.2

    # Detecting if Left Paddel missess the Ball
    if ball.xcor() < -380:
        ball.reset_poss()
        scoreboard.r_point()
        SLEEP_TIME = 0.2

    if scoreboard.l_score == 10 or scoreboard.r_score == 10:
        print("Game Over")
        is_gameover = False


screen.exitonclick()
