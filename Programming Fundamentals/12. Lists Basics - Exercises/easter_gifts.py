"""
As a good friend, you decide to buy presents for your friends.
Create a program that helps you plan the gifts for your friends and family. First, you are going to receive the gifts
you plan on buying on a single line, separated by space, in the following format:
"{gift1} {gift2} {gift3}… {giftn}"
Then you will start receiving commands until you read the "No Money" message. There are three possible commands:
•	"OutOfStock {gift}"
o	Find the gifts with this name in your collection, if any, and change their values to "None".
•	"Required {gift} {index}"
o	If the index is valid, replace the gift on the given index with the given gift.
•	"JustInCase {gift}"
o	Replace the value of your last gift with this one.
In the end, print the gifts on a single line, except the ones with value "None", separated by a single space in the f
ollowing format:

"{gift1} {gift2} {gift3} … {giftn}"

Input / Constraints
•	On the 1st line,  you will receive the names of the gifts, separated by a single space.
•	On the following lines, until the "No Money" command is received, you will be receiving commands.
•	The input will always be valid.

Output
•	Print the gifts in the format described above.
"""

gifts_list = input().split()
command = input()

while command != "No Money":
    if "OutOfStock" in command:
        gift = command[11:]
        for gift_index in range(len(gifts_list)):
            if gift == gifts_list[gift_index]:
                gifts_list[gift_index] = "None"
    elif "Required" in command:
        gift, gift_index = command[9:].split()
        if 0 <= int(gift_index) <= len(gifts_list):
            gifts_list[int(gift_index)] = gift
    elif "JustInCase" in command:
        new_gift = command[11:]
        gifts_list.pop()
        gifts_list.append(new_gift)

    command = input()

while "None" in gifts_list:
    gifts_list.remove("None")

print(" ".join(gifts_list))