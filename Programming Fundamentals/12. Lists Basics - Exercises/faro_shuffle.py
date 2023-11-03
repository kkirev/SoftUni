"""
A faro shuffle is a method for shuffling a deck of cards, in which the deck is split exactly in half.
Then the cards in the two halves are perfectly interleaved, such that the original bottom card is still on the bottom
and the original top card is still on top.
For example, faro shuffling the list ['ace', 'two', 'three', 'four', 'five', 'six'] once,
gives ['ace', 'four', 'two', 'five', 'three', 'six']
Write a program that receives a single string (cards separated by space) and on the second line receives a count of
faro shuffles that should be made. Print the state of the deck after the shuffle.
Note: The length of the deck of cards will always be an even number.

Example:
Input                                           Output
a b c d e f g h                                 ['a', 'c', 'e', 'g', 'b', 'd', 'f', 'h']
5

input                                           Output
one two three four                              ['one', 'three', 'two', 'four']
3
"""

cards_deck = input().split()
shuffles_count = int(input())

current_index = 0
middle_index = len(cards_deck) // 2

for shuffle in range(shuffles_count):
    first_half = cards_deck[:middle_index]
    second_half = cards_deck[middle_index:]
    shuffled_deck = []

    for card in range(len(cards_deck)//2):
        shuffled_deck.append(first_half[current_index])
        shuffled_deck.append(second_half[current_index])
        current_index += 1

    current_index = 0
    cards_deck = shuffled_deck

print(shuffled_deck)

# ----------------------------------------------------------------------------------------------------------------------
# deck_of_cards = input().split()
# count_of_shuffles = int(input())
#
# for shuffle in range(count_of_shuffles):
#     middle_of_deck = len(deck_of_cards) // 2
#     left_part = deck_of_cards[0:middle_of_deck]
#     right_part = deck_of_cards[middle_of_deck:]
#     deck_after_shuffling = []
#
#     for card_index in range(len(left_part)): #(len(right_part))
#         deck_after_shuffling.append(left_part[card_index])
#         deck_after_shuffling.append(right_part[card_index])
#     deck_of_cards = deck_after_shuffling
#
# print(deck_after_shuffling)