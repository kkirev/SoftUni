"""
The group of adventurists has gone on their first task. Now they should walk through fire - literally.
They should use all the water they have left. Your task is to help them survive.
Create a program that calculates the water needed to put out a "fire cell", based on the given information about
its "fire level" and how much it gets affected by water.
First, you will be given the level of fire inside the cell with the integer value of the cell, which represents the
needed water to put out the fire.  They will be given in the following format:
"{typeOfFire} = {valueOfCell}#{typeOfFire} = {valueOfCell}# … {typeOfFire} = {valueOfCell}"
Afterward you will receive the amount of water you have for putting out the fires. There is a range of fire for each
fire type, and if a cell's value is below or exceeds it, it is invalid, and you do not need to put it out.
Type of Fire	Range
High	81 - 125
Medium	51 - 80
Low	1 - 50
If a cell is valid, you should put it out by reducing the water with its value. Putting out fire also takes effort,
and you need to calculate it. Its value is equal to 25% of the cell's value. In the end, you will have to print the
total effort. Keep putting out cells until you run out of water. Skip it and try the next one if you do not have enough
water to put out a given cell. In the end, print the cells you have put out in the following format:
"Cells:
 - {cell1}
 - {cell2}
 …
 - {cellN}"
"Effort: {effort}"
The effort should be formatted to the second decimal place.
In the end, print the total fire you have put out from all the cells in the following format:
"Total Fire: {total_fire}"

Input / Constraints
•	On the 1st line, you will receive the fires with their cells in the format described above – integer numbers in
the range [1…500].
•	On the 2nd line, you will receive the water – an integer number in the range [0….100000].

Output
Print the output as described above.
"""

def calc_effort_and_put_out_fires(fires, water):
	fire_types = {"High": (81, 125), "Medium": (51, 80), "Low": (1, 50)}
	total_effort = 0
	cells_put_out = []

	for fire in fires:
		fire_info = fire.split(" = ")
		fire_type, cell_value = fire_info[0], int(fire_info[1])

		if fire_type in fire_types and fire_types[fire_type][0] <= cell_value <= fire_types[fire_type][1]:
			if water >= cell_value:
				water -= cell_value
				effort = 0.25 * cell_value
				total_effort += effort
				cells_put_out.append(cell_value)

	return cells_put_out, total_effort


fires_info = input().split("#")
water_available = int(input())

put_out_cells, total_effort = calc_effort_and_put_out_fires(fires_info, water_available)

print("Cells:")
for cell in put_out_cells:
	print(f" - {cell}")

print(f"Effort: {total_effort:.2f}")
print(f"Total Fire: {sum(put_out_cells)}")

# Chat GPT Solution, Judge 100/100
