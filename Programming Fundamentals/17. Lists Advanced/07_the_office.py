"""
You will receive two lines of input:
•	a list of employees' happiness as a string of numbers separated by a single space
•	a happiness improvement factor (single number).
Your task is to find out if the employees are generally happy in their office.
First, multiply each employee's happiness by the factor.
Then, print one of the following lines:
•	If half or more of the employees have happiness greater than or equal to the average:
"Score: {happy_count}/{total_count}. Employees are happy!"
•	Otherwise:
"Score: {happy_count}/{total_count}. Employees are not happy!"
"""

employees_happiness = input().split()
improvement_factor = int(input())
hapiness_as_integers = [int(number) for number in employees_happiness]
average_happiness = sum(hapiness_as_integers) / len(hapiness_as_integers)

happy_employees = 0
unhappy_employees = 0
for employee in hapiness_as_integers:
	if employee >= average_happiness:
		happy_employees += 1
	else:
		unhappy_employees += 1

if happy_employees >= unhappy_employees:
	print(f"Score: {happy_employees}/{len(hapiness_as_integers)}. Employees are happy!")
else:
	print(f"Score: {happy_employees}/{len(hapiness_as_integers)}. Employees are not happy!")

multiplied_by_factor = [(int(factor) * improvement_factor) for factor in employees_happiness]

