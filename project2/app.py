import database
import datetime

menu = '''Please select a number
1. Add new movies.
2. view upcoming movie.
3. view all movie
4. watch a movie
5. view watched movies.
6. Add User
7. Search movie
8. Exit.
'''

select = "Select an Option: "
welcome = "welcome to watchlist app"
print(welcome)
print(menu)
database.create_table()

def prompt_add_movie():
    title = input("Movie title: ")
    release_date = input("Release date (dd-mm-yyyy): ")
    parsed_date = datetime.datetime.strptime(release_date, "%d-%m-%Y")
    timestamp = parsed_date.timestamp()

    database.add_movie(title, timestamp)

def print_movie_list(heading, movies):
    print(f"-- {heading} movies --")
    for movie in movies:
        movie_date = datetime.datetime.fromtimestamp(movie[2])
        human_date = movie_date.strftime("%b %d %Y")
        print(f"{movie[0]}. {movie[1]} (on {human_date})")
    print("--- \n")

def print_watched_list(username, movies):
    print(f"--{username}'s watched movies")
    for movie in movies:
        print(movie[0])
    print("--- \n")

def prompt_watch_movie():
    username = input("username: ")
    movie_id = input("Enter movie id: ")
    database.watch_movie(username, movie_id)

def promp_add_user():
    username = input("username: ")
    database.add_user(username)

def prompt_search_movie():
    movie = input("search movie: ")
    return database.search_movie(movie)


while True:
    n = int(input(select))
    if n == 8:
        break
        exit(0)
    elif n == 1:
        prompt_add_movie()
    elif n == 2:
        print_movie_list("upcoming", database.get_movies(True))
    elif n == 3:
        print_movie_list("All", database.get_movies())
    elif n == 4:
        prompt_watch_movie()
    elif n == 5:
        username = input("username :")
        print_watched_list(username, database.get_watched_movies(username))
    elif n == 6:
        prompt_add_user()
    elif n == 7:
        k = prompt_search_movie()
        print_movie_list("Searched", k)
    else:
        print("Invalid input, please try again.")
    
    




