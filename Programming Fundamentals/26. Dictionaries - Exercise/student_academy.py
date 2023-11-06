"""Write a program that keeps the information about students and their grades.
On the first line, you will receive an integer number representing the next pair of rows. On the next lines,
you will be receiving each student's name and their grade.
Keep track of all grades for each student and keep only the students with an average grade higher than or equal to 4.50.
Print the final dictionary with students and their average grade in the following format:
"{name} -> {averageGrade}"
Format the average grade to the 2nd decimal place.
"""

students = {}
pairs_number = int(input())

for pair in range(pairs_number):
	student_name = input()
	grade = float(input())

	if student_name not in students:
		students[student_name] = []
	students[student_name].append(grade)

for student_name, grade in students.items():
	average_grade = sum(grade) / len(grade)
	if average_grade >= 4.5:
		print(f"{student_name} -> {average_grade:.2f}")
