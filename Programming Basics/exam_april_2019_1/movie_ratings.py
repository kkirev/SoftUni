"""
Деси много обича да гледа филми, но често й е трудно да си избере подходящ за гледане. Набелязва си определен брой
филми и иска да си избере кой филм да гледа спрямо рейтинга на филмите.
Напишете програма, която показва кой филм е с най-висок рейтинг, кой е с най-нисък и колко е средният рейтинг от
всички филми, които си е набелязала да гледа.

Вход
От конзолата първо се чете един ред:
•	Брой филми, които си е набелязала Деси – цяло число в интервала [1…20]
За всеки филм се прочитат два отделни реда:
•	Име на филма – текст
•	Рейтинг на филма - реално число в интервала [1.00…10.00]

Изход
Отпечатват се три реда в следния формат:
•	"{име на филма с най-висок рейтинг} is with highest rating: {рейтинг на филма}"
•	"{име на филма с най-нисък рейтинг} is with lowest rating: {рейтинг на филма}"
•	"Average rating: {средният рейтинг на всички филми}"
Максималният, минималният и средният рейтинг да се форматира до първата цифра след десетичния знак.
"""

movies_count = int(input())

highest_rating = 1
highest_rated_movie = ''

lowest_rating = 11
lowest_rated_movie = ''

average_rating = 0
total_ratings = 0

for movie in range(movies_count):
    movie_name = input()
    movie_rating = float(input())

    total_ratings += movie_rating

    if movie_rating > highest_rating:
        highest_rating = movie_rating
        highest_rated_movie = movie_name

    if movie_rating < lowest_rating:
        lowest_rating = movie_rating
        lowest_rated_movie = movie_name

average_rating = total_ratings / movies_count

print(f'{highest_rated_movie} is with highest rating: {highest_rating:.1f}')
print(f'{lowest_rated_movie} is with lowest rating: {lowest_rating:.1f}')
print(f'Average rating: {average_rating:.1f}')
