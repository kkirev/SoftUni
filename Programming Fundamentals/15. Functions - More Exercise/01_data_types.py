"""
Write a function that, depending on the first line of the input, reads one of the following strings: "int", "real", or "string".
•	If the data type is an int, multiply the number by 2.
•	If the data type is real, multiply the number by 1.5 and format the result to the second decimal point.
•	If the data type is a string, surround the input with "$".
Print the result on the console.
"""

def data_type_picker(data_type, data_value: str):
    if data_type == "int":
        return int(data_value) * 2
    if data_type == "real":
        mid_result = float(data_value) * 1.5
        return f"{mid_result:.2f}"
    if data_type == "string":
        return f"${data_value}$"


data_type = input()
data_value = input()
result = data_type_picker(data_type, data_value)
print(result)