# В кутия имаме неопределен брой топки с различни цветове, които ни носят различен брой точки. Задачата ни е да извадим Х бр. топки, които ще бъдат въведени от конзолата, като се има в предвид, че всеки различен цвят влияе на точките ни по следния начин:
# •	Ако топката е “red” точките ни се повишават с 5.
# •	Ако топката е “orange” точките ни се повишават с 10.
# •	Ако топката е “yellow” точките ни се повишават с 15.
# •	Ако топката е “white” точките ни се повишават с 20.
# •	Ако топката е “black” точките ни се делят на 2, като закръгляме към по-малкото цяло число.
# Ако топката е с какъвто и да е цвят, различен от по-горните,
# точките не се манипулират и програмата продължава да работи.

# Вход:
# 1.	От конзолата се чете 1 цяло число N, което е броят на топките в диапазон (0-1000).
# 2.	След това се четат N на брой цветове.

# Изход:
# Отпечатват се следните редове:
# "Total points: {всичките събрани точки}"
# "Red balls: {броят червени топки}"
# "Orange balls: {броят оранжеви топки}"
# "Yellow balls: {броят жълти топки}"
# "White balls: {броят бели топки}"
# "Other colors picked: {броят на избраните топки извън зададените цветове}"
# "Divides from black balls: {броят на пътите, в които точките са били разделяни на 2}"

balls_count = int(input())

red_balls = 0
orange_balls = 0
yellow_balls = 0
white_balls = 0
black_balls = 0
others_balls = 0
total_points = 0

for ball in range(balls_count):
    ball_color = input()

    if ball_color == 'red':
        red_balls += 1
        total_points += 5
    elif ball_color == 'orange':
        orange_balls += 1
        total_points += 10
    elif ball_color == 'yellow':
        yellow_balls += 1
        total_points += 15
    elif ball_color == 'white':
        white_balls += 1
        total_points += 20
    elif ball_color == 'black':
        black_balls += 1
        total_points //= 2
    else:
        others_balls += 1

print(f'Total points: {total_points}')
print(f'Red balls: {red_balls}')
print(f'Orange balls: {orange_balls}')
print(f'Yellow balls: {yellow_balls}')
print(f'White balls: {white_balls}')
print(f'Other colors picked: {others_balls}')
print(f'Divides from black balls: {black_balls}')