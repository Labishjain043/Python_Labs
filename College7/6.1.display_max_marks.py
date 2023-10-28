student_records = []
num_students = int(input("Enter the number of students: "))

for _ in range(num_students):
    name = input("Enter student name: ")
    rollno = input("Enter student roll number: ")
    marks = int(input("Enter student total marks (out of 100): "))
    student_records.append((name, rollno, marks))

max_marks_student = max(student_records, key=lambda x: x[2])

print("Details of the student with the maximum marks:")
print("Name:", max_marks_student[0])
print("Roll Number:", max_marks_student[1])
print("Total Marks:", max_marks_student[2])
