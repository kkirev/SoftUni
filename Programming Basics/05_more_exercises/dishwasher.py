"""
https://judge.softuni.org/Contests/Practice/Index/1684#0

Гошо работи в ресторант и отговаря за зареждането на съдомиялната накрая на деня.
Вашата задача е да напишете програма, която изчислява, дали дадено закупено количество бутилки от препарат за
съдомиялна е достатъчно, за да измие определено количество съдове. Знае се, че всяка бутилка съдържа 750 мл.
препарат, за 1 чиния са нужни 5 мл., а за тенджера 15 мл.  Приемете, че на всяко трето зареждане със съдове,
съдомиялната се пълни само с тенджери, а останалите пъти с чинии. Докато не получите команда "End" ще продължите
да получавате бройка съдове, които трябва да бъдат измити.
Вход
От конзолата се четат:
•	Брой бутилки от препарат, който ще бъде използван за миенето на чинии - цяло число в интервала [1…10]
На всеки следващ ред, до получаване на командата "End" или докато количеството препарат не се изчерпи, брой съдове,
които трябва да бъдат измити - цяло число в интервала [1…100]
Изход
В случай, че количеството препарат е било достатъчно за измиването на съдовете:
"Detergent was enough!"
"{брой чисти чинии} dishes and {брой чисти тенджери} pots were washed."
"Leftover detergent {количество останал препарат} ml."
В случай, че количеството препарат не е било достатъчно за измиването на съдовете:
"abs"
"""

bottles_count = int(input())

detergent = bottles_count * 750
saucepans_count = 0
plates_count = 0
cycle = 0

while detergent >= 0:
    command = input()
    cycle += 1
    if command == 'End':
        break
    if cycle % 3 == 0:
        detergent -= int(command) * 15
        saucepans_count += int(command)
    else:
        detergent -= int(command) * 5
        plates_count += int(command)

if detergent >= 0:
    print(f'Detergent was enough!')
    print(f'{plates_count} dishes and {saucepans_count} pots were washed.')
    print(f'Leftover detergent {detergent} ml.')
else:
    print(f'Not enough detergent, {abs(detergent)} ml. more necessary!')