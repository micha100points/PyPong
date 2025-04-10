from turtle import Turtle

class Thanh_truot(Turtle):
    def __init__(self, position, color="white"):  
        super().__init__()
        self.shape("square")
        self.color(color)  # Đặt màu sắc thanh trượt
        self.shapesize(stretch_wid=6, stretch_len=1)  # Kích thước thanh trượt
        self.penup()
        self.goto(position)
        self.default_color = color  # Lưu màu gốc

    def go_up(self):
        y = self.ycor()
        if y < 250:  # Giới hạn di chuyển thanh trượt lên
            self.sety(y + 20)

    def go_down(self):
        y = self.ycor()
        if y > -240:  # Giới hạn di chuyển thanh trượt xuống
            self.sety(y - 20)

    def highlight(self):  # Thêm hiệu ứng khi bóng chạm thanh trượt
        self.color("yellow")  # Đổi màu thanh trượt thành vàng khi bóng chạm vào
        self.shapesize(stretch_wid=7, stretch_len=1)  # Tăng kích thước thanh trượt
        self.getscreen().ontimer(self.reset_effect, 100)  # Đặt lại hiệu ứng sau 100 ms

    def reset_effect(self):  # Reset hiệu ứng
        self.color(self.default_color)
        self.shapesize(stretch_wid=6, stretch_len=1)
