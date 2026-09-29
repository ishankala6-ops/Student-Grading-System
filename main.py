students = {}
used_rolls = set()


def cg(avg):
    if avg >= 90:
        return "A+"
    elif avg >= 80:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 50:
        return "D"
    elif avg >= 40:
        return "E"
    else:
        return "F"


def ast():
    roll = input("Enter roll number: ").strip()

    if roll in used_rolls:
        print("A student with this roll number already exists.\n")
        return

    name = input("Enter student name: ").strip()
    marks = []

    try:
        n = int(input("How many subjects? "))
    except ValueError:
        print("Please enter a valid number.\n")
        return

    for i in range(n):
        while True:
            try:
                m = float(input("  Enter marks for subject " + str(i + 1) + ": "))

                if m < 0 or m > 100:
                    print("  Marks should be between 0 and 100.")
                else:
                    marks.append(m)
                    break

            except ValueError:
                print("  Please enter a number.")

    total = sum(marks)

    if len(marks) > 0:
        avg = total / len(marks)
    else:
        avg = 0

    grade = cg(avg)

    students[roll] = {
        "name": name,
        "marks": marks,
        "total": total,
        "average": avg,
        "grade": grade
    }

    used_rolls.add(roll)

    print("Student", name, "added successfully. Grade:", grade)
    print()


def vas():
    if len(students) == 0:
        print("No student records yet.\n")
        return

    print()
    print("{:<10}{:<15}{:<10}{:<10}{:<6}".format(
        "Roll", "Name", "Total", "Average", "Grade"
    ))
    print("-" * 55)

    for roll in students:
        s = students[roll]

        print("{:<10}{:<15}{:<10}{:<10.2f}{:<6}".format(
            roll,
            s["name"],
            s["total"],
            s["average"],
            s["grade"]
        ))

    print()


def ss():
    roll = input("Enter roll number to search: ").strip()

    if roll not in students:
        print("No student found with that roll number.\n")
        return

    s = students[roll]

    print()
    print("Name    :", s["name"])
    print("Marks   :", s["marks"])
    print("Total   :", s["total"])
    print("Average :", round(s["average"], 2))
    print("Grade   :", s["grade"])
    print()


def um():
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
        try:
            m = float(input("  New marks for subject " + str(i + 1) + ": "))
            marks.append(m)
        except ValueError:
            print("Invalid marks entered.")
            return

    total = sum(marks)

    if len(marks) > 0:
        avg = total / len(marks)
    else:
        avg = 0

    grade = cg(avg)

    students[roll]["marks"] = marks
    students[roll]["total"] = total
    students[roll]["average"] = avg
    students[roll]["grade"] = grade

    print("Record updated.\n")


def ds():
    roll = input("Enter roll number to delete: ").strip()

    if roll in students:
        students.pop(roll)
        used_rolls.discard(roll)
        print("Student record deleted.\n")
    else:
        print("No such student found.\n")


def ct():
    if len(students) == 0:
        print("No records available.\n")
        return

    top_roll = None
    highest = -1

    for roll in students:
        if students[roll]["average"] > highest:
            highest = students[roll]["average"]
            top_roll = roll

    s = students[top_roll]

    print()
    print(
        "Class Topper:",
        s["name"],
        "(Roll:", top_roll + "),",
        "Average:", round(s["average"], 2)
    )
    print()


def sm():
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
        sm()
        choice = input("Enter your choice (1-7): ").strip()

        if choice == "1":
            ast()

        elif choice == "2":
            vas()

        elif choice == "3":
            ss()

        elif choice == "4":
            um()

        elif choice == "5":
            ds()

        elif choice == "6":
            ct()

        elif choice == "7":
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice, please try again.\n")


if __name__ == "__main__":
    main()
