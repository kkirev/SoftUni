# Напишете програма, която изчислява колко решения в естествените числа (включително и нулата) има уравнението:
# x1 + x2 + x3 = n

result = int(input())
resolutions_counter = 0

for x1 in range(result + 1):
    for x2 in range(result + 1):
        for x3 in range(result + 1):
            if x1 + x2 + x3 == result:
                resolutions_counter += 1
print(resolutions_counter)