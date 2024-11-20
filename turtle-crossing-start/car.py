from turtle import Turtle, Screen
import random
color = ["red", "blue", "yellow", "green", "black"]
POSITION = [-250, -150, -50, 50, 150, 250]
MOVE_DISTANCE = 5


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.screen.tracer(0)
        self.penup()
        self.shape("square")
        self.color(random.choice(color))
        self.shapesize(stretch_wid=1, stretch_len=2)
        random_y = random.choice(POSITION)
        self.goto(350, random_y)
        self.screen.update()
        self.screen.tracer(1)

    def car_move(self):
        new_x = self.xcor() - MOVE_DISTANCE
        self.goto(new_x, self.ycor())

