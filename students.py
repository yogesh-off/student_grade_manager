# students.py
# Functions to add, find, change and delete students.
#
# All students are kept in one dictionary called data. Example:
# data = {
#     "24BCE001": {"name": "Asha Rao", "marks": {"Maths": 90.0, "Python": 85.0}}
# }
# The role number is the key, so every student has a unique roll number.


def add_student(data, roll, name):
    if roll in data:
        raise KeyError("Roll number " + roll + " already exists.")
    data[roll] = {"name": name, "marks": {}}




def get_student(data, roll):
    if roll not in data:
        raise KeyError("No student found with roll number " + roll + ".")
    return data[roll]


def update_name(data, roll, new_name):
    student = get_student(data, roll)
    student["name"] = new_name


def delete_student(data, roll):
    get_student(data, roll)              # this gives an error if roll is not there
    del data[roll]


def set_marks(data, roll, subject, marks):
    student = get_student(data, roll)
    student["marks"][subject] = marks


def search_students(data, text):
    # returns a new dictionary with the students that match
    text = text.strip().lower()
    found = {}
    for roll in data:
        name = data[roll]["name"]
        if text in roll.lower() or text in name.lower():
            found[roll] = data[roll]
    return found
