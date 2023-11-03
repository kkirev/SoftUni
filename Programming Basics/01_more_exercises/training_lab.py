"""
https://judge.softuni.org/Contests/Practice/Index/1642#4

Учебна зала има правоъгълен размер w на h метра, без колони във вътрешността си.
Залата е разделена на две части – лява и дясна, с коридор приблизително по средата. В лявата и в дясната част има редици
 с бюра. В задната част на залата има голяма входна врата. В предната част на залата има катедра с подиум за
 преподавателя. Едно работно място заема 70 на 120 cm (маса с размер 70 на 40 cm + място за стол и преминаване с размер
  70 на 80 cm). Коридорът е широк поне 100 cm. Изчислено е, че заради входната врата (която е с отвор 160 cm) се губи
  точно 1 работно място, а заради катедрата (която е с размер 160 на 120 cm) се губят точно 2 работни места. Напишете
  програма, която въвежда размери на учебната зала и изчислява броя работни места
  в нея при описаното разположение (вж. фигурата).

Вход
От конзолата се четат 2 числа, по едно на ред: w (дължина в метри) и h (широчина в метри).
Ограничения: 3 ≤ h ≤ w ≤ 100.

Изход
Да се отпечата на конзолата едно цяло число: броят места в учебната зала.
"""

hall_length = float(input())
hall_width = float(input())

workplace_length = 1.2
workplace_width = 0.7
workplace = workplace_length * workplace_width
corridor_size = hall_length * 1
podium_size = workplace * 2
door_size = workplace

count_workspace_lengths = hall_length // workplace_length
count_workplace_widths = (hall_width - 1) // workplace_width
count_workplaces = count_workspace_lengths * count_workplace_widths - podium_size - door_size

print(int(count_workplaces))