"""
https://judge.softuni.org/Contests/Practice/Index/1699#0

Напишете програма, която изчислява колко време ще ви отнеме да изгледате всички епизоди на един сериал в минути.
Ще разполагате с брой сезони, брой епизоди на сезон и времетраене на един епизод. Във всеки епизод има реклами, които
са с продължителност 20% от времето на един епизод. Също така знаете, че всеки сезон завършва със специален епизод,
който е с 10м по-дълъг от обичайното.

Вход
От конзолата се четат 4 реда:
•	Име на сериал - текст
•	Брой сезони – цяло число в диапазона [1… 10]
•	Брой епизоди  – цяло число в диапазона [10… 80]
•	Времетраене на обикновен епизод без рекламите – реално число в диапазона [40.0… 65.0]

Изход
Да се отпечата на конзолата времето, необходимо за изглеждане на всички епизоди,
закръглено до най-близкото цяло число надолу в следния формат:
"Total time needed to watch the {име на сериал} series is {време} minutes."
"""
from math import floor

series_name = input()
seasons_count = int(input())
episodes_count = int(input())
episode_length = float(input())

adv_time = 0.2 * episode_length
additional_time = seasons_count * 10
time_needed = (episode_length + adv_time) * episodes_count * seasons_count + additional_time

print(f'Total time needed to watch the {series_name} series is {floor(time_needed)} minutes.')