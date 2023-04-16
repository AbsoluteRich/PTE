from os.path import exists
from os import remove, rename
from sys import exit

edit_suffix = " (edited)"
overwrite = False

file_name = input("Type a file name to edit or create: ")
while not exists(file_name):
    print(f"'{file_name}' not found")
    console = input("Create the file? (y/n) >>")

    if console == "y":
        with open(file_name, "x") as f:
            pass
    else:
        file_name = input("Type a file name to edit or create: ")

print(f"***** {file_name} *****")
while True:
    console = input(">>")
