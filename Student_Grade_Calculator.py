# Function to calculate grade
def calculate_grade(marks):
    if marks >= 90:
        return "A", "Excellent work! Keep shining"
    elif marks >= 80:
        return "B", "Very Good! Keep it up!"
    elif marks >= 70:
        return "C", "Good job! Keep improving"
    elif marks >= 60:
        return "D", "You passed! Try harder next time"
    else:
        return "F", "Don't give up! Work harder"


while True:
    name = input("Enter student name: ")

    try:
        marks = int(input("Enter marks (0-100): "))

        if marks < 0 or marks > 100:
            print("Invalid marks! Enter between 0 and 100.\n")
            continue

        grade, message = calculate_grade(marks)

        print(f"\n📊 RESULT FOR {name.upper()}:")
        print(f"Marks: {marks}/100")
        print(f"Grade: {grade}")
        print(f"Message: {message}")

        break

    except ValueError:
        print("Please enter a valid number!\n")