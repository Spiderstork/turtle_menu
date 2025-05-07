def age_rating_filter_turtle():
    # set turtle
    import turtle
    t = turtle

    # draws shape from top left down then right
    def square_right(fill_color, length):
        for n in range(2):
            t.fillcolor(fill_color)
            t.begin_fill()
            t.forward(120)
            t.right(90)
            t.forward(length)
            t.right(90)
            t.end_fill()

    # set the length and spot
    length = 80
    first_spot = 300
    diffrent_spots = []

    color = "Black"
    diffrent_spots.append(first_spot)
    t.penup()
    t.goto(-114, first_spot)
    t.pendown()
    # makes square
    square_right(color, length)
    # change colour for text
    t.color('white')
    # writes text but moves down each time
    for name in ["G","PG","R"]:
        first_spot -= 25
        t.penup()
        t.goto(-110, first_spot)
        t.pendown()
        t.write(name, font=("Arial", 16, "bold"))