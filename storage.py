# storage.py
# Saves and loads all student data from a file called students.json
# so the data is not lost when the program is closed.

import json
import os

# the file is stored in the same folder as this program
FILE_NAME = os.path.join(os.path.dirname(os.path.abspath(__file__)), "students.json")







def load_data(path=FILE_NAME):
    # if the file does not exist yet (first run) start with empty data
    if not os.path.exists(path):
        return {}
    try:
        f = open(path, "r")
        data = json.load(f)
        f.close()
        return data
    except (ValueError, OSError):
        print("Warning: could not read the data file. Starting with empty data.")
        return {}


def save_data(data, path=FILE_NAME):
    try:
        f = open(path, "w")
        json.dump(data, f, indent=2)
        f.close()
    except OSError:
        print("Error: could not save the data.")
