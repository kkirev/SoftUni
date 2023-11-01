"""
Write a program that receives a sequence of numbers (a string containing integers separated by ", ") and prints the
numbers sorted into lists of 10's in the format "Group of {group}'s: {list_of_numbers}".
Examples:
•	The numbers 2, 8, 4, and 10 fall into the group of 10's.
•	The numbers 13, 19, 14, and 15 fall into the group of 20's.
For more clarification, see the examples below.

Hints
•	Keep track of the group using a variable to store its max value.
•	Create a loop and filter the elements that are less than or equal to the group boundary and remove them from
the original list.
•	Increase the boundary by 10.
•	Loop until the given list is empty.
"""

sequence_of_numbers = input().split(", ")
group = 10
current_group = []
remove_list = []

while sequence_of_numbers:
	for number in sequence_of_numbers:
		if group - 10 < int(number) <= group:
			remove_list.append(number)
			current_group.append(int(number))
	print(f"Group of {group}'s: {current_group}")

	for number in remove_list:
		if number in sequence_of_numbers:
			sequence_of_numbers.remove(number)
	current_group = []
	group += 10

# ----------------------------------------------------------------------------------------------------------------------
#
# sequence_of_numbers = [int(number) for number in input().split(", ")]
# current_group = 10
# while sequence_of_numbers:
#     current_numbers = [number for number in sequence_of_numbers if number <= current_group]
#     print(f"Group of {current_group}'s: {current_numbers}")
#     current_group += 10
#     sequence_of_numbers = [number for number in sequence_of_numbers if number not in current_numbers]
