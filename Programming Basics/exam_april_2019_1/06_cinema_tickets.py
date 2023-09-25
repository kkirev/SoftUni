"""
Вашата задача е да напишете програма, която да изчислява процента на билетите за всеки тип от
продадените билети: студентски(student), стандартен(standard) и детски(kid), за всички прожекции.
Трябва да изчислите и колко процента от залата е запълнена за всяка една прожекция.

Вход
Входът е поредица от цели числа и текст:
•	На първия ред до получаване на командата "Finish" - име на филма – текст
•	На втори ред – свободните места в салона за всяка прожекция – цяло число [1 … 100]
•	За всеки филм, се чете по един ред до изчерпване на свободните места в залата или до получаване на командата "End":
o	Типа на закупения билет - текст ("student", "standard", "kid")

Изход
На конзолата трябва да се печатат следните редове:
•	След всеки филм да се отпечата, колко процента от кино залата е пълна
"{името на филма} - {процент запълненост на залата}% full."
•	При получаване на командата "Finish" да се отпечатат четири реда:
o	"Total tickets: {общият брой закупени билети за всички филми}"
o	"{процент на студентските билети}% student tickets."
o	"{процент на стандартните билети}% standard tickets."
o	"{процент на детските билети}% kids tickets."
"""

standard_tickets = 0
students_tickets = 0
kids_tickets = 0
sold_tickets = 0
total_sold_tickets = 0

movie_name = input()
while movie_name != 'Finish':
    free_seats = int(input())

    while free_seats > 0:
        ticket_type = input()
        if ticket_type == 'End':
            break

        sold_tickets += 1
        free_seats -= 1
        total_sold_tickets += 1

        if ticket_type == 'student':
            students_tickets += 1
        elif ticket_type == 'standard':
            standard_tickets += 1
        elif ticket_type == 'kid':
            kids_tickets += 1

    percent_occupancy = sold_tickets / (free_seats + sold_tickets) * 100

    print(f'{movie_name} - {percent_occupancy:.2f}% full.')
    movie_name = input()
    sold_tickets = 0

    if movie_name == 'Finish':
        print(f'Total tickets: {total_sold_tickets}')
        print(f'{students_tickets / total_sold_tickets * 100:.2f}% student tickets.')
        print(f'{standard_tickets / total_sold_tickets * 100:.2f}% standard tickets.')
        print(f'{kids_tickets / total_sold_tickets * 100:.2f}% kids tickets.')