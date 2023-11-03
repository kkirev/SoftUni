"""
Ely likes to play Pokemon Go a lot.But Pokemon Go bankrupted… So the developers made Pokemon Don't Go out of depression.
And so Ely now plays Pokemon Don't Go. In Pokemon Don't Go, when you walk to a certain pokemon, those closest to you
naturally get further, and those further from you, get closer.
You will receive a sequence of integers, separated by spaces - the distances to the pokemon.
Then you will begin receiving integers, which will correspond to indexes in that sequence.
When you receive an index, you must remove the element at that index from the sequence
(as if you've captured the pokemon).
•	You must increase the value of all elements in the sequence which are less or equal to the removed element with
the value of the removed element.
•	You must decrease the value of all elements in the sequence which are greater than the removed element with the
value of the removed element.
If the given index is less than 0, remove the first element of the sequence, and copy the last element to its place.
If the given index is greater than the last index of the sequence, remove the last element from the sequence,
and copy the first element to its place.
The increasing and decreasing elements should also be done in these cases.
The element whose value you should use is the removed element.
The program ends when the sequence has no elements (there are no pokemon left for Ely to catch).

Input
•	On the first line of input, you will receive a sequence of integers, separated by spaces.
•	On the next several lines, you will receive integers - the indexes.

Output
•	When the program ends, you must print the summed value of all removed elements.
Constrains
•	The input data will consist only of valid integers in the range [-2.147.483.648…2.147.483.647].
"""

start_sequence = [int(number) for number in input().split()]
index = int(input())

selected_num = int(start_sequence[index])
sum_list = []
while start_sequence:
	for number in start_sequence:
		start_sequence.remove(start_sequence[index])

		start_sequence = [
			number + selected_num if number <= selected_num else number - selected_num for number in start_sequence
		]
		# if number <= selected_num:
		# 	start_sequence = [number + selected_num for number in start_sequence]
		# elif number > selected_num:
		# 	start_sequence = [number - selected_num for number in start_sequence]

		if index < 0:
			selected_num = start_sequence[0]
		elif index > len(start_sequence) + 1:
			selected_num = start_sequence[len(start_sequence) - 1]  # check this index (-1) if the program doesn't work

		sum_list.append(selected_num)
	index = int(input())
print(sum_list)
