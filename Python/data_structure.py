# Initialize an empty list to store student data
students = []   # Global list to hold student dictionaries

# Function to check if a student ID already exists
def is_student_id_unique(student_id):
    for student in students:
        if student['id'] == student_id:
            return False
    return True

# Function to create or add a new student
def create_student(student_id, name, age, grade):
    student = {
        'id': student_id,
        'name': name,
        'age': age,
        'grade': grade
    }
    students.append(student)   # Add the student dictionary to the list
    print(f"Student {name} created successfully!")

# Function to read and display student data by student ID
def read_student(student_id):
    for student in students:
        if student['id'] == student_id:
            print(f"Student ID: {student['id']}")
            print(f"Name: {student['name']}")
            print(f"Age: {student['age']}")
            print(f"Grade: {student['grade']}")
            return
    print("Student not found!")

# Function to update an existing student's data
def update_student(student_id, name=None, age=None, grade=None):
    for student in students:
        if student['id'] == student_id:
            if name:
                student['name'] = name
            if age:
                student['age'] = age
            if grade:
                student['grade'] = grade
            print(f"Student {student_id} updated successfully!")
            return
    print("Student not found!")

# Function to delete a student from the list
def delete_student(student_id):
    global students
    for student in students:
        if student['id'] == student_id:
            students = [student for student in students if student['id'] != student_id]
            print(f"Student {student_id} deleted successfully!")
            return
    print("Student not found!")

# Function to get a valid integer input
def get_valid_int(prompt):
    while True:
        user_input = input(prompt)
        try:
            return int(user_input)
        except ValueError:
            print(f"Invalid input: '{user_input}' is not a valid number. Please try again.")

# Function to get a valid number
def get_valid_decimal(prompt):
    while True:
        user_input = input(prompt)
        try:
            return float(user_input)
        except ValueError:
            print(f"Invalid input: '{user_input}' is not a valid number. Please try again.")

# Function for user input handling
def menu():
    while True:
        print("\nStudent Management System")
        print("1. Create Student")
        print("2. Read Student")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':  # Create student
            while True:
                student_id = get_valid_int("Enter student ID: ")
                if is_student_id_unique(student_id):
                    break
                print(f"Error: Student ID {student_id} already exists. Please use a unique ID.")
            while True:
                name = input("Enter student name: ").strip()
                if name:
                    break
                print("Name cannot be empty. Please try again.")
            age = get_valid_int("Enter student age: ")
            grade = get_valid_decimal("Enter student grade: ")
            create_student(student_id, name, age, grade)  # Call create function
        
        elif choice == '2':  # Read student
            student_id = get_valid_int("Enter student ID to read: ")
            read_student(student_id)   # Call read function

        elif choice == '3':  # Update student
            student_id = get_valid_int("Enter student ID to update: ")
            print("Leave blank to keep the current value.")
            name = input("Enter new name (or leave blank): ").strip()
            age_input = input("Enter new age (or leave blank): ")
            grade_input = input("Enter new grade or leave blank: ")

            # Convert inputs to the correct types if not blank
            age = int(age_input) if age_input.strip() else None
            grade = float(grade_input) if grade_input.strip() else None
            update_student(student_id, name if name else None, age, grade)   # Call update function
        
        elif choice == '4':  # Delete student
            student_id = get_valid_int("Enter student ID to delete: ")
            delete_student(student_id)    # Call delete function
        
        elif choice == '5':  # Exit
            print("Exiting system.")
            break
        
        else:
            print("Invalid choice. Please try again.")   # Handle invalid menu choice

# Main function to run the program
def main():
    print("Welcome to the Student Management System!")
    menu()   # Call menu function

# Run the program
if __name__ == "__main__":
    main()   # Call main function