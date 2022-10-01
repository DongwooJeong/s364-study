import datetime

now = datetime.datetime.now()

# Current date and time
cdatetime = now.strftime("%b %d, %H:%M") 
print("Current date and time :", cdatetime)

# Current year
cyear = now.strftime("%Y")
("%Y")
print("Current year :", cyear)

# Month of year
myear = now.strftime("%m")
print("Month of year :", myear)

# Week number of the year
wnum = now.isocalendar().week
print("Week Number of the year:",wnum)

# Weekday of the week
wday = now.strftime("%A")
print("Weekday of the week :",wday)

# Day of year
dyear = now.strftime("%j")
print("Day of year :",dyear)

# Day of the month
dmonth = now.strftime("%d")
print("Day of the month :",dmonth)

# Day of week
dweek = now.strftime("%u")
print("Day of week :",dweek)