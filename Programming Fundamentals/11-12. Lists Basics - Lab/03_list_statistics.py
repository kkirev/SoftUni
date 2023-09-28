"""
On the first line, you will receive a number n. On the following n lines, you will receive integers.
You should create and print two lists:
•	One with all the positives (including 0) numbers
•	One with all the negatives numbers
Finally, print the following message:
"Count of positives: {count_positives}
Sum of negatives: {sum_of_negatives}"

Example:

Input	       Output
5              [10, 3, 2]
10             [-15, -4]
3              Count of positives: 3
2              Sum of negatives: -19
-15
-4
"""

list_positive = []
list_negative = []

numbers_count = int(input())

for number in range(numbers_count):
    current_number = int(input())
    if current_number >= 0:
        list_positive.append(current_number)
    else:
        list_negative.append((current_number))

print(list_positive)
print(list_negative)
print(f"Count of positives: {len(list_positive)}")
print(f"Sum of negatives: {sum(list_negative)}")
