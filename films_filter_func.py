from film_time_filter import time_filter_turtle
from film_genre_filter import genre_filter_turtle
from film_year_filter import turtle_year
from films_age_filter import age_rating_filter_turtle


def filter_options(filter_dict, filter, x, turtle_, add_on_spots):
    # send the program tothe corect funstion do to number or where clicked
    # also check if it is the turtle version or normal version

    # year filter
    if x < 163 and x > 27:
        year_text = turtle_year(add_on_spots)
        return year_text, 4

    # age rating
    elif x < 3 and x > -117:
        age_rating_filter_turtle()
        return False, 3

    # runtime
    elif x < -137 and x > -234:
        min_text = time_filter_turtle(add_on_spots)
        return min_text,2

    # genre
    elif x < -256 and x > -354:
        genre_filter_turtle(filter_dict)
        return True, 1
  

    # clear the filter
    elif x < 346 and x > 186:
        return None, "clr"

    # nothing
    else:
        pass