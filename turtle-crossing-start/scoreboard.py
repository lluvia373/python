from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("black")
        self.score = 1
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.goto(-300, 250)
        self.write(f"level :  {self.score}", align="center", font=("courier", 24, "normal"))

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()