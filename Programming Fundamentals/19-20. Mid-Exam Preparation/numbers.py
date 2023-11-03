numbers = [int(number) for number in input().split()]
average_value = sum(numbers) / len(numbers)

numbers_above_average = [number for number in numbers if number > average_value]
descending_order = sorted(numbers_above_average, reverse=True)

if numbers_above_average:
	print(*descending_order[:5], sep=" ")
else:
	print("No")