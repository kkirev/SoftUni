"""
https://judge.softuni.org/Contests/Compete/Index/2420#1

Напишете програма, в която Марин решава задачи от изпити, докато не получи съобщение "Enough" от лектора си.
При всяка решена задача той получава оценка. Програмата трябва да приключи прочитането на данни при команда "Enough"
или ако Марин получи определения брой незадоволителни оценки. Незадоволителна е всяка оценка,
която е по-малка или равна на 4.
Вход
•	На първи ред - брой незадоволителни оценки - цяло число;
•	След това многократно се четат по два реда:
o	Име на задача – текст;
o	Оценка - цяло число в интервала [2…6]
Изход
•	Ако Марин стигне до командата "Enough", отпечатайте на 3 реда:
o	"Average score: {средна оценка}"
o	"Number of problems: {броя на всички задачи}"
o	"Last problem: {името на последната задача}"
•	Ако получи определеният брой незадоволителни оценки:
o	"You need a break, {брой незадоволителни оценки} poor grades."
Средната оценка да бъде форматирана до втория знак след десетичната запетая.
"""

max_failures = int(input())

tasks_count = 0
failures = 0
total_score = 0
last_task = ''
has_failed = True

while failures < max_failures:
    current_task = input()
    if current_task == 'Enough':
        has_failed = False
        break

    current_score = int(input())

    total_score += current_score
    tasks_count += 1
    last_task = current_task

    if current_score <= 4:
        failures += 1

if has_failed:
    print(f'You need a break, {failures} poor grades.')

else:
    average_score = total_score / tasks_count
    print(f'Average score: {average_score:.2f}')
    print(f'Number of problems: {tasks_count}')
    print(f'Last problem: {last_task}')