# За Лора думите притежават голяма сила. Тя те моли да измислиш алгоритъм, с който да откриеш коя е "най-силната" дума.
# До получаване на команда "End of words" ще се четат от конзолата думи. За да се открие силата на всяка една,
# трябва да се намери сборът от ASCII стойностите на символите, от които се състои думата.
# Ако започва с гласна буква - 'a', 'e', 'i', 'o', 'u', 'y' (или техните еквивалентни главни букви),
# полученият сбор трябва да се умножи по дължината на думата, в противен случай,
# да се раздели на дължината и да се закръгли до най-близкото цяло число надолу.

# Вход
# До получаване на команда "End of words" се чете по един ред от конзолата:
# •	дума – текст

# Изход
# След приключване на програмата се печата на един ред думата с "най-голяма сила":
# •	"The most powerful word is {думата с най-голяма сила} - {силата на думата}"

from math import floor

curr_power = 0
max_power = 0
the_most_powerful_word = ''

command = input()
while command != 'End of words':
    word = str(command)
    for letter in range(len(word)):
        curr_power += ord(word[letter])

    if word[0] == 'a' or word[0] == 'A' or word[0] == 'e' or word[0] == 'E' or word[0] == 'i' or word[0] == 'I' \
            or word[0] == 'o' or word[0] == 'O' or word[0] == 'u' or word[0] == 'U' or word[0] == 'y' \
            or word[0] == 'Y':
        curr_power *= len(word)
    else:
        curr_power = floor(curr_power / len(word))

    if curr_power > max_power:
        max_power = curr_power
        the_most_powerful_word = word

    curr_power = 0
    command = input()

print(f'The most powerful word is {the_most_powerful_word} - {max_power}')