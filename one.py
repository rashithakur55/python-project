# Student Grade Calculator - PS 19

# Function 1: Total marks nikalna
def calculate_total(marks):
    total = 0
    for m in marks:
        total = total + m
    return total


# Function 2: Percentage nikalna (5 subjects = 500 marks)
def calculate_percentage(total):
    return total / 500 * 100


# Function 3: Grade nikalna
def get_grade(percentage):
    if percentage >= 85:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 55:
        return "C"
    elif percentage >= 40:
        return "D"
    else:
        return "F"


# Function 4: Marks lena (galat ho to dobara puchta hai)
def get_marks(subject_no):
    while True:
        try:
            m = float(input(f"Enter marks for subject {subject_no}: "))
            if 0 <= m <= 100:
                return m
            else:
                print("Invalid marks. Enter a number between 0 and 100.")
        except ValueError:
            print("Invalid marks. Enter a number between 0 and 100.")


# ---------- Main Program ---------
while True:
    name = input("Enter student name: ")

    marks = []
    for i in range(1, 6):
        marks.append(get_marks(i))

    total = calculate_total(marks)
    percentage = calculate_percentage(total)
    grade = get_grade(percentage)

    # Pass/Fail: 40% ya usse zyada pass
    if percentage >= 40:
        result = "Pass"
    else:
        result = "Fail"

    print(f"{name} | Total: {total:g} | Percentage: {percentage:.2f}% | Grade: {grade} |")
    print("Result:", result)

    again = input("Another student? (y/n): ")
    if again.lower() != "y":
        break