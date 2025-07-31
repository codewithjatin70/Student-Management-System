import json

class Student:
    students = {}

    def __init__(self):
        # Name
        while True:
            self.name = input("Enter your name: ").strip()
            if self.name:
                break
            print("? Name cannot be empty!")

        # Class
        while True:
            self.student_class = input("Enter your class: ").strip()
            if self.student_class:
                break
            print("? Class cannot be empty!")

        # Roll No
        while True:
            self.roll_no = input("Enter your roll number: ").strip()
            if self.roll_no:
                break
            print("? Roll number cannot be empty!")

        # Student ID
        while True:
            self.student_id = input("Enter your student ID: ").strip()
            if not self.student_id:
                print("? Student ID cannot be empty!")
            elif self.student_id in Student.students:
                print("? Student ID already exists! Try again.")
            else:
                break

        Student.students[self.student_id] = self
        print(f"? Student '{self.name}' added successfully!")

    def display_details(self):
        print(f"? Name       : {self.name}")
        print(f"? Class      : {self.student_class}")
        print(f"? Roll No    : {self.roll_no}")
        print(f"? Student ID : {self.student_id}")

    @staticmethod
    def find_student(student_id):
        if student_id in Student.students:
            Student.students[student_id].display_details()
        else:
            print(f"? Student with ID {student_id} not found.")

    @staticmethod
    def display_all():
        if Student.students:
            print("\n? All Students List")
            print("-" * 30)
            for student in Student.students.values():
                student.display_details()
                print("-" * 30)
        else:
            print("? No students found.")

    @staticmethod
    def save_data():
        with open("students.json", "w") as f:
            json.dump({sid: vars(s) for sid, s in Student.students.items()}, f, indent=4)
        print("? Data saved successfully!")

    @staticmethod
    def load_data():
        try:
            with open("students.json", "r") as f:
                data = json.load(f)
                for sid, details in data.items():
                    student = Student.__new__(Student)  # create object without __init__
                    student.name = details["name"]
                    student.student_class = details["student_class"]
                    student.roll_no = details["roll_no"]
                    student.student_id = details["student_id"]
                    Student.students[sid] = student
            print("? Data loaded successfully!")
        except FileNotFoundError:
            print("? No saved data found. Starting fresh.")

def menu():
    print("\n? Student Management System")
    print("1. Add Student Details")
    print("2. Display Student Details by ID")
    print("3. Find Student by ID")
    print("4. Display All Students")
    print("5. Exit")

# Main program
Student.load_data()

while True:
    menu()
    choice = input("Enter your choice: ").strip()

    if choice == "1":
        student = Student()
    elif choice == "2":
        sid = input("Enter Student ID to display details: ").strip()
        Student.find_student(sid)
    elif choice == "3":
        sid = input("Enter Student ID to search: ").strip()
        Student.find_student(sid)
    elif choice == "4":
        Student.display_all()
    elif choice == "5":
        confirm = input("Are you sure you want to exit? (y/n): ").lower()
        if confirm == "y":
            Student.save_data()
            print("? Exiting program. Goodbye!")
            break
    else:
        print("? Invalid choice! Please try again.")
