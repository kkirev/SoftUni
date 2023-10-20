"""
You will receive a number representing the number of wagons a train has. Create a list (train) with the given length
containing only zeros. Until you receive the command "End", you will receive some of the following commands:
•	"add {people}" – you should add the number of people in the last wagon
•	"insert {index} {people}" - you should add the number of people at the given wagon
•	"leave {index} {people}" - you should remove the number of people from the wagon. There will be no case in which
the people will be more than the count in the wagon.
There will be no case in which the index is invalid!
After you receive the "End" command print the train.
"""

wagons_count = int(input())
train = [0] * wagons_count

# for wagon in wagons_count:
# 	train.append(0)

command = input()
while command != "End":
	action = command.split()[0]

	if action == "add":
		people_count = int(command.split()[1])
		train[-1] += people_count

	elif action == "insert":
		index = int(command.split()[1])
		people_count = int(command.split()[2])
		train[index] += people_count

	elif action == "leave":
		index = int(command.split()[1])
		people_count = int(command.split()[2])
		train[index] -= people_count

	command = input()

print(train)
