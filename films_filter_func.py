from film_time_filter import time_filter, time_filter_turtle
from film_genre_filter import genre_filter, genre_filter_turtle
from film_year_filter import year_filter, turtle_year
from films_age_filter import age_rating_filter, age_rating_filter_turtle


def filter_options(filter_dict, filter, x, turtle_, add_on_spots):
    # send the program tothe corect funstion do to number or where clicked
    # also check if it is the turtle version or normal version

    # year filter
    if filter == 1 or (x < 163 and x > 27):
        if turtle_ == True:
            year_text = turtle_year(add_on_spots)

            return year_text, 4

        else:
            year_filter(filter_dict)
            return True

    # age rating
    elif filter == 2 or (x < 3 and x > -117):
        if turtle_:
            age_rating_filter_turtle()
            return False, 3
        else:
            age_rating_filter(filter_dict)
        return True

    # runtime
    elif filter == 3 or (x < -137 and x > -234):
        if turtle_ == True:
            min_text = time_filter_turtle(add_on_spots)
            return min_text,2
        else:
            time_filter(filter_dict)
            return True

    # genre
    elif filter == 4 or (x < -256 and x > -354):
        if turtle_ == True:
            genre_filter_turtle(filter_dict)
            return True, 1
        else:
            genre_filter(filter_dict)
            return True

    # clear the filter
    elif x < 346 and x > 186:
        return None, "clr"

    # nothing
    else:
        pass

def filter_function(filter_dict,x):
    run = True
    while run:
        print("Filter by:\n1.Release Year\n2.Age Rating\n3.Run Time\n4.Genre\n\nEnter = Back")
        # takes user to appropite menu or opens moive list
        try:
            filter = input(">")
            if filter == "":
                run = False
                continue

            filter = int(filter)
            we_good = False
            we_good = filter_options(filter_dict, filter, x)

            if we_good == False:
              print("\n\33[31minvalid\33[00m\n")
        except:
            print("\n\33[31minvalid\33[00m\n")


