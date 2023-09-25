# Пепи иска да напишете програма, чрез която да разбере кой е най-добрият играч от световното първенство.
# Информацията, която получавате ще бъде играч и колко гола е отбелязал.
# От вас се иска да отпечатате кой е играчът с най-много голове и дали е направил хет-трик. Хет-трик е,
# когато футболистът е вкарал 3 или повече гола. Ако футболистът е вкарал 10 или повече гола, програмата трябва да спре.

# Вход:
# От конзолата се четат по два реда до въвеждане на команда "END":
# •	Име на играч – текст
# •	Брой вкарани голове  – цяло положително число в интервала [1 … 10000]

# Изход:
# На конзолата да се отпечатат 2 реда :
# •	На първия ред:
#             "{име на играч} is the best player!"
# •	На втория ред :
# o	 Ако най-добрият футболист е направил хеттрик:
#                    "He has scored {брой голове} goals and made a hat-trick !!!"
# o	Ако най-добрият футболист не е направил хеттрик:
#                    "He has scored {брой голове} goals."

command = input()

max_goals = 0
best_player = ''
has_hat_trick = False

while command != 'END':
    player_name = command
    goals_count = int(input())

    if goals_count >= 10:
        max_goals = goals_count
        best_player = player_name
        has_hat_trick = True
        break

    if goals_count > max_goals:
        max_goals = goals_count
        best_player = player_name
        if max_goals >= 3:
            has_hat_trick = True

    command = input()

print(f'{best_player} is the best player!')

if has_hat_trick:
    print(f'He has scored {max_goals} goals and made a hat-trick !!!')
else:
    print(f'He has scored {max_goals} goals.')