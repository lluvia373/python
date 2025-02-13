from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")
HiGH_SCORE_FILE = "highscore.txt"
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = self.load_highscore()
        self.penup()
        self.color("white")
        self.goto(0,270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score} HighScore: {self.highscore}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over", align=ALIGNMENT, font=FONT)
    def increase_score(self):
        self.score += 1
        self.clear()
        if self.score > self.highscore:
            self.highscore = self.score
        self.update_scoreboard()
        self.save_highscore()
    def load_highscore(self):
        try:
            with open(HiGH_SCORE_FILE, "r") as file:
                return int(file.read())
        except FileNotFoundError:
            return 0 # try except 구문 설명

    def save_highscore(self):
        with open(HiGH_SCORE_FILE, "w") as file:
            file.write(str(self.highscore))
