"""
Anonymous has created a hyper cyber virus, which steals data from the CIA. The virus is known for its innovative and unbelievably clever merging and dividing data into partitions. As the lead security developer in the CIA, you have been tasked to analyze the software of the virus and observe its actions on the data.
You will receive a single input line containing strings, separated by spaces. The strings may contain any ASCII character except whitespace. Then you will begin receiving commands in one of the following formats:
•	merge {startIndex} {endIndex}
•	divide {index} {partitions}
Every time you receive the merge command, you must merge all elements from the startIndex to the endIndex. In other words, you should concatenate them.
Example: {abc, def, ghi} -> merge 0 1 -> {abcdef, ghi}
If any of the given indexes is out of the array, you must take only the range that is inside the array and merge it.
Every time you receive the divide command, you must divide the element at the given index into several small
substrings with equal length. The count of the substrings should be equal to the given partitions.
Example: {abcdef, ghi, jkl} -> divide 0 3 -> {ab, cd, ef, ghi, jkl}
If the string cannot be exactly divided into the given partitions, make all partitions except the last with equal
lengths and make the last one - the longest.
Example: {abcd, efgh, ijkl} -> divide 0 3 -> {a, b, cd, efgh, ijkl}
The input ends when you receive the command "3:1". At that point, you must print the resulting elements,
joined by a space.

Input
•	The first input line will contain the array of data.
•	On the next several input lines, you will receive commands in the format specified above.
•	The input ends when you receive the command "3:1".
Output
•	As output, you must print a single line containing the elements of the array, joined by a space.

Constrains
•	The strings in the array may contain any ASCII character except whitespace.
•	The startIndex and the endIndex will be in the range [-1000…1000].
•	The endIndex will always be greater than the startIndex.
•	The index in the divide command will always be inside the array.
•	The partitions will be in the range [0…100].
•	Allowed working time/memory: 100ms / 16MB.
"""

# Ivan Shopov Solution

text = input().split()
command = input().split()
while command[0] != "3:1":

	if command[0] == "merge":
		start_index = int(command[1])
		end_index = int(command[2])
		if start_index < 0:
			start_index = 0
		if end_index > len(text) - 1:
			end_index = len(text) - 1
		merged_elements = "".join(text[start_index:end_index + 1])
		# text = text[0:start_index] + [merged_elements] + text[end_index +1]
		text[start_index:end_index + 1] = [merged_elements]

	elif command[0] == "divide":
		index = int(command[1])
		partitions = int(command[2])
		element = text[index]
		divided_partition = []
		partition_length = len(element) // partitions
		for current_element_index in range(partitions):
			if current_element_index != partitions - 1:
				divided_partition.append(
					element[current_element_index * partition_length: (current_element_index + 1) * partition_length])
			else:
				divided_partition.append(element[current_element_index * partition_length:])
		text[index:index + 1] = divided_partition

	command = input().split()
print(" ".join(text))

# ---------------------------------------------------------------------------------------------------------------------
#
# IChat GPT Solution
#
# text = input().split()
#
# while True:
# 	command = input()
# 	if command == "3:1":
# 		break
#
# 	tokens = command.split()
# 	action = tokens[0]
#
# 	if action == "merge":
# 		start_index = max(0, int(tokens[1]))
# 		end_index = min(len(text) - 1, int(tokens[2]))
# 		merged = ''.join(text[start_index:end_index + 1])
# 		text = text[:start_index] + [merged] + text[end_index + 1:]
# 	elif action == "divide":
# 		index = int(tokens[1])
# 		partitions = int(tokens[2])
# 		part_length = len(text[index]) // partitions
# 		extra_length = len(text[index]) % partitions
# 		divided = [text[index][i:i + part_length] for i in range(0, len(text[index]), part_length)]
# 		if extra_length:
# 			divided[-1] += text[index][-extra_length:]
# 		text.pop(index)
# 		text = text[:index] + divided + text[index:]
#
# result = ' '.join(text)
# print(result)
