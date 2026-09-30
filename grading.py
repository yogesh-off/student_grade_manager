# grading.py
# Calculates grade, percentage and pass/fail.

PASS_MARK = 40

def get_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    elif marks >= PASS_MARK:
        return "E"
    else:
        return "F"
 


def get_percentage(marks_dict):
    # percentage = is average of all subject marks (each subject is out of 100)
    if len(marks_dict) == 0:
        return 0.0
    total = 0
    for subject in marks_dict:
        total = total + marks_dict[subject]
    return round(total / len(marks_dict), 2)





def is_pass(marks_dict):
    # student shall passes only if every subject is 40 or more :)
    if len(marks_dict) == 0:
        return False
    for subject in marks_dict:
        if marks_dict[subject] < PASS_MARK:
            return False
    return True
