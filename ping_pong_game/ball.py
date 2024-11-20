import random
from turtle import Turtle
class Ball(Turtle):
    def __init__(self): # 클래스의 생성자
        super().__init__() # turtle 클래스의 생성자를 호출하여 특징을 모두 가져옴 이제 ball객체는 turtle의 특징을 모두 가짐
        self.color("white")
        self.shape("circle")
        self.penup()
        self.speed = 20
        self.set_random_move()

    def set_random_move(self):
        angle = random.uniform(0.3, 0.7)
        self.x_move = self.speed * angle * random.choice([-1, 1])
        self.y_move = self.speed * (1 - angle) * random.choice([-1, 1])

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def reset_position(self):
        self.goto(0, 0)
        self.set_random_move()
        self.bounce_x()
        self.speed = 20

    def change_angle_on_score(self):
        # 점수가 올라갈 때마다 각도를 변경하여 새로운 움직임을 설정
        self.set_random_move()

