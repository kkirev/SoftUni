"""
https://judge.softuni.org/Contests/Practice/Index/1684#0

Напишете програма, която прочита скрито съобщение в поредица от символи. Те се получават по един на ред до получаване
на командата "End". Думите се образуват от буквите в реда на четенето им. Символите, които не са латински букви
трябва да бъдат игнорирани. Думите скрити в потока са разделени от тайна команда от три букви – "c", "o" и "n".
При първото получаване на една от тези букви, тя се маркира като срещната, но не се запазва в думата.
При всяко следващо нейно срещане се записва нормално в думата. След като са налични и трите символа от командата, се
печата думата и интервал " ". Започва се нова дума, която по същия начин чака тайната команда, за да бъде отпечатана.

Вход
От конзолата се чете поредица от редове с един символ на всеки до получаване на командата "End".

Изход
На конзолата се печата на един ред всяка дума след тайната команда, следвана от интервал.
"""

output_string = ''
current_word = ''

c = False
n = False
o = False

command = input()
while command != 'End':
    if not c and command == 'c':
        c = True
    elif not o and command == 'o':
        o = True
    elif not n and command == 'n':
        n = True
    elif 65 <= ord(command) <= 90 or 97 <= ord(command) <= 122:
        current_word += command

    if c and o and n:
        output_string += current_word + ' '
        current_word = ''
        c = False
        o = False
        n = False

    command = input()

print(output_string)

# c = o = n = 0
# string = ''
# current_word = ''
#
# while True:
#     command = input()
#
#     if command == 'End':
#         break
#     if ord(command) < 65 or (90 < ord(command) < 97) or ord(command) > 122:
#         continue
#     if command == 'c' and c != 1 or command == 'o' and o != 1 or command == 'n' and n != 1:
#         if command == 'c': c = 1
#         if command == 'o': o = 1
#         if command == 'n': n = 1
#     else:
#         string += command
#
#     if c and o and n:
#         current_word += string + ' '
#         string = ''
#         c = o = n = 0
#
# print(current_word)