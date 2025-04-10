from turtle import Screen
from classes.paddle import Thanh_truot
from classes.ball import Ball
from classes.score import Score_Player
from utils.constant import LIMIT_TOP, LIMIT_BOTTOM
from utils.key_handler import key_down, key_up, keys_pressed
import time

# Thiết lập màn hình
display = Screen()
display.setup(width=800, height=600)
display.bgcolor("pink")
display.title("Pong")
display.tracer(0)

# Khởi tạo các đối tượng
thanh_truot_phai = Thanh_truot((350, 0), color="#1E90FF")  # Màu xanh dương cho thanh trượt phải
thanh_truot_trai = Thanh_truot((-350, 0), color="#FF4500")  # Màu cam cho thanh trượt trái
ball = Ball()
score = Score_Player()

# Lắng nghe sự kiện bàn phím
display.listen()
display.onkeypress(lambda: key_down("Up"), "Up")
display.onkeyrelease(lambda: key_up("Up"), "Up")
display.onkeypress(lambda: key_down("Down"), "Down")
display.onkeyrelease(lambda: key_up("Down"), "Down")
display.onkeypress(lambda: key_down("w"), "w")
display.onkeyrelease(lambda: key_up("w"), "w")
display.onkeyrelease(lambda: key_up("s"), "s")
display.onkeypress(lambda: key_down("s"), "s")

# Bắt đầu trò chơi
start_game = True
while start_game:
    time.sleep(ball.ball_speed)

    # Kiểm tra trạng thái các phím và di chuyển thanh trượt
    if keys_pressed["Up"]:
        thanh_truot_phai.go_up()
    if keys_pressed["Down"]:
        thanh_truot_phai.go_down()
    if keys_pressed["w"]:
        thanh_truot_trai.go_up()
    if keys_pressed["s"]:
        thanh_truot_trai.go_down()

    display.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.ball_touch_wall()

    # Kiểm tra va chạm với thanh trượt phải
    if ball.xcor() > 340 and ball.distance(thanh_truot_phai) < 50:
        ball.ball_touch_thanh_truot()
        thanh_truot_phai.highlight()  # Thêm hiệu ứng khi bóng chạm thanh trượt phải

    # Kiểm tra va chạm với thanh trượt trái
    if ball.xcor() < -340 and ball.distance(thanh_truot_trai) < 50:
        ball.ball_touch_thanh_truot()
        thanh_truot_trai.highlight()  # Thêm hiệu ứng khi bóng chạm thanh trượt trái

    # Kiểm tra nếu bóng vượt qua thanh trượt phải
    if ball.xcor() > 380:
        ball.reset_Ball()
        score.left_score()

    # Kiểm tra nếu bóng vượt qua thanh trượt trái
    if ball.xcor() < -380:
        ball.reset_Ball()
        score.right_score()

display.exitonclick()
