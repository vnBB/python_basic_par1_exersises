# 12. Write a Python program to print the calendar of a given month and year.
# Note : Use 'calendar' module.
import calendar


def calender_month(year, month):
    """ (integer, integer) -> string

    Enter an integer year and month and the function will return the calender month of that year

    calender_month(2025, 1)
       January 2025
    Mo Tu We Th Fr Sa Su
           1  2  3  4  5
     6  7  8  9 10 11 12
    13 14 15 16 17 18 19
    20 21 22 23 24 25 26
    27 28 29 30 31
    
    calender_month(2019, 12)
       December 2019
    Mo Tu We Th Fr Sa Su
                       1
     2  3  4  5  6  7  8
     9 10 11 12 13 14 15
    16 17 18 19 20 21 22
    23 24 25 26 27 28 29
    30 31
    """

    cal = calendar.TextCalendar(calendar.MONDAY)

    return print(cal.formatmonth(year, month))


get_year = int(input("Enter the year: "))
get_month = int(input("Enter the month: "))

calender_month(get_year, get_month)
