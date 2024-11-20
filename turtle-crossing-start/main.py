import random
import time
from turtle import Screen, Turtle
from car import Car
from scoreboard import Scoreboard
from player import Player

WIDTH = 800
LENGTH = 600
cars = []
CAR_MINIMUM_DISTANCE = 5


player = Player()

def game_end():
    screen.bye()

screen = Screen()
screen.listen()
screen.setup(WIDTH,LENGTH)
screen.title("Turtle Crossing")
screen.onkey(game_end, "Escape")
screen.onkey(player.move_up, "Up")
screen.onkey(player.move_down, "Down")
scoreboard = Scoreboard()
scoreboard.update_scoreboard()

def create_new_car():
    potential_y = random.choice([-250, -150, -50, 50, 150, 250])
    for car in cars:
        # 겹치는지 확인: 기존 차와의 거리 확인
        if abs(car.ycor() - potential_y) < CAR_MINIMUM_DISTANCE:
            return  # 거리가 너무 가까우면 새 자동차를 생성하지 않음
    new_car = Car()
    cars.append(new_car)

def game_loop():
    while True:
        screen.update()
        time.sleep(0.001)

        if player.at_top():
            scoreboard.increase_score()
            player.goto(0,-280)

        # 일정 확률로 새로운 자동차 생성
        if random.randint(1, 6) == 6:
            create_new_car()

        # 모든 자동차 이동
        for car in cars:
            car.car_move()

        # 사고나면 게임 종료
        for car in cars:
            if car.xcor() > -20 and car.xcor() < 20:
                if car.ycor() - 20 <  player.ycor() and player.ycor() < car.ycor() + 20:
                    screen.bye()


game_loop()
screen.exitonclick()


