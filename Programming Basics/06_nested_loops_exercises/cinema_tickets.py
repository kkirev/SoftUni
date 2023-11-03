# Вашата задача е да напишете програма, която да изчислява процента на билетите за всеки тип от продадените билети:
# студентски(student), стандартен(standard) и детски(kid), за всички прожекции. Трябва да изчислите и колко процента
# от залата е запълнена за всяка една прожекция.

# Вход
# Входът е поредица от цели числа и текст:
# •	На първия ред до получаване на командата "Finish" - име на филма – текст
# •	На втори ред – свободните места в салона за всяка прожекция – цяло число [1 … 100]
# •	За всеки филм, се чете по един ред до изчерпване на свободните места в залата или до получаване на командата "End":
# o	Типа на закупения билет - текст ("student", "standard", "kid")

# Изход
# На конзолата трябва да се печатат следните редове:
# •	След всеки филм да се отпечата, колко процента от кино залата е пълна
# "{името на филма} - {процент запълненост на залата}% full."
# •	При получаване на командата "Finish" да се отпечатат четири реда:
# o	"Total tickets: {общият брой закупени билети за всички филми}"
# o	"{процент на студентските билети}% student tickets."
# o	"{процент на стандартните билети}% standard tickets."
# o	"{процент на детските билети}% kids tickets."


movie_name = input()

student_tickets = 0
standard_tickets = 0
kid_tickets = 0

while movie_name != 'Finish':
    free_seats = int(input())
    tickets_per_movie = 0

    while free_seats > 0:
        category = input()
        if category == 'End':
            break
        free_seats -= 1
        tickets_per_movie += 1

        if category == 'student':
            student_tickets += 1
        elif category == 'standard':
            standard_tickets += 1
        elif category == 'kid':
            kid_tickets += 1

    percent_occupancy = tickets_per_movie / (free_seats + tickets_per_movie) * 100
    print(f'{movie_name} - {percent_occupancy:.2f}% full.')

    movie_name = input()
sold_tickets = student_tickets + standard_tickets + kid_tickets

print(f'Total tickets: {sold_tickets}')
print(f'{student_tickets / sold_tickets * 100:.2f}% student tickets.')
print(f'{standard_tickets / sold_tickets * 100:.2f}% standard tickets.')
print(f'{kid_tickets / sold_tickets * 100:.2f}% kids tickets.')