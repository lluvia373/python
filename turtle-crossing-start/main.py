import random
import time
from turtle import Screen, Turtle
from car import Car
from scoreboard import Scoreboard
from player import Player
from car import MOVE_DISTANCE

WIDTH = 800
LENGTH = 600
cars = []
CAR_MINIMUM_DISTANCE = 40
is_paused = False
MOVE_DISTANCE_INCREMENT = 10

def increase_difficulty():
    global MOVE_DISTANCE
    current_score = scoreboard.get_score()
    MOVE_DISTANCE += MOVE_DISTANCE_INCREMENT * current_score

player = Player()

def game_end():
    screen.bye()
def game_pause():
    global is_paused
    is_paused = not is_paused

screen = Screen()
screen.listen()
screen.setup(WIDTH,LENGTH)
screen.title("Turtle Crossing")
screen.onkey(game_end, "Escape")
screen.onkey(player.move_up, "Up")
screen.onkey(player.move_down, "Down")
scoreboard = Scoreboard()
scoreboard.update_scoreboard()
screen.onkey(game_pause, "space")



def create_new_car():
    potential_y = random.choice([-250, -150, -50, 50, 150, 250])
    for car in cars:
        # 겹치는지 확인: 기존 차와의 거리 확인
        if abs(car.xcor() - 350) <= CAR_MINIMUM_DISTANCE:
            return  # 거리가 너무 가까우면 새 자동차를 생성하지 않음
    new_car = Car()
    cars.append(new_car)

def game_loop():
    global is_paused

    while True:
        last_car_creation = time.time()
        screen.update()
        time.sleep(0.1)
        if not is_paused:

            if time.time() - last_car_creation > 0.2:
                create_new_car()
                last_car_creation = time.time()

            if player.at_top():
                scoreboard.increase_score()
                increase_difficulty()
                player.goto(0,-280)

            # 일정 확률로 새로운 자동차 생성
            if random.randint(1, 2) == 2:
                create_new_car()

            # 모든 자동차 이동
            for car in cars:
                car.car_move()

            # 사고나면 게임 종료
            for car in cars:
                if car.xcor() > -20 and car.xcor() < 20:
                    if car.ycor() - 20 <  player.ycor() and player.ycor() < car.ycor() + 20:
                        print(score)
                        screen.bye()


game_loop()
screen.exitonclick()


