"""Write a program that keeps the information about courses. Each course has a name and registered students.
You will be receiving a course name and a student name until you receive the command "end".
You should register each user into the corresponding course. If the given course does not exist, add it.
When you receive the command "end", print the courses with their names and total registered users. For each course,
print the registered users.
Input
•	Until the "end" command is received, you will be receiving input lines in the format:
"{course_name} : {student_name}"
•	The product data is always delimited by " : "
Output
•	Print the information about each course in the following format:
"{course_name}: {registered_students}"
•	Print the information about each student in the following format:
"-- {student_name}"
"""

data = input()
courses = {}

while ":" in data:
	course_name, student_name = data.split(" : ")
	if course_name not in courses:
		courses[course_name] = []
	courses[course_name].append(student_name)
	data = input()

for course_name, student_name in courses.items():
	print(f"{course_name}: {len(student_name)}")
	for student in student_name:
		print(f"-- {student}")