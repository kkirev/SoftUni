"""
Write a function that checks if a given password is valid. Password validations are:
•	It should be 6 - 10 (inclusive) characters long
•	It should consist only of letters and digits
•	It should have at least 2 digits
If a password is valid, print "Password is valid".
Otherwise, for every unfulfilled rule, print a message:
•	"Password must be between 6 and 10 characters"
•	"Password must consist only of letters and digits"
•	"Password must have at least 2 digits"
"""


def password_validator(some_pasword: str) -> list:
	errors_list = []
	if not 6 <= len(some_pasword) <= 10:
		errors_list.append("Password must be between 6 and 10 characters")

	if not some_pasword.isalnum():
		errors_list.append("Password must consist only of letters and digits")

	digits_count = 0
	for char in some_pasword:
		if char.isdigit():
			digits_count += 1
	if digits_count < 2:
		errors_list.append("Password must have at least 2 digits")
	return errors_list


password = input()
validated_password = password_validator(password)

if len(validated_password) == 0:
	print(f"Password is valid")
else:
	print("\n".join(validated_password))


# def password_validator(password: str) -> str:
# 	valid_password = True
# 	if not 6 <= len(password) <= 10:
# 		print(f"Password must be between 6 and 10 characters")
# 		valid_password = False
#
# 	for element in password:
# 		if 49 <= ord(element) <= 57 or 65 <= ord(element) <= 90 or 97 <= ord(element) <= 122:
# 			pass
# 		else:
# 			print(f"Password must be between 6 and 10 characters")
# 			valid_password = False
# 			break
#
# 	digits_count = 0
# 	for element in password:
# 		if 49 <= ord(element) <= 57:
# 			digits_count += 1
# 	if digits_count < 2:
# 		print(f"Password must have at least 2 digits")
# 		valid_password = False
#
# 	if valid_password:
# 		return "Password is valid"
#
#
# password = input()
# print(password_validator(password))
#
# # Judge 40/100 - първоначален опит преди да гледам видео с решението на Иван Шопов от 06.10.2023
