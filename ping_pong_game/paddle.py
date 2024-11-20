from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position_x, position_y):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=0.3)
        self.penup()
        self.goto(position_x, position_y)

    def go_up(self):
        if self.ycor() < 220:
            new_y = self.ycor() + 40
            self.goto(self.xcor(), new_y)

    def go_down(self):
        if self.ycor() > -220:
            new_y = self.ycor() - 40
            self.goto(self.xcor(), new_y)
