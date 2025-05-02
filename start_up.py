import turtle
from films_filter_func import filter_options
from films_start_up import start_up

# make a squar going from the bottom left the right then up
def square(fill_color, length):
    for n in range(2):
        t.fillcolor(fill_color)
        t.begin_fill()
        t.forward(length)
        t.left(90)
        t.forward(25)
        t.left(90)
        t.end_fill()

# makes all clickable buttons not including genre/age rating bar
def buttons():
    t.pendown()
    filters_names = ["Genre", "Run Time", "Age Rating", "Release Year","CLR"]
    length = 100
    count = 0 # slowy increase till it hit 2 where it increase the box size because the text is longer
    first_spot = -355
    diffrent_spots = []
    t.color('white')
    for name in filters_names:
        # check if it clear button if so changes colour to red amkes it more destriquishble
        if name == "CLR":
            color = "red"
        else:
            color = "Black"

        diffrent_spots.append(first_spot) # used to track where the bars are for years and how long the show is
        count += 1
        # goes to where the button starting point is
        t.goto(first_spot,300)
        # check if we need bigger boxs
        if count > 2:
            length += 20
        # makes the shape
        square(color,length)

        # moves back again for text
        t.goto(first_spot+5,300)
        t.write( name, font=("Arial", 16, "bold")) # prints the text
        # moves to the next text button start postion
        first_spot += length + 20

    # speificaly for search button
    t.goto(-355,250) # goes to begin of bottom left of the button
    square("Green",100) # makes the square
    # make text
    t.goto(-350,250)
    t.write( "Search", font=("Arial", 16, "bold"))
    # retrurn diffrent_spots becuase it is ued for the postion of the year filter and runtime filter
    t.penup()
    return diffrent_spots

# this contains all the filters the user added to the moive list and also contain the number to age rating
filter_dict = {
    "age_filter": [],
    "time_filter": 0,
    "year_filter": [],
    "genres_filter": [],
    "all" : [],
    "genres":[],
    1:"G",
    2:"PG",
    3:"R"
}

# take the program to the start up area where it scans the file for diffrent genres width size ect
name_size, genre_size, filter_dict["genres"] = start_up()

# sets up the turtle
screen = turtle.Screen()
t = turtle
t.hideturtle()
t.speed(-100)
screen.tracer(0) # make it so there is no lag
add_on_spots = buttons()

def filter_shower(filter_dict):
    filter_dict["all"] = filter_dict["age_filter"] + filter_dict["year_filter"] + filter_dict["genres_filter"]
    if filter_dict["time_filter"] > 0:
        filter_dict["all"].append(filter_dict["time_filter"])

    length = 120
    first_spot = -235
    y = 250

    t.color('white')

    for name in filter_dict["all"]:
        # check if it clear button if so changes colour to red amkes it more destriquishble
        color = "Blue"
        # goes to where the button starting point is
        t.goto(first_spot,y)
        t.pendown()
        # makes the shape
        square(color,length)
        # moves back again for text
        t.goto(first_spot+5,y)
        t.write( name, font=("Arial", 16, "bold")) # prints the text
        # moves to the next text button start postion
        first_spot += length + 20
        t.penup()


