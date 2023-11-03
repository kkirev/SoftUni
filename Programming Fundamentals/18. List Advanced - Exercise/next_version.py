"""
You are fed up with changing the version of your software manually. Instead, you will create a little script that will
make it for you. You will be given a string representing the version of your software in the format: "{n1}.{n2}.{n3}".
Your task is to print the next version. For example,if the current version is "1.3.4", the next version will be "1.3.5".
The only rule is that the numbers cannot be greater than 9. If it happens, set the current number to 0 and increase the
previous number. For more clarification, see the examples below.
Note: there will be no case in which the first number will become greater than 9.
"""
# Konstantin's task solution

current_version = input().split(".")
new_version = [int(digit) for digit in current_version]

if new_version[2] < 9:
	new_version[2] += 1
else:
	new_version[2] = 0
	if new_version[1] < 9 and new_version[2] == 0:
		new_version[1] += 1
	else:
		new_version[1] = 0
		if new_version[0] < 8 and new_version[1] == 0:
			new_version[0] += 1

print(*new_version, sep=".")

# --------------------------------------------------------------------------------------------------------------------
# Ivan Shopov's task solution
#
# current_version = [int(digit) for digit in input().split(".")]
# current_version[-1] += 1
# for index in range(len(current_version) - 1, 0, -1):
#     if current_version[index] > 9:
#         current_version[index] = 0
#         current_version[index - 1] += 1
# print(".".join(str(digit) for digit in current_version))
