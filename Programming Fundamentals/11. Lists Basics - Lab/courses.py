"""
On the first line, you will receive a single number n. On the following n lines, you will receive names of courses.
You should create a list of courses and print it.
"""

line_numbers = int(input())
courses = []

for course in range(line_numbers):
    current_course = input()
    courses.append(current_course)

print(courses)
