"""
Ани обича да пътува и иска тази година да посети няколко различни дестинации. Като си избере дестинация,
ще прецени колко пари ще й трябват, за да отиде до там, и ще започне да спестява. Когато е спестила достатъчно,
ще може да пътува.
От конзолата всеки път ще се четат първо дестинацията и минималния бюджет (десетично число),
който ще е нужен за пътуването.
След това ще се четат няколко суми (десетични числа), които Ани спестява като работи и когато успее да събере
достатъчно за пътуването, ще заминава, като на конзолата трябва да се изпише: "Going to {дестинацията}!"
Когато е посетила всички дестинации, които иска, вместо дестинация ще въведе "End" и програмата ще приключи.
"""

destination = input()

while destination != 'End':
    budget_needed = float(input())
    current_saves = 0
    while current_saves < budget_needed:
        daily_income = float(input())
        current_saves += daily_income
    print(f'Going to {destination}!')
    destination = input()
