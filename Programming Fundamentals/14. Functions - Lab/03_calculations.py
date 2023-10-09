"""
Create a function that receives three parameters, calculates a result depending on the given operator, and returns it.
Print the result of the function.
The input comes as three parameters – an operator as a string and two integer numbers.
The operator can be one of the following:  "multiply", "divide", "add", "subtract".
"""

def calc(first_num, second_num, calc_operator):
	result = 0
	if calc_operator == "multiply":
		result = first_num * second_num
	elif calc_operator == "divide":
		result = first_num / second_num
	elif calc_operator == "add":
		result = first_num + second_num
	elif calc_operator == "subtract":
		result = first_num - second_num
	return result


operator = input()
num_1 = int(input())
num_2 = int(input())

result = calc(num_1, num_2, operator)
print(int(result))
