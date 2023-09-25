"""
https://judge.softuni.org/Contests/Practice/Index/1680#0

За даден период от време, всеки ден в болницата пристигат пациенти за преглед.
Тя разполага първоначално със 7 лекари. Всеки лекар може да преглежда само по един пациент на ден,
но понякога има недостиг на лекари, затова останалите пациенти се изпращат в други болници. Всеки трети ден,
болницата прави изчисления и ако броят на непрегледаните пациенти е по-голям от броя на прегледаните,
се назначава още един лекар. Като назначаването става преди да започне приемът на пациенти за деня.
Напишете програма, която изчислява за дадения период броя на прегледаните и непрегледаните пациенти.
Вход
Входът се чете от конзолата и съдържа:
•	На първия ред – периода, за който трябва да направите изчисления. Цяло число в интервала [1 ... 1000]
•	На следващите редове(равни на броят на дните) – броя пациенти, които пристигат за преглед за текущия ден.
Цяло число в интервала [0…10 000]
Изход
Да се отпечатат на конзолата 2 реда :
•	На първия ред: "Treated patients: {брой прегледани пациенти}."
•	На втория ред: "Untreated patients: {брой непрегледани пациенти}."
"""

# User input
period_forecast = int(input())

doctors_count = 7
treated_patients = 0
untreated_patients = 0

# Logic
for day in range(1, period_forecast + 1):
    patients_count = int(input())
    if day % 3 == 0 and untreated_patients > treated_patients:
        doctors_count += 1
        treated_patients += doctors_count
        untreated_patients += patients_count - doctors_count
    elif patients_count > doctors_count:
        treated_patients += doctors_count
        untreated_patients += patients_count - doctors_count
    else:
        treated_patients += patients_count

# Output
print(f'Treated patients: {treated_patients}.')
print(f'Untreated patients: {untreated_patients}.')