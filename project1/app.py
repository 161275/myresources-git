from db import add_entry, show_entry, create_table
from datetime import datetime


Menu = """
Please select a number
1. To add entry for today
2. View Entries
3. Exit.
"""
select = "Select an Option: "
today = datetime.today()
dat = today.strftime("%B %d, %Y") 



Welcome = "Welcome to the Programming diary"
print(Welcome)
print(Menu)
create_table()

def new_entry():
    content : str = input("what you have learened today")
    add_entry(content, dat)

def show_entries(entries):
    for entry in entries:
        print(f'content : {entry[0]} | date : {entry[1]}')


while True:
    num = int(input(select))
    if num == 3:
        break
        exit(0)
    elif num == 1:
        new_entry()
    elif num == 2:
        show_entries(show_entry())        
    else:
        print("enter a valid option!")