"""
You are at the zoo, and the meerkats look strange.
You will receive 3 strings on separate lines, representing the tail, the body, and the head of an animal in that order.
Your task is to re-arrange the elements in a list so that the animal looks normal again:
•	On the first position is the head;
•	On the second position is the body;
•	On the last one is the tail.
"""

tail = input()
body = input()
head = input()

meerkat = [head, body, tail]

print(meerkat)
# -------------------------------------------------------------
# tail = input()
# body = input()
# head = input()
#
# meerkat = [tail, body, head]
#
# meerkat[0], meerkat[2] = meerkat[2], meerkat[0]
# print(meerkat)