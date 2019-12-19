# 14. Write a Python program to calculate number of days between two dates.
# Sample dates : (2014, 7, 2), (2014, 7, 11)
# Expected output : 9 days

from datetime import datetime


def difference_between_dates(date1, date2):
    """ (date, date) -> date

    this function will calculate the difference between two dates

    difference_between_dates(2014, 7, 2, 2014, 7, 11)
    9 days
    """

    date1 = datetime.strptime(date1, "%d-%m-%Y")
    date2 = datetime.strptime(date2, "%d-%m-%Y")

    return print("The difference is " + str(abs((date1 - date2).days)) + " days.")


get_date1 = input("Enter the first date: ")
get_date2 = input("Enter the second date: ")

difference_between_dates(get_date1, get_date2)


