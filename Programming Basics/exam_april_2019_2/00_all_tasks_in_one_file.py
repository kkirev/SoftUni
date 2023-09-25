# breads_count = int(input())
# eggs_boxes = int(input())
# cookies_kilograms = int(input())
#
# expenses = (breads_count * 3.2) + (eggs_boxes * 4.35 + (eggs_boxes * 12 * 0.15)) + (cookies_kilograms * 5.4)
# print(f'{expenses:.2f}')
#
# ----------------------------------------------------------------------------------------------------------------------
#
# flour_price_per_kg = float(input())
# flour_amount_in_kg = float(input())
# sugar_amount_in_kg = float(input())
# eggs_box_count = int(input())
# yeast_pack_count = int(input())
#
# sugar_price_per_kg = 0.75 * flour_price_per_kg
# eggs_box_price = 1.1 * flour_price_per_kg
# yeast_pack_price = 0.2 * sugar_price_per_kg
#
# total_sum = ((flour_amount_in_kg * flour_price_per_kg) + (sugar_amount_in_kg * sugar_price_per_kg) +
#              (eggs_box_price * eggs_box_count) + (yeast_pack_price * yeast_pack_count))
# print(f'{total_sum:.2f}')
#
# ----------------------------------------------------------------------------------------------------------------------
#
# guests_count = int(input())
# charge_per_guest = float(input())
# budget = float(input())
# cake_price = 0.1 * budget
#
# if 10 <= guests_count <= 15:
#     charge_per_guest *= 0.85
# elif 16 <= guests_count <= 20:
#     charge_per_guest *= 0.80
# elif guests_count > 20:
#     charge_per_guest *= 0.75
#
# money_needed = guests_count * charge_per_guest + cake_price
# difference = abs(budget - money_needed)
#
# if budget >= money_needed:
#     print(f"It is party time! {difference:.2f} leva left.")
# else:
#     print(f"No party! {difference:.2f} leva needed.")
#
# ----------------------------------------------------------------------------------------------------------------------
#
# from math import ceil
#
# guests_count = int(input())
# budget = int(input())
#
# bread_count = ceil(guests_count / 3)
# eggs_count = guests_count * 2
# bread_price = 4
# egg_price = 0.45
#
# total_expenses = (bread_price * bread_count) + (egg_price * eggs_count)
# difference = abs(budget - total_expenses)
#
# if budget >= total_expenses:
#     print(f"Lyubo bought {bread_count} Easter bread and {eggs_count} eggs.")
#     print(f"He has {difference:.2f} lv. left.")
# else:
#     print(f"Lyubo doesn't have enough money.")
#     print(f"He needs {difference:.2f} lv. more.")
#
# ----------------------------------------------------------------------------------------------------------------------
#
# trip_destination = input()
# trip_period = input()
# nights_count = int(input())
#
# price_per_night = 0
#
# if trip_destination == "France":
#     if trip_period == "21-23":
#         price_per_night = 30
#     elif trip_period == "24-27":
#         price_per_night = 35
#     elif trip_period == "28-31":
#         price_per_night = 40

# elif trip_destination == "Italy":
#     if trip_period == "21-23":
#         price_per_night = 28
#     elif trip_period == "24-27":
#         price_per_night = 32
#     elif trip_period == "28-31":
#         price_per_night = 39

# elif trip_destination == "Germany":
#     if trip_period == "21-23":
#         price_per_night = 32
#     elif trip_period == "24-27":
#         price_per_night = 37
#     elif trip_period == "28-31":
#         price_per_night = 43
#
# trip_expenses = nights_count * price_per_night
# print(f"Easter trip to {trip_destination} : {trip_expenses:.2f} leva.")
#
# ----------------------------------------------------------------------------------------------------------------------
#
# eggs_size = input()
# eggs_color = input()
# eggs_count = int(input())
# eggs_price = 0
#
# if eggs_size == "Large":
#     if eggs_color == "Red":
#         eggs_price = 16
#     elif eggs_color == "Green":
#         eggs_price = 12
#     elif eggs_color == "Yellow":
#         eggs_price = 9

# elif eggs_size == "Medium":
#     if eggs_color == "Red":
#         eggs_price = 13
#     elif eggs_color == "Green":
#         eggs_price = 9
#     elif eggs_color == "Yellow":
#         eggs_price = 7

