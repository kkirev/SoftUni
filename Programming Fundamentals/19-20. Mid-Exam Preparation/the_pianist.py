# pieces_number = int(input())
# for piece in range(pieces_number):
# 	piece_name, composer, key = input().split("|")
#
# command = input()
# while command != "Stop":
# 	if command.split("|")[0] == "Add":
# 		action, piece_name, composer, key = command.split("|")
# 		# some action need to be done
# 		print(f"{piece_name} by {composer} in {key} added to the collection!")
#
# 	elif command.split("|")[0] == "Remove":
# 		action, piece_name = command.split("|")
# 		# some action need to be done
# 		print(f"Successfully removed {piece_name}!")
#
# 	elif command.split("|")[0] == "ChangeKey":
# 		action, piece_name, new_key = command.split("|")
# 		# if something:	# some action need to be done
# 		print(f"Changed the key of {piece_name} to {new_key}!")
# 		# else:
# 		print(f"Invalid operation! {piece_name} does not exist in the collection.")
#
# if command == "Stop":
# 	print(f"{piece_name} -> Composer: {composer}, Key: {key}")
#
# 	command = input()

def add_piece(collection, piece, composer, key):
    if piece not in collection:
        collection[piece] = {"composer": composer, "key": key}
        print(f"{piece} by {composer} in {key} added to the collection!")
    else:
        print(f"{piece} is already in the collection!")


def remove_piece(collection, piece):
    if piece in collection:
        del collection[piece]
        print(f"Successfully removed {piece}!")
    else:
        print(f"Invalid operation! {piece} does not exist in the collection.")


def change_key(collection, piece, new_key):
    if piece in collection:
        collection[piece]["key"] = new_key
        print(f"Changed the key of {piece} to {new_key}!")
    else:
        print(f"Invalid operation! {piece} does not exist in the collection.")


def print_collection(collection):
    for piece, details in collection.items():
        composer = details["composer"]
        key = details["key"]
        print(f"{piece} -> Composer: {composer}, Key: {key}")


n = int(input())
collection = {}

for _ in range(n):
    piece_info = input().split("|")
    piece, composer, key = piece_info
    collection[piece] = {"composer": composer, "key": key}

while True:
    command = input()
    if command == "Stop":
        break

    command_parts = command.split("|")
    action = command_parts[0]
    piece = command_parts[1]

    if action == "Add":
        composer = command_parts[2]
        key = command_parts[3]
        add_piece(collection, piece, composer, key)
    elif action == "Remove":
        remove_piece(collection, piece)
    elif action == "ChangeKey":
        new_key = command_parts[2]
        change_key(collection, piece, new_key)

print_collection(collection)

# Solution by ChatGPT
