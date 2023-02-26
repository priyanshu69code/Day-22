from turtle import Turtle


class Padel(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.color("white")
        self.goto(380, 0)

    def goto_up(self):
        new_pos = self.ycor() + 20
        self.goto(self.xcor(), new_pos)

    def goto_down(self):
        new_pos = self.ycor() - 20
        self.goto(self.xcor(), new_pos)
