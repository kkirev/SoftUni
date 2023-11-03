# Курсът "Train the trainers" е към края си и финалното оценяване наближава. Вашата задача е да помогнете на журито,
# което ще оценява презентациите, като напишете програма, в която да изчислява средната оценка от представянето на
# всяка една презентация от даден студент, а накрая - средния успех от всички тях.
# От конзолата на първият ред се прочита броят на хората в журито n - цяло число.
# След това на отделен ред се прочита името на презентацията – текст.
# За всяка една презентация на нов ред се четат n - на брой оценки - реално число.
# След изчисляване на средната оценка за конкретна презентация, на конзолата се печата:
#  "{името на презентацията} - {средна оценка}."
# След получаване на команда "Finish", на конзолата се печата
# "Student's final assessment is {среден успех от всички презентации}." и програмата приключва.
# Всички оценки трябва да бъдат форматирани до втория знак след десетичната запетая.

jury_count = int(input())
all_grades_sum = 0
tasks_counter = 0

command = input()
while command != 'Finish':
    topic_name = command
    grade_sum = 0
    average_grade = 0
    for i in range(jury_count):
        grade_sum += float(input())
        tasks_counter += 1

    average_grade = grade_sum / jury_count
    all_grades_sum += grade_sum
    print(f'{topic_name} - {average_grade:.2f}.')

    command = input()

print(f"Student's final assessment is {all_grades_sum / tasks_counter:.2f}.")