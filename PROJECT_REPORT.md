# STUDENT MANAGEMENT SYSTEM

## AIML INTERNSHIP – WEEK 1 PROJECT

---

## 1. Project Title

Student Management System using Python

---

## 2. Objective

The objective of this project is to develop a console-based Student Management System using Python.

The system allows users to add, view, search, update, and delete student records. It also calculates total marks, percentage, and grades.

Student records are stored permanently using a JSON file.

---

## 3. Technologies Used

- Python 3
- JSON
- Visual Studio Code

---

## 4. Features

The system provides the following features:

1. Add Student
2. View Students
3. Search Student
4. Update Student
5. Delete Student
6. Calculate Marks & Grade
7. Exit

Additional features include:

- JSON data storage
- Input validation
- Duplicate Student ID protection
- Marks validation from 0 to 100
- Age validation
- Error handling for invalid input

---

## 5. Student Information

Each student record contains:

- Student ID
- Name
- Age
- Python Marks
- Mathematics Marks
- Machine Learning Marks

---

## 6. Grade Calculation

The grading system is:

| Percentage | Grade |
|------------|-------|
| 90 - 100   | A+    |
| 80 - 89    | A     |
| 70 - 79    | B     |
| 60 - 69    | C     |
| 50 - 59    | D     |
| Below 50   | F     |

---

## 7. Data Storage

Student information is stored in:

`students.json`

The Python program uses the built-in `json` module to save and load student records.

---

## 8. Input Validation

The system validates user input to prevent errors.

Examples:

- Student ID must be a number.
- Student IDs cannot be duplicated.
- Age must be greater than zero.
- Marks must be between 0 and 100.
- Invalid numerical input is handled without crashing the program.

---

## 9. Project Structure

```text
Student-Management-System/
│
├── README.md
├── requirements.txt
├── PROJECT_REPORT.md
├── student_management.py
└── students.json