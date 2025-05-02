def start_up():
    f = open("films.txt","r")
    genres = []
    name_size = 0
    genre_size = 0
    for line in f:
        list = line.split(",")

        # cleans data
        for n in range(len(list)):
            list[n] = list[n].strip()

        name = list[1]
        genre = list[5]

        # to store dffrent genres
        if genre not in genres:
            genres.append(genre)

        # for spacing
        if len(name) > name_size:
            name_size = len(name)
        if len(genre) > genre_size:
            genre_size = len(genre)
    f.close()
    return name_size, genre_size, genres