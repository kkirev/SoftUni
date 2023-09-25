# https://judge.softuni.org/Contests/Practice/Index/1538#10

# Българският лекоатлет Тихомир Иванов започва тренировки за предстоящото европейско първенство по лека атлетика
# на закрито в Глазгоу, Шотландия.
# Вашата задача е да напишете софтуер, с който Иванов да следи своя прогрес и дали е достигнал желаните резултати.
# В началото програмата получава желаната височина на летвата от Тихомир, той започва тренировката си като поставя
# летвата на височина 30см по-ниско от целта. За всяка височина той има право на 3 скока, като за да бъде един
# скок успешен, той трябва да бъде над височината на летвата. При успешен скок (над летвата), височината й се вдига с 5
# сантиметра. При три неуспешни скока на една и съща височина, тренировката приключва с неуспех.
# При достигане на желаната височина и нейното успешно прескачане, тренировката приключва с успех.

# Вход
# Входът е поредица от цели числа в интервала [100…300]:
# •	На първия ред се прочита желаната от Тихомир Иванов височина в сантиметри
# •	На всеки следващ ред до приключване на програмата се прочита височината от скока на Иванов

# Изход
# На конзолата трябва да се отпечата един ред:
# •	Ако Тихомир не успее да преодолее желаната височина:
# o	"Tihomir failed at {височина на летвата към момента на провала}cm \
# after {брой скокове от началото на тренировката} jumps."
# •	Ако Тихомир успее да преодолее височината:
# o	"Tihomir succeeded, he jumped over {височина на прескочената последно летва}cm \
# after {брой скокове за цялата тренировка} jumps."

target_jump_height = int(input())
bar_height = target_jump_height - 30
jumps = 0
fails = 0
has_succeeded = False

while fails < 3:
    curr_jump_height = int(input())
    jumps += 1

    if curr_jump_height > bar_height:
        fails = 0
        bar_height += 5
        if bar_height > target_jump_height:
            has_succeeded = True
            break
    else:
        fails += 1

if has_succeeded:
    print(f'Tihomir succeeded, he jumped over {target_jump_height}cm after {jumps} jumps.')
if fails == 3:
    print(f'Tihomir failed at {bar_height}cm after {jumps} jumps.')

#-----------------------------------------------------------------------------------------------------

# target_jump_height = int(input())
# bar_height = target_jump_height - 30
#
# jumps = 0
# fails = 0
#
# while fails < 3:
#     curr_jump_height = int(input())
#     jumps += 1

#     if curr_jump_height > bar_height:
#         fails = 0
#         bar_height += 5
#     else:
#         fails += 1
#
#     if bar_height > target_jump_height:
#         print(f'Tihomir succeeded, he jumped over {target_jump_height}cm after {jumps} jumps.')
#         exit()
#
# print(f'Tihomir failed at {bar_height}cm after {jumps} jumps.')

# -----------------------------------------------------------------------------------------------------

# target = int(input())
#
# current_height = target - 30
# total_jumps = 0
# wrong_jumps = 0
#
# while wrong_jumps < 3:
#     jump = int(input())
#
#     total_jumps += 1
#
#     if jump > current_height:
#         wrong_jumps = 0
#         current_height += 5
#
#         if current_height > target:
#             print(f'Tihomir succeeded, he jumped over {target}cm after {total_jumps} jumps.')
#             break
#     else:
#         wrong_jumps += 1
#
# else:
#     print(f'Tihomir failed at {current_height}cm after {total_jumps} jumps.')