from turtle import Turtle, Screen
import random
screen = Screen()

screen.setup(500,400)

colours = ["red", "orange", "yellow", "green", "blue"]
directions = [0, 90, 180, 270]
all_turtle = []

user_bet = screen.textinput(title = "Make your bet", prompt = "which color win the race select color")
k = 0
for turtle_index in range(5):
    siyun = Turtle(shape = "turtle" )
    siyun.penup()
    siyun.color(colours[turtle_index])
    siyun.goto(x = -230, y = - 100 + k)
    k += 30
    all_turtle.append(siyun)

distance = random.randint(0, 10)
race = True
while race:
    for siyun in all_turtle:
        distance = random.randint(0, 10)
        siyun.forward(distance)
        if siyun.xcor()> 230:
            win_color = siyun.pencolor()
            print(f"win color is {win_color}")
            if user_bet == win_color:
                print("you win")
                race = False
            else:
                print("you lose")
                race = False

# for i in range(3,9):
#     k = 0
#     while k < i:
#         siyun.forward(100)
#         siyun.right(360 / i)
#         k += 1

# for n in range(200):
#     move = random.choice(directions)
#     color = random.choice(colours)
#     siyun.forward(30)
#     siyun.right(move)
#     siyun.color(color)

# for i in range(100):
#     siyun.circle(50)
#     k = 0
#     k += 3.6
#     siyun.right(k)
# def move_forwards():
#     siyun.forward(10)
# screen.listen()
# screen.onkey(key = "space", fun=move_forwards)
#
#
screen.exitonclick()