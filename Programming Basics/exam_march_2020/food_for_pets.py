"""
https://judge.softuni.org/Contests/Practice/Index/2275#6

Ани има два домашни любимеца - куче и котка. Напишете програма, която изготвя статистика за храната на домашните
любимци за определен брой дни. Всеки ден кучето и котката изяждат различно количество от общата им храна.
На всеки трети ден получават награда - бисквитки. Количеството на бисквитките е 10% от общо изядената храна за деня.
Вашата програма трябва да отпечатва статистика за кол-то бисквитки, които са изяли, колко процента от първоначалното
количество обща храна са изяли и колко процента от изядената храна е изяло кучето и колко е изяла котката.

Вход
Първоначално се чете един ред:
•	Брой дни – цяло число в диапазона [1…30]
•	Общо количество храна – реално число в диапазона [0.00…10000.00]
След това за всеки ден се чете:
o	Количество изядена храна от кучето – цяло число в диапазона [10…500]
o	Количество изядена храна от котката – цяло число в диапазона [10…500]

Изход
На конзолата да се отпечатват четири реда:
•	"Total eaten biscuits: {количество изядени бисквитки}gr."
•	"{процент изядена храна}% of the food has been eaten."
•	"{процент изядена храна от кучето}% eaten from the dog."
•	"{процент изядена храна от котката}% eaten from the cat."
Количеството изядени бисквитки трябва да бъде закръглено до най – близкото цяло число, а процентът храна трябва да бъде
форматиран до втората цифра след десетичния знак.
"""
days_count = int(input())
total_food = float(input())

total_eaten_dog = 0
total_eaten_cat = 0
total_eaten_food = 0
total_eaten_biscuits = 0

for day in range(1, days_count + 1):
    dog_eat = int(input())
    cat_eat = int(input())

    if day % 3 == 0:
        eaten_biscuits = (dog_eat + cat_eat) * 0.1
        total_eaten_biscuits += eaten_biscuits

    total_eaten_dog += dog_eat
    total_eaten_cat += cat_eat
    total_eaten_food += dog_eat + cat_eat

percent_eaten_dog = total_eaten_dog / total_eaten_food * 100
percent_eaten_cat = total_eaten_cat / total_eaten_food * 100
percent_eaten_food = total_eaten_food / total_food * 100

print(f"Total eaten biscuits: {round(total_eaten_biscuits)}gr.")
print(f"{percent_eaten_food:.2f}% of the food has been eaten.")
print(f"{percent_eaten_dog:.2f}% eaten from the dog.")
print(f"{percent_eaten_cat:.2f}% eaten from the cat.")