def list():
    t.penup()
    # preset the postion for the begin of the list
    x = -350
    y = 225
    t.goto(x, y) # moves to the begin of the list
    t.color('black') # set colour
    f = open("films.txt","r") # open up where the moive are stored
    # read the file line by line
    for line in f:
        # cleans data
        list = line.split(",")
        for n in range(len(list)):
            list[n] = list[n].strip() # make sure there no white space

        # seprates them
        id      = list[0]
        name    = list[1]
        year    = list[2]
        rating  = list[3]
        runtime = list[4]
        genre   = list[5]


        # pre pair if the test is pass
        test = "|", id, "|", name, "|", year, "|", rating, "|", runtime, "|", genre, "|"
        # goes thre each seprate item and check if it valid with its corsponding filter the turns it into "" if
        # doesnt pass
        if filter_dict["age_filter"]:
            if rating not in filter_dict["age_filter"]:
                test = ""
        if filter_dict["time_filter"] > 0:
            if int(runtime) > filter_dict["time_filter"]:
                test = ""
        if filter_dict["year_filter"]:
            if int(year) not in filter_dict["year_filter"]:
                test = ""
        if filter_dict["genres_filter"]:
            if genre not in filter_dict["genres_filter"]:
                test = ""
        # if it pass the test it will print the line
        if test != "":
            x = -350 # need to be seprate other wise each line will slowy go rigth at the start
            for n in test:
                t.penup()
                t.goto(x, y)
                t.pendown()
                t.write(n, font=("Arial", 10, "bold")) # writes the text
                # gives aqute space
                if n == "|":
                    x += 10
                elif n == id:
                    x += 25
                elif n == name:
                    x += 215
                else:
                    x += 75
            # moves to next line
            y -= 15
    f.close()
    t.penup()


def track_mouse(x, y, blank):
    # i am so sorry i this is so wrong but i cant get it to work any other way
    global genre
    global age

    # check if genres true and if so only check for genre button presses
    if genre:
        current = False
        if x > -351 and x < -231:
            # comedy
            if y > 274 and y < 295:
                current = 1
            # action
            elif y > 247 and y < 274:
                current = 2
            # crime
            elif y > 225 and y < 247:
                current = 3
            # animation
            elif y > 201 and y < 225:
                current = 4
            # fantasy
            elif y > 173 and y < 201:
                current = 5

            # check if a button has been
            if current != False:
                # goes and looks at predefind genres then adds it the filter version
                filter_dict["genres_filter"].append(filter_dict["genres"][current - 1])
            # else it stop the genre slide
            else:
                genre = False
        # else it stop the genre slide
        else:
            genre = False


    # check if age is true and if so only check for age rating button presses
    elif age:
        current = False
        if x > -114 and x < 6:
            # g
            if y > 274 and y < 295:
                current = 1
            # pg
            elif y > 247 and y < 274:
                current = 2
            # r
            elif y > 225 and y < 247:
                current = 3

            # check if a button has been
            if current != False:
                # goes and looks at predefind age rating by number then adds it the filter version
                filter_dict["age_filter"].append(filter_dict[current])
            # else it leaves the coloum
            else:
                age = False
        # else it leaves the coloum
        else:
            age = False

    # thos is the start button it seprated due to the diffret y cordinets
    elif y < 274 and y > 250:
        if x < -255 and x > -356:
            # simply clear the screen
            turtle.clear()
            # then adds everthing back
            buttons()
            # the list does not need to be include due to any click cauing there to be the list

    # if its any of the filter buttons
    elif y < 322 and y > 300:
        # it goes to fil function and find it corect path there the return what is the new filter and what type it is
        # so option = 2008(year) and filter type is 4
        option, filter_type = filter_options(filter_dict, 0, x , True, add_on_spots)
        # check what change needs to happen
        # allows the button to check on genres
        if filter_type == 1:
            genre = True

        # allows the button to check on genres
        if filter_type == 3:
            age = True

        # adds the new year to the year filter
        if filter_type == 4:
            filter_dict["year_filter"].append(int(option))

        # make the new max runtime
        if filter_type == 2:
            filter_dict["time_filter"] = (int(option))

        # reset all filters
        if filter_type == "clr":
            filter_dict["year_filter"].clear()
            filter_dict["time_filter"] = 0
            filter_dict["genres_filter"].clear()
            filter_dict["age_filter"].clear()


    # stop it reseting on genre and age because you will delte bar
    if not genre and not age:
        turtle.clear()
        buttons()
        filter_shower(filter_dict)
        list()

genre = False
age = False
screen.onscreenclick(lambda x, y: track_mouse(x, y, True)) # track where mouse clicks
screen.mainloop()