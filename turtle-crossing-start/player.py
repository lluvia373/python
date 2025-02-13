from turtle import Turtle, Screen

class Player(Turtle):
    def __init__(self):
        super().__init__()
        screen = Screen()
        screen.tracer(0)
        self.penup()
        self.shape("turtle")
        self.left(90)
        self.goto(0, -280)
        screen.tracer(1)

    def move_up(self):
        if self.ycor() >= 280:
            return
        new_y = self.ycor() + 10
        self.goto(0, new_y)

    def move_down(self):
        if self.ycor() <= -280:
            return
        new_y = self.ycor() - 10
        self.goto(0, new_y)

    def at_top(self):
        return self.ycor() > 270

