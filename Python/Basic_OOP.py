# Define the Student class
class Student:  
    def __init__(self, name, age, grades):
    # Initialize the Student with name, age, and grades.
        self.name = name
        self.age = age
        self.grades = grades 

    # Method to display student details
    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Grades: {self.grades}")

    # Method to calculate the average grade
    def calculate_average(self):
        """Calculate and return the average grade."""
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

# Example usage
if __name__ == "__main__":
    # Create Student objects
    student1 = Student("Sanket", 20, [85, 90, 78, 92])
    student2 = Student("Harsh", 22, [88, 76, 95, 89])
    student3 = Student("Santosh", 19, [70, 75, 80, 85])
    student4 = Student("Durvesh", 21, [92, 88, 84, 96])
    student5 = Student("Vishal", 23, [65, 70, 75, 80])


    # Display details for each student and calculate average grades
    for student in [student1, student2, student3, student4, student5]:
        student.display_details()
        average_grade = student.calculate_average()
        print(f"Average Grade: {average_grade:.2f}")
        print()  # Add a new line for better management
