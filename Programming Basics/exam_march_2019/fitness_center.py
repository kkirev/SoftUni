"""
Напишете програма, която да изчислява броя на посетителите в един фитнес център. В началото програмата получава
броя на посетителите на фитнеса и за всеки човек - дейността, която извършва във фитнеса. На края програмата трябва
да отпечата броят трениращи за всяка една дейност ("Back", "Chest", 'Legs", "Abs") и броят клиенти,
закупили продукт ("Protein shake", "Protein bar"). Също така - процентът трениращи (спрямо общия брой посетители)
и процентът на клиентите, закупили продукт от фитнеса.

Вход
От конзолата се чете число, след това поредица от низове, всяко на отделен ред:
•	На първия ред – броят на посетителите във фитнеса – цяло число в интервала [1...1000]
•	За всеки един посетител на отделен ред –
дейността във фитнеса – текст ("Back", "Chest", "Legs", "Abs", "Protein shake" или "Protein bar")

Изход
Да се отпечатат на конзолата 8 реда, които съдържат следната информация:
Ред 1 -	"{брой хора трениращи гръб} - back"
Ред 2 -	"{брой хора трениращи гърди} - chest"
Ред 3 -	"{брой хора трениращи крака} - legs"
Ред 4 -	"{брой хора трениращи коремни мускули} - abs"
Ред 5 -	"{брой хора закупили протеинов шейк} - protein shake"
Ред 6 -	"{брой хора закупили протеинов блок} - protein bar"
Ред 7 -	"{процент на хората дошли да тренират}% - work out"
Ред 8 -	"{процент на хората дошли да купят протеин}% - protein"
Всички проценти трябва да са форматирани до втората цифра след десетичния знак.
"""

visitors_count = int(input())

back_work = 0
chest_work = 0
legs_work = 0
abs_work = 0
protein_shake = 0
protein_bar = 0
work_out = 0
protein = 0
total_visitors = 0

for visitor in range(visitors_count):
    activity = input()

    if activity == 'Back':
        back_work += 1
        work_out += 1
        total_visitors += 1
    elif activity == 'Chest':
        chest_work += 1
        work_out += 1
        total_visitors += 1
    elif activity == 'Legs':
        legs_work += 1
        work_out += 1
        total_visitors += 1
    elif activity == 'Abs':
        abs_work += 1
        work_out += 1
        total_visitors += 1
    elif activity == 'Protein shake':
        protein_shake += 1
        protein += 1
        total_visitors += 1
    elif activity == 'Protein bar':
        protein_bar += 1
        protein += 1
        total_visitors += 1

print(f'{back_work} - back')
print(f'{chest_work} - chest')
print(f'{legs_work} - legs')
print(f'{abs_work} - abs')
print(f'{protein_shake} - protein shake')
print(f'{protein_bar} - protein bar')
print(f'{work_out / total_visitors * 100:.2f}% - work out')
print(f'{protein / total_visitors * 100:.2f}% - protein')