"""
На световно първенство по художествена гимнастика три от държавите се изявяват като лидери в класирането
(Русия, България, Италия). Вашата задача е да изчислите каква е оценката дадена от журито за конкретно съчетание,
като знаете държавата, която е играла и с кой уред е играла - лента, обръч или въже. За съчетанието си, отбора е
получил две оценки: оценка за трудност и оценка за изпълнение на съчетанието, като крайната оценка е сбор на
двете оценки. В таблицата са показани какви оценки за трудност и изпълнение са получили ансамблите за всеки един уред.

  Уред	            Русия	                    България	                Италия
Лента(ribbon)	    Трудност: 9.100             Трудност: 9.600             Трудност: 9.200
                  Изпълнение: 9.400	        Изпълнение: 9.400           Изпълнение: 9.500

Обръч(hoop)	    Трудност: 9.300             Трудност: 9.550             Трудност: 9.450
                  Изпълнение: 9.800           Изпълнение: 9.750           Изпълнение: 9.350

Въже(rope)	    Трудност: 9.600             Трудност: 9.500             Трудност: 9.700
                  Изпълнение: 9.000	        Изпълнение: 9.400           Изпълнение: 9.150

Напишете програма, която изчислява каква е оценката на дадена държава за определен уред и колко процента не
им достигат, за да имат максималната оценка, която е 20.
Вход
Входът се чете от конзолата и се състои от два реда:
•	Първи ред – държава – текст ("Russia", "Bulgaria" или "Italy")
•	Втори ред – уред - текст ("ribbon", "hoop" или "rope")
Изход
На конзолата трябва да се отпечатат два реда:
•	Първи ред: "The team of {държава} get {обща оценка} on {уред}."
•	Втори ред:  "{процентът, който не им достига до максималния брой точки}%"
Общата оценка да бъде форматирана до третата цифра след десетичния знак,
а процентът да бъде форматиран до втората цифра след десетичния знак.
"""

country = input()
equipment = input()

difficulty_score = 0
performance_score = 0

if country == 'Russia':
    if equipment == 'ribbon':
        difficulty_score = 9.100
        performance_score = 9.400
    elif equipment == 'hoop':
        difficulty_score = 9.300
        performance_score = 9.800
    elif equipment == 'rope':
        difficulty_score = 9.600
        performance_score = 9.000
if country == 'Bulgaria':
    if equipment == 'ribbon':
        difficulty_score = 9.600
        performance_score = 9.400
    elif equipment == 'hoop':
        difficulty_score = 9.550
        performance_score = 9.750
    elif equipment == 'rope':
        difficulty_score = 9.500
        performance_score = 9.400
if country == 'Italy':
    if equipment == 'ribbon':
        difficulty_score = 9.200
        performance_score = 9.500
    elif equipment == 'hoop':
        difficulty_score = 9.450
        performance_score = 9.35
    elif equipment == 'rope':
        difficulty_score = 9.700
        performance_score = 9.150

total_score = difficulty_score + performance_score
difference = abs(total_score - 20) / 0.2

print(f'The team of {country} get {total_score:.3f} on {equipment}.')
print(f'{difference:.2f}%')