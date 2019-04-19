"""
 @author    : macab (macab@debian)
 @file      : getweek
 @created   : Saturday Apr 20, 2019 00:01:32 IST
"""

import datetime
import calendar

def findday(date):
    born = datetime.datetime.strptime(date, "%d %m %Y").weekday()
    return (calendar.day_name[born])


date = str(input('enter the date :'))
#print(date)
print(findday(date))

