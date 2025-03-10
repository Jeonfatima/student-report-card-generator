print("Welcome To student report card generator")

def get_student_info():
    students = []  # Initialize the list of students
    while True:
        student = {}  # Create a new student dictionary
        student['name'] = input("Enter the student name:")
        student['roll_no'] = input("Enter the roll number:")
       
        subjects = {"math", "physics", "urdu", "english", "computer"}
        student['marks'] = {}
        for subject in subjects:
            marks = float(input(f"Enter the marks for {subject}:"))
            if 0 <= marks <= 100:
                student['marks'][subject] = marks
            else:
                print(f"Invalid marks for {subject}. Please enter again")
                marks = float(input(f"Enter the marks for {subject}:"))

        students.append(student)  # Append the student dictionary to the students list
        if input("Do you want to add another student? (yes/no):").lower() != 'yes':
            break
    return students

def calculate_total_marks(student):
    total_marks = 0
    for marks in student['marks'].values():
        total_marks += marks
    percentage = (total_marks * 100) / 500  # Fixed percentage calculation
    if percentage >= 80:
        grade = "A+"
    elif 70 <= percentage <= 79:
        grade = "A"
    elif 60 <= percentage <= 69:
        grade = "B"
    elif 50 <= percentage <= 59:
        grade = "C"
    else:
        grade = "F"
        
    return total_marks, percentage, grade

def generate_report(student):
    print("---------------Student Report Card---------------")
    print(f"Student name: {student['name']}")
    print(f"Roll number: {student['roll_no']}")
    print("-------------------------------------------------")
    print("Subject\t\tMarks")
    print("-------------------------------------------------")
    for subject,marks in student['marks'].items():
        print(f"{subject}\t\t{marks}")
    print("-------------------------------------------------")
    total_marks, percentage, grade = calculate_total_marks(student)
    print(f"Total Marks: {total_marks}")
    print(f"Percentage: {percentage}%")
    print(f"Grade: {grade}")
    print("-------------------------------------------------")

def main(): 
    students = get_student_info()
    for student in students:
        generate_report(student)

if __name__ == "__main__":
    main()      
