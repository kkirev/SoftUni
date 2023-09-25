"""
https://judge.softuni.org/Contests/Practice/Index/2275#5

Да се напише програма, която проверява дали първоначално налична сума е достатъчна,
за да се заплати карта за месечен достъп във фитнес.
Цената на картата зависи от пола на клиента и спорта, който практикува:

Пол	    Gym	    Boxing	    Yoga	    Zumba	    Dances	    Pilates
мъж	    $42	    $41	        $45	        $34	        $51	        $39
жена	$35	    $37	        $42	        $31	        $53	        $37

Всички цени на карти за ученици (възраст под 19 години вкл.) са с 20% намаление.
Вход

От конзолата се прочитат 4 реда:
•	Сумата, с която разполагаме - реално число в интервала [10.00…1000.00]
•	Пол - символ ('m' за мъж и 'f' за жена)
•	Възраст - цяло число в интервала [5…105]
•	Спорт - текст (една от възможностите в таблицата)

Изход
На конзолата се отпечатва 1 ред:
•	Ако сумата е достатъчна:
"You purchased a 1 month pass for {sport}."
където {sport} е въведения тип спорт
•	Ако сумата не е достатъчна трябва да се пресметне колко още пари са необходими, за да се закупи карта:
"You don't have enough money! You need ${money} more."
където {money} e оставащата сума нужна, за да се закупи картата, форматирана до втория знак след десетичната запетая.

"""

current_sum = float(input())
sex = input()
age = int(input())
activity = input()

subscription_sum = 0

if sex == 'm':
    if activity == 'Gym':
        subscription_sum = 42
    elif activity == 'Boxing':
        subscription_sum = 41
    elif activity == 'Yoga':
        subscription_sum = 45
    elif activity == 'Zumba':
        subscription_sum = 34
    elif activity == 'Dances':
        subscription_sum = 51
    elif activity == 'Pilates':
        subscription_sum = 39
elif sex == 'f':
    if activity == 'Gym':
        subscription_sum = 35
    elif activity == 'Boxing':
        subscription_sum = 37
    elif activity == 'Yoga':
        subscription_sum = 42
    elif activity == 'Zumba':
        subscription_sum = 31
    elif activity == 'Dances':
        subscription_sum = 53
    elif activity == 'Pilates':
        subscription_sum = 37
if age <= 19:
    subscription_sum *= 0.8

difference = abs(subscription_sum - current_sum)

if current_sum >= subscription_sum:
    print(f'You purchased a 1 month pass for {activity}.')
else:
    print(f"You don't have enough money! You need ${difference:.2f} more.")