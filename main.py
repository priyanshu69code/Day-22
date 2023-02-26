from turtle import Turtle, Screen
from ball import Ball
from paddel import Padel

screen = Screen()
screen.bgcolor("Black")
screen.setup(height=600, width=800)
screen.tracer(0)

# Intiallizing the Ball
ball = Ball()
right_padel = Padel()
left_padel = Padel()
left_padel.goto(-380, 0)
screen.update()


screen.listen()
screen.onkey(right_padel.goto_up, "Up")
screen.onkey(right_padel.goto_down, "Down")
screen.onkey(left_padel.goto_up, "w")
screen.onkey(left_padel.goto_down, "s")
is_gameover = True
while is_gameover:
    screen.update()

screen.exitonclick()
