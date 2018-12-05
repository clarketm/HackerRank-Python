#!/usr/bin/env python3

# Capitalize!
# https://www.hackerrank.com/challenges/capitalize/problem

# Using `list comprehension` and `capitalize` method
# def capitalize(string):
#     new_word = []
#
#     for word in string.split(' '):
#         new_word.append(word.capitalize())
#
#     return ' '.join(new_word)

# Using `list comprehension` with `upper` method
# def capitalize(string):
#     new_word = []
#
#     for word in string.split(' '):
#         new_word.append(word[:1].upper() + word[1:])
#
#     return ' '.join(new_word)

# Using `list comprehension` and `capitalize` method
# def capitalize(string):
#     return ' '.join([w.capitalize() for w in string.split(' ')])


# Using `list comprehension` with `upper` method
def capitalize(string):
    return " ".join([w[:1].upper() + w[1:] for w in string.split(" ")])


# Using `title` method
# DOESN'T WORK FOR ALL TEST CASES
# def capitalize(string):
#     return string.title()

if __name__ == "__main__":
    string = input()
    capitalized_string = capitalize(string)
    print(capitalized_string)
