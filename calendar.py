##This prints the month's calender of the year

import time, calendar
val = int(input("Please enter the year you want to see the calendar for\n"))
val0 = int(input("Please enter the month you want to see the calendar for\n"))
cal = calendar.month(val,val0)
print(cal)
