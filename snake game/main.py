from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.title("Snake Game")
screen.tracer(0.1)

game_is_on = True
is_paused = False
snake = Snake()
food = Food()
scoreboard = Scoreboard()
def game_pause():
    global is_paused
    is_paused = not is_paused
def game_quit():
    global game_is_on
    game_is_on = False
    screen.bye()
    raise SystemExit

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(game_pause, "space")
screen.onkey(game_quit, "Escape")


while game_is_on:
    if not is_paused:
        screen.update()
        time.sleep(0.1)
        snake.move()

        if snake.head.distance(food) < 13:
            food.refresh()
            snake.extend()
            scoreboard.increase_score()

        if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
            game_is_on = False
            scoreboard.game_over()

        for segment in snake.segments:
            if segment == snake.head:
                pass

            elif snake.head.distance(segment) < 10:
                game_is_on = False
                scoreboard.game_over()
    else:
        screen.update()

