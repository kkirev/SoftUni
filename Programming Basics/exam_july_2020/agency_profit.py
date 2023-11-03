# Напишете програма, която изчислява печалбата на агенция за продажба на самолетни билети.
# Агенцията продава самолетни билети на различни авиокомпании. Ще получите информация за броя продадени
# билети за възрастни и броя продадени детски билети. Нетната цена на билета за възрастен се определя от авиокомпанията,
# а детският билет е със 70% по-евтин. Агенцията добавя към нетната цена на всеки билет такса обслужване.
# Крайната печалба на Агенцията е 20% от общата цена на всички билети.

# Вход:
# От конзолата се четат 5 реда:
# 1.	Име на авиокомпанията - текст
# 2.	Брой билети за	 възрастни - цяло число в диапазона [1…400]
# 3.	Брой детски билети - цяло число в диапазона [25…120]
# 4.	Нетна цена на билет за възрастен - реално число в диапазона [100.00…1600.00]
# 5.	Цената на такса обслужване - реално число в диапазона [10.00…50.00]

# Изход:
# Да се отпечата на конзолата крайната печалбата от продажбите, в следния формат:
# •	"The profit of your agency from {име на авиокомпанията} tickets is {печалба за агенцията} lv."
# Цената на печалбата да бъде форматирана до втората цифра след десетичния знак.

company_name = input()
adults_tickets_count = int(input())
kids_tickets_count = int(input())
adults_price = float(input())
service_fee = float(input())

kids_price = 0.3 * adults_price

company_profit = 0.2 * ((adults_tickets_count * (adults_price + service_fee)) +
                        (kids_tickets_count * (kids_price + service_fee)))

print(f'The profit of your agency from {company_name} tickets is {company_profit:.2f} lv.')