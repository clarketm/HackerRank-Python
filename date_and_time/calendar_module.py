#!/usr/bin/env python3

# Calendar Module
# https://www.hackerrank.com/challenges/calendar-module/problem


import calendar

if __name__ == '__main__':
    month, day, year = map(int, input().split())

    dow = calendar.day_name[calendar.weekday(year, month, day)]
    print(dow.upper())
