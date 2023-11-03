"""
https://judge.softuni.org/Contests/Compete/Index/2420#3

Габи иска да започне здравословен начин на живот и си е поставила за цел да върви 10 000 стъпки всеки ден.
Някои дни обаче е много уморена от работа и ще иска да се прибере преди да постигне целта си. Напишете програма,
която чете от конзолата по колко стъпки изминава тя всеки път като излиза през деня и когато постигне целта си да се
изписва "Goal reached! Good job!" и колко стъпки повече е извървяла "{разликата между стъпките} steps over the goal!"
Ако иска да се прибере преди това, тя ще въведе командата "Going home" и ще въведе стъпките, които е извървяла
докато се прибира. След което, ако не е успяла да постигне целта си,
на конзолата трябва да се изпише: "{разликата между стъпките} more steps to reach goal."
"""

steps_reached = 0
while True:
    steps = input()
    if steps == 'Going home':
        steps = int(input())
        steps_reached += steps
        steps_diff = abs(10000 - steps_reached)
        if steps_reached >= 10000:
            print('Goal reached! Good job!')
            print(f'{steps_diff} steps over the goal!')
        else:
            print(f'{steps_diff} more steps to reach goal.')
        break
    else:
        steps = int(steps)
        steps_reached += steps
    if steps_reached >= 10000:
        steps_diff = abs(10000 - steps_reached)
        print('Goal reached! Good job!')
        print(f'{steps_diff} steps over the goal!')
        break
# -----------------------------------------------------------------
#
# steps_reached = 0
# while steps_reached < 10000:
#     steps = input()
#     if steps == 'Going home':
#         steps = int(input())
#         steps_reached += steps
#         break
#     steps_reached += int(steps)
#
# steps_diff = abs(10000 - steps_reached)
# if steps_reached >= 10000:
#     print('Goal reached! Good job!')
#     print(f'{steps_diff} steps over the goal!')
# else:
#     print(f'{steps_diff} more steps to reach goal.')