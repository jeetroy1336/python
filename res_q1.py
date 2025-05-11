class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self, name, roll_no, grade):
        """Adds a student with name, roll number, and grade."""
        student = {
            "name": name,
            "roll_no": roll_no,
            "grade": grade
        }
        self.students.append(student)
        print(f"Added student: {student}")

    def display_students(self):
        """Displays the list of all students."""
        if not self.students:
            print("No students to display.")
            return
        print("\nList of Students:")
        for idx, student in enumerate(self.students):
            print(f"{idx}. Name: {student['name']}, Roll No: {student['roll_no']}, Grade: {student['grade']}")

    def update_student(self, index, name=None, roll_no=None, grade=None):
        """Updates the student's information at the given index."""
        if 0 <= index < len(self.students):
            if name is not None:
                self.students[index]['name'] = name
            if roll_no is not None:
                self.students[index]['roll_no'] = roll_no
            if grade is not None:
                self.students[index]['grade'] = grade
            print(f"Updated student at index {index}: {self.students[index]}")
        else:
            print("Invalid index. No student updated.")


if __name__ == "__main__":
    manager = StudentManager()

    while True:
        print("\n--- Student Manager Menu ---")
        print("1. Add Student")
        print("2. Display Students")
        print("3. Update Student")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            name = input("Enter name: ")
            try:
                roll_no = int(input("Enter roll number: "))
                grade = input("Enter grade: ")
                manager.add_student(name, roll_no, grade)
            except ValueError:
                print("Invalid input for roll number. Please enter an integer.")

        elif choice == "2":
            manager.display_students()

        elif choice == "3":
            try:
                index = int(input("Enter student index to update: "))
                print("Leave field blank to keep current value.")
                name = input("Enter new name (or press Enter to skip): ") or None
                roll_no_input = input("Enter new roll number (or press Enter to skip): ")
                roll_no = int(roll_no_input) if roll_no_input else None
                grade = input("Enter new grade (or press Enter to skip): ") or None
                manager.update_student(index, name, roll_no, grade)
            except ValueError:
                print("Invalid input. Index and roll number must be integers.")

        elif choice == "4":
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")
