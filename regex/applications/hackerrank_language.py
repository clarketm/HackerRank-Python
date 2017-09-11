#!/usr/bin/env python3


import re


# HackerRank Language
# https://www.hackerrank.com/challenges/hackerrank-language/problem
def hackerrank_language(language):
    string = r':C:CPP:JAVA:PYTHON:PERL:PHP:RUBY:CSHARP:HASKELL:CLOJURE:BASH:SCALA:ERLANG:CLISP:LUA:BRAINFUCK:JAVASCRIPT:GO:D:OCAML:R:PASCAL:SBCL:DART:GROOVY:OBJECTIVEC:'
    match = re.search(r':{}:'.format(language), string)
    result = 'VALID' if bool(match) else 'INVALID'
    print(result)


if __name__ == '__main__':
    n = int(input())
    while n > 0:
        _, language = input().split()
        hackerrank_language(language)
        n -= 1
