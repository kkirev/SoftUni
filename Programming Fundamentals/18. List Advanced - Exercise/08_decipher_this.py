"""
You are given a secret message you should decipher. To do that, you need to know that in each word:
•	the second and the last letter are switched (e.g., Holle means Hello)
•	the first letter is replaced by its character code (e.g., 72 means H)
"""

secret_message = input().split()
deciphered_message = []

for word in secret_message:
	firs_letter_as_num = ""
	rest_of_of_the_word = []
	word_as_list = []
	for symbol in word:
		if symbol.isdigit():
			firs_letter_as_num += symbol
		else:
			rest_of_of_the_word.append(symbol)
		word_as_list = [firs_letter_as_num]
		word_as_list.extend(rest_of_of_the_word)
	word_as_list[0] = chr(int(word_as_list[0]))
	word_as_list[1], word_as_list[-1] = word_as_list[-1], word_as_list[1]
	deciphered_message.append("".join(word_as_list))

print(" ".join(deciphered_message))

# ---------------------------------------------------------------------------------------------------------------------
#
# message = input().split()
#
# words, numbers = [], []
# for word in message:
#     num, let = "", ""
#     for symbol in word:
#         if symbol.isdigit():
#             num += symbol
#         else:
#             let += symbol
#     numbers.append(int(num))
#     if len(let) != 1:
#         let = f"{let[-1]}{let[1:-1]}{let[0]}"
#     words.append(let)
#
# for n, w in zip(numbers, words):
#     print(f"{chr(n)}{w}", end=" ")
