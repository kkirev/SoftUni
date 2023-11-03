# https://judge.softuni.org/Contests/2419

# Напишете програма, която чете цяло число от конзолата и на всеки следващ ред цели числа, докато тяхната сума стане
# по-голяма или равна на първоначалното число. След приключване на четенето да се отпечата сумата на въведените числа.

control_num = int(input())
current_sum = 0

while current_sum < control_num:
    next_num = int(input())
    current_sum += next_num
    if current_sum > control_num:
        break
print(current_sum)