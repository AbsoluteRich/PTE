from os.path import exists
from os import remove, rename
from sys import exit
import json

settings = {  # Todo: Implement setting save/load
    "edit_suffix": " (edited)",
    "overwrite": False
}

file_name = input("Type a file name to edit or create: ")
while not exists(file_name):
    print(f"'{file_name}' not found")
    console = input("Create the file? (y/n) >>")

    if console == "y":
        with open(file_name, "x") as f:
            pass
    else:
        file_name = input("Type a file name to edit or create: ")

print(f"\n***** {file_name} *****")
while True:
    console = input("(r)ead, (w)rite, (s)ettings, (e)xit >>")

    match console:
        case "r":
            with open(file_name) as f:
                for line in f:
                    print(line.strip())

        case "w":
            pass
            # Todo: Finish this

        case "s":
            print(json.dumps(settings, sort_keys=True, indent=4))
            print("Type a setting name to edit")
            console = input("SETTINGS >> ")

            if console in settings.keys():
                if console == "overwrite":
                    pass
                else:
                    key = console
                    print("Type your new value")
                    console = input("SETTINGS >> ")
                    settings[key] = console
                    del key

        case "e":
            exit()

    print("\n")
