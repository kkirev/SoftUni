# Магазин за компютърни игри ви наема за да направите статистика на процента продажби на игрите от последния месец,
# като изчислите по колко процента от общите продажби са за някоя от игрите.
# Процентите трябва да бъдат разделени на четири части, три заглавия на игри и всички останали :
# •	Hearthstone
# •	Fornite
# •	Overwatch
# •	Others

# Вход
# От конзолата се четат:
# •	Брой продадени игри- n - цяло положително число в интервала [1… 100]
# За следващите n реда се чете по един ред:
# o	Име на игра - текст

# Изход
# На конзолата да се изпишат четири реда:
# 	"Hearthstone - {процент продажби на Hearthstone}%"
# 	"Fornite - {процент продажби на Fornite}%"
# 	"Overwatch - {процент продажби на Overwatch}%"
# 	"Others - {процент продажби на всички останали игри}%"
# Резултатът да бъде закръглен до втората цифра след десетичния знак.

hearthstone_sold = 0
fornite_sold = 0
overwatch_sold = 0
others_sold = 0
total_sales = 0

games_sold = int(input())
for sales in range(games_sold):
    game_name = input()

    if game_name == 'Hearthstone':
        hearthstone_sold += 1
        total_sales += 1

    elif game_name == 'Fornite':
        fornite_sold += 1
        total_sales += 1

    elif game_name == 'Overwatch':
        overwatch_sold += 1
        total_sales += 1

    else:
        others_sold += 1
        total_sales += 1

print(f'Hearthstone - {hearthstone_sold / total_sales * 100:.2f}%')
print(f'Fornite - {fornite_sold / total_sales * 100:.2f}%')
print(f'Overwatch - {overwatch_sold / total_sales * 100:.2f}%')
print(f'Others - {others_sold / total_sales * 100:.2f}%')