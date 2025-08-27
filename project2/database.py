import sqlite3
import datetime

CREATE_TABLE_MOVIES = '''CREATE TABLE IF NOT EXISTS movies(
id INTEGER PRIMARY KEY,
title TEXT, 
release_date REAL
);'''
CREATE_USER_TABLE = "CREATE TABLE IF NOT EXISTS users(username TEXT PRIMARY KEY);"

CREATE_WATCHLIST_TABLE = '''CREATE TABLE IF NOT EXISTS watched(
name TEXT, 
movie_id INTEGER,
FOREIGN KEY (name) REFERENCES users(name),
FOREIGN KEY (movie_id) REFERENCES movies(id)
);'''
# CREATE_WATCHLIST_TABLE = '''CREATE TABLE IF NOT EXISTS watched(
# name TEXT, 
# title TEXT
# );'''
connection = sqlite3.connect("data1.db")

INSERT_MOVIES = "INSERT INTO movies (title, release_date) VALUES (?,?);"
DELETE_MOVIE = "DELETE FROM movies WHERE title = ?;"
SELECT_ALL_MOVIES = "SELECT * FROM movies;"
SELECT_UPCOMING_MOVIES = "SELECT * FROM movies WHERE release_date > ?;"
# SELECT_WATCHED_MOVIES = "SELECT * FROM watched WHERE name = ?;"
SELECT_WATCHED_MOVIES = '''SELECT movies.title 
FROM watched 
JOIN movies ON watched.movie_id = movies.id 
WHERE watched.name = ?;
'''
# SET_MOVIES_WATCHED = "UPDATE movies SET watched = 1 WHERE title =?;"
INSERT_WATCHED_MOVIE = "INSERT INTO watched (name, movie_id) VALUES(?, ?);"
INSERT_USER = "INSERT INTO users VALUES(?);"
SEARCH_MOVIE = "SELECT * FROM movies WHERE title LIKE ?;"
CREATE_RELEASE_INDEX = "CREATE INDEX IF NOT EXISTS idx_movies_release ON movies(release_timestamp);"


def create_table():
    with connection:
        connection.execute(CREATE_TABLE_MOVIES)
        connection.execute(CREATE_USER_TABLE)
        connection.execute(CREATE_WATCHLIST_TABLE)


def add_movie(title, release_date):
    with connection:
        connection.execute(INSERT_MOVIES,(title, release_date))

def get_movies(upcoming=False):
    with connection:
        cursor = connection.cursor()
        if upcoming:
            today_timestamp = datetime.datetime.today().timestamp()
            cursor.execute(SELECT_UPCOMING_MOVIES, (today_timestamp,))
        else:
            cursor.execute(SELECT_ALL_MOVIES)
        return cursor.fetchall()

def watch_movie(username, movie_id):
    with connection:
        # connection.execute(DELETE_MOVIE, (title,))
        connection.execute(INSERT_WATCHED_MOVIE, (username, movie_id))

def get_watched_movies(username):
    with connection:
        cursor = connection.cursor()
        cursor.execute(SELECT_WATCHED_MOVIES, (username,))
        return cursor.fetchall()

def add_user(username):
     with connection:
        connection.execute(INSERT_USER, (username,))

def search_movie(promt):
    with connection:
        return connection.execute(SEARCH_MOVIE, (f"%{promt}%",))



