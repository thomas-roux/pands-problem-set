# Thomas Roux
# Solution to Problem 8 - outputs today's date in format "Weekday, Month Day Year at HH:MM am/pm"
# Begun: 03/03/2019; 16h00

# Imports datetime module
import datetime as dt

# Creates the necessary suffix for the date based on the date number
# Kudos to ED (fellow student) for explaining
suf = ()
if dt.datetime.strftime(dt.datetime.now(), "%d") == 1 or 21 or 31:
    suf = ("st")
elif dt.datetime.strftime(dt.datetime.now(), "%d") == 2 or 22:
    suf = ("nd")
elif dt.datetime.strftime(dt.datetime.now(), "%d") == 3 or 23:
    suf = ("rd")
else:
    suf = ("th")

# Prints today's date in specified format
# dash (-) in %-d and %-I removes zero - https://stackoverflow.com/questions/904928/python-strftime-date-without-leading-0
print(dt.datetime.strftime(dt.datetime.now(), "%A, %B %-d" + suf + " %Y at %-I:%M %p"))
