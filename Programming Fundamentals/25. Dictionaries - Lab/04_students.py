"""
You will be receiving names of students, their ID, and a course of programming they have taken in the
format "{name}:{ID}:{course}". On the last line, you will receive a name of a course in snake case lowercase letters.
You should print only the information of the students who have taken the corresponding course in the
format: "{name} - {ID}" on separate lines.

			Input				|		Output
---------------------------------------------------
Peter:123:programming basics	|	John - 5622
John:5622:fundamentals			|	Maya - 89
Maya:89:fundamentals			|	Lilly - 633
Lilly:633:fundamentals			|
fundamentals					|

			Input				|		Output
----------------------------------------------------
Alex:6:programming basics		|	Alex - 6
Maria:7:programming basics		|	Maria - 7
Kaloyan:9:advanced				|
Todor:10:fundamentals			|
programming_basics				|
"""

data = input()
courses = {}

while ":" in data:
	student_name, student_id, course_name = data.split(":")
	if course_name not in courses:
		courses[course_name] = {student_id: student_name}
	else:
		courses[course_name][student_id] = student_name
	data = input()

course_name = data.replace("_", " ")  # " ".join(data.split("_"))
students = courses[course_name]

for student_id, name in students.items():
	print(f"{name} - {student_id}")