# elif eggs_size == "Small":
#     if eggs_color == "Red":
#         eggs_price = 9
#     elif eggs_color == "Green":
#         eggs_price = 8
#     elif eggs_color == "Yellow":
#         eggs_price = 5
#
# total_income = eggs_count * eggs_price
# final_profit = total_income * 0.65
# print(f"{final_profit:.2f} leva.")
#
# ----------------------------------------------------------------------------------------------------------------------
#
# first_player_eggs_count = int(input())
# second_player_eggs_count = int(input())
#
# command = input()
#
# while command != "End":
#     if command == "one":
#         second_player_eggs_count -= 1
#     elif command == "two":
#         first_player_eggs_count -= 1
#
#     if first_player_eggs_count <= 0:
#         print(f"Player one is out of eggs. Player two has {second_player_eggs_count} eggs left.")
#         break
#     elif second_player_eggs_count <= 0:
#         print(f"Player two is out of eggs. Player one has {first_player_eggs_count} eggs left.")
#         break
#
#     command = input()
#
# if command == "End":
#     print(f"Player one has {first_player_eggs_count} eggs left.")
#     print(f"Player two has {second_player_eggs_count} eggs left.")
#
# ----------------------------------------------------------------------------------------------------------------------
#
# eggs_stock = int(input())
# eggs_sold = 0
#
# while True:
#     shop_close = False
#     not_enough_eggs = False
#
#     command = input()
#     if command != "Close":
#         eggs_count = int(input())
#     else:
#         shop_close = True
#         break
#
#     if command == "Buy":
#         if eggs_count > eggs_stock:
#             not_enough_eggs = True
#             break
#         else:
#             eggs_stock -= eggs_count
#             eggs_sold += eggs_count
#     elif command == "Fill":
#         eggs_stock += eggs_count
#
# if shop_close:
#     print(f"Store is closed!")
#     print(f"{eggs_sold} eggs sold.")
# if not_enough_eggs:
#     print("Not enough eggs in store!")
#     print(f"You can buy only {eggs_stock}.")
#
# ----------------------------------------------------------------------------------------------------------------------
#
# painted_eggs_count = int(input())
# red_eggs = 0
# orange_eggs = 0
# blue_eggs = 0
# green_eggs = 0
# total_eggs = red_eggs + orange_eggs + blue_eggs + green_eggs
# max_eggs_count = 0
# max_eggs_color = ''
#
# for egg in range(painted_eggs_count):
#     color = input()
#
#     if color == "red":
#         red_eggs += 1
#         if red_eggs > max_eggs_count:
#             max_eggs_count = red_eggs
#             max_eggs_color = "red"
#
#     elif color == "orange":
#         orange_eggs += 1
#         if orange_eggs > max_eggs_count:
#             max_eggs_count = orange_eggs
#             max_eggs_color = "orange"
#
#     elif color == "blue":
#         blue_eggs += 1
#         if blue_eggs > max_eggs_count:
#             max_eggs_count = blue_eggs
#             max_eggs_color = "blue"
#
#     elif color == "green":
#         green_eggs += 1
#         if green_eggs > max_eggs_count:
#             max_eggs_count = green_eggs
#             max_eggs_color = "green"
#
# print(f"Red eggs: {red_eggs}")
# print(f"Orange eggs: {orange_eggs}")
# print(f"Blue eggs: {blue_eggs}")
# print(f"Green eggs: {green_eggs}")
# print(f"Max eggs: {max_eggs_count} -> {max_eggs_color}")
#
# ----------------------------------------------------------------------------------------------------------------------
#
# from math import ceil
#
# easter_breads_count = int(input())
# max_suger_used_grams = 0
# max_flour_used_grams = 0
# necessary_sugar_grams = 0
# necessary_flour_grams = 0
#
# for easter_bread in range(easter_breads_count):
#     sugar_used_grams = int(input())
#     flour_used_grams = int(input())
#
#     necessary_sugar_grams += sugar_used_grams
#     necessary_flour_grams += flour_used_grams
#
#     if sugar_used_grams > max_suger_used_grams:
#         max_suger_used_grams = sugar_used_grams
#     if flour_used_grams > max_flour_used_grams:
#         max_flour_used_grams = flour_used_grams
#
# necessary_sugar_packs = ceil(necessary_sugar_grams / 950)
# necessary_flour_packs = ceil(necessary_flour_grams / 750)
#
# print(f"Sugar: {necessary_sugar_packs}")
# print(f"Flour: {necessary_flour_packs}")
# print(f"Max used flour is {max_flour_used_grams} grams, max used sugar is {max_suger_used_grams} grams.")
#
# ----------------------------------------------------------------------------------------------------------------------
#
# easter_bread_count = int(input())
# max_score = 0
# max_scored_baker = ''
#
# for easter_bread in range(easter_bread_count):
#     baker_name = input()
#     command = input()
#     total_score = 0
#
#     while command != "Stop":
#         easter_bread_rate = int(command)
#         total_score += easter_bread_rate
#         command = input()
#
#         if command == "Stop":
#             print(f"{baker_name} has {total_score} points.")
#             if total_score > max_score:
#                 max_score = total_score
#                 max_scored_baker = baker_name
#                 print(f"{baker_name} is the new number 1!")
#
# print(f"{max_scored_baker} won competition with {max_score} points!")
#
# ----------------------------------------------------------------------------------------------------------------------
#
# customers_count = int(input())
# total_sum = 0
#
# for customer in range(customers_count):
#     items_count = 0
#     current_bill = 0
#     command = input()
#     while command != "Finish":
#         purchase = command
#         items_count += 1
#
#         if purchase == "basket":
#             current_bill += 1.5
#         elif purchase == "wreath":
#             current_bill += 3.8
#         elif purchase == "chocolate bunny":
#             current_bill += 7
#
#         command = input()
#
#         if command == "Finish":
#             if items_count % 2 == 0:
#                 current_bill *= 0.8
#             total_sum += current_bill
#             print(f"You purchased {items_count} items for {current_bill:.2f} leva.")
# average_bill = total_sum / customers_count
# print(f"Average bill per client is: {average_bill:.2f} leva.")