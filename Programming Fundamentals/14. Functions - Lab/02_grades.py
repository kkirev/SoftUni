"""
Write a function that receives a grade between 2.00 and 6.00 and prints the corresponding grade in words.
•	2.00 – 2.99 - "Fail"
•	3.00 – 3.49 - "Poor"
•	3.50 – 4.49 - "Good"
•	4.50 – 5.49 - "Very Good"
•	5.50 – 6.00 - "Excellent"
"""

grade = float(input())

def grade_givers(grade):
	if 2 <= grade < 3:
		return "Fail"
	elif 3 <= grade < 3.5:
		return "Poor"
	elif 3.5 <= grade < 4.5:
		return "Good"
	elif 4.5 <= grade < 5.5:
		return "Very Good"
	elif 5.5 <= grade < 6:
		return "Excellent"


print(grade_givers(grade))