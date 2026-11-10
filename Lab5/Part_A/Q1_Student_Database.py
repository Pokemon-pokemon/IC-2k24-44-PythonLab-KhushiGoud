students = {
    101: {
        "name": "Asha",
        "marks": {"Math": 88, "Physics": 76, "Chem": 92}
    },
    102: {
        "name": "Ravi",
        "marks": {"Math": 35, "Physics": 58, "Chem": 64}
    },
    103: {
        "name": "Meena",
        "marks": {"Math": 72, "Physics": 81, "Chem": 69}
    }
}


# 1. Add Student
def add_student():
    roll_no = int(input("Enter roll number: "))

    if roll_no in students:
        print("Duplicate roll number!")
        return

    name = input("Enter student name: ")
    marks = {}

    n = int(input("Enter number of subjects: "))

    for i in range(n):
        subject = input("Enter subject: ")
        score = int(input("Enter marks: "))

        if score < 0 or score > 100:
            print("Marks must be between 0 and 100!")
            return

        marks[subject] = score

    students[roll_no] = {"name": name, "marks": marks}
    print("Student added successfully!")


# 2. Update Marks
def update_marks():
    roll_no = int(input("Enter roll number: "))

    if roll_no not in students:
        print("Student not found!")
        return

    subject = input("Enter subject name: ")
    score = int(input("Enter new marks: "))

    if score < 0 or score > 100:
        print("Invalid marks!")
        return

    students[roll_no]["marks"][subject] = score
    print("Marks updated successfully!")


# 3. Delete Student
def delete_student():
    roll_no = int(input("Enter roll number: "))

    if roll_no in students:
        del students[roll_no]
        print("Student deleted successfully!")
    else:
        print("Student not found!")


# 4. Show Student Record
def show_student():
    roll_no = int(input("Enter roll number: "))

    if roll_no in students:
        print(students[roll_no])
    else:
        print("Student not found!")


# 5. Reports
def reports():
    if not students:
        print("No student records available!")
        return

    averages = {}

    for roll, data in students.items():
        marks = data["marks"]

        if marks:
            averages[roll] = round(
                sum(marks.values()) / len(marks), 2
            )

    print("\nStudent Averages:")
    print(averages)

    # Topper
    if averages:
        topper = max(averages, key=averages.get)
        print("Topper:", students[topper]["name"])

    # Highest scorer in each subject
    subjects = set()

    for data in students.values():
        subjects.update(data["marks"].keys())

    print("\nHighest Scorer in Each Subject:")

    for subject in sorted(subjects):
        scores = {}

        for roll, data in students.items():
            if subject in data["marks"]:
                scores[roll] = data["marks"][subject]

        if scores:
            highest = max(scores, key=scores.get)
            print(
                subject, "->",
                students[highest]["name"],
                "(", scores[highest], ")"
            )

    # Students scoring below 40
    print("\nStudents Below 40:")

    failed = []

    for data in students.values():
        for subject, marks in data["marks"].items():
            if marks < 40:
                failed.append((data["name"], subject, marks))

    if failed:
        for name, subject, marks in failed:
            print(name, "-", subject, ":", marks)
    else:
        print("No students failed!")

    # Grade-wise grouping
    grades = {
        "A": [],
        "B": [],
        "C": [],
        "D": [],
        "F": []
    }

    for roll, average in averages.items():
        name = students[roll]["name"]

        if average >= 90:
            grades["A"].append(name)
        elif average >= 75:
            grades["B"].append(name)
        elif average >= 60:
            grades["C"].append(name)
        elif average >= 40:
            grades["D"].append(name)
        else:
            grades["F"].append(name)

    print("\nGrade-wise Grouping:")
    print(grades)


# Main Menu
while True:
    print("\n===== STUDENT DATABASE =====")
    print("1. Add Student")
    print("2. Update Marks")
    print("3. Delete Student")
    print("4. Show Student Record")
    print("5. Reports")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        update_marks()

    elif choice == "3":
        delete_student()

    elif choice == "4":
        show_student()

    elif choice == "5":
        reports()

    elif choice == "6":
        print("Exiting Student Database...")
        break

    else:
        print("Invalid choice! Try again.")