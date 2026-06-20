# Faisal Shaikh
# CIS261
# WK10 VIBE Coding

FILE_NAME = "student_grades.txt"


def calculate_average(test1, test2, test3):
    return (test1 + test2 + test3) / 3


def calculate_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"


def get_score(prompt):
    while True:
        try:
            score = float(input(prompt))
            if 0 <= score <= 100:
                return score
            else:
                print("Please enter a score between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def add_student(students):
    print("\nAdd New Student")
    name = input("Enter student name: ")
    student_id = input("Enter student ID: ")

    test1 = get_score("Enter Test 1 score: ")
    test2 = get_score("Enter Test 2 score: ")
    test3 = get_score("Enter Test 3 score: ")

    average = calculate_average(test1, test2, test3)
    grade = calculate_grade(average)

    student = {
        "name": name,
        "id": student_id,
        "test1": test1,
        "test2": test2,
        "test3": test3,
        "average": average,
        "grade": grade
    }

    students.append(student)
    print("Student record added successfully.")


def display_students(students):
    if not students:
        print("\nNo student records found.")
        return

    print("\nAll Student Records")
    print("-" * 95)
    print(f"{'Name':20} {'ID':10} {'Test 1':10} {'Test 2':10} {'Test 3':10} {'Average':10} {'Grade':10}")
    print("-" * 95)

    for student in students:
        print(f"{student['name']:20} {student['id']:10} "
              f"{student['test1']:<10.2f} {student['test2']:<10.2f} "
              f"{student['test3']:<10.2f} {student['average']:<10.2f} "
              f"{student['grade']:10}")


def search_student(students):
    if not students:
        print("\nNo student records to search.")
        return

    search_name = input("\nEnter student name to search: ").lower()
    found = False

    for student in students:
        if search_name in student["name"].lower():
            print("\nStudent Found:")
            print(f"Name: {student['name']}")
            print(f"ID: {student['id']}")
            print(f"Test 1: {student['test1']:.2f}")
            print(f"Test 2: {student['test2']:.2f}")
            print(f"Test 3: {student['test3']:.2f}")
            print(f"Average: {student['average']:.2f}")
            print(f"Grade: {student['grade']}")
            found = True

    if not found:
        print("No student found with that name.")


def class_statistics(students):
    if not students:
        print("\nNo student records available for statistics.")
        return

    averages = [student["average"] for student in students]

    highest = max(averages)
    lowest = min(averages)
    class_avg = sum(averages) / len(averages)

    print("\nClass Statistics")
    print(f"Highest Average: {highest:.2f}")
    print(f"Lowest Average: {lowest:.2f}")
    print(f"Class Average: {class_avg:.2f}")


def save_students(students):
    try:
        with open(FILE_NAME, "w") as file:
            for student in students:
                file.write(
                    f"{student['name']}|{student['id']}|"
                    f"{student['test1']}|{student['test2']}|{student['test3']}|"
                    f"{student['average']}|{student['grade']}\n"
                )
        print("Student records saved successfully.")
    except IOError:
        print("Error saving student records.")


def load_students():
    students = []

    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                data = line.strip().split("|")

                if len(data) == 7:
                    student = {
                        "name": data[0],
                        "id": data[1],
                        "test1": float(data[2]),
                        "test2": float(data[3]),
                        "test3": float(data[4]),
                        "average": float(data[5]),
                        "grade": data[6]
                    }
                    students.append(student)

        print("Student records loaded successfully.")
    except FileNotFoundError:
        print("No saved file found. Starting with empty records.")
    except IOError:
        print("Error loading student records.")

    return students


def menu():
    print("\nStudent Grade Calculator")
    print("1. Add New Student")
    print("2. Display All Students")
    print("3. Search Student by Name")
    print("4. View Class Statistics")
    print("5. Save and Exit")
    print("Press ESC or type esc to exit")


def main():
    students = load_students()

    while True:
        menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            add_student(students)
        elif choice == "2":
            display_students(students)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            class_statistics(students)
        elif choice == "5" or choice.lower() == "esc":
            save_students(students)
            print("Program exited. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


main()