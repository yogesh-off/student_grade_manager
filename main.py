# main.py
# Student Grade Manager - run this file:  python main.py
# It shows a menu and calls the other files to do the work.

import validators
import students
import reports
from storage import load_data, save_data

def show_menu():
    print("")
    print("===== STUDENT GRADE MANAGER =====")
    print("1. Add student")
    print("2. View all students")
    print("3. Search student")
    print("4. Update student name")
    print("5. Delete student")
    print("6. Enter marks")
    print("7. Report card")
    print("8. Class ranking")
    print("9. Class statistics")
    print("0. Exit")
    print("=================================")


def get_input(message, checker):
    # keeps asking until the input is correct.
    # If the user just presses Enter we return "" (means cancel).
    while True:
        text = input(message + " (press Enter to cancel): ")
        if text.strip() == "":
            return ""
        try:
            return checker(text)
        except ValueError as error:
            print("  Wrong input:", error)

def add_student_menu(data):
    roll = get_input("Roll number", validators.check_roll)
    if roll == "":
        return
    name = get_input("Student name", validators.check_name)
    if name == "":
        return
    students.add_student(data, roll, name)
    save_data(data)
    print("Added " + name + " (" + roll + ").")


def view_all_menu(data):
    if len(data) == 0:
        print("No students added yet.")
        return
    print("")
    print("Roll No     Name                    Subjects")
    for roll in sorted(data):
        print(roll.ljust(12) + data[roll]["name"].ljust(24) + str(len(data[roll]["marks"])))
    print("Total students:", len(data))

def search_menu(data):
    text = input("Enter roll number or name to search: ")
    found = students.search_students(data, text)
    if len(found) == 0:
        print("No match found.")
        return
    for roll in sorted(found):
        print(roll.ljust(12) + found[roll]["name"])


def update_menu(data):
    roll = get_input("Roll number", validators.check_roll)
    if roll == "":
        return
    students.get_student(data, roll)      # error if student does not exist
    new_name = get_input("New name", validators.check_name)
    if new_name == "":
        return
    students.update_name(data, roll, new_name)
    save_data(data)
    print("Name updated.")


def delete_menu(data):
    roll = get_input("Roll number to delete", validators.check_roll)
    if roll == "":
        return
    student = students.get_student(data, roll)
    answer = input("Delete " + student["name"] + "? Type YES to confirm: ")
    if answer.strip() == "YES":
        students.delete_student(data, roll)
        save_data(data)
        print("Student deleted.")
    else:
        print("Cancelled.")


def marks_menu(data):
    roll = get_input("Roll number", validators.check_roll)
    if roll == "":
        return
    student = students.get_student(data, roll)
    print("Entering marks for " + student["name"] + ". Press Enter on subject to finish.")
    while True:
        subject = get_input("Subject", validators.check_subject)
        if subject == "":
            break
        marks = get_input("Marks in " + subject + " (0-100)", validators.check_marks)
        if marks == "":
            continue
        students.set_marks(data, roll, subject, marks)
        save_data(data)
        print("  Saved.")


def report_card_menu(data):
    roll = get_input("Roll number", validators.check_roll)
    if roll == "":
        return
    student = students.get_student(data, roll)
    reports.show_report_card(roll, student)


def main():
    data = load_data()
    while True:
        show_menu()
        choice = input("Enter your choice: ").strip()
        try:
            if choice == "1":
                add_student_menu(data)
            elif choice == "2":
                view_all_menu(data)
            elif choice == "3":
                search_menu(data)
            elif choice == "4":
                update_menu(data)
            elif choice == "5":
                delete_menu(data)
            elif choice == "6":
                marks_menu(data)
            elif choice == "7":
                report_card_menu(data)
            elif choice == "8":
                reports.show_ranking(data)
            elif choice == "9":
                reports.show_stats(data)
            elif choice == "0":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number from the menu.")
        except KeyError as error:
            print("Error:", error.args[0])


# this part runs main() only when we run this file directly
try:
    if __name__ == "__main__":
        main()
except (KeyboardInterrupt, EOFError):
    print("\nProgram closed. Goodbye!")
