# validators.py
# These functions check what the user types.
# If the input is fine they return the cleaned value.
# If it is wrong they raise a ValueError with a message.


def check_roll(roll):
    roll = roll.strip().upper()          # remove spaces and make capital letters
    if len(roll) < 3 or len(roll) > 15:
        raise ValueError("Roll number must be 3 to 15 characters long.")
    if not roll.isalnum():
        raise ValueError("Roll number can only have letters and digits.")
    return roll


def check_name(name):
    name = " ".join(name.split())        # remove extra spaces
    if len(name) < 2:
        raise ValueError("Name is too short.")
    for ch in name:
        if not (ch.isalpha() or ch == " "):
            raise ValueError("Name can only have letters and spaces.")
    return name.title()                  # asha rao -> Asha Rao





def check_subject(subject):
    subject = " ".join(subject.split())
    if len(subject) < 2:
        raise ValueError("Subject name is too short.")
    return subject.title()


def check_marks(text):
    # first check that it is a number
    try:
        marks = float(text)
    except ValueError:
        raise ValueError("Marks must be a number.")
    # then check the range (this also rejects nan)
    if not (0 <= marks <= 100):
        raise ValueError("Marks must be between 0 and 100.")
    return marks
