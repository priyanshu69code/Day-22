from turtle import Turtle


class Padel(Turtle):
    def __init__(self, x_cor, y_cor):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.color("white")
        self.goto(x_cor, y_cor)

    def goto_up(self):
        new_pos = self.ycor() + 20
        self.goto(self.xcor(), new_pos)

    def goto_down(self):
        new_pos = self.ycor() - 20
        self.goto(self.xcor(), new_pos)
