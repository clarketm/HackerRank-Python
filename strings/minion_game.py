#!/usr/bin.env/python3

# The Minion Game
# https://www.hackerrank.com/challenges/the-minion-game/problem

# Using a complex, non-optimized algorithm
# - allows for the removal of duplicates
# def minion_game(string):
#     from collections import defaultdict
#     length = len(string)
#     vowels = ('A', 'E', 'I', 'O', 'U')
#
#     # stuart_words = defaultdict(int)
#     stuart_words = {}
#     # kevin_words = defaultdict(int)
#     kevin_words = {}
#
#     for i in range(length):
#         for j in range(i, length):
#             word = ''.join(string[i:j + 1])
#             if word[0] not in vowels:
#                 # stuart_words[word] += 1
#                 stuart_words[word] = stuart_words.get(word, 0) + 1
#             if word[0] in vowels:
#                 # kevin_words[word] += 1
#                 kevin_words[word] = kevin_words.get(word, 0) + 1
#
#     stuart_words_count = sum(stuart_words.values())
#     kevin_words_count = sum(kevin_words.values())
#
#     if stuart_words_count > kevin_words_count:
#         print('Stuart', stuart_words_count)
#     elif kevin_words_count > stuart_words_count:
#         print('Kevin', kevin_words_count)
#     else:
#         print('Draw')


# Using a simple, optimized algorithm
def minion_game(string):
    length = len(string)
    vowels = ('A', 'E', 'I', 'O', 'U')

    stuart_words_count = 0
    kevin_words_count = 0

    for i in range(length):
        if string[i] not in vowels:
            stuart_words_count += length - i
        if string[i] in vowels:
            kevin_words_count += length - i

    if stuart_words_count > kevin_words_count:
        print('Stuart', stuart_words_count)
    elif kevin_words_count > stuart_words_count:
        print('Kevin', kevin_words_count)
    else:
        print('Draw')


if __name__ == '__main__':
    s = input()
    minion_game(s)
