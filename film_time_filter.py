def time_filter_turtle(add_on_spots):
    import turtle
    import time
    from functools import partial

    t = turtle
    spot = add_on_spots[-4]

    t.penup()
    t.goto(spot, 300)
    t.pendown()

    t.fillcolor("Black")
    t.begin_fill()
    t.left(90)
    for n in range(2):
        t.right(90)
        t.forward(100)
        t.right(90)
        t.forward(25)
    t.right(90)

    t.end_fill()

    screen = turtle.Screen()

    class TextBox:
        def __init__(self, x=spot, y=300, w=100, h=25, drawing_pen: turtle.Turtle = None):
            self.x = x
            self.y = y
            self.w = w
            self.h = h
            if drawing_pen is not None:
                self.pen = drawing_pen
            else:
                self.pen = turtle.Turtle()
                self.pen.hideturtle()
                self.pen.penup()
                self.pen.color("White")
            self.text = ""
            self.text_size = int(self.h * 0.4)
            self.blink_timer = time.time()
            self.is_cursor_visible = True
            self.exit_flag = True
            self.active = True

            # Define the exit function

        def exit_program(self):
            self.exit_flag = False

        def add_letter(self, Letter: str):
            if not self.active:
                return
            if len(self.text) <= self.w // self.text_size:
                self.text += Letter

        def remove_letter(self):
            if not self.active:
                return
            self.text = self.text[0: -1]

        def change_active_state(self, x, y):
            self.active = False
            if self.x <= x <= self.x + self.w:
                if self.y - self.h <= y <= self.y:
                    self.active = True
                    return

        def update(self):
            if time.time() - self.blink_timer > 0.5:
                self.blink_timer = time.time()
                self.is_cursor_visible = not self.is_cursor_visible

        def draw(self):
            self.pen.clear()
            self.pen.penup()
            self.pen.goto(self.x, self.y)
            self.pen.pendown()
            for i in range(2):
                self.pen.forward(self.w)
                self.pen.right(90)
                self.pen.forward(self.h)
                self.pen.right(90)

            if self.active:
                if self.is_cursor_visible:
                    text = self.text + "_"
                else:
                    text = self.text + " "
            else:
                if self.text == "":
                    text = "Click to type"
                else:
                    text = self.text

            self.pen.penup()
            self.pen.goto(self.x + self.w // 2, self.y - self.h * 0.85)
            self.pen.write(text, align="center", font=("consolas", self.text_size, "normal"))

    text_box = TextBox()

    for new_letter in "12345678902":
        func = partial(text_box.add_letter, new_letter)
        screen.onkeypress(func, new_letter)
    screen.onkeypress(text_box.remove_letter, "BackSpace")

    screen.onkey(text_box.exit_program, "Return")

    screen.listen()

    while text_box.exit_flag:
        text_box.update()
        text_box.draw()
        screen.update()
        time.sleep(0.01)

    return text_box.text


