initial_cards = input().split(", ")
commands_count = int(input())

for current_comand in range(commands_count):
    command = input().split(", ")
    action = command[0]

    if action == "Add":
        curr_card = command[1]
        if curr_card in initial_cards:
            print("Card is already in the deck")
        else:
            initial_cards.append(curr_card)
            print("Card successfully added")

    elif action == "Remove":
        curr_card = command[1]
        if curr_card in initial_cards:
            initial_cards.remove(curr_card)
            print("Card successfully removed")
        else:
            print("Card not found")

    elif action == "Remove At":
        index = int(command[1])
        if 0 <= index < len(initial_cards):
            initial_cards.pop(index)
            print("Card successfully removed")
        else:
            print("Index out of range")

    elif action == "Insert":
        index = int(command[1])
        curr_card = command[2]
        if 0 <= index < len(initial_cards):
            if curr_card in initial_cards:
                print("Card is already added")
            else:
                initial_cards.insert(index, curr_card)
                print("Card successfully added")
        else:
            print("Index out of range")

print(", ".join(initial_cards))
