"""
>>> days_start_month(2, 1994)
31
>>> days_start_month(3, 1994)
59
>>> days_start_month(3, 2000)
60
"""


def days_start_month(month, year):
    leap_year = False
    if ((year % 4 == 0) and not (year % 100 == 0)) or (year % 400 == 0):
        leap_year = True

    last_day_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if leap_year:
        last_day_list[1] = 29

    soma_days = 0
    for i, value in enumerate(last_day_list):
        if month == i + 1:
            return soma_days
        soma_days += value