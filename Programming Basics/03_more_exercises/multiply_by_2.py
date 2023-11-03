num = 0
while num > -1:
    num = float(input())
    result = num * 2
    if num < 0:
        print('Negative number!')
    elif num >= 0:
        print(f'Result: {result:.2f}')

#   while True:
#       number = float(input())
#       if number < 0:
#           print("Negative number!")
#           break
#
#       result = number * 2
#       print(f"Result: {result:.2f}")