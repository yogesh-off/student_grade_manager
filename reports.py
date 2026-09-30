# reports.py
# Report card, class ranking and class statistics.

from grading import get_grade, get_percentage, is_pass







def show_report_card(roll, student):
    marks = student["marks"]
    print("")
    print("REPORT CARD: " + student["name"] + " (" + roll + ")")
    print("-" * 34)
    if len(marks) == 0:
        print("No marks entered yet.")
        return
    for subject in sorted(marks):
        print(subject.ljust(18) + str(marks[subject]).rjust(6) + "  " + get_grade(marks[subject]))
    percent = get_percentage(marks)
    print("-" * 34)
    print("Percentage:", percent, "%   Grade:", get_grade(percent))
    if is_pass(marks):
        print("Result: PASS")
    else:
        print("Result: FAIL")


def get_ranking(data):
    # Step 1: make a list of [roll, name, percentage] for students who have marks
    people = []
    for roll in sorted(data):
        marks = data[roll]["marks"]
        if len(marks) > 0:
            people.append([roll, data[roll]["name"], get_percentage(marks)])

    # Step 2: bubble sort - highest percentage first
    n = len(people)
    for i in range(n):
        for j in range(n - i - 1):
            if people[j][2] < people[j + 1][2]:
                temp = people[j]
                people[j] = people[j + 1]
                people[j + 1] = temp

    # Step 3: give ranks. Same percentage means same rank.
    ranked = []
    rank = 0
    for i in range(len(people)):
        if i == 0 or people[i][2] != people[i - 1][2]:
            rank = i + 1
        ranked.append([rank, people[i][0], people[i][1], people[i][2]])
    return ranked


def show_ranking(data):
    ranked = get_ranking(data)
    if len(ranked) == 0:
        print("No marks entered yet.")
        return
    print("")
    print("Rank  Roll No     Name                   Percent")
    for row in ranked:
        print(str(row[0]).ljust(6) + row[1].ljust(12) + row[2].ljust(23) + str(row[3]))


def calculate_stats(data):
    # goes through all students and collects the numbers we need
    graded = 0
    passed = 0
    total_percent = 0
    highest = 0
    lowest = 100
    subject_total = {}
    subject_count = {}

    for roll in data:
        marks = data[roll]["marks"]
        if len(marks) == 0:
            continue                      # skip students with no marks
        graded = graded + 1
        percent = get_percentage(marks)
        total_percent = total_percent + percent
        if percent > highest:
            highest = percent
        if percent < lowest:
            lowest = percent
        if is_pass(marks):
            passed = passed + 1
        for subject in marks:
            if subject not in subject_total:
                subject_total[subject] = 0
                subject_count[subject] = 0
            subject_total[subject] = subject_total[subject] + marks[subject]
            subject_count[subject] = subject_count[subject] + 1

    if graded == 0:
        return None

    subject_avg = {}
    for subject in subject_total:
        subject_avg[subject] = round(subject_total[subject] / subject_count[subject], 2)

    return {
        "graded": graded,
        "passed": passed,
        "failed": graded - passed,
        "average": round(total_percent / graded, 2),
        "highest": highest,
        "lowest": lowest,
        "subject_avg": subject_avg,
    }


def show_stats(data):
    stats = calculate_stats(data)
    if stats is None:
        print("No marks entered yet.")
        return
    topper = get_ranking(data)[0]
    print("")
    print("CLASS STATISTICS")
    print("-" * 30)
    print("Students graded  :", stats["graded"])
    print("Passed           :", stats["passed"])
    print("Failed           :", stats["failed"])
    print("Class average    :", stats["average"], "%")
    print("Highest          :", stats["highest"], "%")
    print("Lowest           :", stats["lowest"], "%")
    print("Topper           :", topper[2], "(" + str(topper[3]) + "%)")
    print("Subject averages:")
    for subject in sorted(stats["subject_avg"]):
        print("  " + subject.ljust(18) + str(stats["subject_avg"][subject]))
