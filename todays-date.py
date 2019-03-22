# Thomas Roux
# Solution to Problem 8 - outputs today's date in format "Weekday, Month Day Year at HH:MM am/pm"
# Begun: 03/03/2019; 16h00

# Imports datetime module
import datetime as dt

# Creates a single value integer for today's date to determine suffix - https://www.programiz.com/python-programming/datetime
today = dt.date.today()
day = today.day

# Creates the necessary suffix for the date based on the date number
# Kudos to ED (fellow student) for explaining
if day == 1 or day == 21 or day == 31:
    suf = ("st")
elif day == 2 or day == 22:
    suf = ("nd")
elif day == 3 or day == 23:
    suf = ("rd")
else:
    suf = ("th")

# Prints today's date in specified format
# dash (-) in %-d and %-I removes zero - https://stackoverflow.com/questions/904928/python-strftime-date-without-leading-0
print(dt.datetime.strftime(dt.datetime.now(), f"%A, %B %-d{suf} %Y at %-I:%M %p"))
