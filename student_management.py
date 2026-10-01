# ==========================================
# Student Management System
# AIML Internship - Week 1 Project
# ==========================================

import json

class Student:
    def __init__(self, student_id, name, age, python, mathematics, machine_learning):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.python = python
        self.mathematics = mathematics
        self.machine_learning = machine_learning

    def calculate_total(self):
        return self.python + self.mathematics + self.machine_learning

    def calculate_percentage(self):
        return self.calculate_total() / 3

    def calculate_grade(self):
        percentage = self.calculate_percentage()

        if percentage >= 90:
            return "A+"
        elif percentage >= 80:
            return "A"
        elif percentage >= 70:
            return "B"
        elif percentage >= 60:
            return "C"
        elif percentage >= 50:
            return "D"
        else:
            return "F"

def save_students(students):
    data = []

    for student in students:
        data.append({
            "student_id": student.student_id,
            "name": student.name,
            "age": student.age,
            "python": student.python,
            "mathematics": student.mathematics,
            "machine_learning": student.machine_learning
        })

    with open("students.json", "w") as file:
        json.dump(data, file, indent=4)

    print("Student data saved successfully!")

def load_students():
    try:
        with open("students.json", "r") as file:
            data = json.load(file)

        students = []

        for item in data:
            student = Student(
                item["student_id"],
                item["name"],
                item["age"],
                item["python"],
                item["mathematics"],
                item["machine_learning"]
            )

            students.append(student)

        return students

    except FileNotFoundError:
        return []

    except json.JSONDecodeError:
        print("Error: students.json contains invalid data.")
        return []

    except KeyError as e:
        print("Error: Missing field in students.json:", e)
        return []


students = load_students()


while True:
    print("\n" + "=" * 50)
    print("       STUDENT MANAGEMENT SYSTEM")
    print("          AIML INTERNSHIP")
    print("=" * 50)
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Calculate Marks & Grade")
    print("7. Exit")
    print("=" * 50)

    choice = input("Enter your choice: ")

    if choice == "1":
        try:
            student_id = int(input("Enter Student ID: "))
        except ValueError:
            print("Invalid Student ID! Please enter a number.")
            continue

        duplicate = False

        for student in students:
            if student.student_id == student_id:
                duplicate = True
                break

        if duplicate:
            print("Student ID already exists!")
            continue
        name = input("Enter Student Name: ")
        try:
            age = int(input("Enter Age: "))

            if age <= 0:
                print("Age must be greater than 0.")
                continue

        except ValueError:
            print("Invalid age! Please enter a number.")
            continue

        while True:
            try:
                python_marks = float(input("Enter Python Marks: "))

                if 0 <= python_marks <= 100:
                    break
                else:
                    print("Marks must be between 0 and 100.")

            except ValueError:
                print("Invalid marks! Please enter a number.")
        while True:
            try:
                mathematics_marks = float(input("Enter Mathematics Marks: "))

                if 0 <= mathematics_marks <= 100:
                    break
                else:
                    print("Marks must be between 0 and 100.")

            except ValueError:
                print("Invalid marks! Please enter a number.")
        while True:
            try:
                machine_learning_marks = float(
                    input("Enter Machine Learning Marks: ")
                )

                if 0 <= machine_learning_marks <= 100:
                    break
                else:
                    print("Marks must be between 0 and 100.")

            except ValueError:
                print("Invalid marks! Please enter a number.")
        new_student = Student(
            student_id,
            name,
            age,
            python_marks,
            mathematics_marks,
            machine_learning_marks
        )

        students.append(new_student)

        save_students(students)

        print("Student added successfully!")
    elif choice == "2":
        if len(students) == 0:
            print("No students found.")
        else:
            print("\n" + "=" * 60)
            print("                    ALL STUDENTS")
            print("=" * 60)

            for student in students:
                print("Student ID:", student.student_id)
                print("Name:", student.name)
                print("Age:", student.age)
                print("Python Marks:", student.python)
                print("Mathematics Marks:", student.mathematics)
                print("Machine Learning Marks:", student.machine_learning)
                print("Total Marks:", student.calculate_total())
                print("Percentage:", student.calculate_percentage())
                print("Grade:", student.calculate_grade())
                print("-" * 60)
    elif choice == "3":
        try:
            search_id = int(input("Enter Student ID to search: "))
        except ValueError:
            print("Invalid Student ID! Please enter a number.")
            continue
        found = False

        for student in students:
            if student.student_id == search_id:
                print("\nStudent Found!")
                print("Student ID:", student.student_id)
                print("Name:", student.name)
                print("Age:", student.age)
                print("Python Marks:", student.python)
                print("Mathematics Marks:", student.mathematics)
                print("Machine Learning Marks:", student.machine_learning)
                print("Total Marks:", student.calculate_total())
                print("Percentage:", student.calculate_percentage())
                print("Grade:", student.calculate_grade())

                found = True
                break

        if not found:
            print("Student not found.")

    elif choice == "4":
        try:
            update_id = int(input("Enter Student ID to update: "))
        except ValueError:
            print("Invalid Student ID! Please enter a number.")
            continue

        found = False

        for student in students:
            if student.student_id == update_id:

                print("\nStudent found!")
                print("Enter new details:")

                student.name = input("Enter New Name: ")
                student.age = int(input("Enter New Age: "))

                student.python = float(input("Enter New Python Marks: "))
                student.mathematics = float(input("Enter New Mathematics Marks: "))
                student.machine_learning = float(
                    input("Enter New Machine Learning Marks: ")
                )

                save_students(students)

                print("\nStudent updated successfully!")

                found = True
                break

        if not found:
            print("Student not found.")

    elif choice == "5":
        try:
            delete_id = int(input("Enter Student ID to delete: "))
        except ValueError:
            print("Invalid Student ID! Please enter a number.")
            continue

        found = False

        for student in students:
            if student.student_id == delete_id:
                students.remove(student)
                save_students(students)

                print("\nStudent deleted successfully!")
                found = True
                break

        if not found:
            print("\nStudent not found!")

    elif choice == "6":
        try:
            calculate_id = int(input("Enter Student ID: "))
        except ValueError:
            print("Invalid Student ID! Please enter a number.")
            continue

        found = False

        for student in students:
            if student.student_id == calculate_id:

                total = student.calculate_total()
                percentage = student.calculate_percentage()
                grade = student.calculate_grade()

                print("\n" + "=" * 40)
                print("          MARKS & GRADE")
                print("=" * 40)
                print("Student ID:", student.student_id)
                print("Name:", student.name)
                print("Python Marks:", student.python)
                print("Mathematics Marks:", student.mathematics)
                print("Machine Learning Marks:", student.machine_learning)
                print("Total Marks:", total)
                print("Percentage:", percentage)
                print("Grade:", grade)
                print("=" * 40)

                found = True
                break

        if not found:
            print("Student not found.")

    elif choice == "7":
        print("Thank you for using Student Management System!")
        break

    else:
        print("Invalid choice. Please try again.")