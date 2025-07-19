import os
import json

DATA_FILE = "data.json"

class Student:
    def __init__(self, name, subjects_scores):
        self.name = name
        self.subjects_scores = subjects_scores
        self.average = self.calculate_average()
        self.grade = self.calculate_grade()

    def calculate_average(self):
        return sum(self.subjects_scores.values()) / len(self.subjects_scores)

    def calculate_grade(self):
        avg = self.average
        if avg >= 90:
            return "A"
        elif avg >= 80:
            return "B"
        elif avg >= 70:
            return "C"
        elif avg >= 60:
            return "D"
        else:
            return "F"

    def to_dict(self):
        return {
            "name": self.name,
            "subjects_scores": self.subjects_scores,
            "average": self.average,
            "grade": self.grade
        }

def save_data(students):
    with open(DATA_FILE, "w") as f:
        json.dump([s.to_dict() for s in students], f, indent=4)

def load_data():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        return [Student(s["name"], s["subjects_scores"]) for s in json.load(f)]

def add_student():
    name = input("Student Name: ")
    subjects_scores = {}
    for _ in range(3):  # 3 subjects for simplicity
        subject = input("Subject Name: ")
        score = float(input("Score: "))
        subjects_scores[subject] = score
    student = Student(name, subjects_scores)
    students.append(student)
    save_data(students)
    print(f"{student.name} added with Grade {student.grade}")

def view_students():
    if not students:
        print("No student records.")
        return
    for s in students:
        print(f"{s.name}: Average={s.average:.2f}, Grade={s.grade}")
        for subject, score in s.subjects_scores.items():
            print(f"  {subject}: {score}")

# Load existing data
students = load_data()

# CLI menu
while True:
    print("\n1. Add Student\n2. View Students\n3. Exit")
    choice = input("Enter choice: ")
    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        break
    else:
        print("Invalid choice.")
