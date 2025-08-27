import sqlite3

connection = sqlite3.connect("data.db")
# entries = []

def create_table():
    with connection:
        connection.execute("CREATE TABLE IF NOT EXISTS entries (content TEXT, date TEXT);")
    

def add_entry(content, dat):
    with connection:
        # connection.execute(f"INSERT INTO entries VALUES ('{content}','{dat}')")                 #causes sqlinjection attack
        connection.execute(
            "INSERT INTO entries VALUES (?, ?);", (content,dat)
        )

    


def show_entry():
    return connection.execute("SELECT * FROM entries;")
        
