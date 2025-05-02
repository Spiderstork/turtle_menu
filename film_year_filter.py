def year_filter(filter_dict):
    run = True
    while run:
        # show prechosen year
        print("\nFilter:", end=" ")
        for n in filter_dict["year_filter"]:
            print(n, end=" ")
        print()


        print("Enter = Escape\nc = clear\nEnter year:")
        user = input(">")

        # clears year or return to main program
        if user == "":
            run = False
            continue
        if user == "c":
            filter_dict["year_filter"] = []
            continue

        # adds year to filter dictnary
        try:
            user = int(user.strip())
            filter_dict["year_filter"].append(user)
        except:
            print("\n\33[31minvalid\33[00m\n")

def turtle_year(add_on_spots):
    import turtle
    import time
    from functools import partial

    # set ups turtle
    t = turtle
    screen = turtle.Screen()
    # only uses the year filter start point
    spot = add_on_spots[-2]

    # moves to the start point
    t.penup()
    t.goto(spot,300)
    t.pendown()

    # makes the box going down then right
    t.fillcolor("Black")
    t.begin_fill()
    t.left(90)
    for n in range(2):
        t.right(90)
        t.forward(140)
        t.right(90)
        t.forward(25)
    t.right(90)

    t.end_fill()

    class TextBox:
        def __init__(self, x=25, y=300, w=140, h=25, drawing_pen: turtle.Turtle = None):
            # set the size of text box
            self.x = x
            self.y = y
            self.w = w
            self.h = h

            # Initialize the drawing pen
            if drawing_pen is not None:
                self.pen = drawing_pen
            else:
                self.pen = turtle.Turtle()
                self.pen.hideturtle()
                self.pen.penup()
                self.pen.color("White")
            # pre set of text is empty
            self.text = ""
            self.text_size = int(self.h * 0.4)
            self.blink_timer = time.time()
            self.is_cursor_visible = True
            self.exit_flag = True
            self.active = True

        # allows the user to leave the function
        def exit_program(self):
            self.exit_flag = False

        # add later to text
        def add_letter(self, Letter: str):
            # check if the mouse is on it first
            if not self.active:
                return
            # make sure it doesnt go out side the box
            if len(self.text) <= self.w // self.text_size:
                self.text += Letter

        # removes last later from text
        def remove_letter(self):
            if not self.active:
                return
            self.text = self.text[0: -1]

        # check the mouse is clicked on text thing
        def change_active_state(self, x, y):
            self.active = False
            if self.x <= x <= self.x + self.w:
                if self.y - self.h <= y <= self.y:
                    self.active = True
                    return

        # update the text imagie to include new letters/nums
        def update(self):
            if time.time() - self.blink_timer > 0.5:
                self.blink_timer = time.time()
                self.is_cursor_visible = not self.is_cursor_visible

        # draws the text and the _
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
                # lets its pulse
                if self.is_cursor_visible:
                    text = self.text + "_"
                else:
                    text = self.text + " "
            else:
                if self.text == "":
                    text = "Click to type"
                else:
                    # makes the text
                    text = self.text

            # writes the text to turtle
            self.pen.penup()
            self.pen.goto(self.x + self.w // 2, self.y - self.h * 0.85)
            self.pen.write(text, align="center", font=("consolas", self.text_size, "normal"))

    text_box = TextBox()

    # detect only numbers
    for new_letter in "12345678902":
        func = partial(text_box.add_letter, new_letter)
        screen.onkeypress(func, new_letter)
    screen.onkeypress(text_box.remove_letter, "BackSpace")

    screen.onkey(text_box.exit_program, "Return")

    screen.listen()

    # stops the program if fasle allowing the user to go back
    while text_box.exit_flag:
        text_box.update()
        text_box.draw()
        screen.update()
        time.sleep(0.01)

    return text_box.text




