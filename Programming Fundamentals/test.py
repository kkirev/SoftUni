def win_what(material):
    if material == "shards":
        win = "Shadowmourne"
    elif material == "fragments":
        win = "Valanyr"
    elif material == "motes":
        win = "Dragonwrath"
    return win


legendary_items = {"shards": 0, "fragments": 0, "motes": 0}
obtained = False

while not obtained:
    materials = input().lower().split()
    for index in range(0, len(materials), 2):
        quantity = int(materials[index])
        material = materials[index + 1]

        if material not in legendary_items:
            legendary_items[material] = quantity
        else:
            legendary_items[material] += quantity

        if legendary_items[material] >= 250:
            legendary_items[material] -= 250
            obtained = True
            break

if obtained:
    print(f"{win_what(material)} obtained!")
    for material, quantity in legendary_items.items():
        print(f"{material}: {quantity}")
