def manage_student_marks():
    # Create dictionary of student marks
    students = {
        "John": 85,
        "Emma": 92,
        "Michael": 78,
        "Sarah": 95,
        "David": 88
    }
    
    # Get student name from user
    student_name = input("Enter student name to check marks: ")
    
    # Retrieve and display marks
    if student_name in students:
        marks = students[student_name]
        print(f"\nMarks for {student_name}: {marks}")
    else:
        print(f"\nStudent '{student_name}' not found in the records.")
    
    # Display all students and marks
    print("\nAll Students and Marks:")
    print("-" * 25)
    for name, mark in students.items():
        print(f"{name}: {mark}")

if __name__ == "__main__":
    print("Student Marks Management System")
    manage_student_marks()