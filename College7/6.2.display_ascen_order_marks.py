num_students = int(input("Enter the number of students: "))
student_records = []
for i in range(num_students):
    name = input("Enter student name: ")
    rollno = input(int("Enter student roll number: "))
    marks = int(input("Enter student total marks (out of 100): "))
    student_records.append((name, rollno, marks))

student_records.sort(key=lambda x: x[2], reverse=True)
ranks = list(range(1, num_students + 1))
student_records_with_rank = [(name, rollno, marks, rank) for (name, rollno, marks), rank in zip(student_records, ranks)]

print("Student records with ranks (in ascending order of ranks):")
for record in student_records_with_rank:
    print("Rank:", record[3])
    print("Name:", record[0])
    print("Roll Number:", record[1])
    print("Total Marks:", record[2])
