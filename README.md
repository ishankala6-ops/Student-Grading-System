Student Grade Management System
CSA1021 - Mini Project (VIT Bhopal)

Idea: keep student records in a dictionary, store each student's
marks in a list, calculate total/average using arithmetic operators,
and decide the grade using if-elif-else. A set is used just to make
sure no roll number gets added twice.
"""

# main "database" - roll number is the key, value is another dictionary
# containing name and a list of marks (this is the nested dictionary
# concept from the dictionary slides)
students = {}

# keeps track of roll numbers already used, so we don't allow duplicates
used_rolls = set()


def calculate_grade(average):
    """Decide grade based on average marks using chained if-elif-else."""
    if average >= 90:
        grade = "A+"
    elif average >= 80:
        grade = "A"
    elif average >= 70:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 50:
        grade = "D"
    elif average >= 40:
        grade = "E"
    else:
        grade = "F"
    return grade


def add_student():
    roll = input("Enter roll number: ").strip()

    # basic validation using membership operator ('in')
    if roll in used_rolls:
        print("A student with this roll number already exists.\n")
        return

    name = input("Enter student name: ").strip()

    marks = []  # this list acts like the "array" of marks
    try:
        n = int(input("How many subjects? "))
    except ValueError:
        print("Please enter a valid number.\n")
        return

    for i in range(n):
        while True:
            try:
                m = float(input(f"  Enter marks for subject {i + 1}: "))
                if m < 0 or m > 100:
                    print("  Marks should be between 0 and 100.")
                    continue
                break
            except ValueError:
                print("  That's not a number, try again.")
        marks.append(m)

    total = sum(marks)
    average = total / len(marks) if marks else 0
    grade = calculate_grade(average)

    # store everything as a nested dictionary
    students[roll] = {
        "name": name,
        "marks": marks,
        "total": total,
        "average": average,
        "grade": grade,
    }
    used_rolls.add(roll)

    print(f"Student {name} added successfully. Grade: {grade}\n")


def view_all_students():
    if not students:
        print("No student records yet.\n")
        return

    print("\n{:<10}{:<15}{:<10}{:<10}{:<6}".format(
        "Roll", "Name", "Total", "Average", "Grade"))
    print("-" * 55)
    for roll, info in students.items():
        print("{:<10}{:<15}{:<10}{:<10.2f}{:<6}".format(
            roll, info["name"], info["total"], info["average"], info["grade"]))
    print()


def search_student():
    roll = input("Enter roll number to search: ").strip()
    info = students.get(roll)  # get() returns None if key not found

    if info is None:
        print("No student found with that roll number.\n")
        return

    print(f"\nName    : {info['name']}")
    print(f"Marks   : {info['marks']}")
    print(f"Total   : {info['total']}")
    print(f"Average : {info['average']:.2f}")
    print(f"Grade   : {info['grade']}\n")


def update_marks():
    roll = input("Enter roll number to update: ").strip()
    if roll not in students:
        print("No such student.\n")
        return

    marks = []
    try:
        n = int(input("How many subjects (re-enter all marks)? "))
    except ValueError:
        print("Please enter a valid number.\n")
        return

    for i in range(n):
        m = float(input(f"  New marks for subject {i + 1}: "))
        marks.append(m)

    total = sum(marks)
    average = total / len(marks) if marks else 0
    grade = calculate_grade(average)

    students[roll]["marks"] = marks
    students[roll]["total"] = total
    students[roll]["average"] = average
    students[roll]["grade"] = grade

    print("Record updated.\n")


def delete_student():
    roll = input("Enter roll number to delete: ").strip()
    if roll in students:
        students.pop(roll)      # remove from dictionary
        used_rolls.discard(roll)  # remove from the roll-number set
        print("Student record deleted.\n")
    else:
        print("No such student found.\n")


def class_topper():
    if not students:
        print("No records available.\n")
        return

    # find the student with the highest average
    topper_roll = max(students, key=lambda r: students[r]["average"])
    topper = students[topper_roll]
    print(f"\nClass Topper: {topper['name']} (Roll: {topper_roll}), "
          f"Average: {topper['average']:.2f}\n")


def show_menu():
    print("=" * 40)
    print(" STUDENT GRADE MANAGEMENT SYSTEM")
    print("=" * 40)
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Update Marks")
    print("5. Delete Student")
    print("6. Show Class Topper")
    print("7. Exit")


def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-7): ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            view_all_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_marks()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            class_topper()
        elif choice == "7":
            print("Exiting program. Goodbye!")
            break  # exits the while loop
        else:
            print("Invalid choice, please try again.\n")
            continue


if __name__ == "__main__":
    main()
