"""
https://judge.softuni.org/Contests/2418

Шеф на компания забелязва че все повече служители прекарват  време в сайтове, които ги разсейват.
За да предотврати това, той въвежда изненадващи проверки на отворените табове на браузъра на служителите си.
Според отворения сайт в таба се налагат следните глоби:
•	"Facebook" -> 150 лв.
•	"Instagram" -> 100 лв.
•	"Reddit" -> 50 лв.
От конзолата се четат два реда:
•	Брой отворени табове в браузъра n - цяло число в интервала [1...10]
•	Заплата - число в интервала [500...1500]
След това n – на брой пъти се чете име на уебсайт – текст
Изход
•	Ако по време на проверката заплатата стане по-малка или равна на 0 лева, на конзолата се изписва
"You have lost your salary." и програмата приключва.
•	В противен случай след проверката на конзолата се изписва остатъкът от заплатата (да се изпише като цяло число).
"""

tabs_count = int(input())
salary = int(input())

for tab in range(tabs_count):
    current_website = input()

    if current_website == 'Facebook':
        salary -= 150
    elif current_website == 'Instagram':
        salary -= 100
    elif current_website == 'Reddit':
        salary -= 50

    if salary <= 0:
        print('You have lost your salary.')
        break

if salary > 0:
    print(salary)

# tabs_count = int(input())
# salary = int(input())
#
# for browser_tab in range(tabs_count):
#     current_website = input()
#     if salary <= 0:
#         print('You have lost your salary.')
#         break
#
#     if current_website == 'Facebook':
#         salary -= 150
#     elif current_website == 'Instagram':
#         salary -= 100
#     elif current_website == 'Reddit':
#         salary -= 50
# else:
#     print(salary)