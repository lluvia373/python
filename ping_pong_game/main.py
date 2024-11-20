from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

TIME_SLEEP = 0.001
SPEED_INCREMENT = 1.1
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Ping Pong Game")
screen.tracer(0)
screen.listen()

right_paddle = Paddle(350, 0)
left_paddle = Paddle(-350, 0)
ball = Ball()
score = Scoreboard()
score_title = Scoreboard()
game_type = Scoreboard()

# 게임 상태를 추적하기 위한 변수
game_is_on = False
is_paused = False
is_best_of_three = False
game_over = False

# 게임 시작 함수
def game_start():
    global game_is_on
    game_is_on = True
    print("게임스타트의 game is on은",game_is_on)
    score_title.clear()
    game_type.clear()
    screen.update()
    game_loop()  # 게임 루프 시작

# 게임 종료 함수
def game_end():
    global game_is_on , game_over
    game_is_on = False
    game_over = True
    ball.reset_position()
    score.left_score = 0
    score.right_score = 0
    score.update_scoreboard()
    screen.bye()

# 일시정지 함수
def toggle_pause():
    global is_paused
    is_paused = not is_paused

# 무한 모드 선택 함수
def select_game_type_1():
    global is_best_of_three, game_is_on , game_over
    # 게임 진행 중에는 동작하지 않도록 설정
    if game_is_on:
        is_best_of_three = False
        game_over = False  # 게임 종료 상태 해제
        game_start()
    game_start()


# 3판 2선승제 선택 함수
def select_game_type_2():

    global is_best_of_three
    # 게임 진행 중에는 동작하지 않도록 설정
    if game_is_on:
        return
    is_best_of_three = True
    game_start()


# 타이틀 화면으로 돌아가는 함수
def go_title():
    global game_is_on
    game_is_on = False
    ball.reset_position()  # 공 위치 초기화
    score.left_score = 0  # 점수 초기화
    score.right_score = 0
    score.update_scoreboard()
    score_title.clear()
    show_start_message()

# 타이틀 메시지 출력 함수
def show_start_message():
    score_title.goto(0, 100)
    score_title.write("무한모드를 선택하려면 1번을 누르세요. 3판2선승제를 원하면 2번을 누르세요.\n종료하려면 Esc 키를 누르세요.",
                      align="center", font=("Courier", 16, "normal"))

# 게임 루프 함수
def game_loop():
    global game_is_on
    print("loop의 game is on", game_is_on)
    while game_is_on:
        screen.update()

        # 게임이 일시정지된 경우 대기
        if is_paused:
            time.sleep(0.1)
            continue

        # 게임이 시작된 이후
        time.sleep(TIME_SLEEP)
        ball.move()

        # 위아래 벽에 충돌 시 반사
        if ball.ycor() > 280 or ball.ycor() < -280:
            ball.bounce_y()

        # 패들과 공의 충돌 감지
        if ((ball.xcor() > 320 and ball.distance(right_paddle) < 35 and ball.x_move > 0)
                or (ball.xcor() < -320 and ball.distance(left_paddle) < 35 and ball.x_move < 0)):
            ball.bounce_x()
            # 공의 속도 증가
            ball.x_move *= SPEED_INCREMENT
            ball.y_move *= SPEED_INCREMENT

        # 공이 화면을 벗어났을 때 점수 갱신
        if ball.xcor() > 380:
            ball.reset_position()
            score.left_point()
        if ball.xcor() < -380:
            ball.reset_position()
            score.right_point()

        # 3판 2선승제 체크
        if is_best_of_three:
            if score.left_score >= 2 or score.right_score >= 2:
                winner = "왼쪽 플레이어" if score.left_score >= 2 else "오른쪽 플레이어"
                score_title.goto(0, 0)
                score_title.write(f"{winner} 승리! 게임 종료", align="center", font=("Courier", 24, "bold"))
                game_is_on = False



# 키 입력 이벤트 설정
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")
screen.onkey(left_paddle.go_up, "W")
screen.onkey(left_paddle.go_down, "S")
screen.onkey(game_end, "Escape")
screen.onkey(toggle_pause, "space")
screen.onkey(select_game_type_1, "1")
screen.onkey(select_game_type_2, "2")
screen.onkey(go_title,"0")

# 타이틀 메시지 출력
show_start_message()
screen.exitonclick()


