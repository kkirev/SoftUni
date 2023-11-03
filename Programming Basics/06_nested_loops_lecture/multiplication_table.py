# Отпечатайте на конзолата таблицата за умножение за числата от 1 до 10 във формат:
# "{първи множител} * {втори множител} = {резултат}".

for first_num in range(1, 11):
    for second_num in range(1, 11):
        result = first_num * second_num
        print(f'{first_num} * {second_num} = {result}')