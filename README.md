# Student Grade Manager

A simple command-line program written in Python to manage student marks. Made for the **Python Essentials** course (VITyarthi - Build Your Own Project).






## Overview
The teacher can add students, enter marks for each subject, and see grades, report cards, class ranking and class statistics. All data is saved in a file called `students.json`, so it is still there the next time the program is opened.


## Features
- Add, view, search, update and delete students
- Enter marks for each subject (only numbers from 0 to 100 are accepted)
- Automatic grade, percentage and PASS/FAIL (pass means 40 or more in every subject)
- Report card for each student
- Class ranking (students with the same percentage get the same rank)
- Class statistics: average, highest, lowest, topper, pass/fail count, subject averages
- Clear error messages instead of crashing


## Technologies used
- Python 3.8 or neyer (only built-in modules: `json`, `os`, `unittest`)
- Git and GitHub

## Python concepts used
Functions, variables, if/else, for and while loops, lists, dictionaries, string methods, file handling (JSON), exception handling (try/except), modules (importing our own files), bubble sort, unit testing.

## Project structure
```
student_grade_manager/
├── main.py         # menu and user input
├── students.py     # add / update / delete / search / marks
├── grading.py      # grade, percentage, pass/fail
├── reports.py      # report card, ranking, statistics
├── storage.py      # load and save the JSON file
├── validators.py   # checks the user input
├── tests/          # unit tests
├── README.md
└── statement.md
```

## How to install and run
1. Install Python 3.8 or newer. Check with `python --version`.
2. Open Command Prompt inside the project folder and type:
   ```
   python main.py
   ```
Nothing else needs to be installed.

## How to use
Type the menu number and press Enter. Pressing Enter on an empty question cancels that step.
1. Choose `1` to add a student (example: roll `24BCE001`, name `Asha Rao`)
2. Choose `6` to enter marks (type subject, then marks; press Enter on subject to finish)
3. Choose `7` for report card, `8` for ranking, `9` for class statistics

## Grading scheme
| Marks | Grade |
|-------|-------|
| 90 - 100 | A+ |
| 80 - 89 | A |
| 70 - 79 | B |
| 60 - 69 | C |
| 50 - 59 | D |
| 40 - 49 | E |
| below 40 | F |

## How to run the tests
```
python -m unittest discover -s tests -v
```





