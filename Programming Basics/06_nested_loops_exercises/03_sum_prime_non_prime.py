# Напишете програма, която чете от конзолата цели числа, докато не се получи команда "stop". Да се намери сумата на
# всички въведени прости и сумата на всички въведени непрости числа. Тъй като по дефиниция от математиката отрицателните
# числа не могат да бъдат прости, ако на входа се подаде отрицателно число, да се
# изведе следното съобщение "Number is negative.". В този случай въведено число се игнорира и не се прибавя към нито
# една от двете суми, а програмата продължава своето изпълнение, очаквайки въвеждане на следващо число.
# На изхода да се отпечатат на два реда двете намерени суми в следния формат:
# •	"Sum of all prime numbers is: {prime numbers sum}"

is_prime = True
prime_numbers_sum = 0
non_prime_numbers_sum = 0

input_line = input()
while input_line != 'stop':
    current_num = int(input_line)

    if current_num < 0:
        print('Number is negative.')
    else:
        for number in range(2, current_num): # започваме цикъла от 2, защото всички числа се делят на едно
            if current_num % number == 0:
                is_prime = False
                break
        if is_prime:
            prime_numbers_sum += current_num
        else:
            non_prime_numbers_sum += current_num
            is_prime = True

    input_line = input()

print(f'Sum of all prime numbers is: {prime_numbers_sum}')
print(f'Sum of all non prime numbers is: {non_prime_numbers_sum}')