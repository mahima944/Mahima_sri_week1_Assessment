def get_student_name():
    return input("Enter the student's name: ")

def get_marks():
    marks = []
    for i in range(1, 6):
        mark = float(input(f"Enter marks for subject {i}: "))
        marks.append(mark)
    return marks

def calculate_total_marks(marks):
    return sum(marks)

def calculate_percentage(total_marks):
    return (total_marks / 500) * 100

def display_results(name, total_marks, percentage, grade):
    print(f"Student Name: {name}")
    print(f"Total Marks: {total_marks}")
    print(f"Percentage: {percentage:f}%")
    print(f"Grade: {grade}")

def calculate_grade(percentage):
    if percentage >= 90:
        return 'A'
    elif percentage >= 75:
        return 'B'
    elif percentage >= 50:
        return 'C'
    else:
        return 'Fail'
    

def main():
    name = get_student_name()
    marks = get_marks()
    total_marks = calculate_total_marks(marks)
    percentage = calculate_percentage(total_marks)
    grade = calculate_grade(percentage)
    display_results(name, total_marks, percentage, grade)

main()
