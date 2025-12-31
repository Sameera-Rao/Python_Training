gradebook = [] 

def add_student():
    name = input("Enter student name:")

    marks = []
    subjects = 5 

    for i in range(subjects):
        mark = float(input(f"Enter marks for subject {i + 1}:"))
        marks.append(mark)

    average = sum(marks)/subjects

    student = {
        "name":name,
        "marks":marks,
        "average":average
    }

    gradebook.append(student)
    print("Student added successfully.\n")

def search_student():
    name = input("Enter student name to search: ")

    for student in gradebook:
        if student["name"]==name:
            print(f"Name: {student['name']}")
            print(f"Marks: {student['marks']}")
            print(f"Average: {student['average']}")
            return

    print("Student not found.")


def class_average():
    total = sum(student["average"] for student in gradebook)
    average = total / len(gradebook)
    print(f"Class Average: {average:}\n")


def top_students():
    highest_avg = max(student["average"] for student in gradebook)

    print("Top Performing Students:")
    for student in gradebook:
        if student["average"] == highest_avg:
            print(f"{student['name']}")
    print()


num_students = int(input("Enter number of students: "))

for _ in range(num_students):
    add_student()

search_student()
class_average()
top_students()
