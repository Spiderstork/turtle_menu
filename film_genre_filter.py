from tkinter import mainloop


def genre_filter(filter_dict):
    run = True
    while run:
        # show genres alreay chosen
        print("\nFilter:", end=" ")
        for n in filter_dict["genres_filter"]:
            print(n, end=" ")
        print()

        # print all posible genres
        num = 1
        print("Genres:")
        for n in filter_dict["genres"]:
            print(num,".",n,end="\n")
            num += 1
        print("c . clear")
        user = input(">")

        # allows it to be cleared or return to main program
        if user == "":
            run = False
            continue
        if user == "c":
            filter_dict["genres_filter"] = []
            continue

        # put in genres to filter dictnary
        try:
            current = int(user)
            if current > 0 and current < 6:
                if filter_dict["genres"][current-1] in filter_dict["genres_filter"]:
                    filter_dict["genres_filter"].remove(filter_dict["genres"][current-1])
                else:
                    filter_dict["genres_filter"].append(filter_dict["genres"][current-1])
        except:
            print("\n\33[31minvalid\33[00m\n")


def genre_filter_turtle(filter_dict):
    import turtle
    # set up turtle
    t = turtle

    # draws shape from top left down then right
    def square_right(fill_color, length):
        for n in range(2):
            t.fillcolor(fill_color)
            t.begin_fill()
            t.forward(125)
            t.right(90)
            t.forward(length)
            t.right(90)
            t.end_fill()

    # set the length and spot
    length = 130
    first_spot = 300
    diffrent_spots = []

    color = "Black"
    diffrent_spots.append(first_spot)
    t.penup()
    t.goto(-355, first_spot)
    t.pendown()
    # makes square
    square_right(color, length)
    # change colour for text
    t.color('white')
    #writes text but moves down each time
    for name in filter_dict["genres"]:
        first_spot -= 25
        t.penup()
        t.goto(-350, first_spot)
        t.pendown()
        t.write(name, font=("Arial", 16, "bold"))
