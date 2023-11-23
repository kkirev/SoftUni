"""
Write a program that reads the path to a file and subtracts the file name and its extension.
"""

file_path = input().split("\\")
the_file = file_path[-1]
file_name, file_extension = the_file.split(".")

print(f"File name: {file_name}")
print(f"File extension: {file_extension}")